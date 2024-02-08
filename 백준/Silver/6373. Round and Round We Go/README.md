# [Silver III] Round and Round We Go - 6373 

[문제 링크](https://www.acmicpc.net/problem/6373) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

임의 정밀도 / 큰 수 연산, 사칙연산, 구현, 수학, 시뮬레이션, 문자열

### 제출 일자

2024년 2월 9일 01:01:54

### 문제 설명

<p>A cyclic number is an integer n digits in length which, when multiplied by any integer from 1 to n, yields a “cycle” of the digits of the original number. That is, if you consider the number after the last digit to “wrap around” back to the first digit, the sequence of digits in both numbers will be the same, though they may start at different positions.</p>

<p>For example, the number 142857 is cyclic, as illustrated by the following table:</p>

<ul>
	<li>142857 × 1 = 142857</li>
	<li>142857 × 2 = 285714</li>
	<li>142857 × 3 = 428571</li>
	<li>142857 × 4 = 571428</li>
	<li>142857 × 5 = 714285</li>
	<li>142857 × 6 = 857142</li>
</ul>

<p>Write a program which will determine whether or not numbers are cyclic.</p>

### 입력 

 <p>The input file is a list of integers from 2 to 60 digits in length. (Note that preceding zeros should not be removed, they are considered part of the number and count in determining n. Thus, “01” is a two-digit number, distinct from “1” which is a one-digit number.)</p>

### 출력 

 <p>For each input integer, write a line in the output indicating whether or not it is cyclic.</p>

