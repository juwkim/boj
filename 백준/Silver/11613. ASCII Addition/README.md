# [Silver I] ASCII Addition - 11613 

[문제 링크](https://www.acmicpc.net/problem/11613) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

구현, 문자열

### 제출 일자

2025년 4월 10일 22:41:31

### 문제 설명

<p>Nowadays, there are smartphone applications that instantly translate text and even solve math problems if you just point your phone’s camera at them. Your job is to implement a much simpler functionality reminiscent of the past – add two integers written down as ASCII art.</p>

<p>An ASCII art is a matrix of characters, exactly 7 rows high, with each individual character either a dot or the lowercase letter x.</p>

<p>An expression of the form a + b is given, where both a and b are positive integers. The expression is converted into ASCII art by writing all the expression characters (the digits of a and b as well as the + sign) as 7 × 5 matrices, and concatenating the matrices together with a single column of dot characters between consecutive individual matrices. The exact matrices corresponding to the digits and the + sign are as folows:</p>

<pre>xxxxx  ....x  xxxxx  xxxxx  x...x  xxxxx  xxxxx  xxxxx  xxxxx  xxxxx  .....
x...x  ....x  ....x  ....x  x...x  x....  x....  ....x  x...x  x...x  ..x..
x...x  ....x  ....x  ....x  x...x  x....  x....  ....x  x...x  x...x  ..x..
x...x  ....x  xxxxx  xxxxx  xxxxx  xxxxx  xxxxx  ....x  xxxxx  xxxxx  xxxxx
x...x  ....x  x....  ....x  ....x  ....x  x...x  ....x  x...x  ....x  ..x..
x...x  ....x  x....  ....x  ....x  ....x  x...x  ....x  x...x  ....x  ..x..
xxxxx  ....x  xxxxx  xxxxx  ....x  xxxxx  xxxxx  ....x  xxxxx  xxxxx  .....
</pre>

<p>Given an ASCII art for an expression of the form a + b, find the result of the addition and write it out in the ASCII art form.</p>

### 입력 

 <p>Input consists of exactly 7 lines and contains the ASCII art for an expression of the form a + b, where both a and b are positive integers consisting of at most 9 decimal digits and written without leading zeros.</p>

### 출력 

 <p>Output 7 lines containing ASCII art corresponding to the result of the addition, without leading zeros.</p>

