# [Silver I] Munching - 6189 

[문제 링크](https://www.acmicpc.net/problem/6189) 

### 성능 요약

메모리: 114144 KB, 시간: 124 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 11일 00:36:10

### 문제 설명

<p>Bessie loves her grass and loves to hurry to the barn for her evening milking session. She has partitioned the pasture into a rectilinear grid of R (1 <= R <= 100) rows and C (1 <= C <= 100) columns and marked the squares as grass or rocky (she can't eat rocks and won't even go into those squares). Bessie starts on her map at location R_b,C_b and wishes to munch her way, square by square, to the barn at location 1,1 by the shortest route possible. She moves from one square to any one of the potentially four adjacent squares.</p>

<p>Below is the original map [with rocks ('*'), grass ('.'), the barn ('B'), and Bessie ('C' for cow) at row 5, col 6] and a route map with the optimal route marked with munches ('m'):</p>

<pre>           Map               Optimal Munched Route
        1 2 3 4 5 6  <-col      1 2 3 4 5 6  <-col
      1 B . . . * .           1 B m m m * .
      2 . . * . . .           2 . . * m m m
      3 . * * . * .           3 . * * . * m
      4 . . * * * .           4 . . * * * m
      5 * . . * . C           5 * . . * . m</pre>

<p>Bessie munched 9 squares.</p>

<p>Given a map, determine how many squares Bessie will eat on her shortest route to the barn (there's no grass to eat on the barn's square).</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: R and C</li>
	<li>Lines 2..R+1: Line i+1 describes row i with C characters (and no spaces) as described above</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the number of squares of grass that Bessie munches on the shortest route back to the barn</li>
</ul>

