# [Bronze II] Divisibility by 11 - 6976 

[문제 링크](https://www.acmicpc.net/problem/6976) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

임의 정밀도 / 큰 수 연산(arbitrary_precision), 사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Write a program which accepts as input a positive integer and checks, using the algorithm described below, to see whether or not the integer is divisible by 11. This particular test for divisibility by 11 was given in 1897 by Charles L. Dodgson (Lewis Carroll).</p>

<p>Algorithm:</p>

<p>As long as the number being tested has more than two digits, form a new number by:</p>

<ul>
	<li>deleting the units digit</li>
	<li>subtracting the deleted digit from the shortened number</li>
</ul>

<p>The remaining number is divisible by 11 if and only if the original number is divisible by 11.</p>

### 입력 

 <p>As usual, the first number in the input indicates the number of positive integers that follow. Each positive integer has a maximum of 50 digits. You may assume no leading zeroes exist in the positive integers.</p>

### 출력 

 <p>For each positive integer in the input, the output consists of a series of numbers formed as a digit is deleted and subtracted, followed by a message indicating whether or not the original number is divisible by 11. Outputs for different positive integers are separated by blank lines.</p>

