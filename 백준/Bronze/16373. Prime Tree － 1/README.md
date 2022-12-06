# [Bronze I] Prime Tree - 1 - 16373 

[문제 링크](https://www.acmicpc.net/problem/16373) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

구성적(constructive)

### 문제 설명

<p>A tree is a connected undirected graph that has no cycles. Consider a tree with n vertices, labeled with integers 1, 2, ..., n. Let’s call an edge (u, v) bad if there is an integer d > 1 such that the label of u and the label of v are both divisible by d. For example, in the tree below there are three bad edges: (6, 4) are both divisible by 2, (2, 6) are both divisible by 2, and (3, 6) are both divisible by 3:</p>

<p style="text-align: center;"><img alt="" src="" style="width: 231px; height: 109px;"></p>

<p>Your goal is to relabel vertices in such a way that the number of bad edges is as small as possible. For example, if you relabel vertices of the tree shown above in the following way, there will be only one bad edge (3, 6):</p>

<p style="text-align: center;"><img alt="" src="" style="width: 227px; height: 105px;"></p>

<p>The less bad edges your tree will have the more points you will get.</p>

<p>This is an output-only problem. You need to run your program locally and only submit the answer file for each input file.</p>

### 입력 

 <p>Each input file contains several test cases.</p>

<p>The first line of the input file contains the number of test cases in this input file.</p>

<p>The first line of test case description contains a single integer n, the number of the vertices in the tree.</p>

<p>Each of the following n − 1 lines contains two integers u and v (1 ≤ u, v ≤ n), vertices connected by the edge.</p>

<p>All trees in a single file have the same number of vertices.</p>

### 출력 

 <p>For each test case print one line containing exactly n different integers from 1 to n — labels assigned to vertices 1, 2, . . . , n.</p>

