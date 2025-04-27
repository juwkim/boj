# [Silver I] Number Sets (Small) - 12719 

[문제 링크](https://www.acmicpc.net/problem/12719) 

### 성능 요약

메모리: 110912 KB, 시간: 120 ms

### 분류

구현, 수학, 정수론, 소수 판정

### 제출 일자

2025년 4월 27일 16:19:28

### 문제 설명

<p>You start with a sequence of consecutive integers. You want to group them into sets.</p>

<p>You are given the interval, and an integer <strong>P</strong>. Initially, each number in the interval is in its own set.</p>

<p>Then you consider each pair of integers in the interval. If the two integers share a prime factor which is at least <strong>P</strong>, then you merge the two sets to which the two integers belong.</p>

<p>How many different sets there will be at the end of this process?</p>

### 입력 

 <p>One line containing an integer <strong>C</strong>, the number of test cases in the input file.</p>

<p>For each test case, there will be one line containing three single-space-separated integers <strong>A</strong>, <strong>B</strong>, and <strong>P</strong>.  <strong>A</strong> and <strong>B</strong> are the first and last integers in the interval, and <strong>P</strong> is the number as described above.</p>

<p>Limits</p>

<ul>
	<li>1 <= <strong>C</strong> <= 10</li>
	<li>1 <= <strong>A</strong> <= <strong>B</strong> <= 1000</li>
	<li>2 <= <strong>P</strong> <= <strong>B</strong></li>
</ul>

<div> </div>

### 출력 

 <p>For each test case, output one line containing the string "Case #X: Y" where X is the number of the test case, starting from 1, and Y is the number of sets.</p>

