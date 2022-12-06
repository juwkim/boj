# [Bronze I] Konduktor - 8805 

[문제 링크](https://www.acmicpc.net/problem/8805) 

### 성능 요약

메모리: 196124 KB, 시간: 384 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Konduktor Konrad zajmuje się sprawdzaniem biletów w pociągach jednej z dwóch dużych spółek kolejowych.</p>

<p>W jego pociągu znajduje się <strong>N</strong> przedziałów ponumerowanych od 1 do <strong>N</strong>. Konrad odwiedza je, zaczynając od przedziału z numerem 1, w następującej kolejności: 1, 2, ... , <strong>N</strong>-1, <strong>N</strong>, <strong>N</strong>-1, ... , 2, 1, 2, itd. </p>

<p>Znając <strong>N</strong> - liczbę przedziałów w pociągu oraz <strong>K</strong> - liczbę odwiedzonych przedziałów, oblicz ile razy Konrad odwiedził każdy z przedziałów.</p>

### 입력 

 <p>W pierwszej linii znajduje się jedna liczba naturalna <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10 ) oznaczająca liczbę zestawów testowych. Następnie opisywane są kolejne zestawy.</p>

<p>W pierwszej i jedynej linii zestawu znajduje się para liczb naturalnych <strong>N</strong> ( 1 <= <strong>N</strong> <= 10<sup>6</sup> ) i <strong>K</strong> ( 1 <= <strong>K</strong> <= 10<sup>9</sup> ).</p>

### 출력 

 <p>Dla każdego zestawu testowego w osobnej linii należy wypisać oddzielone spacjami <strong>N</strong> liczb <strong>A</strong><sub><strong>i</strong></sub>, gdzie <strong>A</strong><sub><strong>i</strong></sub> oznacza liczbę kontroli biletów w <strong>i</strong>-tym przedziale. </p>

