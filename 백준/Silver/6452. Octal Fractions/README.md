# [Silver III] Octal Fractions - 6452 

[문제 링크](https://www.acmicpc.net/problem/6452) 

### 성능 요약

메모리: 127776 KB, 시간: 284 ms

### 분류

수학, 정수론

### 제출 일자

2024년 4월 13일 10:01:08

### 문제 설명

<p>Fractions in octal (base 8) notation can be expressed exactly in decimal notation. For example, 0.75 in octal is 0.963125 (7/8 + 5/64) in decimal. All octal numbers of n digits to the right of the octal point can be expressed in no more than 3n decimal digits to the right of the decimal point.</p>

<p>Write a program to convert octal numerals between 0 and 1, inclusive, into equivalent decimal numerals.</p>

### 입력 

 <p>The input to your program will consist of octal numbers, one per line, to be converted. Each input number has the form 0.d<sub>1</sub>d<sub>2</sub>d<sub>3</sub>...d<sub>k</sub>, where the di are octal digits (0..7). There is no limit on k.</p>

### 출력 

 <p>Your output will consist of a sequence of lines of the form</p>

<pre>.d<sub>1</sub>d<sub>2</sub>d<sub>3</sub>...d<sub>k</sub> [8] = 0.D<sub>1</sub>D<sub>2</sub>D<sub>3</sub>...D<sub>m</sub> [10]</pre>

<p>where the left side is the input (in octal), and the right hand side the decimal (base 10) equivalent. There must be no trailing zeros, i.e. D<sub>m</sub> is not equal to 0.</p>

