# [Silver V] gMatrix (Small) - 12064 

[문제 링크](https://www.acmicpc.net/problem/12064) 

### 성능 요약

메모리: 112140 KB, 시간: 336 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2023년 12월 19일 20:24:49

### 문제 설명

<p>You have a square <strong>N</strong> by <strong>N</strong> matrix M of nonnegative integers. We would like to make a list of the maximum values in every sub-matrix of size <strong>K</strong> by <strong>K</strong> within M, and then find the sum of those values together. (Note that the same entry of M might be the maximum value in more than one sub-matrix, in which case it will show up multiple times in the list.) Can you find that sum?</p>

<p>To simplify the input of the matrix, you are given two arrays <strong>A</strong> and <strong>B</strong> of length <strong>N</strong>, and two integers <strong>C</strong> and <strong>X</strong>. Then the entry M<sub>ij</sub> (for the ith row and jth column of the matrix) equals (<strong>A<sub>i</sub></strong>*i+<strong>B<sub>j</sub></strong>*j + <strong>C</strong>) mod <strong>X</strong>, where i and j are in the range [1, <strong>N</strong>].</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case begins with one line with four integers, <strong>N</strong>, <strong>K</strong>, <strong>C</strong> and <strong>X</strong>. Then there are two lines with <strong>N</strong> integers each, representing the arrays <strong>A</strong> and <strong>B</strong>.</p>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the sum of the maximum values in all sub-matrices of size <strong>K</strong> by <strong>K</strong>.</p>

