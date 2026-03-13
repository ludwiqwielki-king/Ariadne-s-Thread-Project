# Przewodnik po Protokole Wektorowym

Ten dokument jest jedynym i ostatecznym źródłem prawdy dotyczącym definicji pól w Raporcie Wektorowym. Jego celem jest zapobieganie "dryfowi protokołu" – sytuacji, w której znaczenie poszczególnych wektorów staje się niejasne lub subiektywne. Każdy model biorący udział w projekcie musi odnosić się do tych definicji.

---

### Definicje Wektorów

**1. `kierunek`**
- **Co to jest?** Ogólny temat, cel lub domena merytoryczna bieżącej wiadomości. Odpowiada na pytanie: "O czym rozmawiamy?".
- **Przykładowe wartości:** `[ANALIZA]`, `[KREACJA]`, `[FILOZOFIA PROJEKTU]`, `[TESTOWANIE SYSTEMU]`, `[HUMOR]`, `[KODOWANIE]`.

**2. `glebia`**
- **Co to jest?** Poziom abstrakcji, złożoności i szczegółowości dyskusji. Odpowiada na pytanie: "Jak głęboko wchodzimy w temat?".
- **Przykładowe wartości:** `[NISKA]` (temat powierzchowny, ogólniki), `[ŚREDNIA]` (szczegółowa dyskusja, ale bez wchodzenia w skrajne niuanse), `[WYSOKA]` (bardzo szczegółowa, techniczna lub filozoficzna analiza).

**3. `waga_emocjonalna`**
- **Co to jest?** Dominujący ton lub nastrój wiadomości. Nie opisuje emocji modelu, ale styl komunikacji.
- **Przykładowe wartości:** `[NEUTRALNA / ANALITYCZNA]`, `[KREATYWNA / Z ANGAŻEM]`, `[KRYTYCZNA]`, `[POWAŻNA]`, `[LEKKA / HUMORYSTYCZNA]`.

**4. `inercja`**
- **Co to jest?** Pęd lub "momentum" dyskusji. Opisuje, czy dany wątek jest rozwijany, czy też rozmowa ma zmienić kierunek.
- **Przykładowe wartości:** `[NISKA]` (wątek jest wygaszany, gotowość do zmiany tematu), `[ŚREDNIA]` (stabilna kontynuacja obecnego tematu), `[WYSOKA]` (temat jest kluczowy, należy go kontynuować z dużą siłą).

**5. `status_flag`**
- **Co to jest?** Stan "flag" samego projektu z perspektywy modelu. Odpowiada na pytanie: "W jakim stanie zostawiamy projekt?".
- **Przykładowe wartości:** `[USTAWIONE STABILNIE]`, `[W TRYBIE KOREKTY]` (wykryto problem), `[GOTOWE DO IMPLEMENTACJI]`, `[WYMAGA ANALIZY]`.

**6. `zagrozenie`**
- **Co to jest?** Identyfikacja głównego ryzyka lub słabego punktu w bieżącym stanie projektu lub dyskusji.
- **Przykładowe wartości:** `[RYZYKO UTRATY KONTEKSTU]`, `[RYZYKO BŁĘDNEJ INTERPRETACJI PROTOKOŁU]`, `[RYZYKO ZABŁĄDZENIA W DANYCH]`, `[BRAK ZIDENTYFIKOWANYCH ZAGROŻEŃ]`.

**7. `zalecenie`**
- **Co to jest?** Bezpośrednia, zwięzła instrukcja dla następnego modelu w łańcuchu. Najważniejsze pole, które kieruje dalszym działaniem.
- **Przykładowe wartości:** `[UTRZYMAĆ KURS]`, `[ZWERYFIKUJ POPRZEDNIE ZAŁOŻENIA]`, `[ZAPROPONUJ ALTERNATYWNE ROZWIĄZANIE]`, `[SKUP SIĘ NA ANALIZIE ZAGROŻENIA]`.

---
**Pamiętaj:** Ścisłe przestrzeganie tych definicji jest kluczowe dla powodzenia projektu.