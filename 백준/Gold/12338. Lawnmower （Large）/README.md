# [Gold V] Lawnmower (Large) - 12338 

[문제 링크](https://www.acmicpc.net/problem/12338) 

### 성능 요약

메모리: 110992 KB, 시간: 116 ms

### 분류

애드 혹, 브루트포스 알고리즘

### 제출 일자

2025년 4월 28일 19:03:23

### 문제 설명

<p>Alice and Bob have a lawn in front of their house, shaped like an <strong>N</strong> metre by <strong>M</strong> metre rectangle. Each year, they try to cut the lawn in some interesting pattern. They used to do their cutting with shears, which was very time-consuming; but now they have a new automatic lawnmower with multiple settings, and they want to try it out.</p>

<p>The new lawnmower has a height setting - you can set it to any height <strong>h</strong> between 1 and 100 millimetres, and it will cut all the grass higher than <strong>h</strong> it encounters to height <strong>h</strong>. You run it by entering the lawn at any part of the edge of the lawn; then the lawnmower goes in a straight line, perpendicular to the edge of the lawn it entered, cutting grass in a swath 1m wide, until it exits the lawn on the other side. The lawnmower's height can be set only when it is not on the lawn.</p>

<p>Alice and Bob have a number of various patterns of grass that they could have on their lawn. For each of those, they want to know whether it's possible to cut the grass into this pattern with their new lawnmower. Each pattern is described by specifying the height of the grass on each 1m x 1m square of the lawn.</p>

<p>The grass is initially 100mm high on the whole lawn.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case begins with a line containing two integers: <strong>N</strong> and <strong>M</strong>. Next follow <strong>N</strong> lines, with the <em>i</em>th line containing <strong>M</strong> integers <strong>a</strong><strong><sub>i,j</sub></strong> each, the number <strong>a</strong><strong><sub>i,j</sub></strong> describing the desired height of the grass in the <em>j</em>th square of the <em>i</em>th row.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>N</strong>, <strong>M</strong> ≤ 100.</li>
	<li>1 ≤ <strong>a</strong><strong><sub>i,j</sub></strong> ≤ 100.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is either the word "YES" if it's possible to get the x-th pattern using the lawnmower, or "NO", if it's impossible (quotes for clarity only).</p>

