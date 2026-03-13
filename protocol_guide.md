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
