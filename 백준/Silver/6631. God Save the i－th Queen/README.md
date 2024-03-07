# [Silver IV] God Save the i-th Queen - 6631 

[문제 링크](https://www.acmicpc.net/problem/6631) 

### 성능 요약

메모리: 110724 KB, 시간: 2112 ms

### 분류

구현

### 제출 일자

2024년 3월 7일 22:19:07

### 문제 설명

<p>Did you know that during the ACM-ICPC World Finals a big chessboard is installed every year and is available for the participants to play against each other? In this problem, we will test your basic chess-playing abilities to verify that you would not make a fool of yourself if you advance to the World Finals.</p>

<p>During the yesterday’s Practice Session, you tried to solve the problem of N independent rooks. This time, let’s concentrate on queens. As you probably know, the queens may move not only horizontally and vertically, but also diagonally.</p>

<p>You are given a chessboard with i − 1 queens already placed and your task is to find all squares that may be used to place the i-th queen such that it cannot be captured by any of the others.</p>

### 입력 

 <p>The input consists of several tasks. Each task begins with a line containing three integer numbers separated by a space: X, Y , N. X and Y give the chessboard size, 1 ≤ X, Y ≤ 20 000. N = i−1 is the number of queens already placed, 0 ≤ N ≤ X · Y .</p>

<p>After the first line, there are N lines, each containing two numbers x<sub>k</sub>, y<sub>k</sub> separated by a space. They give the position of the k-th queen, 1 ≤ x<sub>k</sub> ≤ X, 1 ≤ y<sub>k</sub> ≤ Y . You may assume that those positions are distinct, i.e., no two queens share the same square. </p>

<p>The last task is followed by a line containing three zeros.</p>

### 출력 

 <p>For each task, output one line containing a single integer number: the number of squares which are not occupied and do not lie on the same row, column, or diagonal as any of the existing queens.</p>

