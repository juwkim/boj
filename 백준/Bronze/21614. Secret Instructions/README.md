# [Bronze III] Secret Instructions - 21614 

[문제 링크](https://www.acmicpc.net/problem/21614) 

### 성능 요약

메모리: 28776 KB, 시간: 84 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Professor Santos has decided to hide a secret formula for a new type of biofuel. She has, however, left a sequence of coded instructions for her assistant.</p>

<p>Each instruction is a sequence of five digits which represents a direction to turn and the number of steps to take.</p>

<p>The first two digits represent the direction to turn:</p>

<ul>
	<li>If their sum is odd, then the direction to turn is left.</li>
	<li>If their sum is even and not zero, then the direction to turn is right.</li>
	<li>If their sum is zero, then the direction to turn is the same as the previous instruction.</li>
</ul>

<p>The remaining three digits represent the number of steps to take which will always be at least 100.</p>

<p>Your job is to decode the instructions so the assistant can use them to find the secret formula.</p>

### 입력 

 <p>There will be at least two lines of input. Each line except the last line will contain exactly five digits representing an instruction. The first line will not begin with <code>00</code>. The last line will contain <code>99999</code> and no other line will contain <code>99999</code>.</p>

### 출력 

 <p>There must be one line of output for each line of input except the last line of input. These output lines correspond to the input lines (in order). Each output line gives the decoding of the corresponding instruction: either <code>right</code> or <code>left</code>, followed by a single space, followed by the number of steps to be taken in that direction.</p>

