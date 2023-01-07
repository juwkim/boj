# [Silver IV] Password Security (Small1) - 12040 

[문제 링크](https://www.acmicpc.net/problem/12040) 

### 성능 요약

메모리: 116016 KB, 시간: 140 ms

### 분류

무작위화(randomization)

### 문제 설명

<p>You just bought your young nephew Andrey a complete set of 26 English wooden alphabet letters from A to Z. Because the letters come in a long, linear package, they appear to spell out a 26-letter message.</p>

<p>You use <strong>N</strong> different passwords to log into your various online accounts, and you are concerned that this message might coincidentally include one or more of them. Can you find any arrangement of the 26 letters, such that no password appears in the message as a continuous substring?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each consists of one line with an integer <strong>N</strong>, and then another line with <strong>N</strong> different strings of uppercase English letters <strong>P<sub>1</sub></strong>, <strong>P<sub>2</sub></strong>, ..., <strong>P<sub>N</sub></strong>, which are the passwords.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ length of <strong>P<sub>i</sub></strong> ≤ 26, for all i. (Each password is between 1 and 26 letters long.)</li>
	<li><strong>P<sub>i</sub></strong> ≠ <strong>P<sub>j</sub></strong> for all i ≠ j. (All passwords are different.</li>
	<li><strong>N</strong> = 1.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is a permutation of the entire uppercase English alphabet that contains no password as a continuous substring, or the word <code>IMPOSSIBLE</code> if there is no such permutation.</p>

