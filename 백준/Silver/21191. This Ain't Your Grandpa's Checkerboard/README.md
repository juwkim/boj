# [Silver V] This Ain't Your Grandpa's Checkerboard - 21191 

[문제 링크](https://www.acmicpc.net/problem/21191) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation)

### 문제 설명

<p>You are given an $n$-by-$n$ grid where each square is colored either black or white. A grid is <em>correct</em> if all of the following conditions are satisfied:</p>

<ul>
	<li>Every row has the same number of black squares as it has white squares.</li>
	<li>Every column has the same number of black squares as it has white squares.</li>
	<li>No row or column has $3$ or more consecutive squares of the same color.</li>
</ul>

<p>Given a grid, determine whether it is <em>correct</em>.</p>

### 입력 

 <p>The first line contains an integer $n$ ($2\le n\le 24$; $n$ is even). Each of the next $n$ lines contains a string of length $n$ consisting solely of the characters '<code>B</code>' and '<code>W</code>', representing the colors of the grid squares.</p>

### 출력 

 <p>If the grid is <em>correct</em>, print the number $1$ on a single line. Otherwise, print the number $0$ on a single line.</p>

