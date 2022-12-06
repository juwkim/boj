# [Bronze II] Lonesome Partners - 6013 

[문제 링크](https://www.acmicpc.net/problem/6013) 

### 성능 요약

메모리: 28776 KB, 시간: 396 ms

### 분류

브루트포스 알고리즘(bruteforcing), 기하학(geometry)

### 문제 설명

<p>Bessie and the rest of the herd totaling N (2 <= N <= 500) cows have gone to the dance. For the cows-only part of the dance, two cows are chosen as the "Belles of the Ball". Farmer John records the X,Y coordinates (0 <= X_i <= 5,000; 0 <= Y_i <= 5,000) of all the cows in the dance hall and then asks you to determine the indices of the two cows who are farthest apart (which, happily, is guaranteed to be unique). Distance is the normal cartesian distance calculated as the square root of the sum of the squares of the differences in the row and column coordinates.</p>

<p>In a dance with just eight cows:</p>

<pre> 8 | . C . . . . . . . .
 7 | . . . . . . . . . .
 6 | . C . . . . . . . .
 5 | . . . C C . C . . .
 4 | . . . . C . . . . .
 3 | . . C . . . . . . .
 2 | . . . . . . . . . .
 1 | . . . . . . . . . C
 0 +--------------------
   0 1 2 3 4 5 6 7 8 8 9</pre>

<p>Farmer John hopes you would choose the cows at 2,8 and 9,1 as farthest apart.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N+1: Line i+1 contains the integer coordinate location of cow i: X_i and Y_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: Two sorted integers that are the indices of the two cows that are located farthest apart.</li>
</ul>

<p> </p>

