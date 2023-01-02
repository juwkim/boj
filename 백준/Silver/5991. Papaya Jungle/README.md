# [Silver IV] Papaya Jungle - 5991 

[문제 링크](https://www.acmicpc.net/problem/5991) 

### 성능 요약

메모리: 114328 KB, 시간: 108 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Bessie has wandered off the farm into the adjoining farmer's land. He raises delicious papaya fruit, which is a delicacy for cows. The papaya jungle is partitioned into a grid of squares with R rows and C columns (1 <= R <= 40, 1 <= C <= 40), as is popular in Wisconsin. Bessie can travel from a given square to any existing adjacent square whose route is parallel to the X or Y axis.  So in the following diagram, if Bessie is at the square labeled "B", she can travel to any of the squares labeled "T":</p>

<pre>         .T.
         TBT
         .T.</pre>

<p>Bessie always starts out by munching the papayas in square (row=1,col=1).  After she's done with one square, Bessie always uses her trusty binoculars to count the low-hanging fruit in each of the adjacent squares. She then always moves to the square with the most visible uneaten fruit (a square that happily is always unique).</p>

<p>Sooner or later, following this rule, Bessie always ends up in square (R,C) and eats the fruit there.</p>

<p>Given the dimensions of the papaya jungle and the amount of fruit F_ij in each square (1 <= F_ij <= 100), determine the total number of fruit Bessie consumes for a given papaya jungle.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: R and C</li>
	<li>Lines 2..R+1: Line i+1 describes row i of the jungle with C space-separated integers that tell how many fruit are in each square: F_i1, F_i2, ..., F_iC</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the total number of papayas that Bessie eats by the time she finishes off the papayas at the barn in the lower right corner at coordinate (R,C).</li>
</ul>

<p> </p>

