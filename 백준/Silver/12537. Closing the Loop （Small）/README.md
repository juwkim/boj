# [Silver V] Closing the Loop (Small) - 12537 

[문제 링크](https://www.acmicpc.net/problem/12537) 

### 성능 요약

메모리: 28776 KB, 시간: 72 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting)

### 문제 설명

<p>Given a bag full of rope segments, you will build the longest loop of rope while alternating colors. The bag contains <strong>S</strong> segments and each segment will either be blue (<strong>B</strong>) or red (<strong>R</strong>). You are required to alternate between colors and because of this requirement you might not use every segment in the bag. If you only have segments of a single color, you will not be able to tie any knots and should output <code>0</code>. Each segment length is provided in centimeters and each knot in the loop consumes one centimeter of length from the loop. In other words, a knot consumes one-half of a centimeter from of the two segment it connects.</p>

<p>Note that pieces of string that have length 1, if used in making the cycle, might get reduced to just a pair of knots of total length 0. This is allowed, and each such piece counts as having been used.</p>

### 입력 

 <p>The first line of input gives the number of cases, <strong>N</strong>.<br>
<strong>N</strong> test cases follow. For each test case there will be:</p>

<ul>
	<li>One line containing the value <strong>S</strong>, the number of rope segments in the bag.</li>
	<li>One line containing a space separated list of <strong>S</strong> values. Each value <strong>L</strong> indicates the segment length in centimeters followed by the letter <strong>B</strong> or <strong>R</strong> to indicate the segment color.</li>
</ul>

<h3>Limits</h3>

<ul>
	<li>1 ≤ number of rope segments (<strong>S</strong>) ≤ 1000</li>
	<li>1 ≤ length of a rope segment (<strong>L</strong>) ≤ 100</li>
	<li><strong>N</strong> ≤ 5</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>x</strong>: " followed by the maximum length of the rope loop that can be generated with the rope segments provided.</p>

