# [Silver V] Joint Attack - 17910 

[문제 링크](https://www.acmicpc.net/problem/17910) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

유클리드 호제법(euclidean), 구현(implementation), 수학(math), 정수론(number_theory), 재귀(recursion)

### 문제 설명

<p>General Torstein has sent the x-coordinate for the next joint attack and is expecting you to promptly follow his orders in order to avoid impeding doom. Unfortunately Torstein hates numbers with more than 2 digits and loves horizontal line segments, and has therefore sent the coordinate as a continued fraction, i.e.</p>

<p>\[ x=x_0+\frac{1}{x_1+\frac{1}{\ldots}}\]</p>

<p>Your rocket launcher only accepts coordinates as reduced fractions, so you need to quickly compute the correct numbers to feed it in order to commence the attack. Hurry! Failure may have dire consequences!</p>

### 입력 

 <p>The first line of output is one integer n (1 ≤ n < 40), the number of coefficients in the continued fraction, followed by a line with n integers (1 ≤ x<sub>i</sub> < 100) the coefficients of x.</p>

### 출력 

 <p>The coordinate x as a reduced fraction. It is guaranteed that the numerator and denominator are both less than 10<sup>18</sup>.</p>

