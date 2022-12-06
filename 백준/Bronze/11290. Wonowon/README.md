# [Bronze I] Wonowon - 11290 

[문제 링크](https://www.acmicpc.net/problem/11290) 

### 성능 요약

메모리: 37044 KB, 시간: 88 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math), 정수론(number_theory), 소수 판정(primality_test), 에라토스테네스의 체(sieve)

### 문제 설명

<p>There is a little village in northern Canada called Wonowon, its name coming from the fact that it is located at Mile 101 of the Alaska Highway. While passing through this village, a wandering mathematician had an idea for a new type of number, which he called a wonowon number. He defined a wonowon number as a number whose decimal digits start and end with 1, and alternate between 0 and 1. Thus, the first four wonowon numbers are 101, 10101, 1010101, 101010101.</p>

<p>Neither 2 nor 5 can divide any wonowon number, but it is conjectured that every other prime number divides some wonowon number. For example, 3 divides 10101 (i.e. 3×3367), 7 divides 10101 (i.e. 7×1443), 11 divides 101010101010101010101 (i.e. 11 × 9182736455463728191).</p>

<p>Assume throughout that this conjecture is true, and let W(p) denote the number of digits in the smallest wonowon number divisible by p. Thus, for example, W(3) = 5, W(7) = 5, W(11) = 21, W(13) = 5, W(17) = 15, W(19) = 17.</p>

<p>It has been found experimentally that for many primes p, W(p) = p − 2 (as in the case for p = 7, 17, 19). Thus, your task is to write a program which reads an integer n and outputs the number of primes for which W(p) = p − 2. Note that p cannot be 2 nor 5, and p is a prime number less-than or equal to n.</p>

### 입력 

 <p>The input consists of a single integer 3 ≤ n ≤ 10000.</p>

### 출력 

 <p>The output should consist of a single integer representing the number of primes p for which W(p) = p − 2.</p>

