# [Silver V] Sherlock and Parentheses (Small) - 14314 

[문제 링크](https://www.acmicpc.net/problem/14314) 

### 성능 요약

메모리: 113112 KB, 시간: 128 ms

### 분류

브루트포스 알고리즘(bruteforcing), 조합론(combinatorics), 수학(math)

### 문제 설명

<p>Sherlock and Watson have recently enrolled in a computer programming course. Today, the tutor taught them about the balanced parentheses problem. A string <code>S</code> consisting only of characters <code>(</code> and/or <code>)</code> is balanced if:</p>

<ul>
	<li>It is the empty string, or:</li>
	<li>It has the form <code>(</code>S<code>)</code>, where S is a balanced string, or:</li>
	<li>It has the form S<sub>1</sub>S<sub>2</sub>, where S<sub>1</sub> is a balanced string and S<sub>2</sub> is a balanced string.</li>
</ul>

<p>Sherlock coded up the solution very quickly and started bragging about how good he is, so Watson gave him a problem to test his knowledge. He asked Sherlock to generate a string S of L + R characters, in which there are a total of L left parentheses <code>(</code> and a total of R right parentheses <code>)</code>. Moreover, the string must have as many different balanced non-empty substrings as possible. (Two substrings are considered different as long as they start or end at different indexes of the string, even if their content happens to be the same). Note that S itself does not have to be balanced.</p>

<p>Sherlock is sure that once he knows the maximum possible number of balanced non-empty substrings, he will be able to solve the problem. Can you help him find that maximum number?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of one line with two integers: L and R.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the answer, as described above.</p>

