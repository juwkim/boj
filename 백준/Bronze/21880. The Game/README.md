# [Bronze II] The Game - 21880 

[문제 링크](https://www.acmicpc.net/problem/21880) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구성적(constructive), 구현(implementation)

### 문제 설명

<p>Intellectual TV-game "What? Where? When?" is very popular. Throughout the game, a team of experts attempts to answer questions sent in by viewers. If experts answer the question correctly, one point is awarded to the team of experts, otherwise a point is awarded to the team of viewers. The game ends when one of the teams scores $k$ points.</p>

<p>You are given a final score of $x:y$. So the game consisted of $x + y$ questions asked, and one of the teams scored exactly $k$ points. You are not given $k$, since you can calculate it easily. You are asked to find any valid game scenario that finished with score $x:y$, as the list of scores after each question asked.</p>

<p>The score you are given is correct, and at least one question was asked.</p>

### 입력 

 <p>The first line consists of two integers $x$ and $y$, the final score ($0 \le x, y \le 1000$; $x \ne y$).</p>

### 출력 

 <p>Print $x + y$ lines, $i$-th of them containing a score after $i$-th round. The numbers of points scored have to be separated by colon character ('<code>:</code>'). You can print any game scenario that finishes with score $x:y$.</p>

