# [Silver IV] Against a rock play Spock - 27702 

[문제 링크](https://www.acmicpc.net/problem/27702) 

### 성능 요약

메모리: 110476 KB, 시간: 2508 ms

### 분류

많은 조건 분기, 구현

### 제출 일자

2023년 10월 11일 19:03:08

### 문제 설명

<p>For many people, a Rock-Paper-Scissors game is too simple and thus boring. As IPSC should not be boring, we will be playing an extended version called Rock-Paper-Scissors-Lizard-Spock.</p>

<p>The game contains five gestures: rock, paper, scissors, lizard, and Spock. Lizard is usually formed by a hand closed to a sock-puppet-like mouth and Spock is formed by the Star Trek Vulcan salute. In each round of the game, both players simultaneously show one of the five gestures.</p>

<p>Each round is evaluated as follows: If the two gestures are equal, the round ends in a tie (nobody wins). Otherwise look at the table below and find the row that contains both gestures shown. The player showing the gesture in the left column wins. To the right of the table you can see figures from Wikipedia that contain the same information.</p>

<table class="table table-bordered td-center td-middle">
	<tbody>
		<tr>
			<td>
			<table class="table table-bordered">
				<tbody>
					<tr>
						<td>scissors</td>
						<td>cut</td>
						<td>paper</td>
					</tr>
					<tr>
						<td>paper</td>
						<td>covers</td>
						<td>rock</td>
					</tr>
					<tr>
						<td>rock</td>
						<td>crushes</td>
						<td>lizard</td>
					</tr>
					<tr>
						<td>lizard</td>
						<td>poisons</td>
						<td>Spock</td>
					</tr>
					<tr>
						<td>Spock</td>
						<td>smashes</td>
						<td>scissors</td>
					</tr>
					<tr>
						<td>scissors</td>
						<td>decapitate</td>
						<td>lizard</td>
					</tr>
					<tr>
						<td>lizard</td>
						<td>eats</td>
						<td>paper</td>
					</tr>
					<tr>
						<td>paper</td>
						<td>disproves</td>
						<td>Spock</td>
					</tr>
					<tr>
						<td>Spock</td>
						<td>vaporizes</td>
						<td>rock</td>
					</tr>
					<tr>
						<td>rock</td>
						<td>breaks</td>
						<td>scissors</td>
					</tr>
				</tbody>
			</table>
			</td>
			<td><img alt="" src=""></td>
			<td><img alt="" src="https://upload.acmicpc.net/d155aaa6-1604-4cad-8490-fea545cfdeb0/-/preview/"></td>
		</tr>
	</tbody>
</table>

<p>The input contains the sequence of gestures we are going to play in the following rounds. For each gesture, output a line containing the name of the gesture you are going to play against it.</p>

<p>To solve the easy subtask, your task is to win every round of the game.</p>

<p>To solve the hard subtask, your task is the same. But you have to do it without using the same gesture twice in a row.</p>

<p>For instance, suppose that in round 1 we played Spock and you played paper. If we play rock in round 2, you can only win by playing Spock, you may not play paper again. In round 3, you then cannot play Spock, but you may play paper again, if you wish.</p>

### 입력 

 <p>The first line contains a positive integer r: the number of rounds we will play.</p>

<p>Each of the next r lines contains one of the five strings rock, paper, scissors, lizard, and Spock.</p>

### 출력 

 <p>For each round, output a single line containing your gesture – again, one of the strings rock, paper, scissors, lizard, and Spock. (Note the uppercase ‘S’ in Spock.)</p>

