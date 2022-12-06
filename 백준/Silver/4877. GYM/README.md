# [Silver V] GYM - 4877 

[문제 링크](https://www.acmicpc.net/problem/4877) 

### 성능 요약

메모리: 114328 KB, 시간: 116 ms

### 분류

수학(math), 확률론(probability)

### 문제 설명

<p>Model a stochastic gym exercise.</p>

<p>An entertaining game for elementary school children in gym class is set up as follows:</p>

<ul>
	<li>N baskets are placed at various locations on the gym floor, each with a distinguishing picture on them.</li>
	<li>Each basket contains some index cards. Each index card has a destination written on them.</li>
</ul>

<p>The game proceed as follows: the children gather at a specified start basket. They each take a turn picking a random card from the basket, memorizing the destination, and returning the card before the next child picks one. When the teacher blows the whistle, all the children move to the basket indicated on the notecard.</p>

<p>Given the configuration of index cards at each basket, you are to determine the probabiliites a kindergardener will appear at each basket for the first ten steps of the game.</p>

<p>For example, suppose there are four baskets, "tree," "house," "car" and "park." Each basket has the following index cards:</p>

<ul>
	<li>The "tree" basket has 2 cards with "tree" on it, 1 card with "house", and 2 cards with "car."</li>
	<li>The "house" basket has 1 card with "tree" on it, 1 card with "car" on it, and 2 cards with "park" on it.</li>
	<li>The "car" basket has 1 card with "tree" on it.</li>
	<li>The "park" basket has one of each card in it.</li>
</ul>

<p>This arrangement is summarized by the following table:</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td> </td>
			<td colspan="4"><b>destination</b></td>
		</tr>
		<tr>
			<td><b>basket</b></td>
			<td><b>tree</b></td>
			<td><b>house</b></td>
			<td><b>car</b></td>
			<td><b>park</b></td>
		</tr>
		<tr>
			<td><b>tree</b></td>
			<td>2</td>
			<td>1</td>
			<td>2</td>
			<td>0</td>
		</tr>
		<tr>
			<td><b>house</b></td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td><b>car</b></td>
			<td>1</td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td><b>park</b></td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p>Everyone starts at the tree, so initially,</p>

<ul>
	<li>P<sub>0</sub>(tree)=1, and P<sub>0</sub>(else where)=0</li>
</ul>

<p>In the middle of the game, the probablity of being at some new location is equal to the sum of the probabilities of being at any location on the previous step, times the probablity of moving to the destination location from that past location. For the example,</p>

<ul>
	<li>P<sub>s+1</sub>(tree)=0.20*P<sub>s</sub>(tree)+0.25*P<sub>s</sub>(house)+1.00*P<sub>s</sub>(car)+0.25*P<sub>s</sub>(park)</li>
</ul>

### 입력 

 <p>For N baskets, 2<=N<=10, the input file will contain N lines of information. The N lines will give the index card count as in the table for the example above. There will be at most 10 cards of the same name in any given basket, and each basket will contain at least one card.</p>

### 출력 

 <p>There should be 10 lines of output for any given input. Other than the standard header and footer, you should print out the probabilites for seeing a kindergardener at any given basked for the first 10 steps in the game.</p>

<p>Your results should give the correct probablities to at least four digits of precision. We recommend you do the internal computations using double precision arithmetic.</p>

