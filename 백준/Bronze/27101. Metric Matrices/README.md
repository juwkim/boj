# [Bronze II] Metric Matrices - 27101 

[문제 링크](https://www.acmicpc.net/problem/27101) 

### 성능 요약

메모리: 114328 KB, 시간: 112 ms

### 분류

구현(implementation)

### 문제 설명

<p>Given as input a square distance matrix, where a[i,j] is the distance between point i and point j, determine if the distance matrix is "a metric" or not.</p>

<p>A distance matrix a[x,y] is a metric if and only if</p>

<ol>
	<li>f(x,x) = 0</li>
	<li>f(x,y) > 0 if x != y</li>
	<li>f(x,y) = f(y,x)</li>
	<li>f(x,y) + f(y,z) >= f(x,z)</li>
</ol>

### 입력 

 <ul>
	<li>Line 1: One integer, N, the rows and number of columns, 2 ≤ N ≤ 30</li>
	<li>Line 2..N+1: N lines, each with N space-separated integers (-32000 ≤ each integer ≤ 32000).  The first of these lines represents the first row; the first number in each line is the first column.</li>
</ul>

### 출력 

 <p>A single line with a single digit, which is the lowest digit of the possible facts on this list:</p>

<ul>
	<li>0: The matrix is a metric</li>
	<li>1: The matrix is not a metric, it violates rule 1 above</li>
	<li>2: The matrix is not a metric, it violates rule 2 above</li>
	<li>3: The matrix is not a metric, it violates rule 3 above</li>
	<li>4: The matrix is not a metric, it violates rule 4 above</li>
</ul>

