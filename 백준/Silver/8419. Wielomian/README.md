# [Silver IV] Wielomian - 8419 

[문제 링크](https://www.acmicpc.net/problem/8419) 

### 성능 요약

메모리: 112748 KB, 시간: 304 ms

### 분류

사칙연산, 수학

### 제출 일자

2023년 11월 24일 22:50:30

### 문제 설명

<p>Dla danego wielomianu <em>W</em> oraz zadanej liczby <em>x</em>, wyznacz trzy ostatnie cyfry (cyfrę setek, dziesiątek i jedności) wartości wyrażenia <em>W</em>(<em>x</em>).</p>

<p>Napisz program, który:</p>

<ul>
	<li>wczyta opis wielomianu <em>W</em> oraz liczbę <em>x</em>,</li>
	<li>wyznaczy trzy ostatnie cyfry wartości wyrażenia <em>W</em>(<em>x</em>),</li>
	<li>wypisze wynik.</li>
</ul>

### 입력 

 <p>Pierwszy wiersz zawiera dwie liczby całkowite <em>s</em> (1 ≤ <em>s</em> ≤ 20,000) oraz <em>x</em> (-1,000,000 ≤ <em>x</em> ≤ 1,000,000). Drugi wiersz zawiera <em>s</em> liczb całkowitych <em>w</em><sub>1</sub>, <em>w</em><sub>2</sub>, ..., <em>w<sub>s</sub></em> (-1,000,000 ≤ <em>w<sub>k</sub></em> ≤ 1,000,000), pooddzielanych pojedynczymi odstępami. Liczby te, to kolejne współczynniki wielomianu: <em>W</em>(<em>x</em>) = <em>w</em><sub>1</sub><em>x</em><sup><em>s</em>-1</sup> + <em>w</em><sub>2</sub><em>x</em><sup><em>s</em>-2</sup> + .. + <em>w</em><sub><em>s</em>-1</sub><em>x</em> + <em>w<sub>s</sub></em>.</p>

### 출력 

 <p>Twój program powinien wypisać słowo zbudowane z trzech ostatnich cyfr liczby równej wartości wyrażenia <em>W</em>(<em>x</em>), w kolejności od cyfry setek do cyfry jedności.</p>

