# [Silver IV] Card Stacking - 6149 

[문제 링크](https://www.acmicpc.net/problem/6149) 

### 성능 요약

메모리: 129864 KB, 시간: 192 ms

### 분류

자료 구조(data_structures), 덱(deque), 구현(implementation), 큐(queue), 시뮬레이션(simulation)

### 문제 설명

<p>Bessie is playing a card game with her N-1 (2 <= N <= 100) cow friends using a deck with K (N <= K <= 100,000; K is a multiple of N) cards.  The deck contains M = K/N "good" cards and K-M "bad" cards. Bessie is the dealer and, naturally, wants to deal herself all of the "good" cards. She loves winning.</p>

<p>Her friends suspect that she will cheat, though, so they devise a dealing system in an attempt to prevent Bessie from cheating. They tell her to deal as follows:</p>

<ol>
	<li>Start by dealing the card on the top of the deck to the cow to her right</li>
	<li>Every time she deals a card, she must place the next P (1 <= P <= 10) cards on the bottom of the deck; and</li>
	<li>Continue dealing in this manner to each player sequentially in a counterclockwise manner</li>
</ol>

<p>Bessie, desperate to win, asks you to help her figure out where she should put the "good" cards so that she gets all of them. Notationally, the top card is card #1, next card is #2, and so on.</p>

### 입력 

 <ul>
	<li>Line 1: Three space-separated integers: N, K, and P</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..M: Positions from top in ascending order in which Bessie should place "good" cards, such that when dealt, Bessie will obtain all good cards.</li>
</ul>

<p> </p>

