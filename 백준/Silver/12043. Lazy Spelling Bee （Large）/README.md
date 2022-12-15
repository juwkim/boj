# [Silver IV] Lazy Spelling Bee (Large) - 12043 

[문제 링크](https://www.acmicpc.net/problem/12043) 

### 성능 요약

메모리: 114844 KB, 시간: 132 ms

### 분류

조합론(combinatorics), 수학(math), 문자열(string)

### 문제 설명

<p>In the Lazy Spelling Bee, a contestant is given a target word W to spell. The contestant's answer word A is acceptable if it is the same length as the target word, and the i-th letter of A is either the i-th, (i-1)th, or (i+1)th letter of W, for all i in the range of the length of A. (The first letter of A must match either the first or second letter of W, since the 0th letter of W doesn't exist. Similarly, the last letter of A must match either the last or next-to-last letter of W.) Note that the target word itself is always an acceptable answer word.</p>

<p>You are preparing a Lazy Spelling Bee, and you have been asked to determine, for each target word, how many distinct acceptable answer words there are. Since this number may be very large, please output it modulo 1000000007 (10<sup>9</sup> + 7).</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow; each consists of one line with a string consisting only of lowercase English letters (<code>a</code> through <code>z</code>).</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ length of each string ≤ 1000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the number of distinct acceptable answer words, modulo 10<sup>9</sup> + 7.</p>

