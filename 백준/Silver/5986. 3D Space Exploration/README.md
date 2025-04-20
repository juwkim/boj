# [Silver I] 3D Space Exploration - 5986 

[문제 링크](https://www.acmicpc.net/problem/5986) 

### 성능 요약

메모리: 195840 KB, 시간: 452 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 플러드 필, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 20일 19:55:58

### 문제 설명

<p>Farmer John's cows have finally blasted off from earth and are now floating around space in their Moocraft. The cows want to reach their fiery kin on Io, a moon of Jupiter, but to do so they first must navigate the dangerous asteroid belt.</p>

<p>Bessie is piloting the craft and must guide it through this treacherous N x N x N (1 <= N <= 100) sector of space. All asteroids in this sector comprise some number of 1 x 1 x 1 blocks of space-rock connected along their faces (two blocks sharing only a vertex or only an edge count as two distinct asteroids).</p>

<p>Please help Bessie by counting the number of distinct asteroids in the field.</p>

<p>Consider a 3 x 3 x 3 space where the first slice of space looks like this, with 'M' indicating the starting location of the Moocraft (1,1,1) and 'D' is the destination at (3,3,3). In these maps, these markers serve mostly as map orientation rather than providing useful information to solve the problem.</p>

<p>In these diagrams and also in the input file, the *'s represent asteroid chunks and each '.' represents a vast void of empty space.</p>

<pre>   Close slice    Middle slice     Far Slice     Assembled with overlaps
     +---+            +---+          +---+                  +---+ Far
     |M..|            |..*|          |...|                  |...|
     |.*.|            |.*.|          |.*.|                +---+.|
     |...|            |*..|          |..D|                |..*|D|
     +---+            +---+          +---+              +---+.|-+
                                                        |M..|.|
                                                        |.*.|-+
                                                        |...|
                                                  Close +---+</pre>

<p>Visual inspection shows three asteroids, including a long one through the middle of the map. Here's a map with the asteroid pieces labelled:</p>

<pre>                                 +---+ Far
                                 /|...|
                                / |.1.|
                               /  |...|
                              /   +---+
                             +---+   /
                            /|..3|  /  
                           / |.1.| /
                          /  |2..|/
                         /   +---+
                        +---+   /
                        |...|  /
                        |.1.| /
                        |...|/
                  Close +---+</pre>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N^2+1: Line i-1 contains line 1 + ((k+1)%N) of slice int ((i+N-1)/N ): N characters</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer indicating the number of asteroids in the field</li>
</ul>

<p> </p>

