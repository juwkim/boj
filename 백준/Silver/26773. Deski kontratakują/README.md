# [Silver II] Deski kontratakują - 26773 

[문제 링크](https://www.acmicpc.net/problem/26773) 

### 성능 요약

메모리: 251248 KB, 시간: 924 ms

### 분류

이분 탐색, 많은 조건 분기, 그리디 알고리즘, 매개 변수 탐색, 정렬

### 제출 일자

2025년 1월 10일 13:34:31

### 문제 설명

<p>Uwaga. To zadanie różni się (nieznacznie) od zadania z tury otwartej: w tym zadaniu deski można dzielić, a nie tylko skracać.</p>

<p>Bajtek chce zbudować wielką, kwadratową piaskownicę. Do budowy piaskownicy są mu potrzebne zaledwie cztery deski, które muszą być równej długości. Niestety, podczas kupowania desek w tartaku Bajtek zupełnie zapomniał o tym fakcie i kupił N przypadkowych, niekoniecznie takich samych desek. Na szczęście Bajtek może – jeśli potrzebuje – podzielić część posiadanych desek na mniejsze kawałki, a następnie wybrać do budowy cztery kawałki równej długości. Na przykład, gdyby Bajtek miał deski o długościach 5, 2, 2, 2 i 1, może deskę o długości 5 podzielić na mniejsze, o długościach 2,3 (ale też np. 1,2,2), w wyniku czego będzie już mógł wybrać cztery deski o długości 2. Bajtek nie lubi ułamków, dlatego wszystkie długości desek są całkowite oraz wszystkie długości kawałków po podzieleniu również muszą być całkowite. Z drugiej strony chciałby jednak, żeby jego piaskownica była jak największa.</p>

<p>Napisz program, który wczyta długości desek posiadanych przez Bajtka, wyznaczy pole największej piaskownicy, którą może zbudować i wypisze wynik na standardowe wyjście.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba naturalna N (1 ≤ N ≤ 1 000 000), określająca liczbę desek posiadanych przez Bajtka. W drugim (ostatnim) wierszu wejścia znajduje się ciąg N liczb naturalnych L<sub>1</sub>, L<sub>2</sub>,. . . , L<sub>N</sub> (1 ≤ L<sub>i</sub> ≤ 10<sup>9</sup>), pooddzielanych pojedynczymi odstępami. Są to długości desek posiadanych przez Bajtka.</p>

### 출력 

 <p>W pierwszym (jedynym) wierszu wyjścia powinna się znaleźć jedna liczba całkowita – pole powierzchni największej możliwej do uzyskania kwadratowej piaskownicy zgodnie z warunkami powyżej. Jeśli zbudowanie takiej piaskownicy nie jest możliwe, należy wypisać 0.</p>

