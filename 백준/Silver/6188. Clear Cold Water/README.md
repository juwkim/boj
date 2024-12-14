# [Silver II] Clear Cold Water - 6188 

[문제 링크](https://www.acmicpc.net/problem/6188) 

### 성능 요약

메모리: 117916 KB, 시간: 152 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색, 트리

### 제출 일자

2024년 12월 15일 01:20:32

### 문제 설명

<p>The steamy, sweltering summers of Wisconsin's dairy district stimulate the cows to slake their thirst. Farmer John pipes clear cold water into a set of N (3 <= N <= 99999; N odd) branching pipes conveniently numbered 1..N from a pump located at the barn. As the water flows through the pipes, the summer heat warms it.  Bessie wants to find the coldest water so she can enjoy the weather more than any other cow.</p>

<p>She has mapped the entire set of branching pipes and noted that they form a tree with its root at the farm and furthermore that every branch point has exactly two pipes exiting from it. Surprisingly, every pipe is exactly one unit in length; of course, all N pipes connect up in one way or another to the pipe-tree.</p>

<p>Given the map of all the pipe connections, make a list of the distance from the barn for every branching point and endpoint. Bessie will use the list to find the very coldest water.</p>

<p>The endpoint of a pipe, which might enter a branching point or might be a spigot, is named by the pipe's number. The map contains C (1 <= C <= N) connections, each of which specifies three integers: the endpoint E_i (1 <= E_i <= N) of a pipe and two branching pipes B1_i and B2_i (2 <= B1_i <= N; 2 <= B2_i <= N). Pipe number 1 connects to the barn; the distance from its endpoint to the barn is 1.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and C</li>
	<li>Lines 2..C+1: Line i+1 describes branching point i with three space-separated integers: E_i, B1_i, and B2_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..N: Line i of the output contains a single integer that is the distance from the barn to the endpoint of pipe i</li>
</ul>

