# [Silver II] gCube (Large) - 12077 

[문제 링크](https://www.acmicpc.net/problem/12077) 

### 성능 요약

메모리: 112140 KB, 시간: 472 ms

### 분류

수학

### 제출 일자

2024년 4월 11일 20:20:15

### 문제 설명

<p>Googlers are very interested in cubes, but they are bored with normal three-dimensional cubes and also want to think about other kinds of cubes! A "D-dimensional cube" has D dimensions, all of equal length. (D may be any positive integer; for example, a 1-dimensional cube is a line segment, and a 2-dimensional cube is a square, and a 4-dimensional cube is a hypercube.) A "D-dimensional cuboid" has D dimensions, but they might not all have the same lengths.</p>

<p>Suppose we have an <strong>N</strong>-dimensional cuboid. The <strong>N</strong> dimensions are numbered in order (0, 1, 2, ..., N - 1), and each dimension has a certain length. We want to solve many subproblems of this type:</p>

<ol>
	<li>Take all consecutive dimensions between the <strong>L<sub>i</sub></strong>-th dimension and <strong>R<sub>i</sub></strong>-th dimension, inclusive.</li>
	<li>Use those dimensions to form a D-dimensional cuboid, where D = <strong>R<sub>i</sub></strong> - <strong>L<sub>i</sub></strong> + 1. (For example, if <strong>L<sub>i</sub></strong> = 3 and <strong>R<sub>i</sub></strong> = 6, we would form a 4-dimensional cuboid using the 3rd, 4th, 5th, and 6th dimensions of our <strong>N</strong>-dimensional cuboid.)</li>
	<li>Reshape it into a D-dimensional cube <strong>that has exactly the same volume as that D-dimensional cuboid</strong>, and find the edge length of that cube.</li>
</ol>

<p>Each test case will have <strong>M</strong> subproblems like this, all of which use the same original <strong>N</strong>-dimensional cuboid.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow.</p>

<p>Each test case begins with two integers <strong>N</strong> and <strong>M</strong>; <strong>N</strong> is the number of dimensions and <strong>M</strong> is the number of queries. Then there is one line with <strong>N</strong> positive integers <strong>a<sub>i</sub></strong>, which are the lengths of the dimensions, in order. Then, <strong>M</strong> lines follow. In the ith line, there are two integers <strong>L<sub>i</sub></strong> and <strong>R<sub>i</sub></strong>, which give the range of dimensions to use for the ith subproblem.</p>

### 출력 

 <p>For each test case, output one line containing "Case #x:", where x is the test case number (starting from 1). After that, output <strong>M</strong> lines, where the ith line has the edge length for the ith subproblem. An edge length will be considered correct if it is within an absolute error of 10<sup>-6</sup> of the correct answer.</p>

