# [Silver II] Rational Number Tree (Small) - 12278 

[문제 링크](https://www.acmicpc.net/problem/12278) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

수학, 트리

### 제출 일자

2024년 12월 16일 14:16:24

### 문제 설명

<p>Consider an infinite complete binary tree where the root node is 1/1 and left and right childs of node p/q are p/(p+q) and (p+q)/q, respectively. This tree looks like:</p>

<pre>         1/1
    ______|______
    |           |
   1/2         2/1
 ___|___     ___|___
 |     |     |     |
1/3   3/2   2/3   3/1
...
</pre>

<p>It is known that every positive rational number appears exactly once in this tree. A level-order traversal of the tree results in the following array:</p>

<pre>1/1, 1/2, 2/1, 1/3, 3/2, 2/3, 3/1, ...
</pre>

<p>Please solve the following two questions:</p>

<ol>
	<li>Find the <b>n</b>-th element of the array, where <b>n</b> starts from 1. For example, for the input 2, the correct output is 1/2.</li>
	<li>Given <b>p/q</b>, find its position in the array. As an example, the input 1/2 results in the output 2.</li>
</ol>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow. Each test case consists of one line. The line contains a problem id (1 or 2) and one or two additional integers:</p>

<ol>
	<li>If the problem id is 1, then only one integer <b>n</b> is given, and you are expected to find the <b>n</b>-th element of the array.</li>
	<li>If the problem id is 2, then two integers <b>p</b> and <b>q</b> are given, and you are expected to find the position of <b>p/q</b> in the array.</li>
</ol>

### 출력 

 <p>For each test case:</p>

<ol>
	<li>If the problem id is 1, then output one line containing "<code>Case #x: p q</code>", where <code>x</code> is the case number (starting from 1), and <code>p</code>, <code>q</code> are numerator and denominator of the asked array element, respectively.</li>
	<li>If the problem id is 2, then output one line containing "<code>Case #x: n</code>", where <code>x</code> is the case number (starting from 1), and <code>n</code> is the position of the given number.</li>
</ol>

