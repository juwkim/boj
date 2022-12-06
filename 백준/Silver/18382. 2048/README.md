# [Silver I] 2048 - 18382 

[문제 링크](https://www.acmicpc.net/problem/18382) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>2048 is a sliding block puzzle game. The game's objective is to slide numbered tiles on a grid to combine them to create a tile with the number 2048. It is played on a 4×4 grid, with numbered tiles that slide smoothly when the player moves them using the four arrow keys. Every turn, a new tile will randomly appear in an empty spot on the board with a value of either 2 or 4. Tiles slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid. If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided. The resulting tile cannot merge with another tile again in the same move. The user's score starts at zero, and is incremented whenever two tiles combine, by the value of the new tile.</p>

<p>Write a program that takes the current user score, M number of moves and random appeared numbers (and their location on grid) and the current grid values as inputs and print the final score of the user.</p>

### 입력 

 <p>First line contains current user score. 0 ≤ S ≤ 500</p>

<p>Next line contains M next moves. 0 ≤ M ≤ 10</p>

<ul>
	<li>[move][2|4][at-row][at-column] eg: L200, Left arrow is pressed and then a new 2 is appeared at 0x0</li>
	<li>Move: L for left, U for up, R for right, D for down</li>
</ul>

<p>Next line contains current grid content in a flatten string.</p>

<ul>
	<li>From top left (0x0) to right bottom (3x3)</li>
	<li>Value can be 2,4,8,16,32,64,128,256,512, or 0 (zero indicate empty cell) separated by space.</li>
</ul>

### 출력 

 <p>Print the user score after given moves.</p>

