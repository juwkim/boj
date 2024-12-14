# [Silver II] Cow Hopscotch - 10752 

[문제 링크](https://www.acmicpc.net/problem/10752) 

### 성능 요약

메모리: 110760 KB, 시간: 100 ms

### 분류

브루트포스 알고리즘, 다이나믹 프로그래밍

### 제출 일자

2024년 12월 15일 01:11:58

### 문제 설명

<p>Just like humans enjoy playing the game of Hopscotch, Farmer John's cows have invented a variant of the game for themselves to play. Being played by clumsy animals weighing nearly a ton, Cow Hopscotch almost always ends in disaster, but this has surprisingly not deterred the cows from attempting to play nearly every afternoon.</p>

<p>The game is played on an R by C grid (2 <= R <= 15, 2 <= C <= 15), where each square is colored either red or blue. Cows start in the top-left square and move to the bottom-right square by a sequence of jumps, where a jump is valid if and only if</p>

<p>1) You are jumping to a square of a different color,</p>

<p>2) The square that you are jumping to is at least one row below the current square that you are on, and</p>

<p>3) The square that you are jumping to is at least one column to the right of the current square that you are on.</p>

<p>Please help the cows compute the number of different possible sequences of valid jumps that will take them from the top-left square to the bottom-right square.</p>

### 입력 

 <p>The first line contains the two integers R and C. The next R lines will each contain C characters. Each character is either 'R' or a 'B', indicating a red square or a blue square.</p>

### 출력 

 <p>Output the number of different ways one can jump from the top-left square to the bottom-right square.</p>

