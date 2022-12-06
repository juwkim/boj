# [Bronze II] D as in Daedalus - 11544 

[문제 링크](https://www.acmicpc.net/problem/11544) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

Empty

### 문제 설명

<p>Daedalus is playing the game of “Don’t be greedy”, in which N players sit around a table having each of them five cards labelled 1, 10, 100, 1000 and 10000 points. In “Don’t be greedy” the players may not talk to each other once the game starts, and there are M rounds. In each round, the bank announces a budget B. Then each player chooses one of the cards and places it, face down, on the table. The bank then turns the cards, so that all players can see all N cards. If the sum of the points in the chosen cards is less than or equal to B, then the bank gives to each player exactly the amount of points in the card he or she chose. Otherwise, no one gets anything. Each player gets his or her card back before the next round. The players are very rational and would like to maximize their points and minimize their regrets! What would you do in this situation? Cooperate or defect?</p>

<p>Take the following table as an example. Daedalus won a total of 10 points, in the end, because only the first round was successful. But, looking back on the game, he sees that he could have won 110 points, if he had chosen 100 points in the first round and 10 points in the third round. That is, Daedalus could have won 100 extra points! This holds only, of course, assuming the cards chosen by the other players remain unchanged.</p>

<table class="table table-bordered" style="width:30%">
	<thead>
		<tr>
			<th>round</th>
			<th>budget B</th>
			<th>Daedalus</th>
			<th>Iapyx</th>
			<th>Icarus</th>
			<th>Ariadne</th>
			<th>Minos</th>
			<th>sum</th>
			<th>result</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>300</td>
			<td>10</td>
			<td>100</td>
			<td>10</td>
			<td>1</td>
			<td>10</td>
			<td>131</td>
			<td>success</td>
		</tr>
		<tr>
			<td>2</td>
			<td>1100</td>
			<td>100</td>
			<td>10</td>
			<td>100</td>
			<td>1</td>
			<td>1000</td>
			<td>1211</td>
			<td>fail</td>
		</tr>
		<tr>
			<td>3</td>
			<td>1200</td>
			<td>100</td>
			<td>100</td>
			<td>10</td>
			<td>1</td>
			<td>1000</td>
			<td>1211</td>
			<td>fail</td>
		</tr>
	</tbody>
</table>

<p>Given the budget and the cards chosen in each round, we need to compute the maximum total number of extra points Daedalus could have won, in the end, if he had chosen the best possible card in each round, assuming the cards chosen by the other players remain unchanged.</p>

### 입력 

 <p>The first line contains two integers N and M, representing respectively the number of players and the number of rounds (1 ≤ N ≤ 20 and 1 ≤ M ≤ 50). Each of the next M lines describes a round with an integer B indicating the budget (1 ≤ B ≤ 10<sup>6</sup>), followed by N integers C<sub>1</sub>, C<sub>2</sub>, . . . , CN representing that the i-th player chose the card labelled with C<sub>i</sub> points during that round (C<sub>i</sub> ∈ {1, 10, 100, 1000, 10000} for i = 1, 2, . . . , N). Daedalus is the first player.</p>

### 출력 

 <p>Output a line with an integer representing the maximum total number of extra points Daedalus could have won, if he had chosen the best possible card in each round, assuming the cards chosen by the other players remain unchanged.</p>

