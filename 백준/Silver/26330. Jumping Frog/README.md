# [Silver IV] Jumping Frog - 26330 

[문제 링크](https://www.acmicpc.net/problem/26330) 

### 성능 요약

메모리: 108080 KB, 시간: 88 ms

### 분류

수학

### 제출 일자

2024년 10월 15일 02:44:09

### 문제 설명

<p>A frog is located at the coordinate (x<sub>1</sub>,y<sub>1</sub>). He wants to go to the coordinate (x<sub>2</sub>,y<sub>2</sub>). He will perform one or more jumps to reach his destination. The rule of the jumping is as follows: Suppose the frog is located at the coordinate (x,y); then he can jump to the following four squares:</p>

<ol>
	<li>(x+y,y)</li>
	<li>(x-y,y)</li>
	<li>(x,y+x)</li>
	<li>(x,y-x)</li>
</ol>

<p>Given the coordinates (x<sub>1</sub>,y<sub>1</sub>) and (x<sub>2</sub>,y<sub>2</sub>), you need to determine if it is possible for the frog to travel from (x<sub>1</sub>,y<sub>1</sub>) to (x<sub>2</sub>,y<sub>2</sub>) through a series of jumps as described.</p>

### 입력 

 <p>The first input line contains an integer, n (1 ≤ n ≤ 100), indicating the number of test cases. Each test case consists of four integers (between -1,000,000,000 to +1,000,000,000 inclusive) separated by a single space denoting x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub> and y<sub>2</sub>, respectively.</p>

### 출력 

 <p>For each test case, output 1 if the frog can travel from (x<sub>1</sub>,y<sub>1</sub>) to (x<sub>2</sub>,y<sub>2</sub>) through a series of jumps as described or 0 otherwise.</p>

