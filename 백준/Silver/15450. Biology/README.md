# [Silver I] Biology - 15450 

[문제 링크](https://www.acmicpc.net/problem/15450) 

### 성능 요약

메모리: 116112 KB, 시간: 492 ms

### 분류

구현, 브루트포스 알고리즘

### 제출 일자

2025년 8월 16일 01:44:17

### 문제 설명

<p>Vera has A × B cards. Each card has a rank, an integer between 0 and A − 1, and a suit, an integer between 0 and B − 1. All cards are distinct. A set of five different cards is known as a hand. Each hand is in exactly one of nine categories numbered from 1 to 9. If a hand satisfies the conditions for membership in multiple categories, it is considered to be in the lowest-numbered such category. The rules for each category are:</p>

<ol>
	<li>Straight flush: is a Straight and a Flush.</li>
	<li>Four of a kind: four of the cards have the same rank.</li>
	<li>Full house: three of the cards have the same rank and the remaining two have the same rank.</li>
	<li>Flush: all five cards have the same suit.</li>
	<li>Straight: the ranks of the cards in increasing order are x, x + 1, x + 2, x + 3, x + 4 for some integer x.</li>
	<li>Three of a kind: three of the cards have the same rank.</li>
	<li>Two pair: two cards have the same rank and two other cards have the same rank.</li>
	<li>One pair: two cards have the same rank.</li>
	<li>High card: if a hand does not satisfy any other category.</li>
</ol>

<p>Currently, Vera has two cards with ranks a<sub>1</sub>, a<sub>2</sub> and suits b<sub>1</sub>, b<sub>2</sub>. Of the remaining cards, Vera will choose three more cards and form a hand with her two current cards. Compute the number of different hands formed in this way that belong in each category.</p>

### 입력 

 <p>Line 1 contains integers A and B (5 ≤ A ≤ 25, 1 ≤ B ≤ 4).</p>

<p>Line 2 contains integers a<sub>1</sub>, b<sub>1</sub>, a<sub>2</sub>, b<sub>2</sub> (0 ≤ a<sub>1</sub>, a<sub>2</sub> ≤ A − 1, 0 ≤ b<sub>1</sub>, b<sub>2</sub> ≤ B − 1, (a<sub>1</sub>, b<sub>1</sub>) ≠ (a<sub>2</sub>, b<sub>2</sub>)).</p>

### 출력 

 <p>Print one line with nine integers, the number of different of hands that belong in each category in increasing order of categories (from Straight flush to High card).</p>

