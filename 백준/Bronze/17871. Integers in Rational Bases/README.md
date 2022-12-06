# [Bronze I] Integers in Rational Bases - 17871 

[문제 링크](https://www.acmicpc.net/problem/17871) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

Empty

### 문제 설명

<p>Given relatively prime positive integers p > q, any positive integer, n, can be written uniquely as a linear combination of powers of (p/q) with coefficients in the range 0 … (p-1).</p>

<p style="text-align: center;">n = a0 + a1*(p/q) + a2*(p/q)<sup>2</sup> + …</p>

<p>For instance,</p>

<p style="text-align: center;">15 = 2*(3/2)<sup>4</sup> + 1*(3/2)<sup>3</sup> + 0*(3/2)<sup>2</sup> + 1*(3/2) + 0</p>

<p style="text-align: center;">15 = 4*(7/4)<sup>2</sup> + 1*(7/4) + 1</p>

<p>Write a program to find the base (p/q) expansion of an integer n. As digits for the base (p/q) expansion, use the characters 0-9, then A-Z, then a-z.</p>

### 입력 

 <p>Input consists of a single line that contains 3 space separated decimal values. They are the numerator p (3 <= p <= 62) of the fractional base, followed by the decimal denominator q (2 <= q <= (p-1)) of the fractional base, followed by the positive integer n to be represented in base (p/q). Values of p, q, and n will be chosen so that p and q are relatively prime, the expansion has at most 40 digits and n will fit in a 32-bit unsigned integer.</p>

### 출력 

 <p>Your program should produce a single output line containing a string of digits [0-9,A-Z,a-z] with the most significant digit first.</p>

