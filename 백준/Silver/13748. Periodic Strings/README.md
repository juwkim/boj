# [Silver V] Periodic Strings - 13748 

[문제 링크](https://www.acmicpc.net/problem/13748) 

### 성능 요약

메모리: 113248 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘(bruteforcing), 문자열(string)

### 문제 설명

<p>Define a k-periodic string as follows:</p>

<p>A string s is k-periodic if the length of the string |s| is a multiple of k, and if you chop the string up into |s|/k substrings of length k, then each of those substrings (except the first) is the same as the previous substring, but with its last character moved to the front.</p>

<p>For example, the following string is 3-periodic:</p>

<p>abccabbcaabc</p>

<p>The above string can break up into substrings abc, cab, bca, and abc, and each substring (except the first) is a right-rotation of the previous substring (abc→cab →bca →abc).</p>

<p>Given a string, determine the smallest k for which the string is k-periodic.</p>

### 입력 

 <p>Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. The single line of input contains a string s (1 ≤ |s| ≤ 100) consisting only of lowercase letters.</p>

### 출력 

 <p>Output the integer k, which is the smallest k for which the input string is k-periodic</p>

