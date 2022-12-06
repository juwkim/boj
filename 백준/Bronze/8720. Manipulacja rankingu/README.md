# [Bronze II] Manipulacja rankingu - 8720 

[문제 링크](https://www.acmicpc.net/problem/8720) 

### 성능 요약

메모리: 68992 KB, 시간: 244 ms

### 분류

Empty

### 문제 설명

<p>Dymówka włamał się do obozowej sprawdzarki i może teraz manipulować rankingiem. Konkretniej mówiąc, może on ustawić wagę każdego zadania. Sumaryczna ilość punktów jest obliczana jako: <em>wagazadania</em><sub>1</sub> * <em>punktyzazadanie</em><sub>1</sub> + ... + <em>wagazadania</em><sub>m</sub> * <em>punktyzazadanie</em><sub>m</sub>. Zadania na obozie są oceniane binarnie: rozwiązanie otrzymuje 0 lub 100 punktów. Waga zadania może być ustawiona na dowolną liczbę całkowitą z przedziału [0, 2000]. Dymówka niestety nie umie wyliczyć, na ile opłaca mu się zmiana wag. Pomóż mu w tym.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajdują się dwie liczby całkowite <em>n</em>, <em>m</em> (1 ≤ <em>n</em>, <em>m</em> ≤ 1000), oznaczające odpowiednio liczbę uczestników obozu oraz liczbę zadań na obozie. W następnych <em>n</em> linijkach wyniki kolejnych uczestników: w każdej linijce <em>m</em> liczb (każda równa 0 lub 100) oznaczające wyniki uczestnika w kolejnych zadaniach. Wynik Dymówki jest podany jako pierwszy.</p>

### 출력 

 <p>W jedynej linijce wyjścia wypisz dwie liczby: pierwsza oznaczająca najlepszą pozycję w rankingu, jaką może zdobyć manipulacją Dymówka, oraz druga, oznaczająca minimalną liczbę osób, z którymi będzie on ex aequo na tej najlepszej pozycji. Pozycje w rankingu liczone są od 1.</p>

