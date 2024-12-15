# [Silver II] Neighborhoods in Graphs - 10204 

[문제 링크](https://www.acmicpc.net/problem/10204) 

### 성능 요약

메모리: 112308 KB, 시간: 108 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 플로이드–워셜, 그래프 이론, 그래프 탐색, 파싱, 최단 경로, 문자열

### 제출 일자

2024년 12월 15일 23:33:27

### 문제 설명

<p>Gru and Lucy put together a graph of super-villains to see if they can see any interesting connections, in order to find who stole the Arctic Circle Laboratory. In this graph, there is a node (vertex) for every super-villain, and there is an edge (connection) between two nodes if they have ever concocted a sinister plot together. The figure below shows an example of such a graph over 10 villains (to simplify things for you, we will use made-up simple names for the super-villains, of the form v<sub>1</sub>, v<sub>2</sub>, ..., and so on).</p>

<p>Given such a graph and a super-villain, your goal is to count to the number of super-villains in that super-villain’s 2-hop neighborhood in the graph, i.e., all the nodes that are within a distance of 2 from the given node. (This is also called “friends of friends query” in a social graph setting.) For example, for v<sub>1</sub>, this includes: v<sub>3</sub>, v<sub>2</sub>, v<sub>5</sub>, and v<sub>4</sub> (so the answer would be 4), whereas for v<sub>5</sub>, the 2-hop neighborhood includes: v<sub>1</sub>, v<sub>2</sub>, v<sub>3</sub>, v<sub>4</sub>, v<sub>6</sub>, v<sub>7</sub>, v<sub>8</sub>, v<sub>9</sub>, i.e., all the nodes in the graph (so the answer would be 8). Note that, we don’t count v<sub>5</sub> to be in its own 2-hop neighborhood.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/637c1c2c-d979-4ce9-bb7e-291f54813010/-/preview/" style="width: 379px; height: 177px;"></p>

### 입력 

 <p>The first line in the test data file contains the number of test cases (< 100). After that each line contains a test case. The first two numbers in each test case represent the number of supervillains in the graph, n (n < 100), and the number of edges in the graph, e (e < 1000). After that, the next 2e Strings describe the edges. The last String on each line contains the id of a supervillain, vx.</p>

### 출력 

 <p>For each test case, you are to output the number of nodes in the 2-hop neighborhood of vx. The exact format is shown below in the examples.</p>

