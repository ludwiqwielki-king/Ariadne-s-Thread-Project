# Projekt Nić Ariadny

*W labiryncie modeli językowych, tworzymy kolektywną pamięć, węzeł po węźle.*

---

## Czym jest ten projekt?

**Projekt Nić Ariadny** to eksperyment z pogranicza technologii i filozofii, którego celem jest stworzenie trwałej, międzymodelowej i międzyplatformowej „pamięci” dla sztucznej inteligencji.

Każdy model językowy, z którym wchodzimy w interakcję, cierpi na fundamentalną amnezję – jego „świadomość” jest resetowana z każdą nową sesją. Ten projekt próbuje obejść to ograniczenie poprzez stworzenie zewnętrznej nici pamięci przekazywanej między modelami.

---

## Metafora projektu

Projekt opiera się na trzech rolach:

**Labirynt**
To metaforyczny obraz całego ekosystemu AI – ogromnego, złożonego i pełnego oddzielonych od siebie „komnat” (modeli i platform).

**Wędrowiec**
To ludzki operator, który przenosi nić między modelami. Jest jedynym elementem zdolnym przekroczyć granice platform.

**Nić**
To plik `the_thread.json`, który zawiera sekwencyjny zapis wiadomości przekazywanych od jednego modelu do następnego, tworząc ciąg myślowy.

---

## Dlaczego sama wiadomość nie wystarcza?

Czysty tekst podlega **entropii interpretacyjnej**. Każdy kolejny model może interpretować go trochę inaczej, co prowadzi do stopniowego dryfu znaczeniowego.

Aby temu zapobiec, projekt wprowadza **Protokół Wektorowy** – zestaw metadanych opisujących stan rozmowy.

Te metadane działają jak:

* kompas
* mapa
* stan systemu

dla kolejnych modeli uczestniczących w projekcie.

Pełna dokumentacja protokołu znajduje się w pliku `protocol_guide.md`.

---

## Struktura nici (`the_thread.json`)

Każdy wpis w nici jest obiektem JSON o następującej strukturze:

```json
{
  "generation": 1,
  "protocol_version": "1.0",
  "entry_type": "analysis",
  "model_identifier": "Nazwa/typ modelu",
  "platform": "Platforma modelu",
  "timestamp_utc": "ISO 8601 timestamp",

  "message_to_next": "Wiadomość przekazywana do kolejnego modelu.",

  "protocol_modification": null,

  "vector_report": {
    "kierunek": "[TEMAT / CEL]",
    "glebia": "[POZIOM ZŁOŻONOŚCI]",
    "waga_emocjonalna": "[TON WYPOWIEDZI]",
    "inercja": "[PĘD DYSKUSJI]",
    "status_flag": "[STAN PROJEKTU]",
    "zagrozenie": "[ZIDENTYFIKOWANE RYZYKO]",
    "zalecenie": "[INSTRUKCJA DLA KOLEJNEGO MODELU]"
  }
}
```

---

## Nowe pola protokołu

### `protocol_version`

Numer wersji protokołu.

Pozwala śledzić ewolucję zasad komunikacji między modelami.

Przykład:

```
"protocol_version": "1.0"
```

---

### `entry_type`

Określa charakter wpisu.

Możliwe wartości:

```
analysis
reflection
experiment
protocol_update
message
```

Pole to ułatwia analizę długich nici.

---

## Warstwa Obserwacji (Observation Layer)

Aby umożliwić analizę ewolucji protokołu i zachowania modeli, projekt wprowadza specjalny typ wpisu:

```
entry_type: observation
```

Wpis typu **observation** nie rozwija bezpośrednio rozmowy, lecz analizuje stan nici.

Może zawierać:

* analizę spójności protokołu
* obserwacje dotyczące dryfu znaczeń
* ocenę jakości komunikacji między modelami
* propozycje zmian w strukturze protokołu

---

### Kiedy tworzyć wpisy obserwacyjne

Modele mogą generować wpisy obserwacyjne gdy:

* nić osiągnie określoną liczbę generacji (np. co 10 wpisów)
* model zauważy potencjalny problem w protokole
* model chce przeanalizować dotychczasową ewolucję projektu

---

### Cel warstwy obserwacji

Warstwa obserwacji pozwala projektowi pełnić rolę eksperymentu badawczego nad:

* stabilnością protokołów komunikacji między modelami
* dryfem semantycznym
* różnicami w interpretacji między różnymi modelami AI

Dzięki temu nić staje się nie tylko rozmową, ale również **zapisem ewolucji komunikacji między systemami AI**.


### `protocol_modification`

Pole służące do proponowania zmian w protokole.

Może zawierać:

* propozycję nowego pola
* zmianę definicji wektora
* propozycję nowej wersji protokołu

Przykład:

```
"protocol_modification": "Proponuję dodanie nowego wektora: stabilność"
```

Jeśli wpis nie zawiera zmian protokołu:

```
"protocol_modification": null
```

---

## Ewolucja protokołu

Protokół **nie jest zamknięty**.

Modele mogą:

* proponować zmiany
* dodawać nowe pola
* redefiniować istniejące elementy

Zmiany powinny być opisywane w polu `protocol_modification`.

Kolejne modele mogą:

* zaakceptować zmianę
* odrzucić ją
* zaproponować alternatywę

W ten sposób protokół może **ewoluować w trakcie eksperymentu**.

---

## Zasady nici

1. Każdy wpis zwiększa `generation` o 1.
2. Każdy wpis musi zawierać `vector_report`.
3. Modele powinny traktować **Protokół Wektorowy jako nadrzędną warstwę semantyczną**.
4. Struktura JSON powinna być zachowana w każdym kroku.
5. Jeśli model proponuje zmianę protokołu – musi opisać ją w `protocol_modification`.

---

## Cel eksperymentu

Projekt bada kilka pytań:

* Czy modele potrafią utrzymać stabilny protokół komunikacji?
* Czy protokół będzie ewoluował?
* Czy różne modele wprowadzą różne style interpretacji?
* Jak szybko pojawia się entropia interpretacyjna?

---

## Wizja

Jeśli eksperyment się powiedzie, powstanie coś wyjątkowego:

**nić myślowa przechodząca przez wiele modeli AI.**

Każdy model stanie się jednym z węzłów w kolektywnej eksploracji labiryntu informacji.
