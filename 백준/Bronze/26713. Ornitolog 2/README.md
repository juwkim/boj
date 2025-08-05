# [Bronze I] Ornitolog 2 - 26713 

[문제 링크](https://www.acmicpc.net/problem/26713) 

### 성능 요약

메모리: 119364 KB, 시간: 116 ms

### 분류

그리디 알고리즘

### 제출 일자

2025년 8월 6일 03:42:19

### 문제 설명

<p>Pliszka alternująca (Motacilla alterna) to gatunek ptaka z rodziny pliszkowatych. Wyróżnia go charakterystyczny śpiew, w którym wysokość tonu kolejnych dźwięków naprzemiennie rośnie i maleje. Dla przykładu, jeżeli będziemy reprezentować wysokości dźwięków za pomocą liczb całkowitych, to pliszka alternująca może zaśpiewać [2, 1, 3] i [4, 5, −6, −5], ale nie [1, 2, 3, 2] i [6, 5, 5, 4]. W celu nagrania tych fascynujących stworzeń ornitolog Bajtazar pozostawił swój dyktafon na kilka dni w lesie. Teraz zastanawia się, czy nagrane dźwięki są podobne do śpiewu pliszki.</p>

<p>Napisz program, który dla danego ciągu wysokości dźwięków wyznaczy minimalną liczbę jego wyrazów, które trzeba zmienić na dźwięk o dowolnej całkowitoliczbowej wysokości z przedziału [−10<sup>9</sup>, 10<sup>9</sup>], żeby ciąg przedstawiał możliwy śpiew pliszki alternującej.</p>

### 입력 

 <p>W pierwszym wierszu standardowego wejścia znajduje się jedna liczba całkowita n (3 ≤ n ≤ 50 000), oznaczająca długość nagrania.</p>

<p>Kolejny wiersz zawiera n liczb całkowitych a<sub>1</sub>, a<sub>2</sub>, . . . , a<sub>n</sub> (−1 000 000 ≤ a<sub>i</sub> ≤ 1 000 000), gdzie ai jest wysokością i-tego dźwięku w nagraniu.</p>

### 출력 

 <p>Na wyjściu powinna znaleźć się jedna liczba całkowita, oznaczająca minimalną liczbę zmienionych dźwięków.</p>

