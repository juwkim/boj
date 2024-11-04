# [Silver III] Not So Flat After All - 4891 

[문제 링크](https://www.acmicpc.net/problem/4891) 

### 성능 요약

메모리: 113680 KB, 시간: 164 ms

### 분류

수학

### 제출 일자

2024년 2월 16일 06:25:53

### 문제 설명

<p><img alt="" src="https://www.acmicpc.net/upload/images2/flat1.png" style="float:right; height:231px; width:237px">Any positive integer v can be written as p<sub>1</sub><sup>a<sub>1</sub></sup> ∗ p<sub>2</sub><sup>a<sub>2</sub></sup> ∗ . . . ∗ p<sub>n</sub><sup>a<sub>n</sub></sup> where p<sub>i</sub> is a prime number and a<sub>i</sub> ≥ 0. For example: 24 = 2<sup>3</sup> ∗ 3<sup>1</sup>.</p>

<p>Pick any two prime numbers p<sub>1</sub> and p<sub>2</sub> where p<sub>1</sub> ≠ p<sub>2</sub>. Imagine a two dimensional plane where the powers of p<sub>1</sub> are plotted on the x-axis and the powers of p<sub>2</sub> on the yaxis. Now any number that can be written as p<sub>1</sub><sup>a<sub>1</sub></sup> ∗ p<sub>2</sub><sup>a<sub>2</sub></sup> can be plotted on this plane at location (x, y) = (a<sub>1</sub>, a<sub>2</sub>). The figure on the right shows few examples where p<sub>1</sub> = 3 and p<sub>2</sub> = 2.</p>

<p>This idea can be extended for any N-Dimensional space where each of the N axes is assigned a unique prime number. Each N-Dimensional space has a unique set of primes.</p>

<p>We call such set the Space Identification Set or S for short. |S| (the ordinal of S) is N.</p>

<p>Any number that can be expressed as a multiplication of p<sub>i</sub> ∈ S (each raised to a power (a<sub>i</sub> ≥ 0) can be plotted in this |S|-Dimensional space. The figure at the bottom illustrates this idea for N = 3 and S = {2, 3, 7}. Needless to say, any number that can be plotted on space A can also be plotted on space B as long as S<sub>A</sub> ⊂ S<sub>B</sub>.</p>

<p>We define the distance between any two points in a given N-Dimensional space to be the sum of units traveled to get from one point to the other while following the grid lines (i.e. movement is always parallel to one of the axes.) For example, in the figure below, the distance between 168 and 882 is 4.</p>

<p>Given two positive integers, write a program that determines the minimum ordinal of a space where both numbers can be plotted in. The program also determines the distance between these two integers in that space.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images2/flat2.png" style="height:280px; width:400px"></p>

### 입력 

 <p>Your program will be tested on one or more test cases. Each test case is specified on a line with two positive integers (0 < A, B < 1, 000, 000) where A ∗ B > 1. The last line is made of two zeros.</p>

### 출력 

 <p>For each test case, print the following line:</p>

<pre>k. X:D</pre>

<p>Where k is the test case number (starting at one,) X is the minimum ordinal needed in a space that both A and B can be plotted in. D is the distance between these two points.</p>

