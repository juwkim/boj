# [Bronze III] Test - 8815 

[문제 링크](https://www.acmicpc.net/problem/8815) 

### 성능 요약

메모리: 121220 KB, 시간: 108 ms

### 분류

사칙연산(arithmetic), 수학(math), 문자열(string)

### 문제 설명

<p>Hektor lubi kartkówki w formie testów w których każde pytanie ma cztery możliwe odpowiedzi ( A, B, C lub D ). Kiedy nie zna prawidłowych odpowiedzi, zamiast strzelać, zaznacza odpowiedzi według schematu:</p>

<ol>
	<li>W pierwszym zadaniu odpowiedź A</li>
	<li>W drugim zadaniu kolejna litera w stosunku do poprzednio wybranej, ( B )</li>
	<li>W trzecim zadaniu kolejna litera w stosunku do poprzednio wybranej, ( C )</li>
	<li>W czwartym zadaniu "o jeden mniejsza" litera w stosunku do poprzednio wybranej ( B )</li>
</ol>

<p>A następnie do końca testu powtarza punkty 2,3,4 ( choć konkretne litery w nawiasie oczywiście się zmieniają).</p>

<ul>
	<li>Kolejna litera po A to B</li>
	<li>Kolejna litera po B to C</li>
	<li>Kolejna litera po C to D</li>
	<li>Kolejna litera po D to A</li>
</ul>

<ul>
	<li>Litera o jeden mniejsza od A to D</li>
	<li>Litera o jeden mniejsza od B to A</li>
	<li>Litera o jeden mniejsza od C to B</li>
	<li>Litera o jeden mniejsza od D to C</li>
</ul>

<p>Tak więc na pierwsze 12 pytań Hektor będzie odpowiadał kolejno: ABCBCDCDADAB.</p>

<p>Jak odpowie na <strong>N</strong>-te pytanie? </p>

### 입력 

 <p>W pierwszej linii wejścia znajduje się liczba zestawów testowych <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 1 0 ).</p>

<p>W każdej z kolejnych <strong>Z</strong> linii znajduje się jedna liczba całkowita, <strong>N</strong> ( 1 <= <strong>N</strong> <= 10<sup>9</sup>).</p>

### 출력 

 <p>Dla każdego zestawu należy wypisać jak odpowiedział Hektor na <strong>N</strong>-te pytanie.</p>

