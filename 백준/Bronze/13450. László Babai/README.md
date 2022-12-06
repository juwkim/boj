# [Bronze I] László Babai - 13450 

[문제 링크](https://www.acmicpc.net/problem/13450) 

### 성능 요약

메모리: 28776 KB, 시간: 100 ms

### 분류

애드 혹(ad_hoc), 브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>László Babai is a Hungarian computer scientist and mathematician. He is a Gödel prize winner and an outstanding researcher in the fields of the theory of computation, algorithms, combinatorics, and group theory. Last year, he proposed a subexponential-time algorithm solving Graph Isomorphism in exp((log n)<sup>O(1)</sup>)-time, and the best previous result is an exp(O(√(n log n)))-time algorithm.</p>

<p>Graph Isomorphism is a famous NP problem in theoretical computer science, however, you may wonder what it is. Let us explain for a bit. Given two undirected graphs A = (V<sub>A</sub>, E<sub>A</sub>) and B = (V<sub>B</sub>, E<sub>B</sub>), where A’s vertex set is V<sub>A</sub> = {a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, . . . , a<sub>nA</sub>}, and B’s vertex set is V<sub>B </sub>= {b<sub>1</sub>, b<sub>2</sub>, b<sub>3</sub>, . . . , b<sub>nB</sub>}. Graph A and B are isomorphic if and only if</p>

<ol>
	<li>A and B have the same amount of vertices and edges,</li>
	<li>There exists a bijective (one-to-one and onto) function f : V<sub>A</sub> → V<sub>B</sub> such that {u, v} ∈ E<sub>A</sub> if and only if {f(u), f(v)} ∈ E<sub>B</sub>.</li>
</ol>

<p>In other words, we can relabel the vertex set of graph A to obtain graph B.</p>

<p>Graph Isomorphism is still neither known to be in P nor NP-complete. As up and coming computer scientists, we must be ambitious and never be afraid to dream big! Therefore, let us take on the challenge of testing if two 3-vertex undirected simple graphs G<sub>1 </sub>and G<sub>2</sub> are isomorphic and show the world that we too can accomplish something.</p>

### 입력 

 <p>The first line of the input will be a single integer T (T ≤ 100) representing the number of test cases that will follow.</p>

<p>Every test case then starts with the number of edges m (0 ≤ m ≤ 3) in the first undirected simple graph of 3 vertices (numbered from 1 to 3), followed by m lines each containing two distinct integers u, v (u ≠ v, u, v ∈ {1, 2, 3}) indicating that there exists an edge between vertex u and v. You may assume that there is at most one edge between any pair of vertices. After that the description of the second graph follows in the same format.</p>

### 출력 

 <p>If the two graphs are isomorphic than output “yes” on one line. If not, output “no” instead.</p>

