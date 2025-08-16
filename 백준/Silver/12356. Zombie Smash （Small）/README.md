# [Silver I] Zombie Smash (Small) - 12356 

[문제 링크](https://www.acmicpc.net/problem/12356) 

### 성능 요약

메모리: 111420 KB, 시간: 160 ms

### 분류

브루트포스 알고리즘, 수학

### 제출 일자

2025년 8월 16일 17:30:24

### 문제 설명

<p>You are playing Zombie Smash: a game where the objective is to smash zombies with your trusty Zombie Smasher as they pop out of graves at the graveyard. The graveyard is represented by a flat 2D grid. Each zombie will pop out of a grave at some (X, Y) cell on the grid, stand in place for 1000 milliseconds (ms), and then disappear back into the grave. At most one zombie can stand around a grave at a time.</p>

<p>You can move to any one of the 8 cells adjacent to your location in 100ms; i.e., you can move North, East, South, West, NW, NE, SW, and SE of your current location. You may move through or stand on a cell even if it is currently occupied by a zombie. You can smash a zombie instantly once you reach the cell that the zombie is standing on, but once you smash a zombie it takes 750ms for your Zombie Smasher to recharge before you can smash another zombie. You may move around while Zombie Smasher is recharging. For example, immediately after smashing a zombie at (0, 0):</p>

<ul>
	<li>It will take 750ms to reach and smash a zombie at (1, 1) <strong>or</strong></li>
	<li>2000ms to reach and smash a zombie at (20, 20).</li>
</ul>

<p>You start at cell (0, 0) at the beginning of the game (time=0). After you play a level you would like to know how many zombies you could have smashed, if you had played optimally.</p>

### 입력 

 <p>The first line will contain a single integer <strong>T</strong>, the number of test cases. It is followed by <strong>T</strong>test cases, each starting with a line containing a single integer <strong>Z</strong>, the number of zombies in the level.</p>

<p>The next <strong>Z</strong> lines contain 3 space-separated integers each, representing the location and time at which a given zombie will appear and disappear. The <code>i</code><sup>th</sup> line will contain the integers <strong>X</strong><sub>i</sub>, <strong>Y</strong><sub>i</sub> and <strong>M</strong><sub>i</sub>, where:</p>

<ul>
	<li><strong>X</strong><sub>i</sub> is the X coordinate of the cell at which zombie <code>i</code> appears,</li>
	<li><strong>Y</strong><sub>i</sub> is the Y coordinate of the cell at which zombie <code>i</code> appears,</li>
	<li><strong>M</strong><sub>i</sub> is the time at which zombie <code>i</code> appears, in milliseconds after the beginning of the game. The time interval during which the zombie can smashed is inclusive: if you reach the cell at any time in the range [<strong>M</strong><sub>i</sub>, <strong>M</strong><sub>i</sub> + 1000] with a charged Zombie Smasher, you can smash the zombie in that cell.</li>
</ul>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>-1000 ≤ <strong>X</strong><sub>i</sub>, <strong>Y</strong><sub>i</sub> ≤ 1000.</li>
	<li>0 ≤ <strong>M</strong><sub>i</sub> ≤ 100000000 = 10<sup>8</sup>.</li>
	<li>Two zombies will never be in the same location at the same time. In other words, if one zombie appears at (x, y) at time t, then any other zombie that appears at (x, y) must appear at or before (t - 1001), or at or after (t + 1001).</li>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">Z</strong><span style="line-height:1.6em"> ≤ 8.</span></li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #c: d", where c is the case number (starting from 1), and d is the maximum number of zombies you could have smashed in this level.</p>

