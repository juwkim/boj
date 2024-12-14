# [Silver II] Dynamic Grid (Large) - 12051 

[문제 링크](https://www.acmicpc.net/problem/12051) 

### 성능 요약

메모리: 117452 KB, 시간: 936 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 12월 15일 03:23:58

### 문제 설명

<p>We have a grid with <strong>R</strong> rows and <strong>C</strong> columns in which every entry is either 0 or 1. We are going to perform <strong>N</strong> operations on the grid, each of which is one of the following:</p>

<ul>
	<li>Operation M: Change a number in one cell of the grid to 0 or 1</li>
	<li>Operation Q: Determine the number of different <em>connected regions</em> of 1s. A connected region of 1s is a subset of cells that are all 1, in which any cell in the region can be reached from any other cell in the region by traveling between cells along edges (<strong>not</strong> corners).</li>
</ul>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with one line with two integers, R and C, which represent the number of rows and columns in the grid. Then, there are R lines of C characters each, in which every character is either 0 or 1. These lines represent the initial state of the grid.</p>

<p>The next line has one integer, N, the number of operations to perform on the grid. N more lines follow; each has one operation. All operation Ms will be of the form M x y z, meaning that the cell at row x and column y should be changed to the value z. All operation Qs will be of the form Q.</p>

### 출력 

 <p>For each test case, output one line containing "Case #x:", where x is the test case number (starting from 1). Then, for every operation Q in the test case, in order, output one line containing the number of connected regions of 1s.</p>

