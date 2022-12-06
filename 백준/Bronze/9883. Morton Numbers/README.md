# [Bronze II] Morton Numbers - 9883 

[문제 링크](https://www.acmicpc.net/problem/9883) 

### 성능 요약

메모리: 31996 KB, 시간: 92 ms

### 분류

구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>The Morton number of two integers x and y is the integer formed by interleaving the bits of x and y in binary such that the bits of x are in the even position and the bits of y are in the odd position.</p>

<p>If we consider x and y to represent the 2D coordinates of a point, then the Morton numbers have the property that if two points are close to each other, then their respective Morton numbers will also be close to one another. Furthermore the Morton numbers are proportional to x and y.</p>

<p>In the problem, you will be given two integers x and y in base 10 (0 ≤ x, y ≤ 2<sup>16</sup> - 1) and you should return the Morton number of x and y in base 10.</p>

<p>For example if x = 4 and y = 5, then x = <strong>0000000000000100</strong> and y = 0000000000000101 in binary. Hence the Morton number of x and y is <strong>0</strong>0<strong>0</strong>0<strong>0</strong>0<strong>0</strong>0<strong>0</strong>0<strong>0</strong>0<strong>0</strong>0<strong>0</strong>0<strong>0</strong>0<strong>0</strong>0<strong>0</strong>0<strong>0</strong>0<strong>0</strong>0<strong>1</strong>1<strong>0</strong>0<strong>0</strong>1 in binary which is equivalent to 49. Note that the bits in bold represents the bits from x.</p>

### 입력 

 <p>The input consists of the two integers, x and y, on the same line separated by whitespace.</p>

### 출력 

 <p>Output the Morton number of x and y.</p>

