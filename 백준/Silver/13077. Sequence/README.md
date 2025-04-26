# [Silver I] Sequence - 13077 

[문제 링크](https://www.acmicpc.net/problem/13077) 

### 성능 요약

메모리: 109544 KB, 시간: 96 ms

### 분류

수학, 트리

### 제출 일자

2025년 4월 26일 20:16:26

### 문제 설명

<p>We inductively label the nodes of a rooted binary tree with an infinite number of nodes as follows:</p>

<ul>
	<li>The root is labeled by 1/1,</li>
	<li>If the label of a node is p/q, then
	<ul>
		<li>The label of its left child is p/(p+q), and</li>
		<li>The label of its right child is (p+q)/q. </li>
	</ul>
	</li>
</ul>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/13077/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-09-10%20%EC%98%A4%ED%9B%84%206.39.14.png" style="height:232px; width:315px"></p>

<p>By having this tree in our hand, we define a rational sequence a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, … by a breadth first traversal of the tree in such a way that nodes in the same level are visited from left to right. Therefore, we have a<sub>1 </sub>= 1/1, a<sub>2</sub> = 1/2, a<sub>3</sub> = 2/1, a<sub>4</sub> = 1/3, a<sub>5</sub> = 3/2, …</p>

<p>You are to write a program that gets values p and q and computes an integer n for which a<sub>n</sub> = p/q.</p>

### 입력 

 <p>The first line of the input includes the number of test cases, 1 ≤ t ≤ 1000. Each test case consists of one line. This line contains p, followed by / and then q without any space between them.</p>

### 출력 

 <p>For each test case, output in one line an integer n for which a<sub>n</sub> = p/q. It is guaranteed that in all test cases n fits in a 32-bit integer.</p>

