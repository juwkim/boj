# [Silver V] Roots! Really? - 11317 

[문제 링크](https://www.acmicpc.net/problem/11317) 

### 성능 요약

메모리: 114328 KB, 시간: 132 ms

### 분류

수학(math)

### 문제 설명

<p>A quadratic equation</p>

<p>\[ax^2 + bx + c = 0\]</p>

<p>has two solutions \(x_{+}\) and \(x_{−}\), called roots, which are given by</p>

<p>\[x_{\pm} = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}\]</p>

<p>The two roots may be real or complex, and they may be identical or distinct. Given a quadratic equation and an interval [\(s\), \(t\)] (with \(s\) ≤ \(t\)), we want to know if the equation has a real root in the interval [\(s\), \(t\)]. That is, is it the case that \(s\) ≤ \(r\) ≤ \(t\) where \(r\) is any of the roots \(x_{−}\) or \(x_{+}\)?</p>

### 입력 

 <p>The first line of the input contains an integer, N, the number of test cases (1 ≤ N ≤ 1, 000). Then follows N lines, each containing five integers, \(a\), \(b\), \(c\), \(s\), and \(t\), with −10<sup>7</sup> ≤ \(a\), \(b\), \(c\), \(s\), \(t\) ≤ 10<sup>7</sup> , \(a\) ≠ 0, and \(s\) ≤ \(t\).</p>

### 출력 

 <p>For each of the N test cases, output “Yes” if the equation \(ax^2 + bx + c = 0\) has a real root in the interval [\(s\), \(t\)]. Output “No” otherwise.</p>

