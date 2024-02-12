# [Silver II] Brattleship (Large) - 12148 

[문제 링크](https://www.acmicpc.net/problem/12148) 

### 성능 요약

메모리: 108080 KB, 시간: 104 ms

### 분류

애드 혹, 게임 이론, 수학

### 제출 일자

2024년 2월 13일 04:17:15

### 문제 설명

<p>You're about to play a simplified "battleship" game with your little brother. The board for this game is a rectangular grid with <strong>R</strong> rows and <strong>C</strong> columns. At the start of the game, you will close your eyes, and you will keep them closed until the end of the game. Your little brother will take a single rectangular 1 x <strong>W</strong> ship and place it <strong>horizontally</strong> somewhere on the board. The ship must always fit entirely on the board, with each cell of the ship occupying exactly one of the grid's cells, and it can never be rotated.<br>
<br>
In each turn of the game, you name a cell on the board, and your little brother tells you whether that is a hit (one of the cells occupied by the ship) or a miss. (Your little brother doesn't say <em>which</em> part of the ship was hit -- just that the cell you named has a part of the ship in it.) You have perfect memory, and can keep track of all the information he has given you. Once you have named all of the cells occupied by the ship, the game is over (the ship is sunk), and your score is the number of turns taken. Your goal is to minimize your score.<br>
<br>
Although the ship is not supposed to be moved once it is placed, you know that your little brother, who is a brat, plans to cheat by changing the location of the ship whenever he wants, as long as the ship remains horizontal and completely on the board, and the new location is consistent with all the information he has given so far. For example, for a 1x4 board and 1x2 ship, your little brother could initially place the ship such that it overlaps the leftmost two columns. If your first guess was row 1, column 2, he could choose to secretly move the ship to the rightmost two columns, and tell you that (1, 2) was a miss. If your next guess after that was (1, 3), though, then he could not say that was also a miss and move the ship back to its original location, since that would be inconsistent with what he said about (1, 2) earlier.<br>
<br>
Not only do you know that your little brother will cheat, he knows that you know. If you both play optimally (you to minimize your score, him to maximize it), what is the lowest score that you can <strong>guarantee</strong> you will achieve, regardless of what your little brother does?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> lines follow, each with three space-separated integers <strong>R</strong>, <strong>C</strong>, and <strong>W</strong>: the number of rows and columns of the board, followed by the width of the ship.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>W</strong> ≤ <strong>C</strong>.</li>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>R</strong> ≤ 20.</li>
	<li>1 ≤ <strong>C</strong> ≤ 20.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum score you can guarantee.</p>

