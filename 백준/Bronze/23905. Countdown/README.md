# [Bronze I] Countdown - 23905 

[문제 링크](https://www.acmicpc.net/problem/23905) 

### 성능 요약

메모리: 48144 KB, 시간: 376 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), KMP(kmp), 문자열(string)

### 문제 설명

<p>Avery has an array of <b>N</b> positive integers. The i-th integer of the array is <b>A<sub>i</sub></b>.</p>

<p>A contiguous subarray is an <i>m-countdown</i> if it is of length m and contains the integers m, m-1, m-2, ..., 2, 1 in that order. For example, <code>[3, 2, 1]</code> is a 3-countdown.</p>

<p>Can you help Avery count the number of <b>K</b>-countdowns in her array?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow. Each test case begins with a line containing the integers <b>N</b> and <b>K</b>. The second line contains <b>N</b> integers. The i-th integer is <b>A<sub>i</sub></b>.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the number of <b>K</b>-countdowns in her array.</p>

