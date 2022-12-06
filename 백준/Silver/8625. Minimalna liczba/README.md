# [Silver V] Minimalna liczba - 8625 

[문제 링크](https://www.acmicpc.net/problem/8625) 

### 성능 요약

메모리: 113248 KB, 시간: 104 ms

### 분류

수학(math), 비둘기집 원리(pigeonhole_principle)

### 문제 설명

<p>Dany jest zbiór liczb całkowitych $A$. Należy znaleźć najmniejszą liczbę całkowitą dodatnią nienależącą do zbioru $A$ i podzielną przez pewną z góry ustaloną liczbę $k$.</p>

<p>Napisz program, który:</p>

<ul>
	<li>wczyta ze standardowego wejścia opis zbioru $A$ oraz liczbę $k$,</li>
	<li>wyznaczy najmniejszą liczbę całkowitą dodatnią, której nie ma w zbiorze $A$ i która jest podzielna przez $k$,</li>
	<li>wypisze wynik na standardowe wyjście.</li>
</ul>

### 입력 

 <p>W pierwszym wierszu wejścia znajdują się dwie liczby całkowite $n$ oraz $k$ ($1 ≤ n ≤ 1\,000\,000$, $1 ≤ k ≤ 10^{12}$), oddzielone pojedynczym odstępem. Liczba $n$ oznacza moc (liczbę elementów) zbioru $A$. Drugi wiersz wejścia zawiera $n$ liczb całkowitych $a_i$ ($1 ≤ a_i ≤ 10^{18}$), pooddzielanych pojedynczymi odstępami i oznaczających elementy zbioru $A$. Liczby $a_i$ są parami różne.</p>

### 출력 

 <p>Twój program powinien wypisać w pierwszym i jedynym wierszu wyjścia jedną liczbę całkowitą, będącą najmniejszą liczbą dodatnią niewystępującą w zbiorze $A$, podzielną przez $k$.</p>

