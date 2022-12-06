# [Bronze III] Another Cow Number Game - 6190 

[문제 링크](https://www.acmicpc.net/problem/6190) 

### 성능 요약

메모리: 121220 KB, 시간: 108 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>The cows are playing a silly number game again. Bessie is tired of losing and wants you to help her cheat. In this game, a cow supplies a number N (1 <= N <= 1,000,000). This is move 0. If N is odd, then the number N is multiplied by 3 and incremented by 1. If N is even, the number N is divided by 2. Each time the number is multiplied or divided, the score increases by one point. The game ends -- and the score is finalized -- when N becomes 1. If N is initially 1, the score is 0.</p>

<p>Here's an example with N starting at 5:</p>

<pre>        N     Next Value    Comment    Score
        5        16          3*5+1       1
       16         8           16/2       2
        8         4            8/2       3
        4         2            4/2       4
        2         1            2/2       5</pre>

<p>The final score is 5.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer, N</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the score for this game when starting at N</li>
</ul>

