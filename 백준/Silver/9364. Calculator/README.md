# [Silver I] Calculator - 9364 

[문제 링크](https://www.acmicpc.net/problem/9364) 

### 성능 요약

메모리: 112636 KB, 시간: 156 ms

### 분류

사칙연산, 많은 조건 분기, 구현, 수학, 파싱, 문자열

### 제출 일자

2025년 4월 27일 19:02:59

### 문제 설명

<p>The users feedback for your most beloved open-source operating system is gathered, and guess what the most required feature turned out to be? Yes it is finally what we all have been waiting for so long, extending the built-in calculator functionality! On of the suggested extensions is adding the capability of evaluating polynomials, and that’s what you are thrilled to participate with! </p>

<p>In this problem you’re given a polynomial entered by the user in the calculator and are asked to evaluate it for a certain value. </p>

### 입력 

 <p>The first line of input contains T (0 < T <= 100) the number of polynomials, each test cases consists of two lines, the first line contains an integer (-1000 <= X <= 1000), the value for the variable X for which the polynomial is evaluated. </p>

<p>The second line contains a polynomial P with integer coefficients. P is a sum of terms of the form CX^E , where the coefficient C and the exponent E satisfy the following conditions: </p>

<ol>
	<li>E is an integer satisfying (0 <= E <= 30). If E is 0, then CX^E is expressed as C. If E is 1, then CX^E is expressed as CX, unless C is 1 or -1. In those instances, CX^E is expressed as X or -X. </li>
	<li>C is an integer. If C is 1 or -1 and E is not 0 or 1, then the CX^E will appear as X^E or -X^E. </li>
	<li>Only non-negative C values that are not part of the first term in the polynomial are preceded by +. </li>
	<li>Exponents in consecutive terms are strictly decreasing. </li>
	<li>C fits in a 32-bit signed integer. </li>
	<li>The calculated value of each term CX^E also fits in a 32-bit signed integer.</li>
</ol>

### 출력 

 <p>For each test case, print the value of polynomial evaluation. The result will fit in a 32-bit signed integer. Follow the output format below. </p>

