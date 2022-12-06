# [Bronze II] Sales - 8912 

[문제 링크](https://www.acmicpc.net/problem/8912) 

### 성능 요약

메모리: 28776 KB, 시간: 1348 ms

### 분류

구현(implementation)

### 문제 설명

<p>Mr. Cooper, the CEO of CozyWalk Co., receives a report of daily sales every day since the company has been established. Starting from the second day since its establishment, on receiving the report, he compares it with each of the previous reports in order to calculate the number of previous days whose sales amounts are less than or equal to it. After obtaining the number of such days, he writes it in a list.</p>

<p>This problem can be stated more fomally as follows. Let A = (a<sub>1</sub>, a<sub>2</sub>, .., a<sub>n</sub>) denote the list of daily sales amounts. And let B = (b<sub>1</sub>, b<sub>2</sub>, ..., b<sub>n-1</sub>) be another integer list maintained by Mr. Cooper, each value representing the number of such previous days. On the i-th day (2 ≤ i ≤ n), he calculates b<sub>i-1</sub>, the number of aks such that a<sub>k</sub> ≤ a<sub>i</sub> (1 ≤ k < i).</p>

<p>For example, suppose that A = (20, 43, 57, 43, 20). For the fourth day's sales amount, a<sub>4</sub> = 43, the number of previous days whose sales amounts are less than or equal to it is 2 since a<sub>1</sub> ≤ a<sub>4</sub>, a<sub>2</sub> ≤ a<sub>4</sub>, and a<sub>3</sub> > a<sub>4</sub>. Therefore, b<sub>3</sub> = 2. Similarly, b<sub>1</sub>, b<sub>2</sub>, and b<sub>4</sub> can be obtained and it results in B = (1, 2, 2, 1).</p>

<p>Given an array of size n for the list of daily sales amounts, write a program that prints the sum of the n-1 integers in the list B.</p>

### 입력 

 <p>Your program is to read the input from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case starts with a line containing an integer n (2 ≤ n ≤ 1,000) , which represents the size of the list A. In the following line, n integers are given, each represents the daily sales amounts a<sub>i</sub> (1 ≤ a<sub>i</sub> ≤ 5,000 and 1 ≤ i ≤ n) for the test case.</p>

### 출력 

 <p>Your program is to write to standard output. For each test case, print the sum of the n-1 integers in the list B which is obtained from the list A .</p>

