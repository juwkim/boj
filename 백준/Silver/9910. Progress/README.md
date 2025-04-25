# [Silver II] Progress - 9910 

[문제 링크](https://www.acmicpc.net/problem/9910) 

### 성능 요약

메모리: 109544 KB, 시간: 100 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 4월 25일 19:29:59

### 문제 설명

<p>An arithmetic progression is an ascending sequence a of n numbers a<sub>1</sub> < a<sub>2</sub> < ... < a<sub>n</sub> such that the difference of two consecutive elements is always the same.  Example: The sequence 11 < 21 < 31 < 41 < 51 is an arithmetic progression.  A subsequence of an ascending sequence a of n numbers is a sequence b of m numbers, where m ≤ n, such that every element of b occurs in a.  Example: The sequences 21 < 41 < 51, 11 < 41 and 11 < 21 < 31 < 41 < 51 are three subsequences of the sequence 11 < 21 < 31 < 41 < 51.</p>

<p>Given is an ascending sequence c of k numbers c<sub>1</sub> < c<sub>2</sub> < ... < c<sub>k</sub>, the task is to find the length of a longest arithmetic progression that is a subsequence of c.  Note that there may be more than one such longest arithmetic progression, but the length is unique.</p>

<p>Example: Let c be the sequence 1 < 2 < 4 < 5 < 7 < 8 < 9 < 11 < 13 < 14 < 15 < 16.  There are many arithmetic progressions that are subsequences of c, such as 2 < 4, 2 < 8 < 14, and 13 < 14 < 15 < 16.  The longest arithmetic progression that is a subsequence of c is 5 < 7 < 9 < 11 < 13 < 15, and therefore the answer is 6.</p>

<p>You can assume that the length of the sequence, k, is not smaller than 10 and not bigger than 500, and that the elements of the sequence are positive numbers smaller than 100000.</p>

### 입력 

 <p>The input consists of the following lines:</p>

<ol>
	<li>The first line contains an integer indicating the number k of elements of c.</li>
	<li>The second line consists of the ascending sequence c, where the elements are separated by spaces.</li>
</ol>

### 출력 

 <p>The output contains a single positive integer that indicates the length of the longest arithmetic progression that is a subsequence of c.</p>

