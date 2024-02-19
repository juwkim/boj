# [Silver III] Drum Decorator (Small) - 12145 

[문제 링크](https://www.acmicpc.net/problem/12145) 

### 성능 요약

메모리: 109240 KB, 시간: 116 ms

### 분류

브루트포스 알고리즘, 다이나믹 프로그래밍

### 제출 일자

2024년 2월 20일 07:49:01

### 문제 설명

<p>You are the drummer in the rock band Denise and the Integers. Your drum is a cylinder around which you've wrapped a rectangular grid of cells.<br>
<br>
Your band is scheduled to perform in Mathland. The Mathlanders are a tough audience, and they will expect every cell of your drum to contain a positive integer; zeroes and negative integers are not allowed. Moreover, each integer K must border (share an edge, and not just a point, with) exactly K other cells with the same integer -- that is, a cell with a 1 must touch exactly one other cell with a 1, a cell with a 2 must touch exactly 2 other cells with a 2, and so on. Apart from this restriction, it does not matter what other cells a cell touches. (The circular top and bottom of the drum do not count as cells and do not need to be decorated. Note that this means that the cells along the top and bottom of the drum only touch three other cells each, whereas all the other cells touch four other cells each.)<br>
<br>
For example, this is a valid decoration of a cylinder formed by a grid with 3 rows and 5 columns:<br>
<img src="https://onlinejudgeimages.s3.amazonaws.com/problem/12145/images-76.png" style="height:282px; vertical-align:middle; width:300px"><br>
(Imagine that the unseen two columns on the back of the drum are the same as the three visible columns.)<br>
<br>
You want to know how many different valid decorations are possible. Two decorations are different if one cannot be rotated (around the cylinder's axis of symmetry) to produce the other. The top and bottom of a drum are considered different, so this decoration of a 3x5 grid is different from the one above:<br>
<img src="https://onlinejudgeimages.s3.amazonaws.com/problem/12145/images-77.png" style="height:282px; vertical-align:middle; width:300px"><br>
(Again, imagine that the unseen two columns on the back of the drum are the same as the three visible columns.)<br>
<br>
Your drum has <strong>R</strong> rows and <strong>C</strong> columns. How many different valid decorations are possible? The number may be large, so return the number of decorations modulo 10<sup>9</sup> + 7 (1000000007).</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> lines follow; each contains two space-separated integers, <strong>R</strong> and <strong>C</strong>, which are the number of rows and columns in the drum.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 20.</li>
	<li>2 ≤ <strong>R</strong> ≤ 6.</li>
	<li>3 ≤ <strong>C</strong> ≤ 6.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the number of valid decorations modulo 10<sup>9</sup> + 7, as described above.</p>

