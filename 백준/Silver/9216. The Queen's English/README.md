# [Silver IV] The Queen's English - 9216 

[문제 링크](https://www.acmicpc.net/problem/9216) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

사칙연산, 많은 조건 분기, 수학, 문자열

### 제출 일자

2025년 3월 11일 21:23:31

### 문제 설명

<p>In the official British written word format for numbers, tens and units are separated by a hyphen, and hundreds are separated from tens or units by the word "and". For example the number 123 would be written "one hundred and twenty-three". Large numbers are written in "triads" (groups of three digits) followed by the appropriate suffixes. For example 123456 is "one hundred and twenty-three thousand four hundred and fifty-six". As a special case, if the final triad of a large number has a tens or units component but no hundreds component, it needs an "and". Thus 1001001 is "one million one thousand and one".</p>

<p>Your task is to write a program that produces correct British written format for numbers of up to 9 digits (less than one "short" billion). Note that the correct spellings are "fifteen" and "fifty" ('f' instead of 'v'), and "forty" (no 'u').</p>

### 입력 

 <p>Input will consist of specifications for a series of tests. Information for each test is a single line containing an integer 1 <= n < 1000000000 that specifies the value to process. A line containing the value 0 terminates the input.</p>

### 출력 

 <p>Output should consist of one line for each test comprising the test number (formatted as shown) followed by a single space and the correct British word form of the input value, with a single space between words.</p>

