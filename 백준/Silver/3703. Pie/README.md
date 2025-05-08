# [Silver I] Pie - 3703 

[문제 링크](https://www.acmicpc.net/problem/3703) 

### 성능 요약

메모리: 110724 KB, 시간: 112 ms

### 분류

이분 탐색, 기하학, 매개 변수 탐색

### 제출 일자

2025년 5월 8일 12:46:35

### 문제 설명

<p>My birthday is coming up and traditionally I’m serving pie. Not just one pie, no, I have a number N of them, of various tastes and of various sizes. F of my friends are coming to my party and each of them gets a piece of pie. This should be one piece of one pie, not several small pieces since that looks messy. This piece can be one whole pie though.</p>

<p>My friends are very annoying and if one of them gets a bigger piece than the others, they start complaining. Therefore all of them should get equally sized (but not necessarily equally shaped) pieces, even if this leads to some pie getting spoiled (which is better than spoiling the party). Of course, I want a piece of pie for myself too, and that piece should also be of the same size.</p>

<p>What is the largest possible piece size all of us can get? All the pies are cylindrical in shape and they all have the same height 1, but the radii of the pies can be different.</p>

### 입력 

 <p>One line with a positive integer: the number of test cases. Then for each test case:</p>

<ul>
	<li>One line with two integers N and F with 1 ≤ N, F ≤ 10 000: the number of pies and the number of friends.</li>
	<li>One line with N integers ri with 1 ≤ ri ≤ 10 000: the radii of the pies.</li>
</ul>

### 출력 

 <p>For each test case, output one line with the largest possible volume V such that me and my friends can all get a pie piece of size V. The answer should be given as a floating point number with an absolute error of at most 10<sup>−3</sup>.</p>

