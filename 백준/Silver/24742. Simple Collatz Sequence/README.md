# [Silver II] Simple Collatz Sequence - 24742 

[문제 링크](https://www.acmicpc.net/problem/24742) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

다이나믹 프로그래밍, 수학

### 제출 일자

2025년 4월 25일 19:17:13

### 문제 설명

<p>The Simple Collatz Sequence (SCS) starting at an integer n, is defined by the formula:</p>

<p style="text-align: center;">S(k) = (k/2 if k is even, else (k+1))</p>

<p>The sequence is then n, S(n), S(S(n)), … until the value first reaches 1.</p>

<p>For example, starting at 11, we have:</p>

<p style="text-align: center;">11 -> 12 -> 6 -> 3 -> 4 -> 2 ->1</p>

<p>The sequence always ends at 1. (Fun Fact: The Hard Collatz Sequence sends odd k to 3*k+1. It is unknown whether that sequence always ends at 1.)</p>

<p>Let A(n) = number of steps in the SCS starting at n. For example, A(11) = 6.</p>

<p>Let C(n) = the number of integers m for which A(m) = n. For example, the integers for which A(n) = 6 are:</p>

<p style="text-align: center;">10, 11, 13, 24, 28, 30, 31, 64</p>

<p>So C(6) = 8.</p>

<p>Note that if n > 2<sup>m</sup>, then A(n) > m since we need to divide by 2 at least (m+1) times.</p>

<p>Write a program to compute C(m).</p>

### 입력 

 <p>Input consists of a single line which contains a decimal integer, m, (1 ≤ m ≤ 40000), which is the value for which C(m) is to be found.</p>

### 출력 

 <p>The output consists of a single line that contains the value of C(m) modulo 1000007.</p>

