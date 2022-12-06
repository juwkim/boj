# [Bronze III] Arithmetic and Geometric Sums - 9310 

[문제 링크](https://www.acmicpc.net/problem/9310) 

### 성능 요약

메모리: 121220 KB, 시간: 120 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>An arithmetic series is defined as a series of numbers where each following number is an additive constant away from the previous number.</p>

<p>\[a_1+a_2+a_3+\dots+a_n = a_1 + (a_1+d)+(a_1+2d)+\dots+(a_1+nd)\]</p>

<p>The sum of all values from \(a_1\) to \(a_n\) is given by:</p>

<p>\[s_n = \dfrac{n(2a_1 + (n-1)d)}{2}\]</p>

<p>A geometric series is defined as a series of numbers where each following number is a multiplicative constant away from the previous number.</p>

<p>\[a_1+a_2+a_3+\dots+a_n = a_1 + (ra_1)+(r^2a_1)+\dots+(r^na_1)\]</p>

<p>The sum of all values from \(a_1\) to \(a_n\) is given by:</p>

<p>\[S_n = a_1\dfrac{r^n-1}{r-1}\]</p>

<p>Given the first 3 numbers of either a geometric or arithmetic series, determine the sum to N terms. The first term is index 1, the sum to N terms should include the Nth term in the calculation.</p>

### 입력 

 <p>The input will be given by 2 lines for each data set. The first line will be N, the term to which the sum should be computed. The next line of data is the series of numbers. They will be integers with a space separating each one. The series will be either geometric or arithmetic. The end of the input will be signaled by an N value of zero. You can assume r is integer if given series is gemoetric.</p>

### 출력 

 <p>For each test case output \(S_n\) on its own line.</p>

