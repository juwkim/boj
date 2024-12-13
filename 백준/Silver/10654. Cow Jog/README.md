# [Silver II] Cow Jog - 10654 

[문제 링크](https://www.acmicpc.net/problem/10654) 

### 성능 요약

메모리: 121472 KB, 시간: 148 ms

### 분류

자료 구조, 구현, 스택

### 제출 일자

2024년 12월 14일 00:04:40

### 문제 설명

<p>The cows are out exercising their hooves again!  There are N cows jogging on an infinitely-long single-lane track (1 <= N <= 100,000). Each cow starts at a distinct position on the track, and some cows jog at different speeds.</p>

<p>With only one lane in the track, cows cannot pass each other.  When a faster cow catches up to another cow, she has to slow down to avoid running into the other cow, becoming part of the same running group.</p>

<p>The cows will run for T minutes (1 <= T <= 1,000,000,000).  Please help Farmer John determine how many groups will be left at this time. Two cows should be considered part of the same group if they are at the same position at the end of T minutes.</p>

### 입력 

 <p>The first line of input contains the two integers N and T.</p>

<p>The following N lines each contain the initial position and speed of a single cow.  Position is a nonnegative integer and speed is a positive integer; both numbers are at most 1 billion.  All cows start at  distinct positions, and these will be given in increasing order in the input.</p>

### 출력 

 <p>A single integer indicating how many groups remain after T minutes.</p>

