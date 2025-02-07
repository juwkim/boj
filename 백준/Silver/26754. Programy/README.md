# [Silver II] Programy - 26754 

[문제 링크](https://www.acmicpc.net/problem/26754) 

### 성능 요약

메모리: 339312 KB, 시간: 904 ms

### 분류

그리디 알고리즘, 정렬, 두 포인터

### 제출 일자

2025년 2월 7일 21:03:05

### 문제 설명

<p>Bajtazar zmienia właśnie komputer, musi więc przenieść swoje aktualne oprogramowanie ze starego komputera na nowy. Praca jaką wykonuje Bajtazar wymaga od niego szczególnej dbałości o bezpieczeństwo, dlatego wysyłanie programów do chmury czy przez e-mail nie wchodzi w grę. Zamiast tego Bajtazar postanowił użyć ulubionego nośnika – płyt CD!</p>

<p>Izolacja jest najlepszą metodą bezpieczeństwa, dlatego na każdej płycie Bajtazar zapisze co najwyżej jeden program, niezależnie od tego ile wolnego miejsca miałoby zostać na płycie. Aby wygodnie korzystać z oprogramowania na nowym komputerze Bajtazar postanowił, że nie będzie dzielił programów na wiele płyt CD, to znaczy każdy program będzie zapisany w jednym kawałku na co najwyżej jednej płycie.</p>

<p>Każdy program zajmuje odpowiednią ilość miejsca i każda płyta ma też swoją pojemność. Oczywiście aby zapisać program na danej płycie ilość zajmowanego przez niego miejsca nie może być większa od pojemności płyty.</p>

<p>Być może Bajtazar nie zorientował się jeszcze, że może nie być stanie w ten sposób przenieść wszystkiego – oblicz, ile najwięcej programów będzie jest w stanie przenieść przestrzegając swoich zasad.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba naturalna N (1 ≤ N ≤ 1 000 000) określająca liczbę programów. W drugim wierszu wejścia znajduje się N liczb naturalnych A<sub>i</sub> (1 ≤ A<sub>i</sub> ≤ 10<sup>9</sup>) pooddzielanych pojedynczymi odstępami oznaczających rozmiary kolejnych programów w bajtach.</p>

<p>W trzecim wierszu wejścia znajduje się jedna liczba naturalna M (1 ≤ M ≤ 1 000 000), określająca liczbę płyt. W czwartym (ostatnim) wierszu wejścia znajduje się ciąg M liczb naturalnych B<sub>i</sub> (1 ≤ B<sub>i</sub> ≤ 10<sup>9</sup>) pooddzielanych pojedynczymi odstępami oznaczających pojemności kolejnych płyt w bajtach.</p>

### 출력 

 <p>Twój program powinien wypisać na wyjście dokładnie jedną liczbę całkowitą oznaczającą największą możliwą liczbę programów, którą da się przenieść na płytach zgodnie z zasadami Bajtazara.</p>

