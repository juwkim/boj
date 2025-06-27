# [Silver I] Gridland - 6389 

[문제 링크](https://www.acmicpc.net/problem/6389) 

### 성능 요약

메모리: 110816 KB, 시간: 116 ms

### 분류

애드 혹, 수학

### 제출 일자

2025년 6월 27일 17:22:17

### 문제 설명

<p>For years, computer scientists have been trying to find efficient solutions to different computing problems. For some of them efficient algorithms are already available, these are the “easy” problems like sorting, evaluating a polynomial or finding the shortest path in a graph. For the “hard” ones only exponential-time algorithms are known. The traveling-salesman problem belongs to this latter group. Given a set of N towns and roads between these towns, the problem is to compute the shortest path allowing a salesman to visit each of the towns once and only once and return to the starting point.</p>

<p>The president of Gridland has hired you to design a program that calculates the length of the shortest traveling-salesman tour for the towns in the country. In Gridland, there is one town at each of the points of a rectangular grid. Roads run from every town in the directions North, Northwest, West, Southwest, South, Southeast, East, and Northeast, provided that there is a neighbouring town in that direction. The distance between neighbouring towns in directions North–South or East–West is 1 unit. The length of the roads is measured by the Euclidean distance. For example, Figure 7 shows 2 × 3-Gridland, i.e., a rectangular grid of dimensions 2 by 3. In 2 × 3-Gridland, the shortest tour has length 6.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/c717a8ee-2775-44c2-b041-5aefc78f64fa/-/preview/" style="width: 215px; height: 130px;"></p>

<p style="text-align: center;">Figure 7: A traveling-salesman tour in 2 × 3-Gridland.</p>

<p> </p>

### 입력 

 <p>The first line contains the number of scenarios.</p>

<p>For each scenario, the grid dimensions m and n will be given as two integer numbers in a single line, separated by a single blank, satisfying 1 < m < 50 and 1 < n < 50.</p>

### 출력 

 <p>The output for each scenario begins with a line containing “<code>Scenario #i:</code>”, where <code>i</code> is the number of the scenario starting at 1. In the next line, print the length of the shortest traveling-salesman tour rounded to two decimal digits. The output for every scenario ends with a blank line.</p>

