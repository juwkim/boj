# [Silver IV] Rock, Scissors, Paper - 4340 

[문제 링크](https://www.acmicpc.net/problem/4340) 

### 성능 요약

메모리: 132224 KB, 시간: 748 ms

### 분류

구현, 시뮬레이션

### 문제 설명

<p>Bart's sister Lisa has created a new civilization on a two-dimensional grid. At the outset each grid location may be occupied by one of three life forms: Rocks, Scissors, or Papers. Each day, differing life forms occupying horizontally or vertically adjacent grid locations wage war. In each war, Rocks always defeat Scissors, Scissors always defeat Papers, and Papers always defeat Rocks. At the end of the day, the victor expands its territory to include the loser's grid position. The loser vacates the position.</p>

<p>Your job is to determine the territory occupied by each life form after n days.</p>

### 입력 

 <p>The first line of input contains t, the number of test cases. Each test case begins with three integers not greater than 100: r and c, the number of rows and columns in the grid, and n. The grid is represented by the r lines that follow, each with c characters. Each character in the grid is R, S, or P, indicating that it is occupied by Rocks, Scissors, or Papers respectively.</p>

### 출력 

 <p>For each test case, print the grid as it appears at the end of the nth day. Leave an empty line between the output for successive test cases.</p>

