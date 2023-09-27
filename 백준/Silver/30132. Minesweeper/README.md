# [Silver V] Minesweeper - 30132 

[문제 링크](https://www.acmicpc.net/problem/30132) 

### 성능 요약

메모리: 115136 KB, 시간: 136 ms

### 분류

구현

### 문제 설명

<p>Minesweeper is a single-player computer game. The objective of the game is to clear an abstract minefield without detonating a mine. When the game is started, the player is presented with a grid of n x m blank squares. If the player clicks on a square without a mine, a digit is revealed in that square, the digit indicating the number of adjacent squares that contains mines. Two squares are adjacent if they share an edge or a corner, i. e. a square can have at most 8 adjacent squares. By using logic, players can in many instances use this information to deduce that certain other squares are mine-free (or mine-filled), and proceed to click on additional squares to clear them or mark them with flag graphics to indicate the presence of a mine. </p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/cfadd70c-72cb-403f-9220-2d074f8958d4/-/preview/"></p>

<p>Clark Kent is a Minesweeper addict. And with help from his Kryptonian (a planet far far away from earth) powers he solves them at lightning speed and gives them to you. Your job is to tell him whether the solved version is correct or not. A board is correctly solved iff all flagged squares should contain a mine and every square containing a number X has exactly X adjacent squares flagged. </p>

### 입력 

 <p>The first line of input will contain an integer T ≤ 20 denoting the number of test cases.</p>

<p>Each test case will be formatted as follows:-</p>

<ul>
	<li>The first line will contain two integers separated by a single space denoting 1≤n≤20 and 1 ≤ m≤20 respectively.</li>
	<li>The next n lines will contain m characters each. Each character will either be a digit (0 to 8 inclusive) or 'F'. The presence of 'F' indicates that Clark has flagged the square. The digits indicate the number of mines in the adjacent squares. </li>
</ul>

### 출력 

 <p>Output one line per case:-</p>

<ul>
	<li>'Well done Clark!' if the board was solved successfully. </li>
	<li>'Please sweep the mine again!' otherwise.</li>
</ul>

<p>Note that quotes are for clarity only.</p>

