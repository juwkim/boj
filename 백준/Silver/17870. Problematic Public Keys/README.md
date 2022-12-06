# [Silver IV] Problematic Public Keys - 17870 

[문제 링크](https://www.acmicpc.net/problem/17870) 

### 성능 요약

메모리: 114328 KB, 시간: 156 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math), 정수론(number_theory), 정렬(sorting)

### 문제 설명

<p>On February 15, 2012, the New York Times reported a flaw in the method of generating keys for a public-key encryption system (“Researchers Find a Flaw in a Widely Used Online Encryption Method" by John Markoff). This flaw enables an attacker to determine private keys given a set of flawed public keys.</p>

<p>Your job is to write a program that takes flawed public keys and determines the corresponding private keys. For the purposes of this problem, a private key consists of a pair of prime numbers,</p>

<p style="text-align: center;">2 < K<sub>1</sub>, K<sub>2</sub> < 2<sup>31</sup></p>

<p>and the corresponding public key consists of the product K<sub>1</sub> × K<sub>2</sub>.</p>

### 입력 

 <p>The first line of the input contains an integer value, M (2 ≤ M ≤ 100). M is the number of input lines that follow. Each of the M lines contains a single “public key." Each public key is the product of exactly two prime numbers and will fit in a 32-bit unsigned integer.</p>

### 출력 

 <p>The output lines produced by your program should contain the unique prime factors of the input data values in ascending numeric order, five per line, except for the last line. Output values on the same line are separated by a single space.</p>

