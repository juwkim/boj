# [Bronze I] Increasing Substring - 23003 

[문제 링크](https://www.acmicpc.net/problem/23003) 

### 성능 요약

메모리: 36956 KB, 시간: 6148 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Your friend John just came back from vacation, and he would like to share with you a new property that he learned about strings.</p>

<p>John learned that a string C of length L consisting of uppercase English characters is strictly increasing if, for every pair of indices i and j such that 1 ≤ i < j ≤ L (1-based), the character at position i is smaller than the character at position j.</p>

<p>For example, the strings <code>ABC</code> and <code>ADF</code> are strictly increasing, however the strings <code>ACC</code> and <code>FDA</code> are not.</p>

<p>Now that he taught you this new exciting property, John decided to challenge you: given a string S of length N, you have to find out, for every position 1 ≤ i ≤ N, what is the length of the longest strictly increasing <a href="https://en.wikipedia.org/wiki/Substring">substring</a> that ends at position i.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow.</p>

<p>Each test case consists of two lines.</p>

<p>The first line contains an integer N, representing the length of the string.</p>

<p>The second line contains a string S of length N, consisting of uppercase English characters.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y<sub>1</sub> y<sub>2</sub> ... y<sub>n</sub></code>, where x is the test case number (starting from 1) and y<sub>i</sub> is the length of the longest strictly increasing substring that ends at position i.</p>

