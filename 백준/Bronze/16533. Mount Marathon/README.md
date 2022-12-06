# [Bronze I] Mount Marathon - 16533 

[문제 링크](https://www.acmicpc.net/problem/16533) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>Mount Marathon is a solitaire game that is played using a regular deck of 52 cards. To start the game the player shuffles the deck and lays N cards face up on the table, forming a straight line of N piles, each pile having a single card. No other cards are used during the rest of the play. Then the player repeatedly moves a pile on top of another pile until no more movements are available. The goal of the game is to end up with the minimum number of piles. When moving a pile p on top of another pile q, the following conditions must hold:</p>

<ul>
	<li>Pile p must be a single-card pile.</li>
	<li>The value of the only card in pile p must be greater than or equal the value of the card that is on top of pile q.</li>
	<li>Pile q must be the next pile remaining immediately on the right of pile p.</li>
</ul>

<p>Figure (a) below shows a configuration with six cards at the beginning of the game. The player may move the fifth pile on top of the sixth pile, and then the second pile on top of the third pile; since no more movements are available, this would conclude the game with four piles remaining, as it can be seen in figure (b). However, in this case it is possible to end up the game with just the three piles that appear in figure (c).</p>

<p style="text-align: center;"><img alt="" src="" style="width: 601px; height: 221px;"></p>

<p>Given the initial piles, you must determine the minimum number of piles that it is possible to obtain at the end of the game.</p>

### 입력 

 <p>The first line contains an integer N (1 ≤ N ≤ 52) representing the number of cards in the game. The second line contains N integers C<sub>1</sub>, C<sub>2</sub>, . . . , C<sub>N</sub> (1 ≤ C<sub>i</sub> ≤ 13 for i = 1, 2, . . . , N) indicating the values of the cards in the initial piles, from left to right. Each card value appears at most four times.</p>

### 출력 

 <p>Output a single line with an integer indicating the minimum number of piles that it is possible to obtain at the end of the game.</p>

