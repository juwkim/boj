# [Bronze I] Cataloguing numbers - 22244 

[문제 링크](https://www.acmicpc.net/problem/22244) 

### 성능 요약

메모리: 36396 KB, 시간: 96 ms

### 분류

구현(implementation), 파싱(parsing), 문자열(string)

### 문제 설명

<p>Whenever a new book arrives to the library of the Aglargond School of Magic, it gets a unique number, defined as follows:</p>

<ul>
	<li>First 7 digits represent the publishing date of the book: first 2 for day, next 2 for month and final 3 for year. Magicians use the same date system we use, including the rules regarding leap years (February has 28 days, unless the year is leap, when it has 29 days). If the three digit number for year is in the interval [000, 599] it represents one of the years [2000, 2599], otherwise it is from the interval [1600, 1999].</li>
	<li>Next digit describes author of the book: 1 if the author is a member of Aglargond School of Magic, 6 if the author is a member of other School of Magic and 9 otherwise.</li>
	<li>Final, 9th digit is the control digit, and it represents remainder after division by 7 of the sum of squares of the first 8 digits.</li>
</ul>

<p>Write a program that determines for 3 given number if they are correct cataloguing numbers.</p>

### 입력 

 <p>The input contains 3 lines. Each line contains one 9 digit number.</p>

### 출력 

 <p>The output has exactly 3 lines. In each line write only a single number 0 or 1, where 1 means that corresponding number from the input is correct, and 0 means that it is not correct.</p>

