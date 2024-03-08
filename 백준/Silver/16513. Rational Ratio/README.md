# [Silver III] Rational Ratio - 16513 

[문제 링크](https://www.acmicpc.net/problem/16513) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

사칙연산, 수학, 파싱, 문자열

### 제출 일자

2024년 3월 9일 06:23:18

### 문제 설명

<p>Every (positive) rational number can be expressed as a ratio of two (positive) integers. However, in decimal form, rational numbers often have an infinitely repeating pattern, e.g., 1/7 = 0.142857142857142857... A convenient way of writing this repeating pattern is to put a bar over the first occurrence of the repeating part, so 1/7 would be written:</p>

<p style="text-align: center;">0.<span style="text-decoration: overline;">142857</span>.</p>

<p>Given a rational number consisting of a series of digits, followed by a decimal point, followed by more digits, and then a number indicating how many of the rightmost digits repeat (i.e., the number of digits under the bar), your task is to find the ratio of two integers, in the most reduced form, that represent the same rational number. For example, for the input “0.142857 6” you should find 1/7.</p>

### 입력 

 <p>The input will be a single line with two numbers separated by one space. The first number will consist of 1 to 3 digits (0–9), followed by a decimal point, followed by 1 to 11 digits (0–9), representing the decimal form of the number, possibly with leading zeros. The second number will be a positive integer indicating how many of the rightmost digits of the preceding number repeat. The first number will always be greater than 0. The second number will never be less than 1 nor larger than the number of digits to the right of the decimal point.</p>

### 출력 

 <p>Print the corresponding fraction in its most reduced form, that is, the fraction with the smallest possible integer values in the numerator and denominator.</p>

