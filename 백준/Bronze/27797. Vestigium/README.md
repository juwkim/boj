# [Bronze II] Vestigium - 27797 

[문제 링크](https://www.acmicpc.net/problem/27797) 

### 성능 요약

메모리: 117612 KB, 시간: 280 ms

### 분류

수학, 구현, 사칙연산

### 문제 설명

<p>Vestigium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.</p>

<p>The <i>trace</i> of a square matrix is the sum of the values on the main diagonal (which runs from the upper left to the lower right).</p>

<p>An <b>N</b>-by-<b>N</b> square matrix is a <i>Latin square</i> if each cell contains one of <b>N</b> different values, and no value is repeated within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the <b>N</b> values are the integers between 1 and <b>N</b>.</p>

<p>Given a matrix that contains only integers between 1 and <b>N</b>, we want to compute its trace and check whether it is a natural Latin square. To give some additional information, instead of simply telling us whether the matrix is a natural Latin square or not, please compute the number of rows and the number of columns that contain repeated values.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow. Each starts with a line containing a single integer <b>N</b>: the size of the matrix to explore. Then, <b>N</b> lines follow. The i-th of these lines contains <b>N</b> integers <b>M<sub>i,1</sub></b>, <b>M<sub>i,2</sub></b> ..., <b>M<sub>i,N</sub></b>. <b>M<sub>i,j</sub></b> is the integer in the i-th row and j-th column of the matrix.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: k r c</code>, where <code>x</code> is the test case number (starting from 1), <code>k</code> is the trace of the matrix, <code>r</code> is the number of rows of the matrix that contain repeated elements, and <code>c</code> is the number of columns of the matrix that contain repeated elements.</p>

