# [Gold I] Crazy Rows (Large) - 12630 

[문제 링크](https://www.acmicpc.net/problem/12630) 

### 성능 요약

메모리: 30616 KB, 시간: 88 ms

### 분류

자료 구조(data_structures), 그리디 알고리즘(greedy), 연결 리스트(linked_list)

### 문제 설명

<p>You are given an <strong>N</strong> x <strong>N</strong> matrix with 0 and 1 values. You can swap any two <em>adjacent</em> rows of the matrix.</p>

<p>Your goal is to have all the 1 values in the matrix below or on the main diagonal. That is, for each X where 1 ≤ X ≤ N, there must be no 1 values in row X that are to the right of column X.</p>

<p>Return the minimum number of row swaps you need to achieve the goal.</p>

### 입력 

 <p>The first line of input gives the number of cases, <strong>T</strong>. <strong>T</strong> test cases follow.<br>
The first line of each test case has one integer, <strong>N</strong>. Each of the next <strong>N</strong> lines contains <strong>N</strong>characters. Each character is either 0 or 1.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 60</li>
	<li>1 ≤ <strong>N</strong> ≤ 40</li>
</ul>

### 출력 

 <p>For each test case, output</p>

<pre>Case #X: K</pre>

<p>where <strong>X</strong> is the test case number, starting from 1, and <strong>K</strong> is the minimum number of row swaps needed to have all the 1 values in the matrix below or on the main diagonal.</p>

<p>You are guaranteed that there is a solution for each test case.</p>

