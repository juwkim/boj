# [Silver IV] Road Net - 8073 

[문제 링크](https://www.acmicpc.net/problem/8073) 

### 성능 요약

메모리: 118192 KB, 시간: 260 ms

### 분류

브루트포스 알고리즘(bruteforcing), 그래프 이론(graphs)

### 문제 설명

<p>A diskette was enclosed to a road map. The diskette contains the table of the shortest ways (distances) between each pair of towns on the map. All the roads are two-way. The location of towns on the map has the following interesting property: if the length of the shortest way from town A to town B equals the sum of the lengths of the shortest ways from A to C and C to B then town C lies on (certain) shortest way from A to B. We say that towns A and B are neighbouring towns if there is no town C such that the length of the shortest way from A to B equals the sum of the lengths of the shortest ways from A to C and C to B.</p>

<p>Find all the pairs of neighbouring towns.</p>

<p>For the table of distances:</p>

<pre>  A B C
A 0 1 2
B 1 0 3
C 2 3 0
</pre>

<p>the neighbouring towns are A, B and A, C.</p>

<p>Write a program that:</p>

<ul>
	<li>reads the table of distances from the standard input;</li>
	<li>finds all the pairs of neighbouring towns;</li>
	<li>writes the result to the standard output.</li>
</ul>

### 입력 

 <p>In the first line of the standard input there is an integer n, 1 ≤ n ≤ 200, which equals the number of towns on the map. Towns are numbered from 1 to n.</p>

<p>The table of distances is written in the following n lines. In the (i+1)-st line, 1 ≤ i ≤ n, there are n non-negative integers not greater than 200, separated by single spaces. The j-th integer is the distance between towns i and j.</p>

### 출력 

 <p>Your program should write all the pairs of the neighbouring towns (i.e. their numbers) to the standard output. There should be one pair in each line. Each pair can appear only once. The numbers in each pair should be given in increasing order. Pairs should be ordered so that if the pair (a, b) precedes the pair (c, d) then a < c or (a = c and b < d).</p>

