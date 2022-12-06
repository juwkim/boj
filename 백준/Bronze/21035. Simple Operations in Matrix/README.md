# [Bronze I] Simple Operations in Matrix - 21035 

[문제 링크](https://www.acmicpc.net/problem/21035) 

### 성능 요약

메모리: 28776 KB, 시간: 84 ms

### 분류

구현(implementation)

### 문제 설명

<p>Matrix is a mathematical object which arranges data into a rectangular array of <em>N</em> rows and <em>M</em> columns. The rows are indexed from 1 to <em>N</em>, while the columns are indexed from 1 to <em>M</em>. Matrix is very powerful and extremely useful in many applications. In this problem, we are going to focus on two simple operations in matrix: row addition and column addition.</p>

<p>You are given a matrix of integers of <em>N</em> rows and <em>M</em> columns, and <em>Q</em> queries of the following format:</p>

<ul>
	<li><code>row</code> <em>k</em> <em>val</em>: add each element on the <em>k</em>-th row by <em>val</em>,</li>
	<li><code>col</code> <em>k</em> <em>val</em>: add each element on the <em>k</em>-th column by <em>val</em>.</li>
</ul>

<p>Your task is to output the following three numbers after all queries have been performed:</p>

<ul>
	<li>sum: the sum of all elements in the matrix,</li>
	<li>min: the value of the smallest element in the matrix,</li>
	<li>max: the value of the largest element in the matrix.</li>
</ul>

<p>See the sample input for clarity</p>

### 입력 

 <p>The first line contains two integers: <em>N</em> <em>M</em> (1 ≤ <em>N</em>, <em>M</em> ≤ 50) denoting the size of the matrix (number of rows and columns, respectively). The next <em>N</em> lines, each contains <em>M</em> integers: <em>A<sub>i</sub></em><sub>,<em>j</em></sub> (-100 ≤ <em>A<sub>i</sub></em><sub>,<em>j</em></sub> ≤ 100) denoting the matrix element at the <em>i</em>-th row and <em>j</em>-th column for 1 ≤ <em>i</em> ≤ <em>N</em> and 1 ≤ <em>j</em> ≤ <em>M</em>, respectively. The next line contains an integer: <em>Q</em> (0 ≤ <em>Q</em> ≤ 100) denoting the number of queries. The next <em>Q</em> lines, each contains a query in one of the following format:</p>

<ul>
	<li><code>row</code> <em>k</em> <em>val</em> (1 ≤ <em>k</em> ≤ <em>N</em>; -100 ≤ <em>val</em> ≤ 100)</li>
	<li><code>col</code> <em>k</em> <em>val</em> (1 ≤ <em>k</em> ≤ <em>M</em>; -100 ≤ <em>val</em> ≤ 100)</li>
</ul>

### 출력 

 <p>The output contains three integers (each separated by a single space) in a single line: sum min max, as described in the problem statement.</p>

