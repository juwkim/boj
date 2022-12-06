# [Bronze III] Math Tutoring - 9299 

[문제 링크](https://www.acmicpc.net/problem/9299) 

### 성능 요약

메모리: 123620 KB, 시간: 252 ms

### 분류

미적분학(calculus), 구현(implementation), 수학(math)

### 문제 설명

<p>You are helping a friend with the rule for taking the derivative of a polynomial, but he just can’t seem to get it! You’ve gone over many examples, and finally you decide to just write a program to compute the derivatives for him.</p>

<p>Recall that a polynomial of the form:</p>

<p style="text-align: center;">a<sub>n</sub>x<sup>n</sup> + a<sub>n−1</sub>x<sup>n−1</sup> + . . . + a<sub>2</sub>x<sup>2</sup> + a<sub>1</sub>x + a<sub>0</sub></p>

<p>has as its derivative:</p>

<p style="text-align: center;">na<sub>n</sub>x<sup>n−1</sup> + (n − 1)a<sub>n−1</sub>x<sup>n−2</sup> + . . . + 2a<sub>2</sub>x + a<sub>1</sub></p>

<p>For example, the derivative of 2x<sup>3</sup> − x + 3 is 6x<sup>2</sup> − 1. Likewise, the derivatave of 3x<sup>4</sup> + 2x<sup>3</sup> + 7x<sup>2</sup> + 5x + 7 is 12x<sup>3</sup> + 6x<sup>2</sup> + 14x + 5.</p>

<p>Given a polynomial, provide the derivative. We are only using polynomials of the form presented here.</p>

### 입력 

 <p>The first line of input is the number of test cases that follow.</p>

<p>Each input case appears on a single line, and will start with a single integer, n (1 ≤ n ≤ 100), which is the highest exponent of the polynomial. n + 1 values will follow, which are the coefficients of the terms x<sup>n</sup> down to x<sup>0</sup> = 1, respectively. All coefficients will be integers between -1000 and 1000, inclusive. The highest exponent will always be positive. All numbers will be separated by a single space.</p>

### 출력 

 <p>For each case, output the line “Case x:” where x is the case number, on a single line. The output polynomial is to be formatted in the same manner as the input: the first value being the highest polynomial, and the successive values being the coefficients for the individual terms. Each output case should be on one line, with the values separated by one space.</p>

