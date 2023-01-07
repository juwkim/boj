# [Silver IV] Move & Meet - 18066 

[문제 링크](https://www.acmicpc.net/problem/18066) 

### 성능 요약

메모리: 2020 KB, 시간: 0 ms

### 분류

많은 조건 분기(case_work)

### 문제 설명

<p>Ernesto and Penelope are playing a board game on an infinite grid. Instead of rolling dice, both of them have generated a random number, and now they have to move their pieces that number of times. A single move consists of placing the piece in an adjacent cell; moving diagonally or waiting in place are not legal moves. However, it is permitted to move the piece in the direction it just came from in the previous move.</p>

<p>Ernesto and Penelope are trying to move in such a way that their pieces will end up in the same cell. Is there a cell for which this is possible?</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/31090c92-36ab-45a9-88c8-c9d2222d1b23/-/preview/" style="width: 273px; height: 277px;"></p>

<p style="text-align: center;">Figure M.1: Visualisation of the first sample, including possible paths for the given output.</p>

### 입력 

 <p>The input consists of two lines, both containing three integers x, y (−10<sup>12</sup> ≤ x, y ≤ 10<sup>12</sup>) and d (0 ≤ d ≤ 10<sup>12</sup>), giving for either player the pieces’ initial coordinates and the randomly generated number.</p>

### 출력 

 <p>If there is a cell that both players can end up on, output its coordinates. If there are multiple valid solutions, any will be accepted. If there is no valid cell, output impossible.</p>

