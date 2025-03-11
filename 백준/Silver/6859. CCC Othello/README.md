# [Silver II] CCC Othello - 6859 

[문제 링크](https://www.acmicpc.net/problem/6859) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 3월 11일 23:45:19

### 문제 설명

<p>Othello (also known as Reversi or Black & White Chess) is a game played on an 8x8 board, similar to a checker board. For the purposes of describing this question, the spaces on the board are referred to by their row and column position, with the top row referred to as row 1 and the left hand column referred to as column 1. The game involves placing circular discs, one at a time, on the board. The discs are coloured black on one side and white on the other. One player places his/her discs with the white side up and the other player places his/her discs with the black side up.</p>

<p>The game starts with some discs already placed on the board.</p>

<p>A move is valid if the following two conditions are satisfied:</p>

<ol>
	<li>The piece placed on the board is adjacent to a piece on the board (i.e, beside a piece either horizontally, vertically or diagonally).</li>
	<li>At least one of your opponents’ discs must be “flipped.” If you are playing black pieces, you flip your opponents’ (white) pieces (to black) so long as your opponents’ pieces are on a line (either horizontally, vertically or diagonally) between the latest piece placed on the board and another black piece, with no other black pieces or empty squares in between the most recently placed black piece and the given white piece. The same rule applies if the player is placing white pieces.</li>
</ol>

<p>Here are a couple of sample valid moves, starting from various configurations of the board:</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td>Board at the beginning of the game</td>
			<td>Board after the black player has placed a disc in row 5 and column 6.</td>
		</tr>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/6846183a-bd8d-429a-9ccb-feed644416a7/-/preview/" style="width: 172px; height: 173px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/97ff80f4-583d-4d00-b078-725ce34e6e57/-/preview/" style="width: 173px; height: 173px;"></td>
		</tr>
		<tr>
			<td>Board after several plays by each player</td>
			<td>Board after the white player has placed a disc in row 4 and column 6</td>
		</tr>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/d4ed4f74-aebe-4cae-9732-b35e9efa13d2/-/preview/" style="width: 173px; height: 173px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/1ca3e104-c660-424a-af03-03ece43be6db/-/preview/" style="width: 173px; height: 173px;"></td>
		</tr>
		<tr>
			<td>Board after several plays by each player</td>
			<td>Board after the white player has placed a disc in row 1 and column 4.</td>
		</tr>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/112fb714-322a-49f1-9551-ec61e3cbe227/-/preview/" style="width: 173px; height: 173px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/2598599f-d568-408c-a44b-81f43bc91d1e/-/preview/" style="width: 172px; height: 173px;"></td>
		</tr>
	</tbody>
</table>

<p>In the CCC version of Othello, the board may start with one of 3 configurations. Play will always start with the black player taking the first turn, and then alternating white to black for the rest of the turns. You must write a program to simulate taking turns in an Othello game, and at the end, report how many pieces of each colour are on the board.</p>

### 입력 

 <p>The user will enter three components of input (via the keyboard).</p>

<p>First the user will enter a letter representing the configuration of the initial board (either a, b or c).</p>

<p>Here are the initial configurations for the board.</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td>Configuration ’a’</td>
			<td>Configuration ’b’</td>
			<td>Configuration ’c’</td>
		</tr>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/dc19e32a-b933-43e9-8cff-a6fc889c8cab/-/preview/" style="width: 172px; height: 173px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/0c78fbf3-4b6c-428a-839e-d69c8524b9ad/-/preview/" style="width: 172px; height: 173px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/e8909255-59a6-408b-9a45-f9c76840f8f6/-/preview/" style="width: 172px; height: 173px;"></td>
		</tr>
	</tbody>
</table>

<p>The second component of input will be an integer n, where 0 ≤ n ≤ 30 which indicates the number of moves to be made in the simulation. The third component of input is n pairs of integers (R, C), where 1 ≤ R ≤ 8 and 1 ≤ C ≤ 8, and R represents the row and C represents the column of the next move.</p>

<p>Remember that the first move will be made by the black player, the next move will be made by the white player, then the black player, then the white player, and so on. You may also assume that all moves (R, C) will be valid moves on empty spaces on the board</p>

### 출력 

 <p>The program will output the number of black discs showing followed by the number of white discs showing on the board after the moves have been made. You are not responsible for displaying a picture of the board during the game. However, during your own testing, this may be useful.</p>

