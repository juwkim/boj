# [Silver III] Round Robin - 9436 

[문제 링크](https://www.acmicpc.net/problem/9436) 

### 성능 요약

메모리: 113164 KB, 시간: 136 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 2월 8일 23:06:54

### 문제 설명

<p>Suppose that N players sit in order and take turns in a game, with the first person following the last person, to continue in cyclic order. While doing so, each player keeps track of the number of turns he or she has taken. The game consists of rounds, and in each round T turns are taken. After a round, the player who just had a turn is eliminated from the game. If the remaining players have all had the same number of turns, the game ends. Otherwise, they continue with another round of T moves, starting with the player just after the one who was most recently eliminated.</p>

<p>As an example, assume we begin a game with N=5 and T=17, labeling the players in order as A, B, C, D, and E, with all counts initially zero.</p>

<table class="table table-bordered" style="height:50px; text-align:left; width:250px">
	<tbody>
		<tr>
			<td style="vertical-align:top">Player</td>
			<td style="vertical-align:top">A</td>
			<td style="vertical-align:top">B</td>
			<td style="vertical-align:top">C</td>
			<td style="vertical-align:top">D</td>
			<td style="vertical-align:top">E</td>
		</tr>
		<tr>
			<td style="vertical-align:top">Count</td>
			<td style="vertical-align:top">0</td>
			<td style="vertical-align:top">0</td>
			<td style="vertical-align:top">0</td>
			<td style="vertical-align:top">0</td>
			<td style="vertical-align:top">0</td>
		</tr>
	</tbody>
</table>

<p>Beginning with A, 17 turns are taken. B will have taken the last of those turn, leaving our counts as follows:</p>

<table class="table table-bordered" style="height:50px; text-align:left; width:250px">
	<tbody>
		<tr>
			<td style="vertical-align:top">Player</td>
			<td style="vertical-align:top">A</td>
			<td style="background-color:silver; vertical-align:top">B</td>
			<td style="vertical-align:top">C</td>
			<td style="vertical-align:top">D</td>
			<td style="vertical-align:top">E</td>
		</tr>
		<tr>
			<td style="vertical-align:top">Count</td>
			<td style="vertical-align:top">4</td>
			<td style="background-color:silver; vertical-align:top">4</td>
			<td style="vertical-align:top">3</td>
			<td style="vertical-align:top">3</td>
			<td style="vertical-align:top">3</td>
		</tr>
	</tbody>
</table>

<p>Suppose that after <em>every</em> 17 turns, the player who just had a turn is eliminated from the game. All remaining players then compare their counts. If all of those counts are equal, everyone has had a fair number of turns and the game is considered completed. Otherwise, they continue with another round of 17 moves starting with the player just after the one who was most recently eliminated.</p>

<p>Continuing with our example, B will leave the game, and the next turn will be for C.</p>

<table class="table table-bordered" style="height:50px; text-align:left; width:250px">
	<tbody>
		<tr>
			<td style="vertical-align:top">Player</td>
			<td style="vertical-align:top">A</td>
			<td style="vertical-align:top">C</td>
			<td style="vertical-align:top">D</td>
			<td style="vertical-align:top">E</td>
		</tr>
		<tr>
			<td style="vertical-align:top">Count</td>
			<td style="vertical-align:top">4</td>
			<td style="vertical-align:top">3</td>
			<td style="vertical-align:top">3</td>
			<td style="vertical-align:top">3</td>
		</tr>
	</tbody>
</table>

<p>After 17 more turns starting with C, we find that A, D and E received 4 turns, while C received 5 turns, including the last:</p>

<table class="table table-bordered" style="height:50px; text-align:left; width:250px">
	<tbody>
		<tr>
			<td style="vertical-align:top">Player</td>
			<td style="vertical-align:top">A</td>
			<td style="background-color:silver; vertical-align:top">C</td>
			<td style="vertical-align:top">D</td>
			<td style="vertical-align:top">E</td>
		</tr>
		<tr>
			<td style="vertical-align:top">Count</td>
			<td style="vertical-align:top">8</td>
			<td style="background-color:silver; vertical-align:top">8</td>
			<td style="vertical-align:top">7</td>
			<td style="vertical-align:top">7</td>
		</tr>
	</tbody>
</table>

<p>Then C leaves, and since the remaining counts are not all the same, a new round beings with D having the next turn.</p>

<table class="table table-bordered" style="height:50px; text-align:left; width:250px">
	<tbody>
		<tr>
			<td style="vertical-align:top">Player</td>
			<td style="vertical-align:top">A</td>
			<td style="vertical-align:top">D</td>
			<td style="vertical-align:top">E</td>
		</tr>
		<tr>
			<td style="vertical-align:top">Count</td>
			<td style="vertical-align:top">8</td>
			<td style="vertical-align:top">7</td>
			<td style="vertical-align:top">7</td>
		</tr>
	</tbody>
</table>

<p>The next 17 turns start with D and end with E.   A adds 5 turns, while D and E add 6:</p>

<table class="table table-bordered" style="height:50px; text-align:left; width:250px">
	<tbody>
		<tr>
			<td style="vertical-align:top">Player</td>
			<td style="vertical-align:top">A</td>
			<td style="vertical-align:top">D</td>
			<td style="background-color:silver; vertical-align:top">E</td>
		</tr>
		<tr>
			<td style="vertical-align:top">Count</td>
			<td style="vertical-align:top">13</td>
			<td style="vertical-align:top">13</td>
			<td style="background-color:silver; vertical-align:top">13</td>
		</tr>
	</tbody>
</table>

<p>Then E leaves.</p>

<table class="table table-bordered" style="height:50px; text-align:left; width:250px">
	<tbody>
		<tr>
			<td style="vertical-align:top">Player</td>
			<td style="vertical-align:top">A</td>
			<td style="vertical-align:top">D</td>
		</tr>
		<tr>
			<td style="vertical-align:top">Count</td>
			<td style="vertical-align:top">13</td>
			<td style="vertical-align:top">13</td>
		</tr>
	</tbody>
</table>

<p>At this point, notice that the two remaining players have the same count of 13. Therefore, the game ends. (We note that E's count was irrelevant to the decision to end the game.)</p>

### 입력 

 <p>The input will contain one or more datasets.  Each dataset will be described with a single line containing two integers, <em>N</em> and <em>T</em>, where <em>N</em> (2 ≤ <em>N</em> ≤ 100) is the initial number of  players, and <em>T</em> (2 ≤ <em>T</em> ≤ 100) is the number of turns after which the player with the most recently completed turn leaves.  Following the last dataset is a line containing only 0.</p>

### 출력 

 <p>There is one line of output for each dataset, containing two numbers, <em>p</em> and <em>c</em>.  At the time the game ends <em>p</em> is the number of players that remain in the game and <em>c</em> is the common count they all have.</p>

