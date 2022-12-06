# [Bronze II] Math Practice - 5940 

[문제 링크](https://www.acmicpc.net/problem/5940) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math)

### 문제 설명

<p>One lovely afternoon, Bessie's friend Heidi was helping Bessie review for her upcoming math exam.</p>

<p>Heidi presents two integers A (0 <= A <= 45) and B (1 <= B <= 9) to Bessie who must respond with an integer E in the range 1..62. E is the smallest integer in that range that is strictly greater than A and also has B as the first digit of 2 raised to the E-th power. If there is no answer, Bessie responds with 0.</p>

<p>Help Bessie correctly answer all of Heidi's questions by calculating her responses.</p>

<p>By way of example, consider A=1 and B=6. Bessie might generate a table like this:</p>

<pre>         E         2^E    First digit of 2^E
         2          4            4
         3          8            8
         4         16            1
         5         32            3
         6         64            6      <-- matches B</pre>

<p>Thus, E=6 is the proper answer.</p>

<p>NOTE: The value of 2^44 does not fit in a normal 32-bit integer.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: A and B</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer E calculated as above</li>
</ul>

<p> </p>

