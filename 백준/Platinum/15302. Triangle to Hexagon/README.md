# [Platinum IV] Triangle to Hexagon - 15302 

[문제 링크](https://www.acmicpc.net/problem/15302) 

### 성능 요약

메모리: 1132 KB, 시간: 0 ms

### 분류

기하학(geometry), 선분 교차 판정(line_intersection), 수학(math)

### 문제 설명

<p>Given a triangle ABC with incenter (center of its inscribed circle), I, and circumscribed circle O, let M, N and P be the second points of intersection of the lines through A and I, B and I resp. C and I with the circle O.</p>

<p style="text-align:center"><img alt="" src="" style="height:281px; width:278px"></p>

<p>Let E and F be the intersections of the line NP with AB and AC respectively. Similarly, let G and H be the intersections of the line MN with AC and BC respectively and let J and K be the intersections of the line MP with BC and AB respectively.</p>

<p>Write a program which takes as input the coordinates of the vertices A, B and C of the triangle and outputs the lengths of the segments EF, FG, GH, HJ, JK and KE. Supposedly,</p>

<p style="text-align:center">|EF| + |GH| + |JK| <= |KE| + |FG| + |HJ|.</p>

<p>Computations should be done in double precision floating point.</p>

### 입력 

 <p>The first line of input contains a single integer P, (1 ≤ P ≤ 10000), which is the number of data sets that follow. Each data set should be processed identically and independently.</p>

<p>Each data set consists of one line of input. The line contains the data set number, K, followed by three floating point values: the x coordinate of B, Bx, the x coordinate of C, Cx and the y coordinate of C, Cy. A will always be the origin (0,0) and B will always be on the x-axis so By = 0.</p>

### 출력 

 <p>For each data set there is a single line of output. The single output line consists of the data set number, K followed by the 6 decimal values to 4 decimal places separated by spaces. The values are the lengths of EF, FG, GH, HJ, JK and KE in that order.</p>

