# [Bronze II] Rock, Paper, Scissors - 4593 

[문제 링크](https://www.acmicpc.net/problem/4593) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Rock, Paper, Scissors is a classic hand game for two people. Each participant holds out either a fist (rock), open hand (paper), or two-finger V (scissors). If both players show the same gesture, they try again. They continue until there are two different gestures. The winner is then determined according to the table below:</p>

<table class="table table-bordered" style="width:29%">
	<tbody>
		<tr>
			<td>Rock</td>
			<td>beats</td>
			<td>Scissors</td>
		</tr>
		<tr>
			<td>Paper</td>
			<td>beats</td>
			<td>Rock</td>
		</tr>
		<tr>
			<td>Scissors</td>
			<td>beats</td>
			<td>Paper</td>
		</tr>
	</tbody>
</table>

<p>Your task is to take a list of symbols representing the gestures of two players and determine how many games each player wins.</p>

<p>In the following example:</p>

<pre>Turn     : 1 2 3 4 5
Player 1 : R R S R S
Player 2 : S R S P S</pre>

<p>Player 1 wins at Turn 1 (Rock beats Scissors), Player 2 wins at Turn 4 (Paper beats Rock), and all the other turns are ties.</p>

### 입력 

 <p>The input contains between 1 and 20 pairs of lines, the first for Player 1 and the second for Player 2. Both player lines contain the same number of symbols from the set {'R', 'P', 'S'}.  The number of symbols per line is between 1 and 75, inclusive.  A pair of lines each containing the single character 'E' signifies the end of the input.</p>

### 출력 

 <p>For each pair of input lines, output a pair of output lines as shown in the sample output, indicating the number of games won by each player.</p>

