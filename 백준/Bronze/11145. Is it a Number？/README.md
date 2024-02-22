# [Bronze II] Is it a Number? - 11145 

[문제 링크](https://www.acmicpc.net/problem/11145) 

### 성능 요약

메모리: 31120 KB, 시간: 56 ms

### 분류

파싱, 문자열

### 제출 일자

2024년 2월 23일 05:12:59

### 문제 설명

<p>This is it! You’ve finally graduated and started working. Looking forward to some really cool tasks now. While you’re skipping around in the eagerness of getting started, you’re told what your first task is - Input Validation! You should check whether the typed input is an integer number.</p>

<p>Time to get going! Given a sequence of characters, check whether they describe an integer number. Whitespace is allowed both before and after the number, but the rest of the input must consist of a single, non-negative integer number. Only digits will be accepted as the relevant part of the input (+ is not allowed, for instance).</p>

### 입력 

 <p>The first line of input contains a single number T, the number of test cases to follow. Then follow a single line for each test case; the input to be validated.</p>

<ul>
	<li>0 < T ≤ 500</li>
	<li>Each test case will consist of at least 1 and at most 50 characters (excluding the line break).</li>
	<li>A test case can contain any character with an ASCII value between 32 and 126 (inclusive).</li>
	<li>There should be no leading zeros in the output.</li>
</ul>

### 출력 

 <p>For each test case, output a line containing the value of the number if the input is a valid integer number, or invalid input (all lowercase) if the input is not.</p>

