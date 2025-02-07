# [Silver II] Antiarithmetic? - 4304 

[문제 링크](https://www.acmicpc.net/problem/4304) 

### 성능 요약

메모리: 111180 KB, 시간: 256 ms

### 분류

브루트포스 알고리즘, 수학

### 제출 일자

2025년 2월 7일 16:05:06

### 문제 설명

<p>A permutation of n is a bijective function of the initial n natural numbers: 0, 1, ... n-1. A permutation p is called antiarithmetic if there is no subsequence of it forming an arithmetic progression of length bigger than 2, i.e. there are no three indices 0 ≤ i < j < k < n such that (pi , pj , pk) forms an arithmetic progression.</p>

<p>For example, the sequence (2, 0, 1, 4, 3) is an antiarithmetic permutation of 5. The sequence (0, 5, 4, 3, 1, 2) is not an antiarithmetic permutation as its first, fifth and sixth term (0, 1, 2) form an arithmetic progression; and so do its second, forth and fifth term (5, 3, 1).</p>

<p>Your task is to check whether a given permutation of n is antiarithmetic.</p>

### 입력 

 <p>There are several test cases, followed by a line containing 0. Each test case is a line of the input file containing a natural number 3 ≤ n ≤ 10000 followed by a colon and then followed by n distinct numbers separated by whitespace. All n numbers are natural numbers smaller than n.</p>

### 출력 

 <p>For each test case output one line with yes or no stating whether the permutation is antiarithmetic or not.</p>

