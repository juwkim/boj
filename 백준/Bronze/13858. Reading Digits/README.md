# [Bronze I] Reading Digits - 13858 

[문제 링크](https://www.acmicpc.net/problem/13858) 

### 성능 요약

메모리: 32560 KB, 시간: 192 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Bob has a very special way of encoding strings formed with digits. For instance, he encodes “1211” as: “one of one, one of two, two of one”, or, more precisely: “111221”. Bob’s encoding of the latter string is: “312211”. We call this a “two-times re-encoding of 1211”. Bob likes repeating this process several times.</p>

<p>You are given a string of digits which represents the “kth re-encoding of a string s”. The string s contains only non-zero digits (i.e. [1-9]). Also, it is not possible to have a sequence of more than 9 repeating digits in s. You must find the digit which lays on the pos position (starting from 0) of the string s.</p>

### 입력 

 <p>The input consists of two lines. The first line contains the values k and pos. The second line contains the k th re-encoding of s. We have 1 < k < 40, 0 ≤ pos ≤ 100000, and pos < |s| ≤ 200000.</p>

### 출력 

 <p>The output is the digit from position pos of s.</p>

