# [Silver IV] Serious Cow Tag - 6203 

[문제 링크](https://www.acmicpc.net/problem/6203) 

### 성능 요약

메모리: 116192 KB, 시간: 316 ms

### 분류

기하학(geometry), 구현(implementation), 시뮬레이션(simulation), 정렬(sorting)

### 문제 설명

<p>Farmer John's N (1 <= N <= 1000) cows (conveniently numbered 1..N) are going to play a game of Serious Cow Tag. In Serious Cow Tag, each cow chooses a grid point in the pasture (-7500 <= X <= 7500, -7500 <= Y <= 7500) such that the distances between all pairs of cows are unique.</p>

<p>The cows play in turn, starting with cow #1 and continuing with cows #2, #3, and so on (as long as the cow is still in the game). When it is a cow's turn to play, she finds the nearest cow still playing, ambles over to that cow to tag her, and then returns to her original location. As soon as a cow is tagged, she is out of the game.</p>

<p>The game ends when only one cow remains, and she is declared the winner.</p>

<p>Farmer John is taking bets with neighboring farmers as to which cow will win, so he would like to know the winner in advance. Write a program that will read a description of the cows' positions and determine the winner.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer N, the number of cows</li>
	<li>Lines 2..N+1: Line i+1 contains two space-separated integers that describe the location of cow i.</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The number of the winning cow.</li>
</ul>

