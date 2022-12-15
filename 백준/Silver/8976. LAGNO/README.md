# [Silver IV] LAGNO - 8976 

[문제 링크](https://www.acmicpc.net/problem/8976) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Lagno (also known as Reversi and Othello) is a board game for two players, one black and one white. The board is square, consisting of 8 rows and 8 columns. </p>

<p>In one move, the black player places a black piece into an empty square so that, in at least one of eight directions (up, down, left, right and the four diagonal directions), there is a row of white pieces between the newly placed piece and some other black piece. After placing, all white pieces between (in any direction) the newly placed black piece and pre-existing black pieces become black. </p>

<p>Write a program that, for a given board layout, calculates the largest number of white pieces the black player can convert in one move. </p>

### 입력 

 <p>The input contains eight lines, each consisting of exactly eight characters '.', 'B' or 'W'. The character '.' represents an empty square, the letter 'B' a square with a black piece, and the letter 'W' a square with a white piece. </p>

### 출력 

 <p>Output the largest number of white pieces that black can convert in a single move. If there are no legal moves, output 0. </p>

