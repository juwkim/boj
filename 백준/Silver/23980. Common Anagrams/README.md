# [Silver III] Common Anagrams - 23980 

[문제 링크](https://www.acmicpc.net/problem/23980) 

### 성능 요약

메모리: 180356 KB, 시간: 504 ms

### 분류

브루트포스 알고리즘, 자료 구조, 해시를 사용한 집합과 맵

### 제출 일자

2024년 3월 19일 21:48:08

### 문제 설명

<p>Ayla has two strings <b>A</b> and <b>B</b>, each of length <b>L</b>, and each of which is made of uppercase English alphabet letters. She would like to know how many different substrings of <b>A</b> appear as anagrammatic substrings of <b>B</b>. More formally, she wants the number of different ordered tuples (i, j), with 0 ≤ i ≤ j < <b>L</b>, such that the i-th through j-th characters of <b>A</b> (inclusive) are the same multiset of characters as at least one contiguous substring of length (j - i + 1) in <b>B</b>.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow. Each test case starts with one line, containing <b>L</b>: the length of the string. The next two lines contain one string of <b>L</b> characters each: these are strings <b>A</b> and <b>B</b>, in that order.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the answer Ayla wants, as described above.</p>

