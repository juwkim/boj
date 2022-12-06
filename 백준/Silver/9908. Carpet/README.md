# [Silver V] Carpet - 9908 

[문제 링크](https://www.acmicpc.net/problem/9908) 

### 성능 요약

메모리: 114488 KB, 시간: 132 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Given a rectangular configuration representing a floor plan, where ‘<code>#</code>’ indicates a pillar and ‘<code>.</code>’ a clear space:</p>

<pre>...#...#..
..##.#....
......#.#.
.#........
.........#
.....#.#..
</pre>

<p>What is the area (number of dots) of the largest rectangular carpet whose edges are parallel to the boundary of the floor that can be laid on this piece of land?  For the example above, the largest carpet is represented with ‘<code>*</code>’ symbols:</p>

<pre>...#...#..
..##.#....
......#.#.
.#*******.
..*******#
.....#.#..
</pre>

<p>The area of this carpet is 14.</p>

<p>The rows are numbered from top to bottom starting from row 1, and the columns are numbered from left to right starting from column 1. You can assume that there are at most 20 rows and at most 40 columns.</p>

### 입력 

 <p>The input consists of the following lines:</p>

<ol>
	<li>The first line contains 2 integers indicating the number of rows and number of columns of the floor plan, respectively.</li>
	<li>The second line consists of a positive integer n indicating the number of pillars.</li>
	<li>Each of the subsequent n lines consists of the position of a pillar, represented as 2 integers separated by a space.  The first integer represents the row number and the second integer represents the column number.</li>
</ol>

### 출력 

 <p>The output contains a single integer value, which is the area of the largest carpet that can be laid on the floor. </p>

