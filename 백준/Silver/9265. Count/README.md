# [Silver III] Count - 9265 

[문제 링크](https://www.acmicpc.net/problem/9265) 

### 성능 요약

메모리: 124236 KB, 시간: 7524 ms

### 분류

이분 탐색(binary_search)

### 문제 설명

<p>You have:</p>

<ul>
	<li>A matrix of natural numbers, with the property that all rows and all columns are sorted in ascending order (i.e. A[i,j]>=A[i-1,j] and A[i,j]>=A[i,j-1] for all i,j)</li>
	<li>One or several pairs of numbers (X,Y) with the property that Y>=X.</li>
</ul>

<p>For each (X,Y) pair, count how many numbers from the matrix are greater than or equal to X but smaller than or equal to Y.</p>

### 입력 

 <p>The input file is a binary file containing 32-bit integer numbers. The input file consists of:</p>

<ul>
	<li>One integer N representing the number of rows (no more than 10000)</li>
	<li>One integer M representing the number of columns (no more than 10000)</li>
	<li>NxM integers, representing the values from the matrix, row by row </li>
	<li>An unspecified number of integers, representing the (X,Y) pairs, one pair at a time. </li>
</ul>

<p>There will be at least one pair and at most 100 pairs in the file – and there will not be an incomplete pair at the end of the file.</p>

### 출력 

 <p>For each pair you should write to standard output a value representing how many numbers in the matrix are greater than or equal to X but smaller than or equal to Y.</p>

