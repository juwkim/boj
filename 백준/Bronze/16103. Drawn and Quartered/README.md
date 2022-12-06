# [Bronze II] Drawn and Quartered - 16103 

[문제 링크](https://www.acmicpc.net/problem/16103) 

### 성능 요약

메모리: 28968 KB, 시간: 64 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>You are playing a game which involves drawing and redrawing a string on a blackboard. You start with a string S of length N and perform a switcheroo on the string exactly K times. A switcheroo involves breaking S into quarters, and then moving the middle two quarters to the end of S without changing their relative order to each other. For example, say you start with aabbccdd. After a single switcheroo, the string would become aaddbbcc. After another switcheroo, you would have aaccddbb, and so on.</p>

<p>Given some starting string S and the number of times you should perform a switcheroo, what is the final state of the string?</p>

### 입력 

 <p>The input starts with a line containing two integers N (4 ≤ N ≤ 100 000), which is the length of the string, and K (1 ≤ K ≤ 10<sup>18</sup>), which is the number of times you should perform a switcheroo to S. It is guaranteed that N is a multiple of 4.</p>

<p>The second line contains S. The string S contains only lowercase letters and consists of exactly N characters.</p>

### 출력 

 <p>Display the string after performing K switcheroos.</p>

