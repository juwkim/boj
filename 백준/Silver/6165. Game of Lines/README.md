# [Silver IV] Game of Lines - 6165 

[문제 링크](https://www.acmicpc.net/problem/6165) 

### 성능 요약

메모리: 40396 KB, 시간: 180 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>Farmer John has challenged Bessie to the following game: FJ has a board with dots marked at N (2 <= N <= 200) distinct lattice points. Dot i has the integer coordinates X_i and Y_i (-1,000 <= X_i <= 1,000; -1,000 <= Y_i <= 1,000).</p>

<p>Bessie can score a point in the game by picking two of the dots and drawing a straight line between them; however, she is not allowed to draw a line if she has already drawn another line that is parallel to that line. Bessie would like to know her chances of winning, so she has asked you to help find the maximum score she can obtain.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N+1: Line i+1 describes lattice point i with two space-separated integers: X_i and Y_i.</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer representing the maximal number of lines Bessie can draw, no two of which are parallel.</li>
</ul>

<p> </p>

