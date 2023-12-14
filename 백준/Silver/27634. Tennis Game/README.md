# [Silver IV] Tennis Game - 27634 

[문제 링크](https://www.acmicpc.net/problem/27634) 

### 성능 요약

메모리: 108080 KB, 시간: 116 ms

### 분류

많은 조건 분기

### 제출 일자

2023년 12월 15일 05:12:32

### 문제 설명

<p>Tennis is a racket sport that is played by two opposing players on S sets. Each set consists of at least K games. A set is won by a player if that player wins at least K games and at least 2 games more than the opponent. Once a set is won, the set is ended and the match continues to a new set (if any) where both players start from 0 game won for that new set.</p>

<p>For example, let K = 6, then a set can be ended with any of the following.</p>

<ul>
	<li>P1 (Player 1) wins 6 games while P2 (Player 2) wins 3 games → P1 wins the set.</li>
	<li>P1 wins 7 games while P2 wins 9 games → P2 wins the set.</li>
</ul>

<p>On the other hand, a set cannot be ended with any of the following.</p>

<ul>
	<li>P1 wins 6 games while P2 wins 5 games → no player wins at least 2 games more than the opponent.</li>
	<li>P1 wins 0 game while P2 wins 5 games → no player wins K = 6 games.</li>
	<li>P1 wins 7 games while P2 wins 0 games → the set is already ended when P1 won the first 6 games.</li>
	<li>P1 wins 8 games while P2 wins 5 games → the set must already be ended before it reaches this state, e.g., the set can be ended at 7 − 5, 6 − 4, 6 − 3, etc.</li>
</ul>

<p>You are given K, S and N, determine whether there could be such a tennis match with S sets to ends exactly with N games. If there is such a tennis match, then output “YES” (without quotes) in a single line, otherwise, output “NO” (without quotes) in a single line.</p>

<p>For example, let K = 4, S = 2, and N = 14. It is possible to have such a tennis match. One the possibilities is as follows.</p>

<ul>
	<li>Set 1: P1 wins 6 games while P2 wins 4 games.</li>
	<li>Set 2: P1 wins 4 games while P2 wins 0 games.</li>
</ul>

<p>There are a total of N = 6 + 4 + 4 + 0 = 14 games on S = 2 sets where each set is won if a player won at least K = 4 games and at least 2 games more than the opponent.</p>

### 입력 

 <p>Input contains three integers K S N (2 ≤ K ≤ 10<sup>9</sup>; 1 ≤ S, N ≤ 10<sup>9</sup>) in a line representing the minimum number of games to win a set, the total number of sets, and the total number of games, respectively.</p>

### 출력 

 <p>Output in a line a string “YES” or “NO” (without quotes) whether it is possible to have such a tennis match.</p>

