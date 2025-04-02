# [Silver II] Liczbowy proces - 26775 

[문제 링크](https://www.acmicpc.net/problem/26775) 

### 성능 요약

메모리: 206896 KB, 시간: 868 ms

### 분류

이분 탐색, 자료 구조, 해시를 사용한 집합과 맵, 구현, 시뮬레이션

### 제출 일자

2025년 4월 3일 07:26:01

### 문제 설명

<p>Rozważmy funkcję f(n) zwracającą sumę cyfr liczby n. Na przykład: f(2019) = 2 + 0 + 1 + 9 = 12. Rozważmy też funkcję g(n) = n + f(n)<sup>2</sup>. Na przykład: g(2019) = 2019 + f(2019)<sup>2</sup> = 2019 + 12<sup>2</sup> = 2019 + 144 = 2163.</p>

<p>Bajtazarowi bardzo podoba się funkcja g. Rozpoczyna następujący proces: zaczyna od n = 1, oblicza g(n) i przyjmuje to jako nową wartość n. Następnie ponownie oblicza g(n) i ponownie podmienia n na uzyskany wynik, i tak dalej. Pierwsze cztery liczby uzyskane w wyniku tego procesu to 1,2,6,42.</p>

<p>Bajtazar ma wiele swoich ulubionych liczb i dla każdej z nich zastanawia się czy może ona być uzyskana wskutek jego procesu. Pomóż mu!</p>

<p>Napisz program, który wczyta zapytania Bajtazara, dla każdej podanej przez niego liczby wyznaczy czy jest możliwe jej uzyskanie przez jego proces i wypisze wyniki na standardowe wyjście.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba naturalna Q (1 ≤ Q ≤ 100 000), określająca liczbę zapytań Bajtazara. W kolejnych Q wierszach znajdują się kolejne zapytania Bajtazara, po jednym w wierszu. Opis każdego z zapytań składa się z jednej liczby naturalnej M<sub>i</sub> (1 ≤ M<sub>i</sub> ≤ 5 · 10<sup>9</sup>), określającej zapytanie Bajtazara o to, czy wskutek jego procesu jest możliwe uzyskanie liczby M<sub>i</sub>.</p>

### 출력 

 <p>Twój program powinien wypisać na wyjście dokładnie Q wierszy. W i-tym z nich powinna się znaleźć odpowiedź dla i-tego zapytania Bajtazara: słowo <code>TAK</code> lub <code>NIE</code> w zależności od tego, czy jest możliwe uzyskanie liczby M<sub>i</sub> w procesie Bajtazara.</p>

