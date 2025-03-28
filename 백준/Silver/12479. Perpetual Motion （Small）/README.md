# [Silver II] Perpetual Motion (Small) - 12479 

[문제 링크](https://www.acmicpc.net/problem/12479) 

### 성능 요약

메모리: 113068 KB, 시간: 1344 ms

### 분류

브루트포스 알고리즘, 구현, 시뮬레이션

### 제출 일자

2025년 3월 29일 06:53:53

### 문제 설명

<p>Have you ever been to the Google Lemming Factory? It is a very unusual place. The floor is arranged into an <strong>R</strong> x <strong>C</strong> grid. Within each grid square, there is a conveyor belt oriented up-down, left-right, or along one of the two diagonals. The conveyor belts move either forwards or backwards along their orientations, and you can independently choose which of the two possible directions each conveyor belt should move in.</p>

<p><img src="https://onlinejudgeimages.s3.amazonaws.com/problem/12479/images-36.png" style="border:0px; opacity:0.9; vertical-align:middle"></p>

<p>Currently, there is a single lemming standing at the center of each square. When you start the conveyor belts, each lemming will move in the direction of the conveyor belt he is on until he reaches the center of a new square. All these movements happen simultaneously and take exactly one second to complete. Afterwards, the lemmings will all be on new squares, and the process will repeat from their new positions. This continues forever, or at least until you turn off the conveyor belts.</p>

<ul>
	<li>When a lemming enters a new square, he continues going in the direction he was already going until he reaches the center of that square. He will not be affected by the new conveyor belt until the next second starts.</li>
	<li>If a lemming moves off the edge of the grid, he comes back at the same position on the opposite side. For example, if he were to move diagonally up and left from the top-left square, he would arrive at the bottom-right square. By the miracle of science, this whole process still only takes 1 second.</li>
	<li>Lemmings never collide and can always move past each other without difficulty.</li>
</ul>

<p>The trick is to choose directions for each conveyor belt so that the lemmings will keep moving forever without ever having two of them end up in the center of the same square at the same time. If that happened, they would be stuck together from then on, and that is not as fun for them.</p>

<p>Here are two ways of assigning directions to each conveyor belt from the earlier example:</p>

<p><img src="https://onlinejudgeimages.s3.amazonaws.com/problem/12479/images-37.png" style="border:0px; vertical-align:middle"></p>

<p> </p>

<p>In both cases, we avoid ever sending two lemmings to the center of the same square at the same time.</p>

<p>Given an arbitrary floor layout, calculate <strong>N</strong>, the number of ways to choose directions for each conveyor belt so that no two lemmings will ever end up in the center of the same square at the same time. The answer might be quite large, so please output it modulo 1000003.</p>

### 입력 

 <p>The first line of input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each begins with a line containing positive integers <strong>R</strong> and <strong>C</strong>.</p>

<p>This is followed by <strong>R</strong> lines, each containing a string of <strong>C</strong> characters chosen from <code>"|-/\"</code>. Each character represents the orientation of the conveyor belt in a single square:</p>

<ul>
	<li>'<code>|</code>' represents a conveyor belt that can move up or down.</li>
	<li>'<code>-</code>' represents a conveyor belt that can move left or right.</li>
	<li>'<code>/</code>' represents a conveyor belt that can move up-right or down-left.</li>
	<li>'<code>\</code>' represents a conveyor belt that can move up-left or down-right.</li>
</ul>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 25.</li>
	<li>3 ≤ <strong>R</strong> ≤ 4.</li>
	<li>3 ≤ <strong>C</strong> ≤ 4.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: <strong>M</strong>", where x is the case number (starting from 1), and <strong>M</strong> is the remainder when dividing <strong>N</strong> by 1000003.</p>

