# [Silver I] Draughts - 9540 

[문제 링크](https://www.acmicpc.net/problem/9540) 

### 성능 요약

메모리: 113676 KB, 시간: 264 ms

### 분류

백트래킹, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 28일 19:18:04

### 문제 설명

<p>Draughts (or checkers) is a game played by two opponents, on opposite sides of a 10 × 10 board. The board squares are painted black and white, as on a classic chessboard. One player controls the dark, and the other the light pieces. The pieces can only occupy the black squares. The players make their moves alternately, each moving one of his own pieces.</p>

<p>The most interesting type of move is capturing: if a diagonally adjacent square contains an opponent’s piece, it may be captured (and removed from the game) by jumping over it to the unoccupied square immediately beyond it. It is allowed to make several consecutive captures in one move, if they are all made with a single piece. It is also legal to capture by either forward or backward jumps.</p>

<p style="text-align:center"><img alt="" src="https://www.acmicpc.net/upload/images2/dr.png" style="height:161px; width:321px"></p>

<p style="text-align:center">The board before and after a single move with two captures.</p>

<p>You are given a draughts position. It is the light player’s turn. Compute the maximal possible number of dark pieces he can capture in his next move.</p>

### 입력 

 <p>The first line of input contains the number of test cases T. The descriptions of the test cases follow:</p>

<p>Each test case starts with an empty line. The following 10 lines of 10 characters each describe the board squares. The characters # and . denote empty black and white squares, W denotes a square with a light piece, B – a square with a dark piece.</p>

### 출력 

 <p>For each test case print a single line containing the maximal possible number of captures. If there is no legal move (for example, there are no light pieces on the board), simply output 0.</p>

