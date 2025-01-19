# [Bronze I] Hamzawy - 10692 

[문제 링크](https://www.acmicpc.net/problem/10692) 

### 성능 요약

메모리: 110796 KB, 시간: 100 ms

### 분류

브루트포스 알고리즘, KMP, 문자열

### 제출 일자

2025년 1월 19일 23:48:33

### 문제 설명

<p>Ahmed Samir Hamza (Hamzawy, a world finalist in the 2013 ICPC in St. Petersburg, a judge in the TCPC and an IBM software engineer), was in a programming interview lately and got asked a puzzling question that he could not answer, so he has asked you to help him to solve it.</p>

<p>Here is the question, given a string S of lowercase English characters, find a string which is a prefix of S, a suffix of S and a substring in S. The three occurrences of this string must not overlap. You should find the longest string which satisfies the above conditions.</p>

<p>A prefix of a string S is a string which can be obtained by deleting zero or more characters from the end of S. A suffix of a string S is a string which can be obtained by deleting zero or more characters from the start of S. A substring of a string S is a string which can be obtained by deleting zero or more characters from the end of S and zero or more characters from the start of S.</p>

### 입력 

 <p>Your program will be tested on one or more test cases. The first line of the input will be a single integer T, the number of test cases (1 ≤ T ≤ 100). Followed by T lines, each test case is a single line containing a non-empty string of lowercase English characters (from ‘a’ to ‘z’) containing no more than 106 characters.</p>

### 출력 

 <p>For each test case print a single line containing “Case n:” (without the quotes) where n is the test case number (starting from 1) followed by a space then the longest required string, if there is no such string, print -1 instead.</p>

