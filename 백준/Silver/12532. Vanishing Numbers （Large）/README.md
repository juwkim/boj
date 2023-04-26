# [Silver III] Vanishing Numbers (Large) - 12532 

[문제 링크](https://www.acmicpc.net/problem/12532) 

### 성능 요약

메모리: 143004 KB, 시간: 784 ms

### 분류

임의 정밀도 / 큰 수 연산, 구현

### 문제 설명

<p>There is a pool of numbers which are arbitrary decimal fractions from the interval (0, 1). In the first round of the game the middle third of the interval disappears, and the numbers from this interval are eliminated from the pool. In the next rounds the middle thirds of each of the remaining intervals disappear. In the first round the the interval [1/3, 2/3] is eliminated and in the second round the two intervals [1/9, 2/9] and [7/9, 8/9] are eliminated, and so on. The endpoints of each removed interval are removed as well.</p>

<p>Your role is to sort the pool of numbers in the order that they are eliminated. If some numbers are never eliminated, list them last. In case of a tie, list the smaller numbers first.</p>

### 입력 

 <p>The first line of input will contain <strong>T</strong>, the number of test cases. <strong>T</strong> test cases will follow. Each one will start with a line containing an integer <strong>N</strong>. <strong>N</strong> numbers will follow, one per line. Each number will start with "0.", followed by one or more decimal digits. Each number will be larger than zero and will not have any trailing zeros.</p>

<h3>Limits</h3>

<ul>
	<li><strong>T</strong> ≤ 100</li>
	<li><strong>N</strong> ≤ 100</li>
	<li>Each number will have at most 11 digits after the decimal point.</li>
</ul>

### 출력 

 <p>For each test case, print the line "Case #<strong>x</strong>:", where <strong>x</strong> is the number of the test case, starting with 1. After that line, list the numbers, one per line, in order of elimination.</p>

