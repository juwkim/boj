# [Silver V] Building a House (Small) - 12541 

[문제 링크](https://www.acmicpc.net/problem/12541) 

### 성능 요약

메모리: 115300 KB, 시간: 176 ms

### 분류

Empty

### 문제 설명

<p>You have just bought land and want to plant the largest rectangular field possible. In surveying your land, you find a number of obstacles and decide to draw a map. You indicate in each square of the map whether it contains grass (<strong>G</strong>), rock (<strong>R</strong>), water (<strong>W</strong>), shrubs (<strong>S</strong>), or trees (<strong>T</strong>). While the grass can be mowed and the shrubs dug from the ground, the water, rocks, and trees <strong>cannot</strong> be removed. Given these obstacles, determine the area of the largest rectangular field.</p>

### 입력 

 <p>The first line of input gives the number of cases, <strong>N</strong>.<br>
<strong>N</strong> test cases follow. For each test case there will be:</p>

<ul>
	<li>One line containing two space-separated integers indicating the length (<strong>L</strong>) and width (<strong>W</strong>) of your land.</li>
	<li>Followed by, <strong>W</strong> lines, each containing <strong>L</strong> characters where each indicates the conditions for that square of land (one of <code>G, R, W, S, or T</code>).</li>
</ul>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>L</strong> ≤ 50</li>
	<li>1 ≤ <strong>W</strong> ≤ 50</li>
	<li><strong>N</strong> ≤ 10</li>
	<li>Fewer than 5 obstacles in each test case.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>x</strong>: " followed by the maximum area of the largest rectangle that can be cleared.</p>

