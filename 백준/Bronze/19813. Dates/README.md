# [Bronze II] Dates - 19813 

[문제 링크](https://www.acmicpc.net/problem/19813) 

### 성능 요약

메모리: 28932 KB, 시간: 1940 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>One of the problems in dates processing is that there are several formats of writing down dates.</p>

<p>Peter has the task to write a program that processes an array of texts. Some of them have Russian and European format "day.month.year", while others use American format  --- "month/day/year".</p>

<p>Here, year is a number from 1 to 9999, which may contain leading zeroes to get 2, 3 or 4 digits, month  --- number from 1 to 12, which may contain leading zero to get 2 digits, day  --- number from 1 to 31, which may contain leading zeros to get 2 digits. Dates can be incorrect (for example there can be "Since 2001 isn't a leap year, that's why 29.02.2001  --- incorrect date").</p>

<p>You've got an array of Peters' strings, which correspond to dates. Print each date in two formats: first as "<code>DD.MM.YYYY</code>', second as "<code>MM/DD/YYYY</code>".</p>

### 입력 

 <p>The first line of input contains one integer $n$ ($1 \le n \le 20\,000$).</p>

<p>Each of the following $n$ lines contain one date in format "<code>day.month.year</code>" or "<code>month/day/year</code>".</p>

### 출력 

 <p>Print $n$ lines. Each line should contain the date in two formats: first as "<code>DD.MM.YYYY</code>", second as "<code>MM/DD/YYYY</code>".</p>

