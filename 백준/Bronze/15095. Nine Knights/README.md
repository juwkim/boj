# [Bronze I] Nine Knights - 15095 

[문제 링크](https://www.acmicpc.net/problem/15095) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

구현(implementation)

### 문제 설명

<p>In the game of chess, knights are unique due to their “L-shaped” movement. A knight can move, as shown in Figure A.1, by either moving two squares sideways and one square up or down, or moving one square sideways and two squares either up or down.</p>

<table class="table" style="width:100%">
	<tbody>
		<tr>
			<td style="text-align:center; width:100%"><img alt="" src="" style="height:146px; width:145px"></td>
		</tr>
		<tr>
			<td style="text-align:center; width:100%">Figure A.1: The highlighted squares show all possible moves for a knight.</td>
		</tr>
	</tbody>
</table>

<p style="text-align:center">In the Nine Knights puzzle, exactly nine knights must be positioned on a 5-by-5 board so that no knight can attack another knight with a single move. The configuration shown in Figure A.2 is an invalid solution because two of the knights can attack each other, where the configuration shown in Figure A.3 is a valid solution.</p>

<table class="table" style="width:100%">
	<tbody>
		<tr>
			<td style="text-align:center; width:50%"><img alt="" src="" style="height:146px; width:145px"></td>
			<td style="text-align:center; width:50%"><img alt="" src="" style="height:147px; width:145px"></td>
		</tr>
		<tr>
			<td style="text-align:center; width:50%">Figure A.2: Invalid game configuration</td>
			<td style="text-align:center; width:50%">Figure A.3: Valid game configuration</td>
		</tr>
	</tbody>
</table>

<p>Given the description of a game configuration, your job is to determine whether or not it represents a valid solution to the Nine Knights puzzle.</p>

### 입력 

 <p>The input will consist of 5 lines, each having 5 characters. All characters will be either ’k’, indicating the placement of a knight, or ’.’, indicating an empty space on the board.</p>

### 출력 

 <p>Display the word valid if the given chess board is a valid solution to the Nine Knights puzzle. Otherwise, display the word invalid.</p>

