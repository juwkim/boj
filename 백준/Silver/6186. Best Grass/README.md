# [Silver IV] Best Grass - 6186 

[문제 링크](https://www.acmicpc.net/problem/6186) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 구현(implementation)

### 문제 설명

<p>Bessie is planning her day of munching tender spring grass and is gazing out upon the pasture which Farmer John has so lovingly partitioned into a grid with R (1 <= R <= 100) rows and C (1 <= C <= 100) columns. She wishes to count the number of grass clumps in the pasture.</p>

<p>Each grass clump is shown on a map as either a single '#' symbol or perhaps two '#' symbols side-by-side (but not on a diagonal). No two symbols representing two different clumps are adjacent. Given a map of the pasture, tell Bessie how many grass clumps there are.</p>

<p>By way of example, consider this pasture map where R=5 and C=6:</p>

<pre>.#....
..#...
..#..#
...##.
.#....</pre>

<p>This pasture has a total of 5 clumps: one on the first row, one that spans the second and third row in column 2, one by itself on the third row, one that spans columns 4 and 5 in row 4, and one more in row 5.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: R and C</li>
	<li>Lines 2..R+1: Line i+1 describes row i of the field with C characters, each of which is a '#' or a '.'</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the number of grass clumps Bessie can munch</li>
</ul>

