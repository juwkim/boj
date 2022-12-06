# [Bronze II] Anti-Arithmetic Permutation - 9703 

[문제 링크](https://www.acmicpc.net/problem/9703) 

### 성능 요약

메모리: 114976 KB, 시간: 136 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math)

### 문제 설명

<p>We call a permutation p<sub>0</sub>, p<sub>1</sub>, ... , p<sub>n-1</sub> of integers 0, 1, ... , n-1 anti-arithmetic, when there are no three-term arithmetic series in this permutation, i.e. there are no such three indices i < j < k, that integers p<sub>i</sub>, p<sub>j</sub>, p<sub>k</sub> make an arithmetic series. For example, the series of integers 3, 1, 0, 4, 2 is an anti-arithmetic permutation of integers 0, 1, 2, 3, 4. The series 0, 5, 4, 3, 1, 2 is not an antiarithmetic permutation, because its first, fifth and sixth term: 0, 1, 2 form an arithmetic series (as well as its second, fourth and fifth term: 5, 3, 1 and second third and fourth term: 5, 4, 3 form arithmetic series). Given a permutation of length n determine whether the given permutation is anti-arithmetic or not.</p>

### 입력 

 <p>Input starts with an integer T, the number of test cases.</p>

<p>Each test case consists of two lines. First line contains an integer n. Next line contains n integers separated by a single space. These n integers denotes a permutation of 0, 1, .., n-1. n is between 3 and 50 inclusive.</p>

### 출력 

 <p>For each test case, the output contains a line in the format Case #x: M, where x is the case number (starting from 1) and M is “YES” when the given permutation is anti-arithmetic or “NO” otherwise. Quotes are for clarity only. </p>

