# [Silver I] Laserbox - 3709 

[문제 링크](https://www.acmicpc.net/problem/3709) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

그래프 이론, 그래프 탐색, 구현, 시뮬레이션

### 제출 일자

2025년 4월 6일 00:55:43

### 문제 설명

<p>A laserbox is a game involving some optical equipment. The game board is a square n × n grid. On each grid point, a gadget called a right-turner can be placed and several such gadgets are included. Finally, there is a ruby laser, and if the laser is mounted at the bottom end of a column, the beam will be directed northwards through that column. Analogously, the laser beam may be directed southwards from the top of a column, eastwards from the start of a row or westwards from the end of the row.</p>

<p>The game starts with some right-turners being spread out on some grid points and the laser (switched off) being mounted somewhere along the border of the rectangle. The player then tries to deduce where the beam will emerge when the laser is switched on. The effect of a right-turner is to deflect the beam ninety degrees to the right, regardless of from which of the four directions it enters.</p>

<p>Your program must do exactly what the player is supposed to do.</p>

### 입력 

 <p>On the first line of the input is a single positive integer, telling the number of test cases to follow. The first line of each test case consists of two integers n r, where 1 ≤ n ≤ 50 is the size of the board and 1 ≤ r ≤ 50 the number of right-turners. The following r lines contain the coordinates x y of the right-turners. No two right-turners will have the same coordinates.</p>

<p>Finally, a line with two integers indicating the laser position follows. The bottom of column six is denoted by 6 0 and the start of row seven by 0 7. If the zeroes are replaced by n + 1, the laser is placed at the top of column six and the end of row seven, respectively</p>

### 출력 

 <p>For each test case, output one line containing the coordinates X Y of the beam as it leaves the board. The same rules as for the laser apply, so X may equal 0 or n + 1 or else Y equal 0 or n + 1. If the beam gets caught and does not leave the board, the output should be 0 0.</p>

