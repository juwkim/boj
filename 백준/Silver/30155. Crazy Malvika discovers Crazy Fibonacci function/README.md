# [Silver III] Crazy Malvika discovers Crazy Fibonacci function - 30155 

[문제 링크](https://www.acmicpc.net/problem/30155) 

### 성능 요약

메모리: 119592 KB, 시간: 204 ms

### 분류

수학

### 제출 일자

2024년 2월 13일 06:49:48

### 문제 설명

<p>Malvika was getting bored of the usual Fibonacci problems, and decided to add a little twist to it. She defined a new function f() with the following properties:</p>

<ul>
	<li>She'll give you two integers, A and B. f(1) is defined to be A and f(2) is B.</li>
	<li>And for all integers x ≥ 2, f(x) = f(x-1) + f(x+1).</li>
</ul>

<p>She'll give an integer N, and you have to find out what f(N) is. Output the answers modulo 10<sup>9</sup>+7.</p>

### 입력 

 <p>The first line of input contains a single integer T denoting number of test cases.</p>

<p>The only line of each test case contains three integers: A, B and N, denoting f(1), f(2) and the query.</p>

### 출력 

 <p>For each test case, output a line which contains a single integer, corresponding to f(N) for the given input.</p>

