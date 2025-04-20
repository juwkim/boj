# [Silver I] Linear Equation - 14543 

[문제 링크](https://www.acmicpc.net/problem/14543) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 파싱, 문자열

### 제출 일자

2025년 4월 20일 20:05:42

### 문제 설명

<p>You have been asked to write a program that can solve a simple linear equation.</p>

### 입력 

 <p>The first line of input contains a single integer P, (1 ≤ P ≤ 100), which is the number of data sets that follow. Each data set consists of a single line containing one simple linear equation. Each equation will be in the form of ax, followed by a single space, followed by a sign “+”, followed by b, followed by a single space, followed by a sign “=”, followed by a single space, followed by c.</p>

<p style="text-align: center;">ax + b = c</p>

<p>where x is the variable, and a, b, c are non-negative integers (a, b, c ≤ 10<sup>9</sup>).</p>

### 출력 

 <p>For each data set, generate two lines of output. The first line will contain “Equation n” where n is the number of the data set. The second line will contain the following answer:</p>

<ul>
	<li>If the equation has no solution, print "No solution.".</li>
	<li>If the equation has infinitely many solutions, print "More than one solution.".</li>
	<li>If the equation has exactly one solution, print "x = solution" where solution is replaced by the appropriate real number, <strong>truncated</strong> to six digits after the decimal point.</li>
</ul>

<p>Print a blank line after each data set case.</p>

