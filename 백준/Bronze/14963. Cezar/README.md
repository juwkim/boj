# [Bronze I] Cezar - 14963 

[문제 링크](https://www.acmicpc.net/problem/14963) 

### 성능 요약

메모리: 29200 KB, 시간: 72 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Little Caesar likes card games. Everytime he comes to Zagreb, he plays blackjack, the famous card game, with his friends.</p>

<p>In this game, the player draws cards while the sum of the cards in his hand is less than or equal to 21 or until he says “DOSTA” (Croatian for “STOP”). At the beginning of the game, there are 52 cards in the deck, thirteen ranks of each of the four suits. The card ranks are two, three, …, ten, Jack, Queen, King and Ace. The card values are the following: the cards with numbers on them are worth that number (e.g., “nine” is 9), the cards with pictures (Jack, Queen, and King) are worth 10, whereas the Ace is worth 11.</p>

<p>Caesar has found himself in an interesting situation. During the game, he already drew N cards whose sum is less than or equal to 21 and is now having second thoughts about drawing one more card or not. Let’s assume X is the difference from the sum of the cards so far to 21. Everybody knows that you don’t draw a card if the number of the remaining cards in the deck whose value is greater than X is greater than or equal to the number of the remaining cards in the deck whose value is less than or equal to X.</p>

<p>Since Caesar is having a difficult time calculating whether he needs to draw another card or not, he’s asking you to do it for him.</p>

### 입력 

 <p>The first line of input contains the positive integer N (1 ≤ N ≤ 52), the number of cards Caesar has drawn so far.</p>

<p>Each of the following N lines contains a single positive integer, the value of the i th card Caesar drew.</p>

### 출력 

 <p>If Caesar should draw another card, output “VUCI” (Croatian for “DRAW”), otherwise output “DOSTA” (Croatian for “STOP”).</p>

