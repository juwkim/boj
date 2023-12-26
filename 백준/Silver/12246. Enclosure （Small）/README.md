# [Silver IV] Enclosure (Small) - 12246 

[문제 링크](https://www.acmicpc.net/problem/12246) 

### 성능 요약

메모리: 110592 KB, 시간: 128 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2023년 12월 27일 00:59:35

### 문제 설명

<p>Your task in this problem is to find out the minimum number of stones needed to place on an N-by-M rectangular grid (N horizontal line segments and M vertical line segments) to enclose at least K intersection points. An intersection point is enclosed if either of the following conditions is true:</p>

<ol>
	<li>A stone is placed at the point.</li>
	<li>Starting from the point, we cannot trace a path along grid lines to reach an empty point on the grid border through empty intersection points only.</li>
</ol>

<p>For example, to enclose 8 points on a 4x5 grid, we need at least 6 stones. One of many valid stone layouts is shown below. Enclosed points are marked with an "x".</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/12246/images-61.png" style="height:150px; width:181px"></p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> lines follow. Each test case is a line of three integers: <strong>N</strong> <strong>M</strong> <strong>K</strong>.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>N</strong>.</li>
	<li>1 ≤ <strong>M</strong>.</li>
	<li>1 ≤ <strong>K</strong> ≤ <strong>N</strong> × <strong>M</strong>.</li>
	<li><strong style="line-height:1.6em">N</strong><span style="line-height:1.6em"> × </span><strong style="line-height:1.6em">M</strong><span style="line-height:1.6em"> ≤ 20.</span></li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of stones needed.</p>

