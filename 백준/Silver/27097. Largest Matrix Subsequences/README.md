# [Silver II] Largest Matrix Subsequences - 27097 

[문제 링크](https://www.acmicpc.net/problem/27097) 

### 성능 요약

메모리: 1732 KB, 시간: 20 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 3월 21일 03:53:47

### 문제 설명

<p>Define an 'increasing sequence' as a matrix of numbers which grows when read from left to right and from top to bottom along every row and every column.  An example:</p>

<pre>1 2 3 6
3 5 7 9</pre>

<p>Find the largest increasing sequence sub-matrix (or sub-matrices) in a matrix of integers (whose range is [0..32,000]).  The largest sub-matrix is that sub-matrix with the largest product of nrows*ncolumns.  If more than one largest sub-matrix exists, print each of them, with the list in 'numerical order'.</p>

<p>In the example above, row 1 is "1 2 3 6" and column 1 is "1 3".</p>

### 입력 

 <ul>
	<li>Line 1: Two space separated integers: R, C (1 ≤ R,C ≤ 150).  These are the number of rows and columns, respectively.</li>
	<li>Line 2..end: R*C space-separated integers that represent the matrix. These integers are presented 20 per line, except possibly the last line.  The first integer belongs in row 1 column 1; the second integer belongs in row 1 column 2; and so on for a total of R*C integers.</li>
</ul>

### 출력 

 <p>A series of one or more lines, each with four space-separated integers. The first two integers are the row and column of the upper left element; the second two integers are the extent of the submatrix (number of rows, number of columns).</p>

