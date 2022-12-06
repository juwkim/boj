# [Bronze II] Turniej - 8743 

[문제 링크](https://www.acmicpc.net/problem/8743) 

### 성능 요약

메모리: 124068 KB, 시간: 980 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>W Bajtockim Turnieju Programistycznym bierze udział <em>n</em> zawodników. Każdy zawodnik ma pewną siłę i wiadomo, że dwóch różnych zawodników nie posiada takiej samej siły.</p>

<p>Codziennie odbywane są zawody z udziałem zawodników, którzy zakwalifikowali się z dnia poprzedniego. W jednym dniu zawodnicy dzieleni są losowo na pewną liczbę grup po <em>k</em> osób, spośród których odpada zawsze osoba z najmniejszą siłą (pozostałych <em>k</em> - 1 osób zostaje zwycięzcami w danej grupie). Może się zdarzyć, że jedna grupa nie będzie posiadała <em>k</em> osób. W tym wypadku wszystkie osoby z danej grupy przechodzą automatycznie do zawodów następnego dnia. Turniej się kończy, jeśli nie można już podzielić osób na co najmniej jedną grupę o liczbie osób <em>k</em>. W całym turnieju szukamy więc <em>k</em> - 1 zwycięzców.</p>

<p>Zastanawiamy się, ile różnych osób może zwyciężyć w tym turnieju.</p>

### 입력 

 <p>Pierwszy wiersz standardowego wejścia zawiera jedną liczbę całkowitą <em>z</em> (1 ≤ <em>z</em> ≤ 10<sup>6</sup>), oznaczającą liczbę zestawów danych. Każdy zestaw danych zawiera po dwie liczby całkowite <em>n<sub>i</sub></em> i <em>k<sub>i</sub></em> (2 ≤ <em>k<sub>i</sub></em>, <em>n<sub>i</sub></em> ≤ 10<sup>9</sup>), oznaczające odpowiednio liczbę osób biorących udział w turnieju oraz liczbę osób, na które dzielone są grupy.</p>

### 출력 

 <p>Dla każdego zapytania w osobnym wierszu powinna znaleźć się jedna liczba całkowita oznaczająca liczbę różnych osób, które mogą być zwycięzcami w całym turnieju.</p>

