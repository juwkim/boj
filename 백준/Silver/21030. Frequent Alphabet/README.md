# [Silver V] Frequent Alphabet - 21030 

[문제 링크](https://www.acmicpc.net/problem/21030) 

### 성능 요약

메모리: 115172 KB, 시간: 128 ms

### 분류

문자열(string)

### 문제 설명

<p>Your social media account has just been hacked, and you are advised to change your password. You have two favorite strings S and T, each contains exactly N lowercase alphabets. You want the new password to be some combinations of these two strings. Specifically, the new password P should contain N alphabets such that the i<sup>th</sup> character of P is either the i<sup>th</sup> character of S or the i<sup>th</sup> character of T.</p>

<p>For example, let S = “<code>icyz</code>” and T = “<code>ixpc</code>”. There are 8 different possible new passwords which you can choose: “<code>icyz</code>”, “<code>icyc</code>”, “<code>icpz</code>”, “<code>icpc</code>”, “<code>ixyz</code>”, “<code>ixyc</code>”, “<code>ixpz</code>”, and “<code>ixpc</code>”.</p>

<p>The score of a password P is defined as the number of occurences of the most frequent alphabet in P. For example, let P = “<code>icpc</code>”. The password “<code>icpc</code>” has one occurence of ‘<code>i</code>’, two occurences of ‘<code>c</code>’, and one occurence of ‘<code>p</code>’. The most frequent alphabet in P is ‘<code>c</code>’ with the number of occurences of 2. Therefore, the score of “<code>icpc</code>” is 2.</p>

<p>Given two strings S and T, your task is to find the highest score you can get for your new password.</p>

### 입력 

 <p>Input begins with a line containing an integer: N (1 ≤ N ≤ 100 000) representing the length of the password. The next line contains a string S containing N lowercase alphabets representing your first favorite string. The next line contains a string T containing N lowercase alphabets representing your second favorite string.</p>

### 출력 

 <p>Output in a line an integer representing the highest score you can get for your new password.</p>

