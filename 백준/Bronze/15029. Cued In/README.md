# [Bronze I] Cued In - 15029 

[문제 링크](https://www.acmicpc.net/problem/15029) 

### 성능 요약

메모리: 45540 KB, 시간: 164 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation), 문자열(string)

### 문제 설명

<p>Snooker is a cue sport played by two players on a rectangular table. The players take turns to pot a series of balls of varying colours, where each colour represents a distinct point value for potting the ball.</p>

<p>A player may pot any ball on the table initially, however any subsequent shots must follow a pattern: if the previous ball was red, the next ball must be another colour; otherwise, if there are still red balls left, the next ball must be red.</p>

<p>Balls of any colour other than red are initially replaced on the table every time they are potted, and may be used again to score more points. The balls stop being replaced once all of the red balls have been potted.</p>

<p>The values of each coloured ball are:</p>

<table class="table table-bordered" style="width:50%">
	<tbody>
		<tr>
			<th>Colour</th>
			<td>red</td>
			<td>yellow</td>
			<td>green</td>
			<td>brown</td>
			<td>blue</td>
			<td>pink</td>
			<td>black</td>
		</tr>
		<tr>
			<th>Value</th>
			<td>1</td>
			<td>2</td>
			<td>3</td>
			<td>4</td>
			<td>5</td>
			<td>6</td>
			<td>7</td>
		</tr>
	</tbody>
</table>

<p>Snooker players are respected universally for their prowess in mental arithmetic. One sweeping glance across the table is enough to tell an experienced contestant how much they could score.</p>

<p>For newer players, however, this is a challenge. Write a program to help calculate a score for a given list of balls remaining on the table.</p>

### 입력 

 <ul>
	<li>one line containing the integers N (1 ≤ N ≤ 21), the number of balls remaining on the table.</li>
	<li>N further lines, each containing the colour of one of the balls on the table.</li>
</ul>

<p>The list of balls will not be ordered in any way and will contain at most one of each of yellow, green, brown, blue, pink and black.</p>

### 출력 

 <p>Output the largest possible score the player can make.</p>

