# [Bronze II] Positive Con Sequences - 11517 

[문제 링크](https://www.acmicpc.net/problem/11517) 

### 성능 요약

메모리: 28776 KB, 시간: 188 ms

### 분류

브루트포스 알고리즘(bruteforcing), 많은 조건 분기(case_work), 수학(math)

### 문제 설명

<p>Your younger sister is studying for an upcoming standardized test in mathematics. She needs practice with the common style of problem in which the student is asked to fill in the missing value in a sequence of numbers.</p>

<p>The vast majority of these problems feature either arithmetic sequences (where each number in the sequence is formed by adding an integer constant to the prior number) or geometric sequences (where each number in the sequence is formed by multiplying the prior number by an integer constant).</p>

<p>Write a program that will help your sister practice on this style of problem by allowing her to check her answers on sample problems.</p>

### 입력 

 <p>Input will consist of one or more datasets.</p>

<p>Each dataset will be a single line containing 4 integers defining a sequence. One of these will be -1, denoting the missing value. The remainder will be positive integers in the range 1..10,000, inclusive. Other than the -1 placeholder value, the values will be in non-decreasing order.</p>

<p>End of input will be signaled by a line containing four -1 values.</p>

### 출력 

 <p>For each dataset, print one line of output.</p>

<p>If an integer in the range 1..10,000 inclusive exists that can be filled in to the missing value position to create an arithmetic or geometric sequence, print that missing value.</p>

<p>If there is no such positive integer, print -1.</p>

