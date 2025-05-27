# [Silver I] Bacteria (Small) - 12567 

[문제 링크](https://www.acmicpc.net/problem/12567) 

### 성능 요약

메모리: 130396 KB, 시간: 2596 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 5월 27일 18:27:23

### 문제 설명

<p>A number of bacteria lie on an infinite grid of cells, each bacterium in its own cell.</p>

<p>Each second, the following transformations occur (all simultaneously): </p>

<ol>
	<li>If a bacterium has no neighbor to its north and no neighbor to its west, then it will die.</li>
	<li>If a cell has no bacterium in it, but there are bacteria in the neighboring cells to the north and to the west, then a new bacterium will be born in that cell.</li>
</ol>

<p>Upon examining the grid, you note that there are a positive, finite number of bacteria in one or more rectangular regions of cells.</p>

<p>Determine how many seconds will pass before all the bacteria die.</p>

<p>Here is an example of a grid that starts with 6 cells containing bacteria, and takes 6 seconds for all the bacteria to die. '1's represent cells with bacteria, and '0's represent cells without bacteria.</p>

<p> </p>

<pre>000010
011100
010000
010000
000000

000000
001110
011000
010000
000000

000000
000110
001100
011000
000000

000000
000010
000110
001100
000000

000000
000000
000010
000110
000000

000000
000000
000000
000010
000000

000000
000000
000000
000000
000000</pre>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line containing <strong>C</strong>, the number of test cases.</li>
</ul>

<p>Then for each test case:</p>

<ul>
	<li>One line containing <strong>R</strong>, the number of rectangles of cells that initially contain bacteria.</li>
	<li><strong>R</strong> lines containing four space-separated integers <strong>X</strong><sub>1</sub> <strong>Y</strong><sub>1</sub> <strong>X</strong><sub>2</sub> <strong>Y</strong><sub>2</sub>. This indicates that all the cells with X coordinate between X<sub>1</sub> and X<sub>2</sub>, inclusive, and Y coordinate between Y<sub>1</sub> and Y<sub>2</sub>, inclusive, contain bacteria.</li>
</ul>

<p>The rectangles may overlap.</p>

<p>North is in the direction of decreasing Y coordinate. <br>
West is in the direction of decreasing X coordinate.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>C</strong> ≤ 100.</li>
	<li>1 ≤ <strong>R</strong> ≤ 10 </li>
	<li>1 ≤ <strong>X<sub>1</sub></strong> ≤ <strong>X<sub>2</sub></strong> ≤ 100 </li>
	<li>1 ≤ <strong>Y<sub>1</sub></strong> ≤ <strong>Y<sub>2</sub></strong> ≤ 100 </li>
	<li>The number of cells initially containing bacteria will be at most 1000000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #N: T", where N is the case number (starting from 1), and T is the number of seconds until the bacteria all die.</p>

