# [Bronze I] Brownie Points I - 4291 

[문제 링크](https://www.acmicpc.net/problem/4291) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Stan and Ollie play the game of Odd Brownie Points. Some brownie points are located in the plane, at integer coordinates. Stan plays first and places a vertical line in the plane. The line must go through a brownie point and may cross many (with the same x-coordinate). Then Ollie places a horizontal line that must cross a brownie point already crossed by the vertical line.</p>

<p>Those lines divide the plane into four quadrants. The quadrant containing points with arbitrarily large positive coordinates is the top-right quadrant.</p>

<p>The players score according to the number of brownie points in the quadrants. If a brownie point is crossed by a line, it doesn't count. Stan gets a point for each (uncrossed) brownie point in the top-right and bottom-left quadrants. Ollie gets a point for each (uncrossed) brownie point in the top-left and bottom-right quadrants.</p>

<p>Your task is to compute the scores of Stan and Ollie given the point through which they draw their lines.</p>

### 입력 

 <p>Input contains a number of test cases. The data of each test case appear on a sequence of input lines. The first line of each test case contains a positive odd integer 1 < n < 200000 which is the number of brownie points. Each of the following n lines contains two integers, the horizontal (x) and vertical (y) coordinates of a brownie point. No two brownie points occupy the same place. The input ends with a line containing 0 (instead of the n of a test).</p>

### 출력 

 <p>For each test case of input, print a line with two numbers separated by a single space. The first number is Stan's score, the second is the score of Ollie when their lines cross the point whose coordinates are given at the center of the input sequence of points for this case.</p>

