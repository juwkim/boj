# [Silver III] Daisy Chains in the Field - 5938 

[문제 링크](https://www.acmicpc.net/problem/5938) 

### 성능 요약

메모리: 115544 KB, 시간: 144 ms

### 분류

너비 우선 탐색(bfs), 깊이 우선 탐색(dfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

### 문제 설명

<p>Farmer John let his N (1 <= N <= 250) cows conveniently numbered 1..N play in the field. The cows decided to connect with each other using cow-ropes, creating M (1 <= M <= N*(N-1)/2) pairwise connections. Of course, no two cows had more than one rope directly connecting them. The input shows pairs of cows c1 and c2 that are connected (1 <= c1 <= N; 1 <= c2 <= N; c1 != c2).</p>

<p>FJ instructed the cows to be part of a chain which contained cow #1. Help FJ find any misbehaving cows by determining, in ascending order, the numbers of the cows not connected by one or more ropes to cow 1 (cow 1 is always connected to herself, of course). If there are no misbehaving cows, output 0.</p>

<p>To show how this works, consider six cows with four connections:</p>

<pre>    1---2  4---5
     \  |
      \ |      6
       \|
        3</pre>

<p>Visually, we can see that cows 4, 5, and 6 are not connected to cow 1.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and M</li>
	<li>Lines 2..M+1: Line i+1 shows two cows connected by rope i with two space-separated integers: c1 and c2</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..???: Each line contains a single integer</li>
</ul>

<p> </p>

