# [Bronze II] Number Pairs - 15234 

[문제 링크](https://www.acmicpc.net/problem/15234) 

### 성능 요약

메모리: 48716 KB, 시간: 124 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>Given a sequence of N distinct integer numbers compute the number of pairs that sum to K.</p>

<p>Example:</p>

<p>Given the sequence {1, 2, 3, 4, 5, 6}</p>

<ul>
	<li>There are 1 pair of numbers that sums to 3: (1, 2)</li>
	<li>There are 1 pair of numbers that sums to 4: (3, 1)</li>
	<li>There are 2 pairs of numbers that sum to 5: (1, 4) and (3, 2)</li>
	<li>There are 2 pairs of numbers that sum to 6: (5, 1) and (4, 2)</li>
	<li>There are 3 pairs of numbers that sum to 7: (1, 6), (2, 5) and (3, 4).</li>
	<li>There are 2 pairs of numbers that sum to 8: (2, 6) and (5, 3)</li>
	<li>There are 2 pairs of numbers that sum to 9: (6, 3) and (5, 4)</li>
	<li>...</li>
</ul>

<p>Note that we consider that the pairs (1, 6) and (6, 1) are the same.</p>

### 입력 

 <p>The first line will contain two integers N and K.</p>

<p>N represents the number of elements in the sequence and K the goal value.</p>

<p>We want to know how many pairs of numbers sum to K.</p>

<p>The second line will contain N integers separated by spaces.</p>

<p>N <= 1000</p>

<p>The numbers in the sequence will be between 1 and 10^6.</p>

### 출력 

 <p>An integer, the number of pairs that add K.</p>

