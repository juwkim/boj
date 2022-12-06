# [Silver I] Googlander (Large) - 12181 

[문제 링크](https://www.acmicpc.net/problem/12181) 

### 성능 요약

메모리: 28776 KB, 시간: 72 ms

### 분류

다이나믹 프로그래밍(dp)

### 문제 설명

<p>Eric Googlander is a fashion model who performs by walking around on a stage made of squares that form a grid with <strong>R</strong> rows and <strong>C</strong> columns. He begins at the leftmost bottom square, facing toward the top edge of the stage, and he will perform by making a series of moves. Googlander knows only the following two moves:<br>
<br>
1. Take one step forward in the direction he is currently facing<br>
<br>
2. Make a single 90 degree turn to the right, then take one step forward in the new direction he is facing following the turn<br>
<br>
(Note that Googlander does not know how to make a 90 degree <em>left</em> turn.)<br>
<br>
If a move would take Googlander off of the stage or onto a square he has already visited, that move is <em>unfashionable</em>. Whenever Googlander is in a position for which neither of the two possible moves is unfashionable, he is free to choose either move (independently of any other choices he has made in the past), but he must choose one of them. Whenever one of the possible moves he can make is unfashionable, he must make the other move. If at any point both of the possible moves are unfashionable, the show immediately ends without Googlander making another move. Note that Googlander cannot stop the show early -- he must keep moving until both possible moves become unfashionable.<br>
<br>
How many different paths is it possible for Googlander to walk? (Two paths are the same if and only if they visit the same squares in the same order.)</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> lines follow; each consists of two space-separated integers <strong>R</strong> and <strong>C</strong>.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>R, C</strong> ≤ 25.</li>
	<li>The limits ensure that the answer will always fit in a 64-bit signed integer.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the number of different paths that Googlander can walk.</p>

