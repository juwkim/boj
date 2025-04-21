# [Silver I] Pretty Average Primes - 17014 

[문제 링크](https://www.acmicpc.net/problem/17014) 

### 성능 요약

메모리: 142016 KB, 시간: 196 ms

### 분류

수학, 정수론, 소수 판정, 에라토스테네스의 체

### 제출 일자

2025년 4월 21일 12:42:47

### 문제 설명

<p>For various given positive integers N > 3, find two primes, A and B such that N is the average (mean) of A and B. That is, N should be equal to (A+B)/2.</p>

<p>Recall that a prime number is an integer P > 1 which is only divisible by 1 and P. For example, 2, 3, 5, 7, 11 are the first few primes, and 4, 6, 8, 9 are not prime numbers.</p>

### 입력 

 <p>The first line of input is the number T (1 ≤ T ≤ 1000), which is the number of test cases. Each of the next T lines contain one integer N<sub>i</sub> (4 ≤ N<sub>i</sub> ≤ 1000000, 1 ≤ i ≤ T).</p>

<p>For 6 of the available 15 marks, all N<sub>i</sub> < 1000.</p>

### 출력 

 <p>The output will consist of T lines. The i<sup>th</sup> line of output will contain two integers, A<sub>i</sub> and B<sub>i</sub>, separated by one space. It should be the case that N<sub>i</sub> = (A<sub>i</sub> + B<sub>i</sub>)/2 and that A<sub>i</sub> and B<sub>i</sub> are prime numbers.</p>

<p>If there are more than one possible A<sub>i</sub> and b<sub>i</sub> for a particular N<sub>i</sub>, output any such pair. The order of the pair A<sub>i</sub> and B<sub>i</sub> does not matter.</p>

<p>It will be the case that there will always be at least one set of values A<sub>i</sub> and B<sub>i</sub> for any given N<sub>i</sub>.</p>

