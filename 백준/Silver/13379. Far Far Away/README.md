# [Silver I] Far Far Away - 13379 

[문제 링크](https://www.acmicpc.net/problem/13379) 

### 성능 요약

메모리: 218512 KB, 시간: 1016 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색, 트리

### 제출 일자

2025년 4월 25일 20:58:55

### 문제 설명

<p>Thai University lecturers often have to work all the time even when they are sleeping. The only time that they can rest is when they are going to academic events, such as conferences, seminar, etc. Since the travel time to such an event is considered work time, a group of ICT instructors came up with an idea to use that travel time to simply sleep. Hence, whenever they get to choose which academic events to travel to, they always choose the one that is farthest away from the university. More recently, they’ve become a little picky: they’ll only go if the total travel time is no less than a threshold M.</p>

<p>You will be presented with multiple cities (vertices) and a number of flight options (directed edges). The cities are numbered. The instructors will start from vertex 1. This is where the university is located. Every city that appears in the input is a valid destination (i.e., it has an academic event). However, traveling to an academic event often requires connecting through a number of cities. But each city has exactly one direct connection into it. This means, the input is a directed tree where every vertex, except for vertex 1, has precisely one incoming edge.</p>

### 입력 

 <p>The first line contains a number, T, the number of test cases where 0 < T <= 20. For each of the following test cases, the first line contains two numbers, C, and M. Here, C (1 < C <= 100000) is the number of cities, and M (1 <= M <= 100,000,000) is the “pickiness” threshold (i.e., the minimum travel time for a trip to be worthwhile). For the next C-1 lines, each line contains three numbers, C1, C2, and D, representing a directed edge of distance D (0 < D <= 100) from C1 to C2. Here, C1 and C2 are cities, so 1 <= C1, C2 <= C.</p>

<p>All input numbers are integers. When there are multiple integers on the same line, they are each separated by a single white space.</p>

### 출력 

 <p>For each test case, a single number in a single line, the distance of the longest route. However, you will output -1 if there is no route with distance at least M from the university to anywhere (see the sample test case #2).</p>

<p> </p>

