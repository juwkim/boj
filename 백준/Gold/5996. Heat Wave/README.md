# [Gold V] Heat Wave - 5996 

[문제 링크](https://www.acmicpc.net/problem/5996) 

### 성능 요약

메모리: 111904 KB, 시간: 120 ms

### 분류

그래프 이론, 최단 경로, 데이크스트라

### 제출 일자

2025년 8월 13일 23:40:31

### 문제 설명

<p>The good folks in Texas are having a heatwave this summer. Their Texas Longhorn cows make for good eating but are not so adept at creating creamy delicious dairy products. Farmer John is leading the charge to deliver plenty of ice cold nutritious milk to Texas so the Texans will not suffer the heat too much.</p>

<p>FJ has studied the routes that can be used to move milk from Wisconsin to Texas. These routes have a total of T (1 <= T <= 2,500) towns conveniently numbered 1..T along the way (including the starting and ending towns). Each town (except the source and destination towns) is connected to at least two other towns by bidirectional roads that have some cost of traversal (owing to gasoline consumption, tolls, etc.). Consider this map of seven towns; town 5 is the source of the milk and town 4 is its destination (bracketed integers represent costs to traverse the route):</p>

<pre>                              [1]----1---[3]-
                             /               \
                      [3]---6---[4]---3--[3]--4
                     /               /       /|
                    5         --[3]--  --[2]- |
                     \       /        /       |
                      [5]---7---[2]--2---[3]---
                            |       /
                           [1]------</pre>

<p>Traversing 5-6-3-4 requires spending 3 (5->6) + 4 (6->3) + 3 (3->4) = 10 total expenses.</p>

<p>Given a map of all the C (1 <= C <= 6,200) connections (described as two endpoints R1i and R2i (1 <= R1i <= T; 1 <= R2i <= T) and costs (1 <= Ci <= 1,000), find the smallest total expense to traverse from the starting town Ts (1 <= Ts <= T) to the destination town Te (1 <= Te <= T).</p>

### 입력 

 <ul>
	<li>Line 1: Four space-separated integers: T, C, Ts, and Te</li>
	<li>Lines 2..C+1: Line i+1 describes road i with three space-separated integers: R1i, R2i, and Ci</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the length of the shortest route from Ts to Te. It is guaranteed that at least one route exists.</li>
</ul>

<p> </p>

