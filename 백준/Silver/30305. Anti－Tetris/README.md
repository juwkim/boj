# [Silver I] Anti-Tetris - 30305 

[문제 링크](https://www.acmicpc.net/problem/30305) 

### 성능 요약

메모리: 111124 KB, 시간: 112 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 5월 11일 01:00:58

### 문제 설명

<p>In the game <em>Tetris</em>, the goal is to position blocks falling down a grid as well as possible. <em>Before</em> the block falls down, the player can shift the block to the left and right, and rotate it in steps of $90$ degrees. Then, the block falls down vertically until it hits another block. Completely filling a row removes this row from the grid, clearing up space for more falling blocks.</p>

<p>You have played this game one too many times, and to shake things up, you decide to play <em>Anti-Tetris</em>: instead of controlling the positioning of the blocks falling down, the goal is to design a Tetris grid that will perfectly fit a given block. That is, a grid such that after optimally positioning the new block, all rows of the grid are cleared and no filled cells remain.</p>

<p>As an example, consider the first sample case, shown in Figure A.1. The input block can be rotated clockwise $90$ degrees and shifted left to make it fit exactly and clear all rows of the grid once it touches down.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/57f05ba1-5d71-4171-abf4-7ffcf3abff1b/-/preview/" style="width: 512px; height: 152px;"></p>

<p style="text-align: center;">Figure A.1: Visualization of the first sample case. The falling block (the input, light yellow) perfectly fits in the Tetris grid (the output, other colours).</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with two integers $h$ and $w$ ($1\leq h, w\leq 100$), the height and width of the Tetris block that is about to enter the grid.</li>
	<li>$h$ lines with $w$ characters, each character being either '<code>#</code>' or '<code>.</code>', representing a filled or unfilled cell of the block, respectively.</li>
</ul>

<p>The input block is a single orthogonally<sup>1</sup> connected component and exactly fits in the $w \times h$ bounding box, i.e. the first and last row and column contain at least one '<code>#</code>'.</p>

<hr>
<p><sup>1</sup>Two cells are orthogonal neighbours if and only if they are horizontal or vertical neighbours.</p>

### 출력 

 <p>If there exists no Tetris grid that perfectly fits the input block, output "<code>impossible</code>". Else, output a grid such that placing the the input block optimally removes all rows, in the following format:</p>

<ul>
	<li>Two integers $h, w$ ($1\leq h, w\leq 1000$), the height and width of the Tetris grid.</li>
	<li>$h$ strings with $w$ characters, each character being either '<code>#</code>' or '<code>.</code>', representing a filled or unfilled cell in the Tetris grid, respectively.</li>
</ul>

<p>A row in the output grid may not be completely filled before the block is added, since such a row would already have been removed by the game.</p>

<p>Note that it is not required to print empty rows at the top of the output grid, since the block can be rotated and shifted to the left and right <em>before</em> it falls down.</p>

<p>If there are multiple valid solutions, you may output any one of them.</p>

