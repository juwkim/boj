# [Gold IV] Diamond Inheritance (Large) - 12383 

[문제 링크](https://www.acmicpc.net/problem/12383) 

### 성능 요약

메모리: 160144 KB, 시간: 400 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 2월 16일 05:53:25

### 문제 설명

<p>You are asked to help diagnose class diagrams to identify instances of diamond inheritance. The following example class diagram illustrates the property of diamond inheritance. There are four classes: A, B, C and D. An arrow pointing from X to Y indicates that class X inherits from class Y.</p>

<p><img src="https://onlinejudgeimages.s3.amazonaws.com/problem/12382/images-49.png" style="vertical-align:middle"></p>

<p>In this class diagram, D inherits from both B and C, B inherits from A, and C also inherits from A. An inheritance path from X to Y is defined as a sequence of classes X, C<sub>1</sub>, C<sub>2</sub>, C<sub>3</sub>, ..., C<sub>n</sub>, Y where X inherits from C<sub>1</sub>, C<sub>i</sub> inherits from C<sub>i + 1</sub> for 1 ≤ i ≤ n - 1, and C<sub>n</sub> inherits from Y. There are two inheritance paths from D to A in the example above. The first path is D, B, A and the second path is D, C, A.</p>

<p>A class diagram is said to contain a diamond inheritance if there exists a pair of classes X and Y such that there are at least two different inheritance paths from X to Y. The above class diagram is a classic example of diamond inheritance. Your task is to determine whether or not a given class diagram contains a diamond inheritance.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> test cases follow, each specifies a class diagram. The first line of each test case gives the number of classes in this diagram, <strong>N</strong>. The classes are numbered from 1 to <strong>N</strong>.  <strong>N</strong> lines follow. The i<sup>th</sup> line starts with a non-negative integer <strong>M<sub>i</sub></strong> indicating the number of classes that class <em>i</em> inherits from. This is followed by <strong>M<sub>i</sub></strong> distinct positive integers each from 1 to <strong>N</strong> representing those classes. You may assume that:</p>

<ul>
	<li>If there is an inheritance path from X to Y then there is no inheritance path from Y to X.</li>
	<li>A class will never inherit from itself.</li>
</ul>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 50.</li>
	<li>0 ≤ <strong>M<sub>i</sub></strong> ≤ 10.</li>
	<li>1 ≤ <strong>N</strong> ≤ 1,000.</li>
</ul>

### 출력 

 <p>For each diagram, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is "Yes" if the class diagram contains a diamond inheritance, "No" otherwise.</p>

