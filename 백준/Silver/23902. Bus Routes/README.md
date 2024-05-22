# [Silver III] Bus Routes - 23902 

[문제 링크](https://www.acmicpc.net/problem/23902) 

### 성능 요약

메모리: 110404 KB, 시간: 124 ms

### 분류

그리디 알고리즘

### 제출 일자

2024년 5월 23일 02:46:35

### 문제 설명

<p>Bucket is planning to make a very long journey across the countryside by bus. Her journey consists of <b>N</b> bus routes, numbered from 1 to <b>N</b> in the order she must take them. The buses themselves are very fast, but do not run often. The i-th bus route only runs every <b>X<sub>i</sub></b> days.</p>

<p>More specifically, she can only take the i-th bus on day <b>X<sub>i</sub></b>, 2<b>X<sub>i</sub></b>, 3<b>X<sub>i</sub></b> and so on. Since the buses are very fast, she can take multiple buses on the same day.</p>

<p>Bucket must finish her journey by day <b>D</b>, but she would like to start the journey as late as possible. What is the latest day she could take the first bus, and still finish her journey by day <b>D</b>?</p>

<p>It is guaranteed that it is possible for Bucket to finish her journey by day <b>D</b>.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow. Each test case begins with a line containing the two integers <b>N</b> and <b>D</b>. Then, another line follows containing <b>N</b> integers, the i-th one is <b>X<sub>i</sub></b>.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the latest day she could take the first bus, and still finish her journey by day <b>D</b>.</p>

