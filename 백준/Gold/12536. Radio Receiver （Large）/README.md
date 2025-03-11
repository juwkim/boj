# [Gold II] Radio Receiver (Large) - 12536 

[문제 링크](https://www.acmicpc.net/problem/12536) 

### 성능 요약

메모리: 111420 KB, 시간: 180 ms

### 분류

이분 탐색, 매개 변수 탐색, 정렬

### 제출 일자

2025년 3월 12일 01:38:46

### 문제 설명

<p>You have a radio receiver and want to receive <strong>N</strong> messages. Each message is transmitted at a predetermined time measured in seconds since the epoch. Also each message is transmitted from a predetermined position representing the displacement in meters from the origin (you are in 1-dimensional space). Your radio is capable of receiving any message that is transmitted no farther than <strong>D</strong> meters from your current position, where <strong>D</strong>is a nonnegative real number.</p>

<p>You can start at any position of your choice and move at the rate of at most one meter per second. The action of receiving a message itself takes no time. Your task is to find the smallest <strong>D</strong> that allows you to get all messages.</p>

### 입력 

 <p>The first line of input gives the number of test cases, <strong>C</strong>. <strong>C</strong> test cases follow. For each test case there will be:</p>

<ul>
	<li>One line containing the integer <strong>N</strong>, the number of messages.</li>
	<li><strong>N</strong> lines corresponding to the <strong>N</strong> messages where each of them contains 2 integers <strong>P</strong> and <strong>T</strong> separated by one space. <strong>P</strong> is the position where the message is transmitted from and <strong>T</strong> is the time when this message is transmitted (The messages will have distinct transmission times).</li>
</ul>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>C</strong> ≤ 100</li>
	<li>1 ≤ <strong>N</strong> ≤ 1000</li>
	<li>0 ≤ <strong>P</strong> ≤ 10<sup>9</sup></li>
	<li>0 ≤ <strong>T</strong> ≤ 10<sup>9</sup></li>
</ul>

<div> </div>

<p> </p>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>x</strong>: ", where <strong>x</strong> is the number of the test case, followed by the minimum value <strong>D</strong> that allows you to get all messages. Answers with a relative or absolute error of at most 10<sup>-9</sup> will be considered correct.</p>

