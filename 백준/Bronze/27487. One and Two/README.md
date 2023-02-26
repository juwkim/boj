# [Bronze II] One and Two - 27487 

[문제 링크](https://www.acmicpc.net/problem/27487) 

### 성능 요약

메모리: 115136 KB, 시간: 148 ms

### 분류

애드 혹(ad_hoc), 구현(implementation), 수학(math)

### 문제 설명

<p>You are given a sequence $a_1, a_2, \ldots, a_n$. Each element of $a$ is $1$ or $2$.</p>

<p>Find out if an integer $k$ exists so that the following conditions are met.</p>

<ul>
	<li>$1 \leq k \leq n-1$, and</li>
	<li>$a_1 \cdot a_2 \cdot \ldots \cdot a_k = a_{k+1} \cdot a_{k+2} \cdot \ldots \cdot a_n$.</li>
</ul>

<p>If there exist multiple $k$ that satisfy the given condition, print the smallest.</p>

### 입력 

 <p>Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 100$). Description of the test cases follows.</p>

<p>The first line of each test case contains one integer $n$ ($2 \leq n \leq 1000$).</p>

<p>The second line of each test case contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \leq a_i \leq 2$).</p>

### 출력 

 <p>For each test case, if there is no such $k$, print $-1$.</p>

<p>Otherwise, print the smallest possible $k$.</p>

