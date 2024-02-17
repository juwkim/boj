# [Silver III] Best Rational Approximation - 15299 

[문제 링크](https://www.acmicpc.net/problem/15299) 

### 성능 요약

메모리: 129580 KB, 시간: 368 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 2월 17일 09:31:10

### 문제 설명

<p>Many microcontrollers have no floating point unit but do have a (reasonably) fast integer divide unit. In these cases it may pay to use rational values to approximate floating point constants. For instance,</p>

<p style="text-align:center">355/113 = 3.1415929203539823008849557522124</p>

<p>is a quite good approximation to</p>

<p style="text-align:center">π = 3.14159265358979323846</p>

<p>A best rational approximation, p/q, to a real number, x, with denominator at most M is a rational number, p/q (in lowest terms), with q <= M such that, for any integers, a and b with b <= M, and a and b relatively prime, p/q is at least as close to x as a/b:</p>

<p style="text-align:center">|x – p/q| ≤ |x – a/b|</p>

<p>Write a program to compute the best rational approximation to a real number, x, with denominator at most M.</p>

### 입력 

 <p>The first line of input contains a single integer P, (1 ≤ P ≤ 1000), which is the number of data sets that follow. Each data set should be processed identically and independently.</p>

<p>Each data set consists of a single line of input. It contains the data set number, K, followed by the maximum denominator value, M (15 ≤ M ≤ 100000), followed by a floating-point value, x, (0 ≤ x < 1).</p>

### 출력 

 <p>For each data set there is a single line of output. The single output line consists of the data set number, K, followed by a single space followed by the numerator, p, of the best rational approximation to x, followed by a forward slash (/) followed by the denominator, q, of the best rational approximation to x.</p>

