# [Bronze II] Bike Tour - 23901 

[문제 링크](https://www.acmicpc.net/problem/23901) 

### 성능 요약

메모리: 30840 KB, 시간: 80 ms

### 분류

구현(implementation)

### 문제 설명

<p>Li has planned a bike tour through the mountains of Switzerland. His tour consists of <b>N</b> checkpoints, numbered from 1 to <b>N</b> in the order he will visit them. The i-th checkpoint has a height of <b>H<sub>i</sub></b>.</p>

<p>A checkpoint is a <i>peak</i> if:</p>

<ul>
	<li>It is not the 1st checkpoint or the <b>N</b>-th checkpoint, and</li>
	<li>The height of the checkpoint is <i>strictly greater than</i> the checkpoint immediately before it and the checkpoint immediately after it.</li>
</ul>

<p>Please help Li find out the number of peaks.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow. Each test case begins with a line containing the integer <b>N</b>. The second line contains <b>N</b> integers. The i-th integer is <b>H<sub>i</sub></b>.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the number of peaks in Li's bike tour.</p>

