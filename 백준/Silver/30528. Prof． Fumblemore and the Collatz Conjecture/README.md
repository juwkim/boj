# [Silver I] Prof. Fumblemore and the Collatz Conjecture - 30528 

[문제 링크](https://www.acmicpc.net/problem/30528) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

수학, 브루트포스 알고리즘, 사칙연산

### 제출 일자

2025년 5월 18일 21:38:26

### 문제 설명

<p>The <em><strong>Collatz function</strong></em>, C(<em>n</em>), on positive integers is:</p>

<p style="text-align: center;"><em>n</em>/2 if <em>n</em> is even and 3<em>n</em>+1 if <em>n</em> is odd</p>

<p>The <em><strong>Collatz sequence</strong></em>, CS(<em>n</em>), of a positive integer, <em>n</em>, is the sequence</p>

<p style="text-align: center;">CS(<em>n</em>) = n, C(<em>n</em>), C(C(<em>n</em>)), C(C(C(<em>n</em>))), ...</p>

<p>For example, CS(12) = 12, 6, 3, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, ...</p>

<p>The <em><strong>Collatz Conjecture</strong></em> (also known as the <em>3n+1 problem</em>) is that CS(<em>n</em>) for every positive integer <em>n</em> eventually ends repeating the sequence 4, 2, 1. To date, the status of this conjecture is still unknown. No proof has been given and no counterexample has been found up to very large values.</p>

<p>Prof. Fumblemore wants to study the problem using <em>Collatz sequence types</em>. The <em>Collatz sequence type</em> (CST) of an integer <em>n</em>, CST(<em>n</em>) is a sequence of letters E and O (for even and odd) which describe the parity of the values in CS(<em>n</em>) up to but not including the first power of 2. So,</p>

<p style="text-align: center;">CST(12) = EEOEO</p>

<p>Note that</p>

<p style="text-align: center;">CS(908) = 908, 454, 227, 682, 341, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 3, 2, ...</p>

<p>so 12 and 908 have the same CST.</p>

<p>Prof. Fumblemore needs a program which allows him to enter a sequence of E's and O's and returns the <strong>smallest</strong> integer <em>n</em> for which the given sequence is CST(<em>n</em>).</p>

<p>Notes:</p>

<ul>
	<li>E's are even numbers which are not powers of 2,</li>
	<li>O's are odd numbers greater than 1.</li>
	<li>The last letter in a sequence must be an O (if C(<em>n</em>) is a power of 2, so is <em>n</em>)</li>
	<li>There can not be two O's in succession (C(odd) = even)</li>
	<li>Since, Prof. Fumblemore does not type well, you must check that the input sequence is valid before attempting to find <em>n</em>. That is, the sequence contains only E's and O's, ends in O and no two O's are adjacent.</li>
</ul>

### 입력 

 <p>Input consists of one line containing a string of up to 50 letters composed of E's and O's.</p>

### 출력 

 <p>There is one line of output that consists of the string <code>INVALID</code> if the input line is invalid, or a single decimal integer, <em>n</em>, such that <em>n</em> is the <em>smallest</em> integer for which CST(<em>n</em>) is the input sequence. Input will be chosen such that <em>n</em> ≤ 2<sup>47</sup>.</p>

