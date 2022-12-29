# [Bronze I] Bovine Birthday - 27001 

[문제 링크](https://www.acmicpc.net/problem/27001) 

### 성능 요약

메모리: 126184 KB, 시간: 240 ms

### 분류

구현(implementation)

### 문제 설명

<p>Bessie asked her friend what day of the week she was born on. She knew that she was born on 2003 May 25, but didn't know what day it was. Write a program to help. Note that no cow was born earlier than the year 1800.</p>

<p>Facts to know:</p>

<ul>
	<li>January 1, 1900 was on a Monday.</li>
	<li>Lengths of months:</li>
</ul>

<pre>    Jan 31          May 31      Sep 30
    Feb 28 or 29    Jun 30      Oct 31
    Mar 31          Jul 31      Nov 30
    Apr 30          Aug 31      Dec 31
</pre>

<ul>
	<li>Every year evenly divisible by 4 is a leap year (1992 = 4*498 so 1992 will be a leap year, but the year 1990 is not a leap year).</li>
	<li>The rule above does not hold for century years. Century years divisible by 400 are leap years, all other are not. Thus, the century years 1700, 1800, 1900 and 2100 are not leap years, but 2000 is a leap year.</li>
</ul>

### 입력 

 <ul>
	<li>Line 1: Three space-separated integers that represent respectively the year, month (range 1..12), and day of a date.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single word that is the day of the week of the specified date (from the lower-case list: monday, tuesday, wednesday, thursday, friday, saturday, sunday).</li>
</ul>

