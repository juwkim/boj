# [Silver III] Pionki - 26762 

[문제 링크](https://www.acmicpc.net/problem/26762) 

### 성능 요약

메모리: 387772 KB, 시간: 864 ms

### 분류

애드 혹

### 제출 일자

2024년 5월 2일 04:02:17

### 문제 설명

<p>Bajtek gra w Pionki, prostą grę planszową dla jednego gracza. Na niektórych polach szachownicy o wymiarach N × M stoją pionki, na każdym polu co najwyżej jeden. W jednym ruchu można przesunąć pionek o dowolną liczbę pól w pionie lub poziomie, być może przeskakując inne pionki lub wskakując na pole, na którym stoją już jakieś pionki. Celem gry jest sprawić, aby wszystkie pionki stanęły na tym samym polu, wykonując przy tym jak najmniejszą liczbę ruchów.</p>

<p>Bajtek zastanawia się, czy gra w tę grę optymalnie. Pomóż mu i napisz program, który wczyta sytuację początkową na planszy i wyznaczy minimalną liczbę ruchów prowadzących do osiągnięcia celu.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajdują się dwie dodatnie liczby całkowite N i M (1 ≤ N · M ≤ 1 000 000) oddzielone pojedynczym odstępem i określające kolejno: wysokość i szerokość szachownicy. W kolejnych N wierszach znajduje się opis sytuacji początkowej na szachownicy. Każdy z tych wierszy zawiera po M znaków. Znak . (kropka) oznacza, że dane pole jest puste, zaś # (hasz) oznacza, że na tym polu stoi pionek.</p>

### 출력 

 <p>W pierwszym (jedynym) wierszu wyjścia należy wypisać jedną liczbę całkowitą – minimalną liczbę ruchów potrzebną do sprowadzenia wszystkich pionków na to samo pole.</p>

