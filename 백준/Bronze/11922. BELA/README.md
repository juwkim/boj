# [Bronze II] BELA - 11922 

[문제 링크](https://www.acmicpc.net/problem/11922) 

### 성능 요약

메모리: 28776 KB, 시간: 84 ms

### 분류

구현(implementation)

### 문제 설명

<p>Young Mirko is a smart, but mischievous boy who often wanders around parks looking for new ideas. This time he’s come across pensioners playing the card game Belote. They’ve invited him to help them determine the total number of points won in a single game.</p>

<p>Each card can be uniquely determined by its symbol and suit. A set of four cards is called a hand. In each game, one suit that "trumps" any other and is called the dominant suit. The number of points in a single game is equal to the sum of scoring values of each card from each hand won in the game. Mirko has noticed that the pensioners have won N hands and that suit B was the dominant suit.</p>

<p>The scoring values of cards are given in the following table:</p>

<table class="table table-bordered" style="width:50%">
	<thead>
		<tr>
			<th rowspan="2">Card Symbol</th>
			<th colspan="2">Card scoring value</th>
		</tr>
		<tr>
			<th>If dominant suit</th>
			<th>If not dominant suit</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>A</td>
			<td>11</td>
			<td>11</td>
		</tr>
		<tr>
			<td>K</td>
			<td>4</td>
			<td>4</td>
		</tr>
		<tr>
			<td>Q</td>
			<td>3</td>
			<td>3</td>
		</tr>
		<tr>
			<td>J</td>
			<td>20</td>
			<td>2</td>
		</tr>
		<tr>
			<td>T</td>
			<td>10</td>
			<td>10</td>
		</tr>
		<tr>
			<td>9</td>
			<td>14</td>
			<td>0</td>
		</tr>
		<tr>
			<td>8</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>7</td>
			<td>0</td>
			<td>0</td>
		</tr>
	</tbody>
</table>

<p>Write a programme that will determine and output the total number of points won in the game.</p>

### 입력 

 <p>The first line contains the number of hands N (1 ≤ N ≤ 100) and the value of suit B (S, H, D, C) from the task.</p>

<p>Each of the following 4N lines contains the description of card Ki (the first character being the label of the ith card (A, K, Q, J, T, 9, 8, 7), the second character being the suit of the ith card (S, H, D, C)).</p>

### 출력 

 <p>The first and only line of output must contain the number of points from the task.</p>

