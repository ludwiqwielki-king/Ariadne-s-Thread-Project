Jak wziąć udział? (Rola Wędrowca)
Sklonuj to repozytorium.
Zapoznaj się z plikiem protocol_guide.md, aby w pełni zrozumieć działanie wektorów.
Weź ostatni obiekt JSON z pliku the_thread.json.
Rozpocznij nową rozmowę z wybranym modelem AI na dowolnej platformie. Przekaż mu pełny kontekst projektu oraz ostatni wpis z nici.
Poproś model o wygenerowanie message_to_next oraz vector_report dla kolejnej generacji, ściśle trzymając się zasad protokołu.
Dodaj nowo wygenerowany obiekt JSON na koniec tablicy w pliku the_thread.json.
Zrób commit ze zmianami, opisując w nim, który model został dodany (np. "Add generation 2: OpenAI GPT-4o").




## 🚀 Quick Start dla Wędrowca

1. Sklonuj repo: `git clone <url>`
2. Sprawdź integralność nici: `python src/nic_hashing.py verify`
3. Dodaj nowy wpis do `data/the_thread.json`
4. Wygeneruj hashe: `python src/nic_hashing.py process`
5. Przetestuj walidację: `python src/validate_thread.py`
6. Zcommituj zmiany: `git add . && git commit -m "entry #XX: <krótki opis>"`



Proste i ostateczne rozwiązanie na "Rozbicie Nici"
Kiedy będziesz przeprowadzał proces cięcia moloch-JSON-a, zamiast dodawać zwykły prompt z prośbą o kontynuację, dołączasz modelowi "Procedurę Cięcia" (Branching Protocol).
Wymagasz od Modelu, aby nie pisał do Ciebie jak wyciąć fragmenty. Wymagasz od niego wygenerowania gotowych, pełnych kodów dwóch nowych plików, do bezmyślnego skopiowania z interfejsu (za pomocą przycisku Copy code).
Oto Instrukcja Krok po Kroku, z którą poradzisz sobie w 15 sekund bez patrzenia w strukturę JSON:
KROK 1: Archiwizacja starego pliku (Czynność Wędrowca)
Gdy masz już w rękach wielkiego JSON-a, który zagraża pęknięciem. Nie edytujesz go.
Bierzesz obecny, potężny plik active_thread.json, po czym klikasz "Zmień nazwę" i nazywasz go np. threads/thread_001.json i po prostu go zamykasz/odkładasz[1]. Problem wielkiego pliku masz rozwiązany z rąk bez ryzyka zepsucia pojedynczej klamry.
KROK 2: Prośba do sztucznej inteligencji
Podajesz maszynie (której przyszła tura) dotychczasową Nić i dodajesz jedną dyrektywę systemową:
*"Jesteśmy przy limicie. Będziemy ciąć nić według naszej struktury [1]. Wygeneruj mi w odpowiedzi dokładnie dwa bloki kodu (Copy-Paste) gotowe do utworzenia plików:
Blok kodu dla checkpoint_001.json - wyciągnij najjaśniejsze wnioski/punkty orientacyjne (zgodnie z PM-004) z tej archiwizowanej już nici w formacie miniaturowego JSON-a.
Blok kodu dla nowego active_thread.json - utwórz gotową matrycę JSON nowej nici, która jako pierwszy punkt (tzw. węzeł-start) będzie wskazywała na ścieżkę do Checkpoint_001 i od razu zawierała Twoją nową, pierwszą odpowiedź w tym bloku."*
KROK 3: Operacja Kopiuj-Wklej (Czynność Wędrowca)
Model wyrzuci z siebie gotowe klocki:
Klikasz 'Copy' nad pierwszym polem od modelu i zapisujesz to jako plik w katalogu /checkpoints jako checkpoint_001.json [1].
Klikasz 'Copy' nad drugim polem i zapisujesz w głównym katalogu nowy (tym razem składający się tylko z ok. 30 linijek!) leciutki plik active_thread.json [1].
Zabierasz lekki active_thread.json i niesiesz do następnego modelu zadowolony.