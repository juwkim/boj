# [Silver II] Atomic Computer - 11247 

[문제 링크](https://www.acmicpc.net/problem/11247) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

다이나믹 프로그래밍, 수학

### 제출 일자

2025년 2월 9일 00:04:47

### 문제 설명

<p>Mathematical calculation is no longer a problem because one particular professor has invented “Atomic Computer” that is 8,000,000,000 times faster than the normal computer.</p>

<p>This Atomic Computer store data in special kind of very expensive memory. This memory store information very similar to traditional binary computer. The only exception is that one bit in this memory can represent 3 different states. These 3 states represents value -1, 0 and 1 respectively. This professor use the amazing property of this memory to construct marvelous things. You, as a senior student, would like to do a senior project with him.</p>

<p>The professor has suggested basic usage of the Atomic Computer to you. You try to have the computer store a value 1 in the memory. You then realized that the computer might store the value 1 in various way, one possible way is as (1)<sub>2</sub> and another possible way is (1)(-1)<sub>2</sub></p>

<p>Write a program that read an integer value that you want to store in the memory and a number of bits in the memory. Calculate the number of all possible ways to store that number in the Atomic Computer.</p>

### 입력 

 <p>The first line of input contain one integer T that gives the number of test cases. For each test case, there will be one line of input containing two integer x<sub>i</sub> and y<sub>i</sub> where x<sub>i</sub> is the integer value we want to store in the memory and y<sub>i</sub> is the number of bits in the computer. (-2,000,000,000 ≤ x<sub>i</sub> ≤ 2,000,000,000 and 1 ≤ y<sub>i</sub> ≤ 20)</p>

### 출력 

 <p>There will be T lines of output. The ith line gives the number of all possible ways to store the integer x<sub>i</sub> using y<sub>i</sub> bits of memory.</p>

