# [Silver II] Treasure Cave - 6125 

[문제 링크](https://www.acmicpc.net/problem/6125) 

### 성능 요약

메모리: 109544 KB, 시간: 96 ms

### 분류

그래프 이론, 그래프 탐색, 트리

### 제출 일자

2024년 12월 15일 07:25:45

### 문제 설명

<p>Bessie's grandfather was a pirate who accumulated a great treasure chest of golden plunder. He hid the treasure chest in a cave that Bessie has recently discovered right on Farmer John's land! Just inside the cave's entrance she found a map that told her how to get the treasure.</p>

<p>The cave has P passages (3 <= P <= 5,000) conveniently numbered 1..P. The entrance is passage 1; the treasure is located in some reachable passage T (2 <= T <= P), whose value is supplied. Passages are all approximately the same length; each one leads to a split where hitherto unexplored numbered passages take the inquisitive cow deeper underground. No passage appears as the split from more than one passage, and the map contains a total of NS splits (1 <= NS <= 5,000).</p>

<p>Bessie wants to know both how far away from the entrance the treasure lies and also which passage numbers to take to get to the treasure.</p>

<p>Consider the schematic representation of a cave shown below. Passage numbers are shown close to the passage they name. For this example, the treasure is at the end of passage number 7:</p>

<pre>                   3/
                   /
                  +
                 / \   /5
               2/  4\ /
           1   /     +
          ----+      6\   #7    /11
               \       \ /     /
              13\       +     +
                        8\ 10/ \
                          \ /   \12
                           +
                           9\
                             \</pre>

<p>Bessie would have to traverse passages 1, 2, 4, 6, and 7 to get to the treasure, a total distance of 5 (which is simply the passage count).</p>

<p>The input file includes a set of lines, each with a passage number N (1 <= N <= P) and the two passages (B1 and B2; 1 <= B1 <= P; 1 <= B2 <= P) that branch off from it. Some line in the input file will include passage number 1 and its two branches (for our example, passages 2 and 13; likewise, passage number 8 has two branches: 9 and 10).</p>

<p>Tell Bessie how to get to the treasure.</p>

### 입력 

 <ul>
	<li>Line 1: Line 1 contains three space-separated integers: P, NS, and T</li>
	<li>Lines 2..NS+1: Each line contains three space-separated integers: N, B1, and B2</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The distance D from the entrance to the treasure</li>
	<li>Lines 2..D+1: Line i+1 contains a single integer that is next passage Bessie takes to get to the treasure.</li>
</ul>

<p> </p>

