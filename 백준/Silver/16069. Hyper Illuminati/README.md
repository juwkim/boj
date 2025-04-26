# [Silver I] Hyper Illuminati - 16069 

[문제 링크](https://www.acmicpc.net/problem/16069) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

브루트포스 알고리즘, 수학

### 제출 일자

2025년 4월 26일 20:02:03

### 문제 설명

<p>Once again the time dawns to demonstrate the sheer power of the Illuminati. To do so, it was decided to build an n-dimensional hyper-step pyramid using n-dimensional blocks:</p>

<ul>
	<li>All the steps of the pyramid are n-dimensional hyper-cuboids.</li>
	<li>Every step has a height of exactly 1 block in the n-th dimension.</li>
	<li>The pyramid has s steps and the base step is s blocks long in every other of the n − 1 dimensions.</li>
	<li>Every subsequent higher step is 1 block shorter in each of the n − 1 dimensions than the step below it.</li>
	<li>The top step is exactly 1 block.</li>
</ul>

<p>To prove their might even further the Illuminati leaders have decided to add two more requirements:</p>

<ul>
	<li>n must be at least 3.</li>
	<li>The number of blocks used to build the pyramid must be a meaningful number.</li>
</ul>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/979cebbd-3373-4509-a764-883772ca7190/-/preview/" style="width: 323px; height: 199px;"></p>

<p style="text-align: center;">Figure H.1: A 3-dimensional hyper pyramid with 3 steps consisting of 14 blocks in total.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>one line with a single integer m (1 ≤ m ≤ 10<sup>16</sup>) . This integer is the meaningful number the leaders have chosen.</li>
</ul>

### 출력 

 <p>If a hyper-step pyramid matching all the requirements exists, output a single line with two integers n and s, the dimension of the pyramid and its number of steps. If none exists, output impossible. If multiple solutions exist, any will be accepted.</p>

