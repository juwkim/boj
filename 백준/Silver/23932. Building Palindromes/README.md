# [Silver I] Building Palindromes - 23932 

[문제 링크](https://www.acmicpc.net/problem/23932) 

### 성능 요약

메모리: 250564 KB, 시간: 972 ms

### 분류

애드 혹, 누적 합, 문자열

### 제출 일자

2025년 5월 10일 19:10:54

### 문제 설명

<p>Anna has a row of <b>N</b> blocks, each with exactly one letter from <code>A</code> to <code>Z</code> written on it. The blocks are numbered 1, 2, ..., <b>N</b> from left to right.</p>

<p>Today, she is learning about palindromes. A palindrome is a string that is the same written forwards and backwards. For example, <code>ANNA</code>, <code>RACECAR</code>, <code>AAA</code> and <code>X</code> are all palindromes, while <code>AB</code>, <code>FROG</code> and <code>YOYO</code> are not.</p>

<p>Bob wants to test how well Anna understands palindromes, and will ask her <b>Q</b> questions. The i-th question is: can Anna use all of the blocks numbered from <b>L<sub>i</sub></b> to <b>R<sub>i</sub></b>, inclusive, rearranging them if necessary, to form a palindrome? After each question, Anna puts the blocks back in their original positions.</p>

<p>Please help Anna by finding out how many of Bob's questions she can answer "yes" to.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow. Each test case starts with a line containing the two integers <b>N</b> and <b>Q</b>, the number of blocks and the number of questions, respectively. Then, another line follows, containing a string of <b>N</b> uppercase characters (<code>A</code> to <code>Z</code>). Then, <b>Q</b> lines follow. The i-th line contains the two integers <b>L<sub>i</sub></b> to <b>R<sub>i</sub></b>, describing the i-th question.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the number of questions Anna can answer "yes" to.</p>

