# [Bronze III] Collatz Conjecture - 13236 

[문제 링크](https://www.acmicpc.net/problem/13236) 

### 성능 요약

메모리: 121220 KB, 시간: 112 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>The Collatz conjecture is a conjecture in mathematics named after Lothar Collatz, who first proposed it in 1937 and is still an open problem in mathematics.  The sequence of numbers involved is referred to as the hailstone sequence or hailstone numbers (because the values are usually subject to multiple descents and ascents like hailstones in a cloud. The conjecture is that no matter what number you start with, you will always eventually reach 1. The property has also been called oneness.</p>

<p>The computation (also known as 3n + 1) is stated as follows: </p>

<ol>
	<li>We have an integer number n.</li>
	<li>If n == 1: stop</li>
	<li>If n is even: divide the number by 2. Then go to step 1</li>
	<li>If n is odd: multiply by 3 and add 1. Then go to step 1</li>
</ol>

<p>As the conjecture states, you repeat this steps for any positive integer you will eventually end up with n = 1. The values we find define a sequence from n to 1.</p>

<p>For example, if we start with n = 14.</p>

<ul>
	<li>14 is even so the new value will be 7 (14/2)</li>
	<li>7 is odd so the new value will be 22 (3*7 + 1)</li>
	<li>22 is even so the new value will be 11 (22/2)</li>
	<li>11 is odd so the new value will be 34 (3*11 + 1)</li>
	<li>34 is even so the new value will be 17</li>
</ul>

<p>If we continue until we have a value of 1, the final sequence will be:</p>

<p>14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1</p>

<p>Your task is to write a program that, given the starting point n, prints the whole Collatz sequence for this value.</p>

### 입력 

 <p>A integer value n. The value of n will be between 1 and 100000.</p>

### 출력 

 <p>Print the Collatz sequence with the elements separated by a single space. Do not add any space at the beginning or the end of the line.</p>

