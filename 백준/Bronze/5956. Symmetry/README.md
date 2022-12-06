# [Bronze II] Symmetry - 5956 

[문제 링크](https://www.acmicpc.net/problem/5956) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

수학(math), 재귀(recursion)

### 문제 설명

<p>Farmer John loves symmetry and is currently arranging his cows on his field partitioned into an N x M (1 <= N <= 1,000,000,000; 1 <= M <= 1,000,000,000) grid.</p>

<p>To preserve symmetry, Farmer John places cows in the following way. He puts a cow in the very center grid-square of the field; if no such grid-square exists, he simply stops. Then he partitions the field into four equal-sized smaller fields (separated by the row and column of the cow in the center) and arranges cows on each of those fields as before. He repeats the partitioning for ever-smaller fields until no center grid-square of a field exists or the field can not be subdivided.</p>

<p>By way of example, if N = 7 and M = 15 then Farmer John will place a cow in row 4, column 8 and arrange each of the resulting 3x7 fields. In each of the 3x7 fields, Farmer John will place a cow in row 2, column 4 and arrange each of the resulting 1x3 fields. The process is shown here (where C denotes a cow):</p>

<pre>...............    ...............    .......|.......    .C.|.C.|.C.|.C.
...............    ...............    ...C...|...C...    ---C---|---C---
...............    ...............    .......|.......    .C.|.C.|.C.|.C.
............... -> .......C....... -> -------C------- -> -------C-------
...............    ...............    .......|.......    .C.|.C.|.C.|.C.
...............    ...............    ...C...|...C...    ---C---|---C---
...............    ...............    .......|.......    .C.|.C.|.C.|.C.</pre>

<p>21 cows are required for this field. On the other hand, if N = M = 5 then Farmer John will only need to place one cow since the resulting 2x2 fields do not have center grid-squares. Help Farmer John determine how many cows he needs to arrange his field.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and M</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The number of cows needed</li>
</ul>

<p> </p>

