# [Bronze I] Fiborooji Sequence - 25802 

[문제 링크](https://www.acmicpc.net/problem/25802) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 비둘기집 원리(pigeonhole_principle)

### 문제 설명

<p>The Fibonacci sequence is defined as follows:</p>

<ul>
	<li>F<sub>0</sub> = 0</li>
	<li>F<sub>1</sub> = 1</li>
	<li>F<sub>n</sub> = F<sub>n–1</sub> + F<sub>n–2</sub> for n ≥ 2</li>
</ul>

<p>The numbers in this sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, … The Fibonacci sequence has many applications including Mathematics, Computer Science, Nature, Economics, Art, and Music.</p>

<p>The Fiborooji sequence is a simplified version of the Fibonacci sequence. The Fiborooji sequence starts with two single-digit, non-negative numbers (at least one of the two numbers being nonzero). Each subsequent number is the sum of its preceding two numbers (like the Fibonacci sequence) but the numbers always stay single digit. This is done by keeping only the rightmost digit if the sum of the preceding two numbers end up having two digits. For example, if we have 8 and 7, the sum will be 15 but the next number will be 5 and not 15. As another example, if we have 4 and 6, the sum will be 10 but the next number will be 0 and not 10. Here is the Fiborooji sequence if we start with 2 and 1: 2, 1, 3, 4, 7, 1, 8, 9, 7, 6, …</p>

<p>Applications of the Fiborooji sequence are being studied. One observation (discovery!) is that, regardless of the first two numbers (single digit) you start with, these two numbers will be repeated after a while which means the sequence will loop through the same numbers.</p>

<p>Given the first two single-digit numbers, find the length of the sequence when the starting two numbers repeat (i.e., reappear consecutively).</p>

### 입력 

 <p>There is only one input line; it contains two single-digit, non-negative numbers, at least one of the two numbers being non-zero.</p>

### 출력 

 <p>Print the length of the sequence when the starting two numbers repeat.</p>

