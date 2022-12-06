# [Bronze III] Simplified Calendar System - 25774 

[문제 링크](https://www.acmicpc.net/problem/25774) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Consider a simplified calendar system where each year is 12 months and each month is 30 days, i.e., each year is 360 days. This sure makes the math easy, or does it?</p>

<p>Given a date and what day of the week it is, determine what day of the week a second date is. The second date will be after (timewise) the first date.</p>

### 입력 

 <p>There are two input lines. The first input line contains four integers:</p>

<ul>
	<li>d (1 ≤ d ≤ 30), providing what day of the month the first date is,</li>
	<li>m (1 ≤ m ≤ 12), providing what month of the year the first date is,</li>
	<li>y (1000 ≤ y ≤ 2999), providing what year the first date is, and</li>
	<li>n (1 ≤ n ≤ 7), providing what day of the week the given date is (1 represents Sunday, 2 represents Monday, …, 7 represents Saturday).</li>
</ul>

<p>The second input line provides the second date; it contains three integers (similar to the first three integers of the first input line). Again, the second date will be later than the first date (timewise).</p>

### 출력 

 <p>Print an integer (between 1 and 7, inclusive) indicating what day of the week the second date is.</p>

