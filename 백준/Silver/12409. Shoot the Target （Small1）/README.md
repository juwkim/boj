# [Silver IV] Shoot the Target (Small1) - 12409 

[문제 링크](https://www.acmicpc.net/problem/12409) 

### 성능 요약

메모리: 108080 KB, 시간: 120 ms

### 분류

브루트포스 알고리즘, 기하학, 수학

### 제출 일자

2023년 12월 23일 05:03:06

### 문제 설명

<p>Kazuki is playing Worms. There is a target above the ground which he has to hit. However, it is slanted so that it is not perpendicular to the ground. Kazuki is allowed to shoot from anywhere on the ground and he wants to find the best place to stand to maximize the visible angle of the target. Find this maximum visible angle in degrees.</p>

<p>The world is a 2D plane, with the y-axis pointing up towards the sky. The ground can be considered as the x-axis. You will be given the coordinates of the two endpoints of the target -- <strong>(X1, Y1)</strong> and <strong>(X2, Y2)</strong>. The target is a line segment between those two points.</p>

<p>Note that the visible angle of the target that Kazuki wants to maximize is the angle formed by the points <strong>(X1, Y1)</strong>, <strong>(X, 0)</strong> and <strong>(X2, Y2)</strong>. The optimal <strong>X</strong> will not necessarily be an integer.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> lines follow. Each lines consists of 4 integers <strong>X1</strong>, <strong>Y1</strong>, <strong>X2</strong> and <strong>Y2</strong> separated by spaces, where <strong>(X1, Y1)</strong> and <strong>(X2, Y2)</strong> are the coordinates of the two ends of the target.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li><strong>X1</strong> ≠ <strong>X2</strong></li>
	<li>1 ≤ <strong>Y1, Y2</strong> ≤ 10</li>
	<li>-10 ≤ <strong>X1, X2</strong> ≤ 10</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #t: Z", where t is the case number (starting from 1) and <strong>Z</strong> is the maximum visible angle of the target in degrees that Kazuki can achieve. Answers accurate to within an absolute or relative error of 10<sup>-4</sup> will be accepted.</p>

