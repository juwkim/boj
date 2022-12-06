# [Bronze III] ID - 9907 

[문제 링크](https://www.acmicpc.net/problem/9907) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>The National Identity Card number of the city state of Eropagnis, NICE, consists of seven digits and a letter appended behind.  This letter is calculated from the digits using the Modulo Eleven method.</p>

<p>The steps involved in the computation are as follows:</p>

<ol>
	<li>Multiply each digit in the NICE number by its weight.  The weight of the first digit is 2, the weight of the second is 7, the third is 6, the fourth is 5, the fifth is 4, the sixth is 3, and the seventh is 2.</li>
	<li>Add all resulting products.</li>
	<li>Find the remainder of dividing the sum by 11.</li>
	<li>Map the remainder to a capital letter as follows: 0=J, 1=A, 2=B, 3=C, 4=D, 5=E, 6=F, 7=G, 8=H, 9=I, 10=Z.</li>
</ol>

<p>Example: Given the digits “6830907”, the sum is 2 × 6 + 7 × 8 + 6 × 3 + 5 × 0 + 4 × 9 + 3 × 0 + 2 × 7 = 12 + 56 + 18 + 0 + 36 + 0 + 14 = 136.  The number 136 has a remainder of 4, when divided by 11, and 4 is mapped to the letter “D”.  So, the actual NICE should be “6830907D”.</p>

<p>Write a program to read the seven digits of the NICE, and output the letter that needs to be appended.</p>

### 입력 

 <p>The input consists of seven digits of the NICE.</p>

### 출력 

 <p>The output contains a single capital character, which is the letter to be appended to form the correct NICE. </p>

