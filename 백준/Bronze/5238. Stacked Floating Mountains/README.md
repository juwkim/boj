# [Bronze II] Stacked Floating Mountains - 5238 

[문제 링크](https://www.acmicpc.net/problem/5238) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>The floating mountains of Pandora present a challenge for the human scientists, especially geologists and physicists, who have been trying to understand how such structures could exist. While exploring the mountains, the scientists stumbled across interesting stacked floating mountain structures, where different mountains appeared stacked above one other, with the larger mountains being higher up in the stack. The scientists were able to calculate the size of each mountain, and they made an interesting observation: that the sizes of the mountains formed a (generalized) Fibbonacci sequence.</p>

<p>A sequence of numbers: x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>, is called a generalized Fibbonacci sequence if, for all i > 2,</p>

<p style="text-align: center;">x<sub>i</sub> = x<sub>i−1</sub> + x<sub>i−2</sub></p>

<p>The standard Fibbonacci sequence is simply a generalized Fibbonacci sequence with x<sub>1</sub> = x<sub>2</sub> = 1.</p>

<p>An example of generalized Fibbonacci sequence is: 2, 5, 7, 12, 19, ...</p>

<p>Your goal is to help the scientists verify this conjecture. Specifically, you are to write a program that, given a sequence of numbers, decides whether the sequence is a generalized Fibbonacci sequence or not.</p>

### 입력 

 <p>The first line in the test data file contains the number of test cases, n. After that, each line contains one test case. The test case begins with the number of elements in the sequence, k, and then we have k numbers which form the sequence. Assume all numbers are ≥ 0, and that the numbers are all < 2<sup>30</sup>.</p>

### 출력 

 <p>For each test case, you are to output “YES” (if the sequence is a generalized Fibbonacci sequence) or “NO” (if it is not).</p>

