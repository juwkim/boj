# [Silver IV] Electricity - 5723 

[문제 링크](https://www.acmicpc.net/problem/5723) 

### 성능 요약

메모리: 124360 KB, 시간: 344 ms

### 분류

구현

### 문제 설명

<p>Martin and Isa stopped playing crazy games and finally got married. It’s good news! They’re pursuing a new life of happiness for both and, moreover, they’re moving to a new house in a remote place, bought with most of their savings.</p>

<p>Life is different in this new place. In particular, electricity is very expensive, and they want to keep everything under control. That’s why Martin proposed to keep a daily record of how much electricity has been consumed in the house. They have an electricity meter, which displays a number with the amount of KWh (kilowatt-hour) that has been consumed since their arrival.</p>

<p>At the beginning of each day they consult the electricity meter, and write down the consumption. Some days Martin does it, and some days Isa does. That way, they will be able to look at the differences of consumption between consecutive days and know how much has been consumed.</p>

<p>But some days they simply forget to do it, so, after a long time, their register is now incomplete. They have a list of dates and consumptions, but not all of the dates are consecutive. They want to take into account only the days for which the consumption can be precisely determined, and they need help.</p>

### 입력 

 <p>The input contains several test cases. The first line of each test case contains one integer N indicating the number of measures that have been taken (2 ≤ N ≤ 10<sup>3</sup>). Each of the N following lines contains four integers D, M, Y and C, separated by single spaces, indicating respectively the day (1 ≤ D ≤ 31), month (1 ≤ M ≤ 12), year (1900 ≤ Y ≤ 2100), and consumption (0 ≤ C ≤ 10<sup>6</sup>) read at the beginning of that day. These N lines are increasingly ordered by date, and may include leap years. The sequence of consumptions is strictly increasing (this is, no two different readings have the same number). You may assume that D, M and Y represent a valid date.</p>

<p>Remember that a year is a leap year if it is divisible by 4 and not by 100, or well, if the year is divisible by 400.</p>

<p>The end of input is indicated by a line containing only one zero.</p>

<p>The input must be read from standard input.</p>

### 출력 

 <p>For each test case in the input, your program must print a single line containing two integers separated by a single space: the number of days for which a consumption can be precisely determined, and the sum of the consumptions for those days.</p>

<p>The output must be written to standard output.</p>

