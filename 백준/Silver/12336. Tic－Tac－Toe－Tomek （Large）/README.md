# [Silver IV] Tic-Tac-Toe-Tomek (Large) - 12336 

[문제 링크](https://www.acmicpc.net/problem/12336) 

### 성능 요약

메모리: 116156 KB, 시간: 320 ms

### 분류

구현(implementation)

### 문제 설명

<p>Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.</p>

<p>After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.</p>

<p>Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:</p>

<ul>
	<li>"X won" (the game is over, and X won)</li>
	<li>"O won" (the game is over, and O won)</li>
	<li>"Draw" (the game is over, and it ended in a draw)</li>
	<li>"Game has not completed" (the game is not over yet)</li>
</ul>

<p>If there are empty cells, and the game is not over, you should output "Game has not completed", even if the outcome of the game is inevitable.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line.</p>

<p>Limits</p>

<ul>
	<li>The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as described above.</li>
	<li>1 ≤ <strong>T</strong> ≤ 1000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above. Make sure to get the statuses exactly right. When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on.</p>

