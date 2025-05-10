# [Silver I] JEZIK - 3242 

[문제 링크](https://www.acmicpc.net/problem/3242) 

### 성능 요약

메모리: 111520 KB, 시간: 100 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색, 파싱, 문자열

### 제출 일자

2025년 5월 10일 19:29:24

### 문제 설명

<p>When analyzing source code in some programming language, it’s sometimes useful to know if there are some functions that will never execute. If there are, that may lead to an error in the code.</p>

<p>In this occasion we observe simple programming language that consists of following functions:</p>

<ul>
	<li><code>RADI</code>: program continues to next function</li>
	<li><code>IDI a</code>: program goes to a-th function</li>
	<li><code>IDI a ILI b</code>: program goes to a-th or b-th function</li>
</ul>

<p>Program always starts at first function.</p>

<p>Write the program that will calculate the number of functions that will never execute.</p>

### 입력 

 <p>In every line of input file there is one function, in i-th line there is i-th function.</p>

<p>In last line (after last function, i+1-th line) there is ‘.’ (a spot). That line is not the part of a program and is not considered function.</p>

<p>Number of functions will be less or equal then 10,000.</p>

### 출력 

 <p>In first and only line of output should be printed the number of unexecuted functions.</p>

