# [Silver V] Lucky Chances - 11477 

[문제 링크](https://www.acmicpc.net/problem/11477) 

### 성능 요약

메모리: 116556 KB, 시간: 228 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Lucky Chances is a lottery game. Each lottery ticket has a play field and a scratch area. The play field is a rectangular r × c field filled with numbers. The scratch area hides row and column numbers that specify the bet cell.</p>

<p>There are four possible winning directions: up, down, left and right. You win a direction if all numbers in this direction from the bet cell are strictly less than a number in the bet cell. And if the bet cell is on the edge of the grid, you win the corresponding direction automatically!</p>

<p style="text-align: center;"><img alt="" src="" style="height:159px; width:123px"></p>

<p style="text-align: center;">Unscratched ticket</p>

<p style="text-align: center;"><img alt="" src="" style="height:165px; width:168px"></p>

<p style="text-align: center;">Scratched ticket 1</p>

<p style="text-align: center;"><img alt="" src="" style="height:169px; width:167px"></p>

<p style="text-align: center;">Scratched ticket 2</p>

<p>Larry wants to choose the ticket that has maximum total number of winning directions for all possible bet cells. Write a program that determines this number for the given grid.</p>

### 입력 

 <p>The first line of the input file contains two integers r and c — the number of rows and columns in the grid (1 ≤ r, c ≤ 100).</p>

<p>The following r lines contain c integers each — the numbers printed on the grid. Each number is positive and does not exceed 1000.</p>

### 출력 

 <p>Output a single integer w — the total number of winning directions for the given grid.</p>

