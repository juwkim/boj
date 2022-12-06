# [Bronze II] Millennium - 7015 

[문제 링크](https://www.acmicpc.net/problem/7015) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>A wise king declared a new calendar. "Tomorrow shall be the first day of the calendar, that is, the day 1 of the month 1 of the year 1. Each year consists of 10 months, from month 1 through month 10, and starts from a big month. A common year shall start with a big month, followed by small months and big months one after another. Therefore the first month is a big month, the second month is a small month, the third a big month, ..., and the 10th and last month a small one. A big month consists of 20 days and a small month consists of 19 days. However years which are multiples of three, that are year 3, year 6, year 9, and so on, shall consist of 10 big months and no small month."</p>

<p>Many years have passed since the calendar started to be used. For celebration of the millennium day (the year 1000, month 1, day 1), a royal lottery is going to be organized to send gifts to those who have lived as many days as the number chosen by the lottery. Write a program that helps people calculate the number of days since their birthdate to the millennium day.</p>

### 입력 

 <p>The input is formatted as follows.</p>

<pre>n
Y<sub>1</sub> M<sub>1</sub> D<sub>1</sub>
Y<sub>2</sub> M<sub>2</sub> D<sub>2</sub>
...
Y<sub>n</sub> M<sub>n</sub> D<sub>n</sub></pre>

<p>Here, the first line gives the number of datasets as a positive integer n, which is less than or equal to 100. It is followed by n datasets. Each dataset is formatted in a line and gives three positive integers, Y<sub>i</sub> (< 1000), M<sub>i</sub> (≤ 10), and D<sub>i</sub> (≤ 20), that correspond to the year, month and day, respectively, of a person's birthdate in the king's calendar. These three numbers are separated by a space.</p>

### 출력 

 <p>For the birthdate specified in each dataset, print in a line the number of days from the birthdate, inclusive, to the millennium day, exclusive. Output lines should not contain any character other than this number.</p>

