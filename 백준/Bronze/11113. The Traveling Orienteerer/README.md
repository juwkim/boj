# [Bronze II] The Traveling Orienteerer - 11113 

[문제 링크](https://www.acmicpc.net/problem/11113) 

### 성능 요약

메모리: 30840 KB, 시간: 120 ms

### 분류

기하학(geometry), 구현(implementation), 수학(math), 피타고라스 정리(pythagoras)

### 문제 설명

<p>Lasse is organizing the orienteering world championship in Trondheim in 2008. Since he has been running in Bymarka for decades, he has a lot of route proposals. He must find a route with just the right length, but he doesn’t have time to measure them all by running through the control points in order, as he is too busy parallelizing code. The job is therefore given to Ola, who he thinks spends too much time with schoolwork.</p>

<p>As Ola is slightly less interested in orienteering, he figures out a more time-saving way of measuring the length of all the routes. He brings his GPS, visits all the points of all the routes in the most convenient order, and goes home early to do the rest of the job on his computer.</p>

### 입력 

 <p>The first line of input gives 1 ≤ n ≤ 1000, the total number of control points. Then follow n lines giving their coordinates, with two floating-point numbers x<sub>i</sub> and y<sub>i</sub>, with 0.0 ≤ x<sub>i</sub>, y<sub>i</sub> ≤ 10000.0. The number of routes is then given by 1 ≤ m ≤ 100. Each route is defined by first a line with 2 ≤ p ≤ 17, the number of control points (including start and goal), and then a line with p indexes 0 ≤ i < n, identifying them.</p>

### 출력 

 <p>For each test case output the total track distance, rounded, with no decimals.</p>

