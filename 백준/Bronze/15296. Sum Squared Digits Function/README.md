# [Bronze II] Sum Squared Digits Function - 15296 

[문제 링크](https://www.acmicpc.net/problem/15296) 

### 성능 요약

메모리: 28776 KB, 시간: 152 ms

### 분류

수학(math)

### 문제 설명

<p>The Sum Squared Digits function, SSD(b, n) of a positive integer n, in base b is defined by representing n in base b as in:</p>

<p style="text-align:center">n = a<sub>0</sub> + a<sub>1</sub>*b + a<sub>2</sub>*b<sup>2</sup> + …</p>

<p>then:</p>

<p style="text-align:center">SSD(b, n) = a<sub>0</sub><sup>2</sup> + a<sub>1</sub><sup>2</sup> + a<sub>2</sub><sup>2</sup> + …</p>

<p>is the sum of squares of the digits of the representation.</p>

<p>Write a program to compute the Sum Squared Digits function of an input positive number.</p>

### 입력 

 <p>The first line of input contains a single decimal integer P, (1 ≤ P ≤ 10000), which is the number of data sets that follow. Each data set should be processed identically and independently.</p>

<p>Each data set consists of a single line of input. It contains the data set number, K, followed by the base, b (3 ≤ b ≤ 16) as a decimal integer, followed by the positive integer, n (as a decimal integer) for which the Sum Squared Digits function is to be computed with respect to the base b. n will fit in a 32 bit unsigned integer. </p>

### 출력 

 <p>For each data set there is a single line of output.</p>

<p>The single line of output consists of the data set number, K, followed by a single space followed by the value of SSD(b, n) as a decimal integer.</p>

