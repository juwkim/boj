# [Bronze II] Router 2 - 13193 

[문제 링크](https://www.acmicpc.net/problem/13193) 

### 성능 요약

메모리: 32952 KB, 시간: 68 ms

### 분류

애드 혹(ad_hoc), 구성적(constructive), 구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Henry and Hetty were recently hired by a networking company from Piatra Neamț. Their first project is to create a new type of router, the revolutionary Connect Ethernet Operating Interface 2016, comprised of:</p>

<ul>
	<li>N input nodes, numbered from 1 to N;</li>
	<li>N output nodes, numbered from N+1 to 2×N;</li>
	<li>K internal nodes, numbered from 2×N+1 to 2×N+K;</li>
	<li>M unidirectional direct connections between pairs of distinct nodes.</li>
</ul>

<p>A node X can send data to a node Y (and hence Y can receive data from X) if:</p>

<ul>
	<li>X = Y, or</li>
	<li>there exists a node Z such that X can send data to Z and there is a direct connection from node Z to node Y.</li>
</ul>

<p>If a node X can send data to a node Y, and X ≠ Y, then we define a data path from X to Y as a set of direct connections {(A<sub>1</sub>, A<sub>2</sub>), (A<sub>2</sub>, A<sub>3</sub>), … (A<sub>L-1</sub>, A<sub>L</sub>)} for some L ≥ 2, such that A<sub>1</sub> = X and A<sub>L</sub> = Y.</p>

<p>A router works properly if:</p>

<ul>
	<li>Each input node can send data to each output node;</li>
	<li>Each input node can receive data only from itself;</li>
	<li>Each output node can send data only to itself;</li>
	<li>For any two nodes X and Y, if X ≠ Y and X can send data to Y, then Y cannot send data to X;</li>
	<li>For any two nodes X and Y, if X ≠ Y and X can send data to Y, then the data path from X to Y is unique. In particular, any two nodes X and Y should be connected by at most 1 direct connection.</li>
</ul>

<p>Like any other electronic device, a router needs electricity to work. Let's define the power needed to operate a node X as P<sub>X</sub> = IN<sub>X</sub> × OUT<sub>X</sub>, where IN<sub>X</sub> is the number of input nodes that can send data to X, and OUT<sub>X</sub> is the number of output nodes that can receive data from X. Let's define the maximum power used by the router as P<sub>max</sub> = max(P<sub>1</sub>, P<sub>2</sub>, … P<sub>2×N+K</sub>).</p>

<p>The project manager has given Henry and Hetty the technical specifications for building a few test routers, listed in the table below. For each of these specifications, the manager wants a router which:</p>

<ul>
	<li>has exactly N input nodes and N output nodes;</li>
	<li>uses at most M<sub>lim</sub> direct connections;</li>
	<li>uses a maximum power which is at most Plim;</li>
	<li>uses at most 500 000 nodes overall (Total nodes = N<sub>tot</sub> = 2×N + K ≤ 500 000).</li>
</ul>

### 입력 

 <p>On the first and only line, three integers: N, the number of input and output nodes; M<sub>lim</sub>, the maximum number of direct connections allowed; and P<sub>lim</sub>, the maximum power the router uses.</p>

<p>N = 223, M<sub>lim</sub> = 1 000 000, P<sub>lim</sub> =1 000 000</p>

### 출력 

 <p>You will output two integer numbers separated by a space: N<sub>tot</sub> = 2×N + K, representing the total number of nodes used to build the router; and M, representing the total number of direct connections used. On each of the following M lines you should output a pair of integers X and Y, meaning a direct connection from node X to node Y was built.</p>

