# [Silver I] Cow Hopscotch - 10748 

[문제 링크](https://www.acmicpc.net/problem/10748) 

### 성능 요약

메모리: 111656 KB, 시간: 548 ms

### 분류

깊이 우선 탐색, 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 11일 00:49:26

### 문제 설명

<p>Just like humans enjoy playing the game of Hopscotch, Farmer John's cows have invented a variant of the game for themselves to play. Being played by clumsy animals weighing nearly a ton, Cow Hopscotch almost always ends in disaster, but this has surprisingly not deterred the cows from attempting to play nearly every afternoon.</p>

<p>The game is played on an R by C grid (2 <= R <= 100, 2 <= C <= 100), where each square is labeled with an integer in the range 1..K (1 <= K <= R*C). Cows start in the top-left square and move to the bottom-right square by a sequence of jumps, where a jump is valid if and only if</p>

<p>1) You are jumping to a square labeled with a different integer than your current square,</p>

<p>2) The square that you are jumping to is at least one row below the current square that you are on, and</p>

<p>3) The square that you are jumping to is at least one column to the right of the current square that you are on.</p>

<p>Please help the cows compute the number of different possible sequences of valid jumps that will take them from the top-left square to the bottom-right square.</p>

### 입력 

 <p>The first line contains the integers R, C, and K. The next R lines will each contain C integers, each in the range 1..K.</p>

### 출력 

 <p>Output the number of different ways one can jump from the top-left square to the bottom-right square, mod 1000000007.</p>

