# [Silver IV] Albocede DNA (Small) - 12072 

[문제 링크](https://www.acmicpc.net/problem/12072) 

### 성능 요약

메모리: 128120 KB, 시간: 324 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2023년 12월 26일 23:17:03

### 문제 설명

<p>The DNA of the Albocede alien species is made up of 4 types of nucleotides: <code>a</code>, <code>b</code>, <code>c</code>, and <code>d</code>. Different Albocedes may have different sequences of these nucleotides, but any Albocede's DNA sequence obeys all of the following rules:</p>

<ul>
	<li>It contains at least one copy of each of <code>a</code>, <code>b</code>, <code>c</code>, and <code>d</code>.</li>
	<li>All <code>a</code>s come before all <code>b</code>s, which come before all <code>c</code>s, which come before all <code>d</code>s.</li>
	<li>There are exactly as many <code>'a'</code>s as <code>'c'</code>s.</li>
	<li>There are exactly as many <code>'b'</code>s as <code>'d'</code>s.</li>
</ul>

<p>For example, <code>abcd</code> and <code>aabbbccddd</code> are valid Albocede DNA sequences. <code>acbd</code>, <code>abc</code>, and <code>abbccd</code> are not.</p>

<p>The Albocede-n is an evolved species of Albocede. The DNA sequence of an Albocede-n consists of one or more valid Albocede DNA sequences, concatenated together end-to-end. For example, <code>abcd</code> and <code>aaabcccdaabbbccdddabcd</code> are valid Albocede-n DNA sequences. (Observe that a valid Albocede-n DNA sequence is not necessarily also a valid Albocede DNA sequence.)</p>

<p>From one of your alien expeditions, you retrieved an interesting sequence of DNA made up of only <code>a</code>s, <code>b</code>s, <code>c</code>s, and <code>d</code>s. You are interested in how many of the different <a href="https://en.wikipedia.org/wiki/Subsequence" style="color: rgb(85, 26, 139);" target="_blank">subsequences</a> of that sequence would be valid Albocede-n DNA sequences. (Even if multiple different selections of nucleotides from the sequence produce the same valid subsequence, they still all count as distinct subsequences.) Since the result may be very large, please find it modulo 1000000007 (10<sup>9</sup> + 7).</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. Each of the next <strong>T</strong> lines contains a string <strong>S</strong> that consists only of the characters <code>a</code>, <code>b</code>, <code>c</code>, and <code>d</code>.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 20.</li>
	<li>1 ≤ <strong>length of S</strong> ≤ 50.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the output of the x<sup>th</sup> test case.</p>

