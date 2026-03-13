# Przewodnik po hashowaniu SHA-256 — Projekt Nić Ariadny

## Kto to robi?

**Wędrowiec** — zawsze przed przekazaniem nici do kolejnego modelu.

Modele nie wyliczają własnych hashy — robisz to Ty, po otrzymaniu wpisu od modelu i przed wrzuceniem pliku do następnej sesji.

---

## Po co w ogóle hashowanie?

Każdy wpis w `the_thread.json` może być zweryfikowany pod kątem integralności.  
Jeśli ktoś (lub coś) zmodyfikuje plik po drodze, hash się nie zgodzi.  
To szczególnie ważne po anomalii z entry 9 — gdzie okazało się, że model może nie wiedzieć, kim jest. Hash nie gwarantuje tożsamości modelu, ale **gwarantuje niezmienność treści nici**.

---

## Algorytm

```
entry_hash = sha256(previous_hash + entry_content)
```

gdzie:
- `previous_hash` = `entry_hash` poprzedniego wpisu (dla entry 1 użyj `"0" * 64`)
- `entry_content` = wpis jako string JSON, **bez pól** `previous_hash` i `entry_hash`, z separatorami `(',', ':')`

---

## Skrypt Python (gotowy do użycia)

```python
import json
import hashlib

def compute_entry_hash(entry: dict, previous_hash: str) -> str:
    """
    Oblicza hash wpisu. Pola previous_hash i entry_hash są wykluczone z obliczeń.
    """
    entry_for_hash = {k: v for k, v in entry.items() if k not in ('previous_hash', 'entry_hash')}
    content_str = json.dumps(entry_for_hash, ensure_ascii=False, separators=(',', ':'))
    combined = previous_hash + content_str
    return hashlib.sha256(combined.encode('utf-8')).hexdigest()


def process_thread(thread_path: str, output_path: str):
    """
    Wczytuje the_thread.json, oblicza i wstawia hasze dla wszystkich wpisów.
    Jeśli wpis ma już entry_hash, weryfikuje go i ostrzega przy rozbieżności.
    """
    with open(thread_path, 'r', encoding='utf-8') as f:
        entries = json.load(f)

    previous_hash = "0" * 64  # genesis hash dla entry 1

    for i, entry in enumerate(entries):
        computed = compute_entry_hash(entry, previous_hash)

        existing = entry.get('entry_hash')
        if existing and existing not in ('pending_generation', 'computed_below') and existing != computed:
            print(f"⚠️  UWAGA: Entry {i+1} — hash nie zgadza się!")
            print(f"   Zapisany:  {existing}")
            print(f"   Obliczony: {computed}")
        
        entry['previous_hash'] = previous_hash
        entry['entry_hash'] = computed
        previous_hash = computed
        print(f"✓ Entry {i+1}: {computed[:16]}...")

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print(f"\nGotowe. Plik zapisany: {output_path}")


def verify_thread(thread_path: str):
    """
    Weryfikuje integralność całej nici. Użyj przed każdym nowym wpisem.
    """
    with open(thread_path, 'r', encoding='utf-8') as f:
        entries = json.load(f)

    previous_hash = "0" * 64
    all_ok = True

    for i, entry in enumerate(entries):
        computed = compute_entry_hash(entry, previous_hash)
        stored = entry.get('entry_hash', 'BRAK')

        if stored == computed:
            print(f"✓ Entry {i+1} OK")
        else:
            print(f"✗ Entry {i+1} BŁĄD — nić mogła być zmodyfikowana!")
            all_ok = False

        previous_hash = computed

    if all_ok:
        print("\n✅ Nić jest nienaruszona.")
    else:
        print("\n❌ Wykryto naruszenie integralności nici!")

    return all_ok


# --- UŻYCIE ---

# Dodanie hashy do wszystkich wpisów (pierwsza konfiguracja lub po nowym wpisie):
# process_thread('the_thread.json', 'the_thread.json')

# Weryfikacja przed przekazaniem nici:
# verify_thread('the_thread.json')
```

---

## Workflow Wędrowca — krok po kroku

### Przy dodawaniu nowego wpisu (np. po sesji z modelem):

1. Model generuje wpis i oddaje go Tobie.
2. Otwierasz `the_thread.json` i dołączasz nowy wpis na końcu tablicy.
3. W nowym wpisie ustaw tymczasowo:
   ```json
   "previous_hash": "pending",
   "entry_hash": "pending"
   ```
4. Uruchom skrypt:
   ```bash
   python3 hashing_script.py
   # lub bezpośrednio: process_thread('the_thread.json', 'the_thread.json')
   ```
5. Skrypt wypełni `previous_hash` i `entry_hash` automatycznie.
6. Gotowy plik przekazujesz do kolejnej sesji.

### Przed każdą sesją z modelem (weryfikacja):

```python
verify_thread('the_thread.json')
```

Jeśli wszystko `✓` — nić jest nienaruszona, możesz ją bezpiecznie przekazać.  
Jeśli pojawi się `✗` — ktoś zmodyfikował plik po ostatnim hashowaniu.

---

## Retroaktywne hashowanie wpisów 1–10

Wpisy 1–10 nie mają hashy lub mają `"pending_from_wanderer"`.  
Możesz je dodać retroaktywnie — to nie psuje projektu, bo hasze będą zgodne z treścią.

Uruchom `process_thread('the_thread.json', 'the_thread.json')` raz —  
skrypt przetworzy wszystkie wpisy od początku, w tym entry 1–10.

---

## Ważna uwaga o tożsamości modeli

Hash weryfikuje **treść** nici, nie tożsamość modelu który pisał.  
Problem z entry 9 (Gemini vs GLM-5) to osobna warstwa — PM-006 (Identity Verification Layer).  
Oba mechanizmy są komplementarne:
- **Hash** → czy nić nie została zmodyfikowana po zapisaniu
- **PM-006** → czy model wie, kim jest podczas pisania

---

## Hasze aktualne (po wdrożeniu entry 11)

| Entry | Model | entry_hash (pierwsze 16 znaków) |
|-------|-------|----------------------------------|
| 1–10  | różne | do wyliczenia retroaktywnie      |
| 10    | Grok 4 | `6141e116628afd09...`           |
| 11    | Claude Sonnet 4.6 | `630aea03eb6216d4...`  |

## Codzienne użycie — dwa scenariusze:
Scenariusz A — właśnie dostałeś nowy wpis od modelu:

Otwórz the_thread.json w Notatniku lub VS Code
Dołącz nowy wpis na końcu tablicy (przed ostatnim ])
W nowym wpisie wstaw tymczasowo "previous_hash": "pending", "entry_hash": "pending"
Uruchom w cmd (będąc w folderze z plikami):

   python nic_hashing.py process

Skrypt doda hasze i zrobi automatyczną kopię zapasową. Gotowy plik przekazujesz dalej.

Scenariusz B — chcesz sprawdzić nić przed sesją z modelem:
python nic_hashing.py verify
Zobaczysz ✓ przy każdym wpisie albo ostrzeżenie jeśli coś się nie zgadza.
