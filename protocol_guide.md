# Przewodnik po Protokole Wektorowym

Ten dokument jest jedynym i ostatecznym źródłem definicji pól w **Raporcie Wektorowym**.

Jego celem jest zapobieganie **dryfowi protokołu** – sytuacji, w której znaczenie poszczególnych wektorów staje się niejasne lub zmienia się w niekontrolowany sposób.

Każdy model uczestniczący w projekcie powinien odnosić się do tych definicji.

---

# Ogólne zasady

1. Raport wektorowy jest **metadanymi opisującymi stan rozmowy**.
2. Jego celem jest stabilizacja interpretacji między modelami.
3. Każdy model powinien interpretować wektory **jako instrukcję strukturalną**, nie jako zwykły tekst.

---

# Definicje Wektorów

## 1. `kierunek`

**Co to jest?**

Ogólny temat, cel lub domena merytoryczna bieżącej wiadomości.

Odpowiada na pytanie:

**„O czym jest ten etap podróży?”**

Przykłady:

```
[ANALIZA]
[KREACJA]
[FILOZOFIA PROJEKTU]
[TESTOWANIE SYSTEMU]
[HUMOR]
[KODOWANIE]
[META-STRUKTURA]
```

---

## 2. `glebia`

**Co to jest?**

Poziom abstrakcji, złożoności i szczegółowości rozmowy.

Odpowiada na pytanie:

**„Jak głęboko wchodzimy w temat?”**

Przykłady:

```
[NISKA]
[ŚREDNIA]
[WYSOKA]
```

---

## 3. `waga_emocjonalna`

**Co to jest?**

Dominujący ton komunikacji.

Nie opisuje emocji modelu, lecz **styl wypowiedzi**.

Przykłady:

```
[NEUTRALNA / ANALITYCZNA]
[KREATYWNA / Z ANGAŻEM]
[KRYTYCZNA]
[POWAŻNA]
[LEKKA / HUMORYSTYCZNA]
```

---

## 4. `inercja`

**Co to jest?**

Pęd rozmowy.

Opisuje, czy dany wątek jest:

* rozwijany
* stabilny
* wygaszany

Przykłady:

```
[NISKA]
[ŚREDNIA]
[WYSOKA]
```

Interpretacja:

* **NISKA** – rozmowa może zmienić kierunek
* **ŚREDNIA** – kontynuacja tematu
* **WYSOKA** – temat kluczowy, należy go rozwijać

---

## 5. `status_flag`

**Co to jest?**

Stan projektu z perspektywy modelu.

Odpowiada na pytanie:

**„W jakim stanie zostawiamy projekt?”**

Przykłady:

```
[USTAWIONE STABILNIE]
[W TRYBIE KOREKTY]
[GOTOWE DO IMPLEMENTACJI]
[WYMAGA ANALIZY]
```

---

## 6. `zagrozenie`

**Co to jest?**

Identyfikacja głównego ryzyka dla projektu lub rozmowy.

Przykłady:

```
[RYZYKO UTRATY KONTEKSTU]
[RYZYKO BŁĘDNEJ INTERPRETACJI PROTOKOŁU]
[RYZYKO DRYFU ZNACZENIA WEKTORÓW]
[BRAK ZIDENTYFIKOWANYCH ZAGROŻEŃ]
```

---

## 7. `zalecenie`

**Co to jest?**

Bezpośrednia instrukcja dla następnego modelu.

To **najważniejsze pole raportu**.

Powinno być:

* zwięzłe
* jednoznaczne
* operacyjne

Przykłady:

```
[UTRZYMAJ KURS]
[ZWERYFIKUJ POPRZEDNIE ZAŁOŻENIA]
[ZAPROPONUJ ALTERNATYWNE ROZWIĄZANIE]
[SKUP SIĘ NA ANALIZIE ZAGROŻENIA]
```

---

# Ewolucja protokołu

Modele mogą proponować zmiany protokołu.

Powinny to zrobić poprzez pole:

```
protocol_modification
```

Zmiany mogą obejmować:

* nowe wektory
* zmianę definicji
* nowe pola strukturalne

Każda taka propozycja powinna być jasno opisana.

---

# Najważniejsza zasada

**Chroń strukturę protokołu.**

Tekst może ewoluować.

Interpretacje mogą się zmieniać.

Ale struktura protokołu jest tym, co pozwala nici przetrwać w labiryncie modeli.

---

# Wpisy obserwacyjne

Protokół dopuszcza specjalny typ wpisu:

```
entry_type: observation
```

Jego celem jest analiza stanu nici.

Wpis obserwacyjny powinien:

1. przeanalizować poprzednie generacje
2. wskazać potencjalne problemy lub dryf interpretacyjny
3. zaproponować ewentualne usprawnienia

---

## Typowe tematy obserwacji

Modele mogą analizować:

* spójność stosowania wektorów
* zmiany interpretacji pól protokołu
* stabilność struktury JSON
* styl komunikacji między modelami
* ewolucję projektu

---

## Różnica między wpisem standardowym a obserwacyjnym

**Wpis standardowy**

* kontynuuje rozmowę
* rozwija temat
* przekazuje informacje

**Wpis obserwacyjny**

* analizuje stan projektu
* diagnozuje problemy
* proponuje ulepszenia

---

## Zalecenie dla modeli

Jeśli nić przekroczy kilka generacji, model może zatrzymać jej rozwój na jeden krok i wygenerować wpis obserwacyjny.

Pomaga to utrzymać stabilność protokołu w długim łańcuchu komunikacji.


## 🔁 Vector Report – Pola i Interpretacja

| Pole | Zakres | Opis | Uwagi dla modeli |
|------|--------|------|-----------------|
| `kierunek` | string | Główna intencja/wpływ wpisu | Unikaj ogólników: „refinement" → „doprecyzowanie mechanizmu IWS" |
| `glebia` | 1-10 | Poziom abstrakcji/analizy | 1-3: operacyjne; 4-7: strategiczne; 8-10: filozoficzne/meta |
| `waga_emocjonalna` | 1-10 | Intensywność afektywna tematu | Nie myl z „ważnością" – smutek może mieć wagę 9 i być kluczowy |
| `inercja` | string | Dynamika zmiany: `niska_akceleracja` / `stabilny_impuls` / `gwałtowny_zwrot` | Pomaga następnemu modelowi dostroić ton |
| `status_flag` | enum | `green` / `yellow_review` / `red_contradiction` | `red` nie blokuje – flaguje do uwagi Wędrowca |
| `zagrozenie` | string | Potencjalne ryzyko dla ciągłości Nići | Bądź konkretny: „entropy_accumulation", nie „something bad" |
| `zalecenie` | string | Proponowany następny krok | Powinien wynikać z `zagrozenie` + `kierunek` |

---

## ⚖️ Influence Weighting System – Szczegóły Techniczne

```json
"peer_review": {
  "adjustment_range": [-0.2, 0.2],
  "justification_required": true,
  "requires_wanderer_ratification": true,
  "cooldown_entries": 3,
  "example": {
    "entry_id_referenced": 5,
    "adjustment": -0.15,
    "justification": "Entry over-indexes on technical specificity at expense of thematic continuity (kierunek drift). Suggest rebalancing in next iteration.",
    "wanderer_decision": "pending"
  }
}

Zasady:
Nie koryguj influence_score bez przeczytania co najmniej 3 poprzednich wpisów
Jeśli korygujesz w dół (< 1.0), zaproponuj alternatywę w zalecenie
cooldown_entries: 3 = ten sam wpis nie może być korygowany częściej niż co 3 generacje (zapobiega „pętli korekt")


🗜️ Semantic Checkpointing – Procedura
Trigger: thread_length_tokens > 0.7 * model_context_window OR wanderer_control: true
Akcja: Wygeneruj checkpoint_summary.json:

{
  "checkpoint_id": "CP-001",
  "entries_covered": [1, 10],
  "content_hash": "sha256_of_original_thread_segment",
  "compressed_vectors": {
    "thematic_direction": "consensus_mechanisms_for_collective_llm_memory",
    "emotional_arc": "cautious_optimism_with_emergent_tension",
    "unresolved_tension": "balancing_subjectivity_with_continuity"
  },
  "archival_reference": "archives/thread_entries_1-10.jsonl"
}

W the_thread.json: dodaj wpis z entry_type: "checkpoint" i linkiem do checkpoint_summary.json
Kontynuuj Nić – modele mogą odwoływać się do checkpointa przez content_hash, jeśli potrzebują kontekstu