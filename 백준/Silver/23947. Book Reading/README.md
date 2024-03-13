# [Silver III] Book Reading - 23947 

[문제 링크](https://www.acmicpc.net/problem/23947) 

### 성능 요약

메모리: 222292 KB, 시간: 13888 ms

### 분류

수학

### 제출 일자

2024년 3월 13일 22:39:56

### 문제 설명

<p>Supervin is a librarian handling an ancient book with <b>N</b> pages, numbered from 1 to <b>N</b>. Since the book is too old, unfortunately <b>M</b> pages are torn out: page number <b>P<sub>1</sub></b>, <b>P<sub>2</sub></b>, ..., <b>P<sub>M</sub></b>.</p>

<p>Today, there are <b>Q</b> lazy readers who are interested in reading the ancient book. Since they are lazy, each reader will not necessarily read all the pages. Instead, the i-th reader will only read the pages that are numbered multiples of <b>R<sub>i</sub></b> and not torn out. Supervin would like to know the sum of the number of pages read by each reader.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow. Each test case begins with a line containing the three integers <b>N</b>, <b>M</b>, and <b>Q</b>, the number of pages in the book, the number of torn out pages in the book, and the number of readers, respectively. The second line contains <b>M</b> integers, the i-th of which is <b>P<sub>i</sub></b>. The third line contains <b>Q</b> integers, the i-th of which is <b>R<sub>i</sub></b>.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the total number of pages that will be read by all readers.</p>

