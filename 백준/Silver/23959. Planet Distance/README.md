# [Silver I] Planet Distance - 23959 

[문제 링크](https://www.acmicpc.net/problem/23959) 

### 성능 요약

메모리: 115408 KB, 시간: 208 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 7월 5일 07:50:00

### 문제 설명

<p>There are <b>N</b> planets in the universe, and Google's Space division has installed <b>N</b> vacuum tubes through which you can travel from one planet to another. The tubes are bidirectional; travelers may use a tube between two planets to travel from either of those planets to the other. Each vacuum tube connects two planets and no two vacuum tubes connect the same pair of planets. These tubes connect the planets such that it is possible to travel from any planet to any other planet using one or more of them. Some of these tubes are connected such that there exists exactly one cycle in the universe. Google has hidden gifts in all the planets that are part of this cycle. Now, Google wants to know how far away each of the planets in the universe is from the gifts.</p>

<p>Your task is to find the minimum distance (in terms of the number of vacuum tubes) between each planet and a planet that is part of the cycle. Planets that are part of the cycle are assumed to be at distance 0.</p>

### 입력 

 <p>The first line contains an integer <b>T</b>, the number of test cases. <b>T</b> test cases follow. The first line of each test case contains an integer <b>N</b>, the number of planets and vacuum tubes. The planets are numbered from 1 to <b>N</b>.</p>

<p><b>N</b> lines follow, the i-th of these lines contains two integers <b>x<sub>i</sub></b> and <b>y<sub>i</sub></b>, indicating that the i-th vacuum tube connects planet <b>x<sub>i</sub></b> and planet <b>y<sub>i</sub></b>.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is a list of <b>N</b> space-separated values in which the i-th value represents the minimum distance between the i-th planet and a planet in the cycle.</p>

