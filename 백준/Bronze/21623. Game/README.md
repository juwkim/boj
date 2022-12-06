# [Bronze II] Game - 21623 

[문제 링크](https://www.acmicpc.net/problem/21623) 

### 성능 요약

메모리: 40340 KB, 시간: 128 ms

### 분류

구현(implementation)

### 문제 설명

<p>Petya was bored during the lockdown, so he came up with a new single player game that uses random numbers generator.</p>

<p>The game consists of several rounds, each round consists of one or more moves. Throughout the game Petya keeps track of his current score.</p>

<p>At the beginning of every round Petya has the score equal to $n$. Every move the generator outputs a non-negative integer and Petya tries to subtract it from his current score. If the result is non-negative, he changes his score to the result of the subtracation, otherwise, the result is ignored and the score does not change. For example, if the current score is $3$, and the generator outputs $2$, Petya does the subtraction and the score changes to $1$. If the generator output is $5$, the result is ignored and the score remains $3$.</p>

<p>If the score after the current move is $0$, the round ends, and at the beginning of the next move Petya is back to the score of $n$.</p>

<p>Lockdown had ended long ago, but Petya has suddenly came across a sheet of paper that contains a sequence of $k$ integers ---generator output throughout the game. The boy wonders how many rounds had he played and what was his current score when he stopped the game. Help him find it out using the notes on the sheet.</p>

### 입력 

 <p>The first line of input contains two integers: $k$ --- the number of moves Petya made, $n$ --- the score at the beginning of every round ($1 \le k \le 100\,000$, $1 \le n \le 10^8$).</p>

<p> The second line contains $k$ integers --- output of random numbers generator ($0 \le a_i \le 10^8$).</p>

### 출력 

 <p>The first line must contain one integer --- the amount of played rounds.</p>

<p>The second line must contain one integer --- the score at the end of the game. </p>

<p>If the last move of the game had ended the round, Petya didn't not begin a new round and his score was $0$.</p>

