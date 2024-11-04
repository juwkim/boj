# [Silver III] Pretty Good Proportion (Small) - 12121 

[문제 링크](https://www.acmicpc.net/problem/12121) 

### 성능 요약

메모리: 110552 KB, 시간: 264 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 2월 16일 06:12:25

### 문제 설명

<p>I have a sequence of <strong>N</strong> binary digits. I am looking for a substring with just the right proportion of 0s and 1s, but it may not exist, so I will settle for something that's just pretty good.</p>

<p>Can you find a substring where the fraction of 1s is as close as possible to the given fraction <strong>F</strong>? Output the earliest possible index at which such a substring starts.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> test cases follow. Each one starts with a line containing <strong>N</strong> and <strong>F</strong>. <strong>F</strong> will be a decimal fraction between 0 and 1 inclusive, with exactly 6 digits after the decimal point. The next line contains <strong>N</strong> digits, each being either 0 or 1.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>0 ≤ <strong>F</strong> ≤ 1</li>
	<li><strong>F</strong> will have exactly 6 digits after the decimal point.</li>
	<li>1 ≤ <strong>N</strong> ≤ 1000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the 0-based index of the start of the substring with the fraction of 1s that is as close as possible to <strong>F</strong>. If there are multiple possible answers, output the smallest correct value.</p>

