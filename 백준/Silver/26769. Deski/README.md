# [Silver IV] Deski - 26769 

[문제 링크](https://www.acmicpc.net/problem/26769) 

### 성능 요약

메모리: 261688 KB, 시간: 616 ms

### 분류

그리디 알고리즘, 수학, 정렬

### 문제 설명

<p>Bajtek chce zbudować wielką, kwadratową piaskownicę. Do budowy piaskownicy są mu potrzebne zaledwie cztery deski, które muszą być równej długości. Niestety, podczas kupowania desek w tartaku Bajtek zupełnie zapomniał o tym fakcie i kupił N desek o niekoniecznie równych długościach. Bajtek może (ale nie musi) najpierw skrócić posiadane deski, a następnie wybrać cztery kawałki równej długości i zbudować z nich piaskownicę. Zauważ, że deska może jedynie być skracana, a nie dzielona, czyli nie można na przykład z jednej deski o długości 4 otrzymać dwóch desek o długości 2. Bajtek nie lubi ułamków, dlatego wszystkie długości desek są całkowite oraz wszystkie długości skróconych kawałków również muszą być całkowite.</p>

<p>Napisz program, który: wczyta długości desek posiadanych przez Bajtka, wyznaczy pole największej piaskownicy, którą może zbudować i wypisze wynik na standardowe wyjście.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba naturalna N (1 ≤ N ≤ 1 000 000), określająca liczbę desek posiadanych przez Bajtka. W drugim (ostatnim) wierszu wejścia znajduje się ciąg N liczb naturalnych L<sub>1</sub>, L<sub>2</sub>,. . . , L<sub>N</sub> (1 ≤ L<sub>i</sub> ≤ 10<sup>9</sup>), pooddzielanych pojedynczymi odstępami. Są to długości desek posiadanych przez Bajtka.</p>

### 출력 

 <p>W pierwszym (jedynym) wierszu wyjścia powinna się znaleźć jedna liczba całkowita – pole powierzchni największej możliwej do uzyskania kwadratowej piaskownicy zgodnie z warunkami powyżej. Jeśli zbudowanie takiej piaskownicy nie jest możliwe, należy wypisać 0.</p>

