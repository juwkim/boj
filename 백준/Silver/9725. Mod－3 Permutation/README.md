# [Silver I] Mod-3 Permutation - 9725 

[문제 링크](https://www.acmicpc.net/problem/9725) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

애드 혹, 그리디 알고리즘

### 제출 일자

2025년 5월 4일 03:26:37

### 문제 설명

<p>We call a permutation p<sub>0</sub>, p<sub>1</sub>, ... , p<sub>n-1</sub> of a sequence of integers 0, 1, ... , n-1 mod-3 when for each index i, p<sub>i</sub> mod 3 = i mod 3. For example, the permutation 3,1,5,0,4,2 is mod-3 but the permutation 1,2,0,4,5,3 is not. You will be given a permutation. You are required to convert the given permutation into a mod-3 permutationin the minimum number of steps. For each step of the conversion, you need to select two different indices and swap their values. </p>

### 입력 

 <p>The first line has a positive integer T, T <= 100000, denoting the number of test cases. This is followed by each test case per line.</p>

<p>Each test case consists of two lines; the first line contains an integer n while the next line contains n integers separated by a single space. These n integers denotes a permutation of 0, 1, .., n-1. n is between 3 and 501 inclusive and is always a multiple of 3. </p>

### 출력 

 <p>For each test case, the output contains a line in the format Case #x: M, where x is the case number (starting from 1) and M is the minimum number of swaps required to convert the given permutation into a mod-3 permutation. </p>

