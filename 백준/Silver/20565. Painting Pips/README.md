# [Silver V] Painting Pips - 20565 

[문제 링크](https://www.acmicpc.net/problem/20565) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

그리디 알고리즘(greedy), 수학(math), 확률론(probability)

### 문제 설명

<p>Alice and Bob like playing games. Lately, they've been playing a game where Alice rolls $N$ dice and Bob pays her a dollar amount equal to the product of the numbers rolled on the $N$ dice; however, due to the lack of required skill, Alice and Bob have gotten bored.</p>

<p>To spice things up, they decide to use a custom set of dice. Specifically, Alice has $N$ blank $6$-sided dice and she gets to paint pips on them. She has enough paint to paint $M$ pips. Subject to this constraint, she can paint the dice however she wants; for example, she may paint more than $6$ pips on one side of a die. Note that she can choose to paint $0$ pips on a side; if any of the rolled numbers is $0$, the product is $0$.</p>

<p>Assuming Alice paints the dice optimally, what is the expected value of her winnings in this game?</p>

### 입력 

 <p>The only line of input contains two space-separated integers, $N$ ($1 \leq N \leq 20$) and $M$ ($1 \leq M \leq 100$): the number of dice in the game and the maximum number of pips Alice may paint in total, respectively.</p>

### 출력 

 <p>Output a single real number, Alice's expected winnings. Your answer is considered correct if its absolute or relative error is at most $10^{-6}$.</p>

