# [Bronze I] A No-Win Situation - 4119 

[문제 링크](https://www.acmicpc.net/problem/4119) 

### 성능 요약

메모리: 115352 KB, 시간: 236 ms

### 분류

브루트포스 알고리즘

### 문제 설명

<p>Consider a simple variation of the card game Blackjack. In this game, a single player plays against the dealer. The game uses a standard deck of cards, where numbered cards are worth the number of points on the card for the cards numbered 2 to 10, 10 points for the face cards (King, Queen, and Jack) and either 1 or 11 points for the Aces.</p>

<p>The dealer deals the first card in the deck to the player, the second to the dealer, the third to the player, and the fourth to the dealer. The player then may continue to draw cards until s/he decides that the total is as close as possible to 21 and stops voluntarily or until s/he goes over 21. If the player goes over 21, the player loses. Then the dealer must draw cards until s/he reaches 17 or more points (with aces counting as 11 when possible). If the dealer goes over 21, the dealer loses. If neither of them goes over 21, the winner is the one who comes as close as possible to 21. If the player and the dealer have the same total, the player wins.</p>

<p>For example, suppose the first cards in the deck are Queen, 6, 4, 9, and 10. On the initial deal, the player will receive Queen and 4 (for a total of 14) and the dealer will receive 6 and 9 (for a total of 15). If the player does not select a card, the dealer will have to draw (because the dealer's total is less than 17) and will draw the 10, going over, so the player will win. But if the player draws a card (the 10), the player's total will be 24, so the player will lose.</p>

<p>In some situations, it is impossible for the player to win. Consider the case when the cards in the deck are: 10, 3, 4, King, 3, 5. The player will be dealt the cards 10 and 4. The dealer will have 3 and King. The table below illustrates what happens for each number of cards the player might draw: </p>

<table class="table table-bordered" style="width:60%">
	<thead>
		<tr>
			<th>Cards drawn</th>
			<th>Player's hand (Points)</th>
			<th>Dealer's hand (Points)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>10, 4 (14)</td>
			<td>3, King, 3, 5 (21)</td>
		</tr>
		<tr>
			<td>1</td>
			<td>10, 4, 3 (17)</td>
			<td>3, King, 5 (18)</td>
		</tr>
		<tr>
			<td>2</td>
			<td>10, 4, 3, 5 (22)</td>
			<td>3, King (13)</td>
		</tr>
	</tbody>
</table>

<p>No matter how many cards the player draws, the player cannot win.</p>

<p>In this problem, you will analyze decks to determine if they lead to a situation in which the player cannot win. </p>

### 입력 

 <p>The input to the program will be one or more decks. Each deck will be represented by a string, on its own line. Each deck will consist of at least 4 cards. where a card is either an integer d, 2 <= d <= 9, representing a numbered card, or one of the letters A, K, Q, J or T, representing Ace, King, Queen, Jack, or Ten, respectively. The letters will be in upper case. There will be no other characters on a line. In particular, there will be no spaces. There will always be enough cards to try all valid draws. End of input is indicated by the word JOKER, alone on a line. </p>

### 출력 

 <p>Print a list of responses for the input sets, one per line. Print the word Yes if there is a number of cards the player can draw and win, and No if there is no way for the player to win. Print these words exactly as they are shown. Do not print any blank lines between outputs. </p>

