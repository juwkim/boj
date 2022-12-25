# [Silver IV] Sudoku Checker (Small) - 12266 

[문제 링크](https://www.acmicpc.net/problem/12266) 

### 성능 요약

메모리: 115308 KB, 시간: 180 ms

### 분류

구현(implementation)

### 문제 설명

<p><strong>Sudoku</strong> is a popular single player game. The objective is to fill a 9x9 matrix with digits so that each column, each row, and all 9 non-overlapping 3x3 sub-matrices contain all of the digits from 1 through 9. Each 9x9 matrix is partially completed at the start of game play and typically has a unique solution.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/12266/images-59.png" style="height:250px; opacity:0.9; width:250px"></p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/12266/images-60.png" style="height:250px; width:250px"></p>

<p>Given a completed <strong>N</strong><strong><sup>2</sup></strong>x<strong>N</strong><strong><sup>2</sup></strong> Sudoku matrix, your task is to determine whether it is a <em>valid</em> solution. A <em>valid</em> solution must satisfy the following criteria:</p>

<ul>
	<li>Each row contains each number from <strong>1</strong> to <strong>N</strong><strong><sup>2</sup></strong>, once each.</li>
	<li>Each column contains each number from <strong>1</strong> to <strong>N</strong><strong><sup>2</sup></strong>, once each.</li>
	<li>Divide the <strong>N</strong><strong><sup>2</sup></strong>x<strong>N</strong><strong><sup>2</sup></strong> matrix into <strong>N</strong><strong><sup>2</sup></strong> non-overlapping <strong>N</strong>x<strong>N</strong> sub-matrices. Each sub-matrix contains each number from <strong>1</strong> to <strong>N</strong><strong><sup>2</sup></strong>, once each.</li>
</ul>

<p>You don't need to worry about the uniqueness of the problem. Just check if the given matrix is a valid solution.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case starts with an integer <strong>N</strong>. The next <strong>N</strong><strong><sup>2</sup></strong> lines describe a completed Sudoku solution, with each line contains exactly <strong>N</strong><strong><sup>2</sup></strong> integers. All input integers are positive and less than 1000.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li><strong style="line-height:1.6em">N</strong><span style="line-height:1.6em"> = 3.</span></li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is "Yes" (quotes for clarity only) if it is a valid solution, or "No" (quotes for clarity only) if it is invalid. Note that the judge is case-sensitive, so answers of "yes" and "no" will not be accepted.</p>

