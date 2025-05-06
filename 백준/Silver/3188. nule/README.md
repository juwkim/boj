# [Silver I] nule - 3188 

[문제 링크](https://www.acmicpc.net/problem/3188) 

### 성능 요약

메모리: 153624 KB, 시간: 564 ms

### 분류

수학, 다이나믹 프로그래밍, 정수론

### 제출 일자

2025년 5월 6일 19:15:14

### 문제 설명

<p>We are given a game board consisting of squares arranged in N rows and N columns, with each square containing a single non-negative integer</p>

<p>In the beginning of the game, a piece is situated on the top-left square (1,1) and it has to get to the bottom-right square (N,N) only moving one-square-down or one-square-to-the-right in each step. Furthermore, a piece can not be placed on a square containing number 0.</p>

<p>We define the cost of a path to be the product of all the numbers on that path.</p>

<p>We say that some path is optimal if number of zeros at the end of decimal representation of its cost is minimal.</p>

<p>Write a program that will calculate the number of zeros at the end of the decimal representation of cost of optimal path.</p>

### 입력 

 <p>First line of input contains the integer N, 1 ≤ N ≤ 1000.</p>

<p>Each of the following N lines contains N numbers. These numbers represent the board from the problem statement. All the numbers will be non-negative integers less than or equal to 1,000,000.</p>

<p>Note: there will always be solution for each test data.</p>

### 출력 

 <p>First and only line of output should contain the number of zeros from the problem statement. </p>

