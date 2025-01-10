# [Silver II] Leave No One Behind - 25528 

[문제 링크](https://www.acmicpc.net/problem/25528) 

### 성능 요약

메모리: 118592 KB, 시간: 228 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 1월 10일 13:24:55

### 문제 설명

<p>A card game similar to Old Maid is played by <i>n</i> players <i>P</i><sub>1</sub>, ..., and <i>P<sub>n</sub>,</i> sitting clockwise in this order.</p>

<p>For this game, <i>n</i> pairs of cards numbered 1 through <i>n</i> are used. Each player has two cards at hand to start with.</p>

<p>First, any player who has a pair of cards with the same number discards them. If by chance all the players discard the cards in hand, the game ends. Otherwise, the following actions are repeated until the game ends. Note that, from now on, for a player <i>p,</i> <em>the next player</em> means the player closest to <i>p</i> in the clockwise direction among those who still have one or more cards at that point in time.</p>

<ul>
	<li>Choose the player <i>p</i> as follows.

	<ul>
		<li>For the first turn, choose <i>P</i><sub>1</sub>. If, however, <i>P</i><sub>1</sub> has no cards, choose the next player of <i>P</i><sub>1</sub>.</li>
		<li>For the second and subsequent turns, choose the next player of the one chosen for the previous turn.</li>
	</ul>
	</li>
	<li>The next player of <i>p</i>, say <i>p′,</i> looks at the card(s) in the hand of <i>p</i> and draws the one having the smallest number among them.</li>
	<li>If that makes a pair of cards with the same number in the hand of <i>p′</i>, the pair is discarded. If no cards remain in any players' hands at this point, the game ends.</li>
</ul>

<p>Figure B-1 shows the initial hands of the three players of the second dataset in Sample Input. Immediately after, the player <i>P</i><sub>1</sub> discards the two cards in the hand. <i>p</i> of the first turn is <i>P</i><sub>2</sub> because <i>P</i><sub>1</sub> has no cards.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/42f7bcc2-617f-4ae2-973c-a67debb0cab1/-/preview/" style="width: 400px; height: 330px;"></p>

<p style="text-align: center;">Figure B-1: The initial hands of the second dataset in Sample Input</p>

<p>Figure B-2 shows the hands of the five players of the last dataset in Sample Input after the following actions:</p>

<ul>
	<li><i>P</i><sub>1</sub> is chosen first and the next player of <i>P</i><sub>1</sub>, that is, <i>P</i><sub>2</sub>, draws the card with the smallest number 1 from the <i>P</i><sub>1</sub>'s hand. <i>P</i><sub>2</sub> has three cards with numbers 1, 3, and 5 in hand at the end of this turn;</li>
	<li><i>P</i><sub>3</sub>, <i>P</i><sub>4</sub>, and <i>P</i><sub>5</sub>, in this order, draw the same card with the number 1 that was initially in the <i>P</i><sub>1</sub>'s hand; and</li>
	<li><i>P</i><sub>5</sub> discards the pair of cards with the number 1.</li>
</ul>

<p>After this, <i>P</i><sub>1</sub> draws the only remaining card in <i>P</i><sub>5</sub>'s hand and discards the drawn card and the card with the same number 2 in the hand. The player to be drawn from the hand next is the next player of <i>P</i><sub>5</sub>, which is <i>P</i><sub>2</sub> because <i>P</i><sub>1</sub>'s hand is empty now.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/efe95bd2-ac19-4828-8d7b-d99f5f43cb39/-/preview/" style="width: 400px; height: 347px;"></p>

<p style="text-align: center;">Figure B-2: The hands of the last dataset in Sample Input after the fourth turn</p>

<p>Since at least one pair of cards is discarded between two drawings from the hand of the same player, the game will end sooner or later. Unlike Old Maid, no cards will be left in the hand of any player at the end.</p>

<p>Write a program that, for given initial hands of all the players, computes the number of times cards are drawn by the end of the game.</p>

### 입력 

 <p>The input consists of multiple datasets, each in the following format.</p>

<pre><i>n</i>
<i>c</i><sub>1,1</sub> <i>c</i><sub>1,2</sub>
⋮
<i>c</i><sub><i>n</i>,1</sub> <i>c</i><sub><i>n</i>,2</sub></pre>

<p><i>n</i> is the number of players. <i>n</i> is an integer no less than two and no more than 1000. <i>c</i><sub><i>i</i>,1</sub> and <i>c</i><sub><i>i</i>,2</sub> are the numbers on the two cards in the initial hand of <i>P<sub>i</sub></i> (1 ≤ <i>i</i> ≤ <i>n</i>). Each integer between 1 and <i>n,</i> inclusive, appears exactly twice in <i>c</i><sub>1,1</sub>, <i>c</i><sub>1,2</sub>, ..., <i>c</i><sub><i>n</i>,1</sub>, and <i>c</i><sub><i>n</i>,2</sub>.</p>

<p>The end of the input is indicated by a line containing a zero. The input has at most 10000 lines.</p>

### 출력 

 <p>For each dataset, output a single line containing the integer that is the number of times cards are drawn.</p>

