# [Silver I] Coin Collection - 5352 

[문제 링크](https://www.acmicpc.net/problem/5352) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 5월 4일 03:35:45

### 문제 설명

<p>Coins are placed on the squares of an nxm board, with no more than one coin per square. A robot, located in the upper left square of the board, needs to collect as many coins as possible and bring them to the bottom right square. On each step the robot can move either one cell to the right or one cell down from its current location. When the robot visits a cell with a coin, it always picks up the coin. Design an algorithm to find the maximum number of coins the robot can collect.</p>

<p>For example, given the 5x7 board below the robot can collect at most 6 coins.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/ba0d92f4-f6e2-4865-a876-cb0ffdbc0a4d/-/preview/" style="width: 203px; height: 105px;"></p>

### 입력 

 <p>The first line of input will be a positive integer indicating the number of problem sets. Each problem set will start with a line that has two positive integers, n ≤ 50 and m ≤ 50, which represent the board size. The next n lines will contain m characters that are either an X or C. The X will represent a blank and the C a coin. Thus, the example 5x7 board above is represented by problem set</p>

<pre>5 7
CXXXXCC
XCCCXXX
XXXXXXC
CXCCXXX
XCXXXCX</pre>

### 출력 

 <p>For each problem set print, on a separate line, the maximum number of coins the robot can collect.</p>

