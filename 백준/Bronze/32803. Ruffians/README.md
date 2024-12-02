# [Bronze II] Ruffians - 32803 

[문제 링크](https://www.acmicpc.net/problem/32803) 

### 성능 요약

메모리: 111908 KB, 시간: 136 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2024년 12월 3일 03:22:01

### 문제 설명

<p>Ashley and Brandon are playing the new hit card game, Ruffians!</p>

<p>In Ruffians, ten cards are dealt out in a grid of two rows and five columns. Each card has a number on it from 1 to 9. Ashley and Brandon are both looking for a pair of cards that have the same number.</p>

<p>After playing this game for a while, they realize that there is always a pair of cards that have the same number. To make the game harder, they require that they find a pair of cards with the same number, and that the two cards are in different rows and different columns.</p>

<p>Given an arrangement of cards, determine if such a pair exists or not.</p>

### 입력 

 <p>The first line of input contains a single integer $t$ ($1\leq t \leq 10^3$). This is the number of test cases.</p>

<p>Each test case is represented on two lines.</p>

<p>The first line of each test case contains five integers, each between $1$ and $9$. The second line of the test case also contains five integers, each between $1$ and $9$. These two lines combined form the grid of two rows and five columns of cards.</p>

### 출력 

 <p>Output $t$ lines, one for each test case.</p>

<p>For each test case, if there exists a pair of cards with the same number in different rows and different columns, output <code>YES</code>. Otherwise, output <code>NO</code>.</p>

