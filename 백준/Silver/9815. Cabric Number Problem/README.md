# [Silver V] Cabric Number Problem - 9815 

[문제 링크](https://www.acmicpc.net/problem/9815) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>If we input a number formed by 4 digits and these digits are not all of one same value, then it obeys the following law. Let us operate the number in the following way: </p>

<ol>
	<li>Arrange the digits in the way from bigger to smaller, such that it forms the biggest number that could be made from these 4 digits; </li>
	<li>Arrange the digits in the way from smaller to bigger, such that it forms the smallest number that could be made from these 4 digits (If there is 0 among these 4 digits, the number obtained may be less than four digits); </li>
	<li>Find the difference of these two numbers that is a new four digital number. </li>
</ol>

<p>Repeat the above process, we can finally always get the result 6174 or 0. </p>

<p>Please write the program to realize the above algorithm. </p>

### 입력 

 <p>Each case is a line of an integer.-1 denotes the end of input.</p>

### 출력 

 <p>If the integer is formed exactly by 4 digits and these digits are not all of one same value, then output from the program should show the procedure for finding this number and the number of repetition times. Otherwise output "No!!".</p>

