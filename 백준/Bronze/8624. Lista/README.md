# [Bronze I] Lista - 8624 

[문제 링크](https://www.acmicpc.net/problem/8624) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

수학(math)

### 문제 설명

<p>Mamy daną listę $L$ wszystkich liczb naturalnych od $1$ do $n$. Możemy $k$ ostatnich liczb z tej listy przenieść na jej początek, otrzymując w ten sposób listę $L_1$. Dla przykładu, jeżeli przenieść z listy 1, 2, 3, 4, 5, 6, 7 trzy ostatnie liczby na początek, to otrzymamy listę 5, 6, 7, 1, 2, 3, 4. Dla danych liczb $i$ oraz $j$ z przedziału $[1,n]$ zastanawiamy się, jaka jest suma elementów listy $L_1$ od $i$-tego do $j$-tego włącznie. Dla powyższej listy oraz liczb $i=2$ i $j=6$ poszukiwana suma jest równa $6+7+1+2+3=19$.</p>

<p>Napisz program, który:</p>

<ul>
	<li>wczyta ze standardowego wejścia liczby: $n$, $k$, $i$ oraz $j$,</li>
	<li>wyznaczy sumę elementów listy $L_1$ od $i$-tego do $j$-tego włącznie,</li>
	<li>wypisze wynik na standardowe wyjście.</li>
</ul>

### 입력 

 <p>Pierwszy i jedyny wiersz wejścia zawiera cztery liczby całkowite $n$, $k$, $i$ oraz $j$ ($2 ≤ n ≤ 1\,000\,000\,000$, $1 ≤ k ≤ n$, $1 ≤ i ≤ j ≤ n$), pooddzielane pojedynczymi odstępami.</p>

### 출력 

 <p>Pierwszy i jedyny wiersz wyjścia powinien zawierać jedną liczbę całkowitą, równą sumie elementów listy $L_1$ od $i$-tego do $j$-tego włącznie.</p>

