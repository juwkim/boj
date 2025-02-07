# [Silver II] fusnote - 3205 

[문제 링크](https://www.acmicpc.net/problem/3205) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

그리디 알고리즘, 구현, 시뮬레이션

### 제출 일자

2025년 2월 7일 21:54:41

### 문제 설명

<p>A text in a book consists of a sequence of lines. A line may contain references to footnotes. A footnote consists of one or more lines and it have to be printed together with its reference on the same page. Once a footnote is printed on a page, only another footnote may follow it on that page. A maximal number of lines that can be printed on one page is known. No page of a book may contain more than that number of lines, including footnotes.</p>

<p>Write a program that will compute the minimal number of pages a book can have.</p>

### 입력 

 <p>The first line of input contains two integers: N, a number of lines in a document (2 ≤ N ≤ 1000), and K, maximal number of lines a page of a book may contain (2 ≤ K ≤ 1000), separated by a space character.</p>

<p>The second line of input contains an integer F, 1 ≤ F ≤ 100, a number of footnotes in a book.</p>

<p>Each of the next F lines consists of two numbers, X and Y, separated by a space character, meaning that X-th line of the text has a reference to a footnote consisting of Y lines. Those footnotes descriptions will be sorted with respect to the lines where they are being referenced.</p>

<p>Note: Input data will be chosen so that a solution always exists.</p>

### 출력 

 <p>The first and only line of output should contain the minimal number of pages a book can have.</p>

