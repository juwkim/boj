# [Silver IV] Polynomial Remains - 1716 

[문제 링크](https://www.acmicpc.net/problem/1716) 

### 성능 요약

메모리: 115436 KB, 시간: 136 ms

### 분류

많은 조건 분기(case_work), 수학(math)

### 문제 설명

<p>Given the polynomial</p>

<p style="text-align: center;">a(x) = a<sub>n</sub> x<sup>n</sup> + ... + a<sub>1</sub> x + a<sub>0</sub>,</p>

<p>compute the remainder r(x) when a(x) is divided by x<sup>k</sup>+1.</p>

### 입력 

 <p>The input consists of a number of cases. The first line of each case specifies the two integers n and k (0 ≤ n, k ≤ 10000). The next n+1 integers give the coefficients of a(x), starting from a<sub>0</sub> and ending with a<sub>n</sub>. The input is terminated if n = k = -1.</p>

### 출력 

 <p>For each case, output the coefficients of the remainder on one line, starting from the constant coefficient r<sub>0</sub>. If the remainder is 0, print only the constant coefficient. Otherwise, print only the first d+1 coefficients for a remainder of degree d. Separate the coefficients by a single space.</p>

<p>You may assume that the coefficients of the remainder can be represented by 32-bit integers.</p>

