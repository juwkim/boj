# [Bronze II] K-Goodness String - 22999 

[문제 링크](https://www.acmicpc.net/problem/22999) 

### 성능 요약

메모리: 31032 KB, 시간: 252 ms

### 분류

그리디 알고리즘(greedy), 문자열(string)

### 문제 설명

<p>Charles defines the goodness score of a string as the number of indices i such that S<sub>i</sub> ≠ S<sub>N−i+1</sub> where 1 ≤ i ≤ N/2 (1-indexed). For example, the string CABABC has a goodness score of 2 since S<sub>2</sub> ≠ S<sub>5</sub> and S<sub>3</sub> ≠ S<sub>4</sub>.</p>

<p>Charles gave Ada a string S of length N, consisting of uppercase letters and asked her to convert it into a string with a goodness score of K. In one operation, Ada can change any character in the string to any uppercase letter. Could you help Ada find the minimum number of operations required to transform the given string into a string with goodness score equal to K?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow.</p>

<p>The first line of each test case contains two integers N and K. The second line of each test case contains a string S of length N, consisting of uppercase letters.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where x is the test case number (starting from 1) and y is the minimum number of operations required to transform the given string S into a string with goodness score equal to K.</p>

