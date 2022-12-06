# [Bronze II] Hailstone Sequences - 5679 

[문제 링크](https://www.acmicpc.net/problem/5679) 

### 성능 요약

메모리: 30840 KB, 시간: 120 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>Consider the sequence formed by starting from a positive integer h<sub>0</sub> and iterating with n = 1, 2, ... the following definition until h<sub>n</sub> = 1:</p>

<ul>
	<li>h<sub>n</sub> = h<sub>n-1</sub> / 2 (if h<sub>n-1</sub> is even)</li>
	<li>h<sub>n</sub> = 3 × h<sub>n-1</sub> + 1 (if h<sub>n-1</sub> is odd)</li>
</ul>

<p>For instance, if we start with h<sub>0</sub> = 5 the following sequence is generated: 5, 16, 8, 4, 2, 1. If we start with h<sub>0</sub> = 11, the sequence generated is 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.</p>

<p>As you can see from these examples, the numbers go up and down, but eventually comes down to end in 1 (at least for all numbers that have ever been tried). These sequences are called Hailstone sequences because they are similar to the formation of hailstones, which get carried upward by the winds over and over again before they finally descend to the ground.</p>

<p>In this problem, given a positive integer, your task is to compute the highest number in the Hailstone sequence which starts with the given number.</p>

### 입력 

 <p>Each test case is described using a single line. The line contains an integer H representing the starting value to build the sequence (1 ≤ H ≤ 500).</p>

<p>The last test case is followed by a line containing one zero.</p>

### 출력 

 <p>For each test case output a line with an integer representing the highest number in the Hailstone sequence that starts with the given input value.</p>

