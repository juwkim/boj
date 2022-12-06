# [Silver V] Next Mayor - 4962 

[문제 링크](https://www.acmicpc.net/problem/4962) 

### 성능 요약

메모리: 115136 KB, 시간: 252 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>One of the oddest traditions of the town of Gameston may be that even the town mayor of the next term is chosen according to the result of a game. When the expiration of the term of the mayor approaches, at least three candidates, including the mayor of the time, play a game of pebbles, and the winner will be the next mayor.</p>

<p>The rule of the game of pebbles is as follows. In what follows, n is the number of participating candidates.</p>

<ul>
	<li>Requisites
	<ul>
		<li>A round table, a bowl, and plenty of pebbles.</li>
	</ul>
	</li>
	<li>Start of the Game
	<ul>
		<li>A number of pebbles are put into the bowl; the number is decided by the Administration Commission using some secret stochastic process. All the candidates, numbered from 0 to n-1 sit around the round table, in a counterclockwise order. Initially, the bowl is handed to the serving mayor at the time, who is numbered 0.</li>
	</ul>
	</li>
	<li>Game Steps
	<ul>
		<li>When a candidate is handed the bowl and if any pebbles are in it, one pebble is taken out of the bowl and is kept, together with those already at hand, if any. If no pebbles are left in the bowl, the candidate puts all the kept pebbles, if any, into the bowl. Then, in either case, the bowl is handed to the next candidate to the right. This step is repeated until the winner is decided.</li>
	</ul>
	</li>
	<li>End of the Game
	<ul>
		<li>When a candidate takes the last pebble in the bowl, and no other candidates keep any pebbles, the game ends and that candidate with all the pebbles is the winner.</li>
	</ul>
	</li>
</ul>

<p>A math teacher of Gameston High, through his analysis, concluded that this game will always end within a finite number of steps, although the number of required steps can be very large.</p>

### 입력 

 <p>The input is a sequence of datasets. Each dataset is a line containing two integers n and p separated by a single space. The integer n is the number of the candidates including the current mayor, and the integer p is the total number of the pebbles initially put in the bowl. You may assume 3 ≤ n ≤ 50 and 2 ≤ p ≤ 50.</p>

<p>With the settings given in the input datasets, the game will end within 1000000 (one million) steps.</p>

<p>The end of the input is indicated by a line containing two zeros separated by a single space.</p>

### 출력 

 <p>The output should be composed of lines corresponding to input datasets in the same order, each line of which containing the candidate number of the winner. No other characters should appear in the output.</p>

