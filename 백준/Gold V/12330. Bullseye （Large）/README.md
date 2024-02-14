# [Gold V] Bullseye (Large) - 12330 

[문제 링크](https://www.acmicpc.net/problem/12330) 

### 성능 요약

메모리: 111492 KB, 시간: 176 ms

### 분류

임의 정밀도 / 큰 수 연산, 이분 탐색, 기하학, 수학, 매개 변수 탐색

### 제출 일자

2024년 2월 15일 04:26:43

### 문제 설명

<p>Maria has been hired by the Ghastly Chemicals Junkies (GCJ) company to help them manufacture <strong>bullseyes</strong>. A <strong>bullseye</strong> consists of a number of concentric rings (rings that are centered at the same point), and it usually represents an archery target. GCJ is interested in manufacturing black-and-white bullseyes. </p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/12329/images-53.png" style="height:222px; width:224px"></p>

<p>Maria starts with <strong>t</strong> millilitres of black paint, which she will use to draw rings of thickness 1cm (one centimetre). A ring of thickness 1cm is the space between two concentric circles whose radii differ by 1cm.</p>

<p>Maria draws the first black ring around a white circle of radius <strong>r</strong> cm. Then she repeats the following process for as long as she has enough paint to do so:</p>

<ol>
	<li>Maria imagines a white ring of thickness 1cm around the last black ring.</li>
	<li>Then she draws a new black ring of thickness 1cm around that white ring.</li>
</ol>

<p>Note that each "white ring" is simply the space between two black rings.</p>

<p>The area of a disk with radius 1cm is <strong>π</strong> cm<sup>2</sup>. One millilitre of paint is required to cover area <strong>π</strong> cm<sup>2</sup>. What is the maximum number of black rings that Maria can draw? Please note that:</p>

<ul>
	<li>Maria only draws complete rings. If the remaining paint is not enough to draw a complete black ring, she stops painting immediately.</li>
	<li>There will always be enough paint to draw at least one black ring.</li>
</ul>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case consists of a line containing two space separated integers: <strong>r</strong> and <strong>t.</strong></p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 6000.</li>
	<li>1 ≤ <strong>r</strong> ≤ 10<sup>18</sup>.</li>
	<li>1 ≤ <strong>t</strong> ≤ 2 × 10<sup>18</sup>.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>x</strong>: <strong>y</strong>", where <strong>x</strong> is the case number (starting from 1) and <strong>y</strong> is the maximum number of black rings that Maria can draw.</p>

