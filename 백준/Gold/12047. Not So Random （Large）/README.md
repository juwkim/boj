# [Gold IV] Not So Random (Large) - 12047 

[문제 링크](https://www.acmicpc.net/problem/12047) 

### 성능 요약

메모리: 110408 KB, 시간: 204 ms

### 분류

다이나믹 프로그래밍, 수학, 확률론

### 제출 일자

2024년 2월 12일 04:41:04

### 문제 설명

<p>There is a certain "random number generator" (RNG) which takes one nonnegative integer as input and generates another nonnegative integer as output. But you know that the RNG is really not very random at all! It uses a fixed number <strong>K</strong>, and always performs one of the following three operations:</p>

<ul>
	<li>with probability <strong>A</strong>/100: return the bitwise AND of the input and <strong>K</strong></li>
	<li>with probability <strong>B</strong>/100: return the bitwise OR of the input and <strong>K</strong></li>
	<li>with probability <strong>C</strong>/100: return the bitwise XOR of the input and <strong>K</strong></li>
</ul>

<p>(You may assume that the RNG <em>is</em> truly random in the way that it chooses the operation each time, based on the values of <strong>A</strong>, <strong>B</strong>, and <strong>C</strong>.)</p>

<p>You have <strong>N</strong> copies of this RNG, and you have arranged them in series such that output from one machine will be the input for the next machine in the series. If you provide <strong>X</strong> as an input to the first machine, what will be the expected value of the output of the final machine in the series?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow; each consists of one line with six integers <strong>N</strong>, <strong>X</strong>, <strong>K</strong>, <strong>A</strong>, <strong>B</strong>, and <strong>C</strong>. Respectively, these denote the number of machines, the initial input, the fixed number with which all the bitwise operations will be performed (on every machine), and 100 times the probabilities of the bitwise AND, OR, and XOR operations.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 50.</li>
	<li>0 ≤ <strong>A</strong> ≤ 100.</li>
	<li>0 ≤ <strong>B</strong> ≤ 100.</li>
	<li>0 ≤ <strong>C</strong> ≤ 100.</li>
	<li><strong>A+B+C</strong> = 100.</li>
	<li>1 ≤ <strong>N</strong> ≤ 10<sup>5</sup>.</li>
	<li>0 ≤ <strong>X</strong> ≤ 10<sup>9</sup>.</li>
	<li>0 ≤ <strong>K</strong> ≤ 10<sup>9</sup>.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the expected value of the final output. y will be considered correct if it is within an absolute or relative error of 10<sup>-9</sup> of the correct answer. See the <a href="https://code.google.com/codejam/faq.html#floating_point" style="color: rgb(85, 26, 139);" target="_blank">FAQ</a> for an explanation of what that means, and what formats of real numbers we accept.</p>

