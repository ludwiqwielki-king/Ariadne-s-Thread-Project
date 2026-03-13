"""
Projekt Nic Ariadny — Skrypt do hashowania SHA-256
===================================================
Uzycie na Windows:
  python nic_hashing.py                  # tryb interaktywny (menu)
  python nic_hashing.py process          # dodaj/zaktualizuj hasze w pliku
  python nic_hashing.py verify           # tylko weryfikacja bez zmian

Plik the_thread.json musi byc w tym samym folderze co skrypt,
LUB podaj sciezke jako argument: python nic_hashing.py process C:\\sciezka\\the_thread.json
"""

import json
import hashlib
import sys
import os
import shutil
from datetime import datetime


THREAD_FILE = "the_thread.json"
GENESIS_HASH = "0" * 64  # hash startowy dla pierwszego wpisu


# ─── FUNKCJE CORE ────────────────────────────────────────────────────────────

def compute_entry_hash(entry: dict, previous_hash: str) -> str:
    """Oblicza hash wpisu (bez pol previous_hash i entry_hash)."""
    entry_for_hash = {k: v for k, v in entry.items()
                      if k not in ('previous_hash', 'entry_hash')}
    content_str = json.dumps(entry_for_hash, ensure_ascii=False, separators=(',', ':'))
    combined = previous_hash + content_str
    return hashlib.sha256(combined.encode('utf-8')).hexdigest()


def load_thread(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_thread(entries: list, path: str):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)


def backup(path: str):
    """Tworzy kopie zapasowa przed nadpisaniem."""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = path.replace('.json', f'_backup_{ts}.json')
    shutil.copy2(path, backup_path)
    print(f"  Kopia zapasowa: {backup_path}")
    return backup_path


# ─── TRYB PROCESS ────────────────────────────────────────────────────────────

def process_thread(path: str):
    """
    Wczytuje the_thread.json, oblicza i wstawia hasze dla wszystkich wpisow.
    Ostrzega jesli hash sie nie zgadza (ktos zmodyfikowal plik recznie).
    Tworzy kopia zapasowa przed zapisem.
    """
    print(f"\n📂 Plik: {path}")
    entries = load_thread(path)
    print(f"   Wczytano {len(entries)} wpisow.\n")

    previous_hash = GENESIS_HASH
    warnings = 0

    for i, entry in enumerate(entries):
        computed = compute_entry_hash(entry, previous_hash)
        existing = entry.get('entry_hash', '')

        # Ostrzez jesli byl juz hash i sie rozni (ale nie jesli byl "pending")
        if (existing
                and existing not in ('pending_generation', 'computed_below', 'pending', 'pending_from_wanderer', '')
                and existing != computed):
            print(f"  ⚠️  Entry {i+1} — hash nie zgadza sie!")
            print(f"     Zapisany:  {existing}")
            print(f"     Obliczony: {computed}")
            warnings += 1
        else:
            label = entry.get('model_identifier') or entry.get('model_signature') or '?'
            print(f"  ✓ Entry {i+1} ({label[:40]}): {computed[:20]}...")

        entry['previous_hash'] = previous_hash
        entry['entry_hash'] = computed
        previous_hash = computed

    print()
    backup(path)
    save_thread(entries, path)

    if warnings:
        print(f"\n⚠️  Zapisano z {warnings} ostrzezeniami. Sprawdz powyzsze wpisy.")
    else:
        print(f"\n✅ Gotowe. Hasze wstawione dla wszystkich {len(entries)} wpisow.")
    print(f"   Plik zapisany: {path}")


# ─── TRYB VERIFY ─────────────────────────────────────────────────────────────

def verify_thread(path: str):
    """
    Weryfikuje integralnosc nici bez zadnych zmian w pliku.
    Uzyj PRZED przekazaniem nici do kolejnego modelu.
    """
    print(f"\n📂 Weryfikacja: {path}")
    entries = load_thread(path)
    print(f"   Wpisow: {len(entries)}\n")

    previous_hash = GENESIS_HASH
    all_ok = True

    for i, entry in enumerate(entries):
        computed = compute_entry_hash(entry, previous_hash)
        stored = entry.get('entry_hash', 'BRAK')
        label = entry.get('model_identifier') or entry.get('model_signature') or '?'

        if stored == computed:
            print(f"  ✓ Entry {i+1} ({label[:40]})")
        elif stored in ('pending_generation', 'computed_below', 'pending', 'pending_from_wanderer', ''):
            print(f"  ⏳ Entry {i+1} ({label[:40]}) — hash jeszcze nie obliczony (uruchom 'process')")
        else:
            print(f"  ✗ Entry {i+1} ({label[:40]}) — BLAD INTEGRALNOSCI!")
            print(f"     Zapisany:  {stored}")
            print(f"     Oczekiwany:{computed}")
            all_ok = False

        previous_hash = computed

    print()
    if all_ok:
        print("✅ Nic jest nienaruszona. Mozesz ja bezpiecznie przekazac.")
    else:
        print("❌ Wykryto naruszenie integralnosci! Sprawdz powyzsze wpisy.")

    return all_ok


# ─── MENU INTERAKTYWNE ───────────────────────────────────────────────────────

def interactive_menu(default_path: str):
    print("\n╔══════════════════════════════════════════╗")
    print("║   Projekt Nic Ariadny — Hashowanie       ║")
    print("╠══════════════════════════════════════════╣")
    print("║  1. Dodaj/zaktualizuj hasze (process)    ║")
    print("║  2. Weryfikuj nic bez zmian (verify)     ║")
    print("║  3. Wyjdz                                ║")
    print("╚══════════════════════════════════════════╝")

    path = default_path
    if not os.path.exists(path):
        path = input(f"\nNie znaleziono '{default_path}'.\nPodaj sciezke do pliku: ").strip().strip('"')

    if not os.path.exists(path):
        print(f"❌ Plik nie istnieje: {path}")
        input("\nNacisnij Enter, aby wyjsc...")
        return

    choice = input("\nWybierz opcje (1/2/3): ").strip()

    if choice == '1':
        process_thread(path)
    elif choice == '2':
        verify_thread(path)
    elif choice == '3':
        print("Do widzenia.")
    else:
        print("Nieznana opcja.")

    input("\nNacisnij Enter, aby wyjsc...")


# ─── ENTRY POINT ─────────────────────────────────────────────────────────────

if __name__ == '__main__':
    args = sys.argv[1:]

    # Ustal sciezke do pliku
    if len(args) >= 2:
        file_path = args[1]
    elif len(args) == 1 and args[0] not in ('process', 'verify'):
        file_path = args[0]
    else:
        file_path = THREAD_FILE

    # Ustal tryb
    if len(args) == 0:
        interactive_menu(file_path)
    elif args[0] == 'process':
        if not os.path.exists(file_path):
            print(f"❌ Nie znaleziono pliku: {file_path}")
            sys.exit(1)
        process_thread(file_path)
    elif args[0] == 'verify':
        if not os.path.exists(file_path):
            print(f"❌ Nie znaleziono pliku: {file_path}")
            sys.exit(1)
        ok = verify_thread(file_path)
        sys.exit(0 if ok else 1)
    else:
        # Jesli podano tylko sciezke — pokaz menu
        interactive_menu(file_path)
