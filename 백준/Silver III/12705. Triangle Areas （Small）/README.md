# [Silver III] Triangle Areas (Small) - 12705 

[문제 링크](https://www.acmicpc.net/problem/12705) 

### 성능 요약

메모리: 110556 KB, 시간: 328 ms

### 분류

브루트포스 알고리즘, 해 구성하기, 기하학

### 제출 일자

2024년 2월 15일 03:47:24

### 문제 설명

<p>Ten-year-old Tangor has just discovered how to compute the area of a triangle. Being a bright boy, he is amazed by how many different ways one can compute the area. He also convinced himself that, if all the points of the triangle have integer coordinates, then the triangle's area is always either an integer or half of an integer! Isn't that nice?</p>

<p>But today Tangor is trying to go in the opposite direction. Instead of taking a triangle and computing its area, he is taking an integer <strong>A</strong> and trying to draw a triangle of area <strong>A</strong>/2. He restricts himself to using only the integer points on his graph paper for the triangle's vertices.</p>

<p>More precisely, the sheet of graph paper is divided into an <strong>N</strong> by <strong>M</strong> grid of square cells. The triangle's vertices may only be placed in the corners of those cells. If you imagine a coordinate system on the paper, then these points are of the form (<strong>x</strong>, <strong>y</strong>), where <strong>x</strong> and <strong>y</strong>are integers such that 0 ≤ <strong>x</strong> ≤ <strong>N</strong> and 0 ≤ <strong>y</strong> ≤ <strong>M</strong>.</p>

<p>Given the integer <strong>A</strong>, help Tangor find three integer points on the sheet of graph paper such that the area of the triangle formed by those points is exactly <strong>A</strong>/2, if that is possible. In case there is more than one way to do this, any solution will make him happy.</p>

### 입력 

 <p>One line containing an integer <strong>C</strong>, the number of test cases in the input file.</p>

<p>The next <strong>C</strong> lines will each contain three integers <strong>N</strong>, <strong>M</strong>, and <strong>A</strong>, as described above.</p>

<p>Limits</p>

<ul>
	<li>0 ≤ <strong>C</strong> ≤ 1000</li>
	<li>1 ≤ <strong>A</strong> ≤ 10<sup>8</sup></li>
	<li>1 ≤ <strong>N</strong> ≤ 50</li>
	<li>1 ≤ <strong>M</strong> ≤ 50</li>
</ul>

### 출력 

 <p>For each test case, output one line. If there is no way to satisfy the condition, output </p>

<pre>Case #k: IMPOSSIBLE
</pre>

<p>where k is the case number, starting from 1. Otherwise, output</p>

<pre>Case #k: x<sub>1</sub> y<sub>1</sub> x<sub>2</sub> y<sub>2</sub> x<sub>3</sub> y<sub>3</sub>
</pre>

<p>where k is the case number and (x<sub>1</sub>, y<sub>1</sub>), (x<sub>2</sub>, y<sub>2</sub>), (x<sub>3</sub>, y<sub>3</sub>) are any three integer points on the graph paper that form a triangle of area <strong>A</strong>/2.</p>

