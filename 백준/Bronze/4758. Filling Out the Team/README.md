# [Bronze III] Filling Out the Team - 4758 

[문제 링크](https://www.acmicpc.net/problem/4758) 

### 성능 요약

메모리: 121220 KB, 시간: 100 ms

### 분류

구현(implementation)

### 문제 설명

<p>Over the years, the people of the great city of Pittsburgh have repeatedly demonstrated a collective expertise at football second to none. Recently a spy has discovered the true source of the city’s football power—a wizard known only as “Myron,” who is infallible at selecting the proper position at which each player will excel.</p>

<p>Now that you know the source of Pittsburgh’s wisdom, you are determined to provide your school’s football team with a computer program that matches the wisdom of “Myron.” You have consulted with the best football minds you can find, and they have dispensed their wisdom on the slowest speed, minimum weight, and minimum strength required to play each position.</p>

<table border="1" cellpadding="1" cellspacing="1" style="width:500px">
	<tbody>
		<tr>
			<td style="text-align: center;">Position</td>
			<td style="text-align: center;">Slow. Speed</td>
			<td style="text-align: center;">Min. Weight</td>
			<td style="text-align: center;">Min. Strength</td>
		</tr>
		<tr>
			<td style="text-align: center;">Wide Receiver</td>
			<td style="text-align: center;">4.5</td>
			<td style="text-align: center;">150</td>
			<td style="text-align: center;">200</td>
		</tr>
		<tr>
			<td style="text-align: center;">Lineman </td>
			<td style="text-align: center;">6.0</td>
			<td style="text-align: center;">300</td>
			<td style="text-align: center;">500</td>
		</tr>
		<tr>
			<td style="text-align: center;">Quarterback</td>
			<td style="text-align: center;">5.0</td>
			<td style="text-align: center;">200</td>
			<td style="text-align: center;">300</td>
		</tr>
	</tbody>
</table>

<p>Using this knowledge, you will develop a program that reads in several players physical at- tributes and outputs what position(s) they are able to play.</p>

### 입력 

 <p>Each line of the input file will list the attributes for one player:</p>

<p><speed> <weight> <strength></p>

<p>Each number will be a real-valued number. The file will end with a line reading “0 0 0”</p>

### 출력 

 <p>For each player, you will output one line listing the positions that player can play. A player can play a position if each of their attributes is greater or equal to the minimum for weight and strength, and less than or equal to the slowest speed. If a player can play multiple positions, output them in the order listed above, separated by whitespace. You may leave an extra space at the end of the line. If a player can play no positions, write “No positions” on the line.</p>

