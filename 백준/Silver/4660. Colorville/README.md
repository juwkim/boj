# [Silver III] Colorville - 4660 

[문제 링크](https://www.acmicpc.net/problem/4660) 

### 성능 요약

메모리: 108080 KB, 시간: 104 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 4월 13일 10:36:11

### 문제 설명

<p>A simple matching game for children uses a board that is a sequence of colored squares. Each player has a game piece. Players alternate turns, drawing cards containing either one colored square or two colored squares of the same color. Players move their pieces forward on the board to the next square that matches the single color on the card, or forward to the second matching square if the card contains two colored squares, or forward to the last square on the board if there is no square matching the description above. A player wins if his piece lands on the last square of the board. It is possible for all the cards to be drawn and still not have a winner.</p>

<p>This problem represents colors with capital letters from A-Z. Below is a diagram of a sample board.</p>

<table border="1" cellpadding="1" cellspacing="1" style="width:300px">
	<tbody>
		<tr>
			<td style="text-align: center;">R</td>
			<td style="text-align: center;">Y</td>
			<td style="text-align: center;">G</td>
			<td style="text-align: center;">P</td>
			<td style="text-align: center;">B</td>
			<td style="text-align: center;">R</td>
			<td style="text-align: center;">Y</td>
			<td style="text-align: center;">G</td>
			<td style="text-align: center;">B</td>
			<td style="text-align: center;">R</td>
			<td style="text-align: center;">P</td>
			<td style="text-align: center;">O</td>
			<td style="text-align: center;">P</td>
		</tr>
	</tbody>
</table>

<p>START                                                                      FINISH</p>

<p>Consider the deck of cards: R, B, GG, Y, P, B, P, RR</p>

<p>For 3 players, the game proceeds as follows:</p>

<p>Player 1 draws R,    moves to 1st square<br>
Player 2 draws B,   moves to 5th square<br>
Player 3 draws GG, moves to 8th square<br>
Player 1 draws Y,    moves to 2nd square<br>
Player 2 draws P,   moves to 11th square<br>
Player 3 draws B,   moves to 9th square<br>
Player 1 draws P,    moves to 4th square<br>
Player 2 draws RR, Wins! (no Rs in front of piece so it goes to last square)</p>

<p>Using the same board and the same deck of cards, but with 2 players, Player 1 wins after 7 cards. With 4 players, no one wins after exhausting the deck of 8 cards.</p>

### 입력 

 <p>Input consists of information for one or more games. Each game starts with one line containing the number of players (1-4), the number of squares on the board (1-79), and the number of cards in the deck (1-200). This is followed by a single line of characters representing the colored squares on the board. Following this are the cards in the deck, one card per line. Cards can have only a single character, or two of the same character. The end of the input is signalled by a line with 0 for the number of players - the other two values will be present but indeterminate.</p>

### 출력 

 <p>For each game, the output is either the winning player and the total number of cards drawn, or the number of cards in the deck, as shown in the sample output. Always use the plural "cards".</p>

