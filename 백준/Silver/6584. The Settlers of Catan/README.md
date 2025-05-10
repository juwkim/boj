# [Silver I] The Settlers of Catan - 6584 

[문제 링크](https://www.acmicpc.net/problem/6584) 

### 성능 요약

메모리: 111412 KB, 시간: 140 ms

### 분류

백트래킹, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 5월 11일 03:30:52

### 문제 설명

<p>Within <em>Settlers of Catan</em>, the 1995 German game of the year, players attempt to dominate an island by building roads, settlements and cities across its uncharted wilderness.</p>

<p>You are employed by a software company that just has decided to develop a computer version of this game, and you are chosen to implement one of the game's special rules:</p>

<blockquote>When the game ends, the player who built the longest road gains two extra victory points.</blockquote>

<p>The problem here is that the players usually build complex road networks and not just one linear path. Therefore, determining the longest road is not trivial (although human players usually see it immediately).</p>

<p>Compared to the original game, we will solve a simplified problem here: You are given a set of nodes (cities) and a set of edges (road segments) of length 1 connecting the nodes.</p>

<p>The longest road is defined as the longest path within the network that doesn't use an edge twice. Nodes may be visited more than once, though.</p>

<p>Example: The following network contains a road of length 12.</p>

<pre>o      o--o      o
 \    /    \    /
  o--o      o--o
 /    \    /    \
o      o--o      o--o
           \    /
            o--o
</pre>

### 입력 

 <p>The input file will contain one or more test cases.</p>

<p>The first line of each test case contains two integers: the number of nodes <em>n</em> (2 ≤ n ≤ 25) and the number of edges <em>m</em> (1 ≤ m ≤ 25). The next <em>m</em> lines describe the <em>m</em> edges. Each edge is given by the numbers of the two nodes connected by it. Nodes are numbered from <em>0</em> to <em>n-1</em>. Edges are undirected. Nodes have degrees of three or less. The network is not neccessarily connected.</p>

<p>Input will be terminated by two values of 0 for <em>n</em> and <em>m</em>.</p>

### 출력 

 <p>For each test case, print the length of the longest road on a single line.</p>

