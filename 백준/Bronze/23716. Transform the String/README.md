# [Bronze II] Transform the String - 23716 

[문제 링크](https://www.acmicpc.net/problem/23716) 

### 성능 요약

메모리: 30840 KB, 시간: 24448 ms

### 분류

문자열(string)

### 문제 설명

<p>You are given a string $S$ which denotes a padlock consisting of lower case English letters. You are also given a string $F$ consisting of set of favorite lower case English letters. You are allowed to perform several operations on the padlock. In each operation, you can change one letter of the string to the one following it or preceding it in the alphabetical order. For example: for the letter <code>c</code>, you are allowed to change it to either <code>b</code> or <code>d</code> in an operation. The letters can be considered in a cyclic order, i.e., the preceding letter for letter <code>a</code> would be letter <code>z</code>. Similarly, the following letter for letter <code>z</code> would be letter <code>a</code>.</p>

<p>Your aim is to find the minimum number of operations that are required such that each letter in string $S$ after applying the operations, is present in string $F$.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, $T$. $T$ test cases follow.</p>

<p>Each test case consists of two lines.</p>

<p>The first line of each test case contains the string $S$.</p>

<p>The second line of each test case contains the string $F$.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where $x$ is the test case number (starting from 1) and $y$ is the minimum number of operations that are required such that each letter in string $S$ after applying the operations, is one of the characters in string $F$.</p>

