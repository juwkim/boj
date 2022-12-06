# [Bronze II] Table 1 - 22221 

[문제 링크](https://www.acmicpc.net/problem/22221) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

구성적(constructive), 수학(math)

### 문제 설명

<p>For the given integer M, build a square table with N rows and N columns (2 ≤ N ≤ 10), filled with decimal digits, with the following restriction: the N-digit numbers formed by the digits in each table row (from left to right), each table column (from top to bottom) and each main diagonal (from top to bottom) must be multiples of M, must not start with the digit 0 and must be unique within the table.</p>

<p>For example, a valid table for M = 2 is</p>

<pre>2 3 4
5 6 6
8 2 0
</pre>

<p>The following tables are not valid for M = 2:</p>

<pre>4
</pre>

<p>because N < 2;</p>

<pre>2 0
4 8
</pre>

<p>because the numbers in the last column and on one of the main diagonals start with the digit 0;</p>

<pre>2 3 4
5 8 8
2 0 2
</pre>

<p>because the number 482 is present twice in the table.</p>

<p>It is not always possible to solve this task. For example, the task is unsolvable for M = 10.</p>

### 입력 

 <p>The first line contain one value of M.</p>

### 출력 

 <p>The first line of a file must contain N, the number of rows and columns in the table. The i+1-st line of the file (1 ≤ i ≤ N) must contain the elements of the i-th row of the table as N digits, separated by spaces.</p>

