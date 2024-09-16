# [Bronze V] Christmas Tree Adapter - 32314 

[문제 링크](https://www.acmicpc.net/problem/32314) 

### 성능 요약

메모리: 108080 KB, 시간: 84 ms

### 분류

사칙연산, 수학

### 제출 일자

2024년 9월 16일 23:07:16

### 문제 설명

<p>Adapters (Transformers) are used with many devices (e.g., cell phones) to convert the 110 volt coming out of the outlet. The adapter for Dr. Orooji's Christmas Tree broke and Dr. O could not find that model online or in stores. The tree adapter was showing the “ampere” but the adapters online were showing “watt” and “volt”! So, Dr. O had to refer to the “Electricity 101 Book” to figure out what to buy:</p>

<ul>
	<li>Watt: measure of power</li>
	<li>Volt: measure of electric potential</li>
	<li>Ampere: measure of current</li>
	<li>watt = ampere × volt → ampere = watt / volt</li>
</ul>

<p>Given the ampere for Dr. O’s Christmas tree, and the watt and volt for a candidate adapter, determine if the candidate adapter will work with the tree. The adapter will work if its ampere is greater than or equal to the tree’s ampere.</p>

### 입력 

 <p>The first input line contains an integer, a (1 ≤ a ≤ 20), indicating the ampere for the Christmas tree. The second input line contains two integers: w (1 ≤ w ≤ 2000), indicating the watt for the candidate adapter and v (1 ≤ v ≤ 100), indicating the volt for the candidate adapter. Assume that the input will not result in fractions in divisions.</p>

### 출력 

 <p>Print 1 if the candidate adapter will work with the tree, 0 (zero) otherwise.</p>

