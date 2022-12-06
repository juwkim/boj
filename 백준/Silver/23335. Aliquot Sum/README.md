# [Silver V] Aliquot Sum - 23335 

[문제 링크](https://www.acmicpc.net/problem/23335) 

### 성능 요약

메모리: 2032 KB, 시간: 4992 ms

### 분류

수학(math), 정수론(number_theory)

### 문제 설명

<p>A divisor of a positive integer n is an integer d where m = n d is an integer. In this problem, we define the aliquot sum s(n) of a positive integer n as the sum of all divisors of n other than n itself. For examples, s(12) = 1 + 2 + 3 + 4 + 6 = 16, s(21) = 1 + 3 + 7 = 11, and s(28) = 1 + 2 + 4 + 7 + 14 = 28.</p>

<p>With the aliquot sum, we can classify positive integers into three types: abundant numbers, deficient numbers, and perfect numbers. The rules are as follows.</p>

<ol>
	<li>A positive integer x is an abundant number if s(x) > x.</li>
	<li>A positive intewer y is a deficient number if s(y) < y.</li>
	<li>A positive integer z is a perfect number if s(z) = z.</li>
</ol>

<p>You are given a list of positive integers. Please write a program to classify them.</p>

### 입력 

 <p>The first line of the input contains one positive integer T indicating the number of test cases. The second line of the input contains T space-separated positive integers n<sub>1</sub>, ..., n<sub>T</sub>.</p>

### 출력 

 <p>Output T lines. If n<sub>i</sub> is an abundant number, then print <code>abundant</code> on the i-th line. If n<sub>i</sub> is a deficient number, then print <code>deficient</code> on the i-th line. If n<sub>i</sub> is a perfect number, then print <code>perfect</code> on the i-th line.</p>

