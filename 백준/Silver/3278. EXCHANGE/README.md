# [Silver I] EXCHANGE - 3278 

[문제 링크](https://www.acmicpc.net/problem/3278) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 5월 11일 05:10:15

### 문제 설명

<p>Dave somehow acquired exchange rates of US dollar to German marks for several days in the future. Write a program that will suggest Dave when to buy or sell marks or dollars so that, starting with 100 marks he ends up with the highest possible amount of marks at the end of the last day.</p>

### 입력 

 <p>The first line of input file contains a natural number N, 1 ≤ N ≤ 100, the number of future days for which Dave knows exchange rates.</p>

<p>Each of N following lines contains two natural numbers B and S separated with a space, 100 ≤ B ≤ S ≤ 1000. The (i+1)th line describes the exchange rate of ith day in advance.</p>

<p>Those two numbers determine the exchange rate in the following way: B dollars can be bought for 100 marks, and 100 marks can be bought for S dollars.</p>

### 출력 

 <p>The first and only line of output file should contain a desired amount written to two decimal places.</p>

<p>Remark: Due to real arithmetic round off errors, results within error of 0.05 marks of correct value will be regarded as correct.</p>

