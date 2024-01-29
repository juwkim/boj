# [Silver III] Kodowanie - 8857 

[문제 링크](https://www.acmicpc.net/problem/8857) 

### 성능 요약

메모리: 109240 KB, 시간: 128 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 1월 30일 05:20:00

### 문제 설명

<p>Pawła, studenta informatyki na Uniwersytecie Wrocławskim, w ostatnim semestrze bardzo zaciekawiły problemy poruszane na przedmiocie Kompresja danych. Jako zdolny uczeń, Paweł postanowił wymyślić nowy sposób na kompresję sekwencji liczb naturalnych.</p>

<p>Pierwszym krokiem algorytmu Pawła jest zamiana ciągów liczb naturalnych na ciągi liczb zapisanych binarnie. Nie można zrobić tego tak po prostu - trzeba umieć oddzielać kolejne kodowane liczby używając tylko zer i jedynek. W tym celu, Paweł postanowił wykorzystać dwie sąsiednie jedynki jako znacznik końca pojedynczej liczby. Ta metoda pociąga za sobą jednak pewne konsekwencje. Aby móc rozdzielać kolejne elementy ciągu, binarny kod żadnej z liczb nie może zawierać dwóch sąsiednich jedynek, a także musi zaczynać się od jedynki.</p>

<p>Chcąc zbadać skuteczność kompresji, Paweł potrzebuje wiedzieć ile różnych liczb jest w stanie zakodować używając <strong>n</strong> bitów. Niestety, Paweł w obecnym semestrze ma sporo pracy - poprosił więc Ciebie o pomoc. Twoim zadaniem jest napisanie programu, który dla podanej wartości <strong>n</strong> obliczy ile jest różnych, binarnych kodów długości <strong>n</strong>, które zaczynają się od jedynki i nie zawierają dwóch jedynek koło siebie.</p>

### 입력 

 <p>W pierwszej linii wejścia znajduje się jedna liczba całkowita <strong>T</strong> (1<=<strong>T</strong><=100), oznaczająca ilość zestawów danych. Następnie na wejściu podane są opisy kolejnych zestawów danych. Pojedynczy zestaw danych składa się z jednej linii. Znajduje się w niej jedna liczba całkowita <strong>n</strong> (1<=<strong>n</strong><=45).<strong> </strong></p>

### 출력 

 <p>Dla każdego zestawu danych Twój program powinien wypisać pojedynczą linię zawierającą jedną liczbę całkowitą. Jest to liczba różnych ciągów zero-jedynkowych długości <strong>n</strong>, które zaczynają się od jedynki i nie zawierają dwóch sąsiednich jedynek.</p>

