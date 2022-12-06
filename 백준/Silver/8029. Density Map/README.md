# [Silver V] Density Map - 8029 

[문제 링크](https://www.acmicpc.net/problem/8029) 

### 성능 요약

메모리: 116920 KB, 시간: 6792 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>There are given:</p>

<ul>
	<li>integers n > r ≥ 0,</li>
	<li>F - the table n x n with the numbers from the set {0,1}; columns and lines of the table are numbered from 1 to n; the number in i-th column and j-th line of the table is denoted by F[i,j].</li>
</ul>

<p>If [i,j] and [i’,j’] are two positions in the table F, the distance between them is max(|i-i’|,|j-j’|).</p>

<p>The table W, n x n, should be computed, where W[i,j] (the number in i-th column and j-th line of the table W) is equal to the sum of all the numbers F[x,y], such that the distance between [x,y] and [i,j] is not greater than r.</p>

<p>Write a program, which:</p>

<ul>
	<li>reads integers n, r and the table F from the standard input,</li>
	<li>computes the table W,</li>
	<li>writes the table W to the standard output.</li>
</ul>

### 입력 

 <p>In the first line of standard input there are two positive integers separated by a single space: n and r, where 0 ≤ r < n ≤ 250. In the following n lines the table F is described. Each of these lines contains n integers from the set {0,1}, separated by single spaces. The i-th number written in (j+1)-st line is equal to F[i,j].</p>

### 출력 

 <p>The standard output should contain exactly n lines. In the j-th line the values W[1,j]…W[n,j] should be written respectively; they should be separated by single spaces.</p>

