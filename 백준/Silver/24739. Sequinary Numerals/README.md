# [Silver V] Sequinary Numerals - 24739 

[문제 링크](https://www.acmicpc.net/problem/24739) 

### 성능 요약

메모리: 130160 KB, 시간: 288 ms

### 분류

사칙연산(arithmetic), 유클리드 호제법(euclidean), 구현(implementation), 수학(math), 정수론(number_theory), 문자열(string)

### 문제 설명

<p>A sequinary numeral is a sequence of digits:</p>

<p style="text-align: center;">d<sub>n</sub>d<sub>n-2</sub>...d<sub>1</sub>d<sub>0</sub></p>

<p>where d<sub>n</sub> is 1 or 2 and the others are 0, 1, or 2.</p>

<p>It represents the rational number:</p>

<p style="text-align: center;">d<sub>0</sub> + d1 * (3/2) + d<sub>2</sub> * (3/2)<sup>2</sup> + ... + d<sub>n</sub> * (3/2)<sup>n</sup></p>

<p>Write a program which takes a sequinary numeral as input and returns the number it represents as a proper fraction.</p>

### 입력 

 <p>The single line of input contains a sequinary numeral of no more than 32 digits.</p>

### 출력 

 <p>Output consists of a single line.</p>

<p>If the result is an integer, the output is the decimal integer. Otherwise, the output is N a single space and K/M where N, K and M are decimal integers where K < M and K/M is in lowest terms (GCD(K, M) = 1).</p>

