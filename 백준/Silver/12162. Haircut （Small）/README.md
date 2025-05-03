# [Silver I] Haircut (Small) - 12162 

[문제 링크](https://www.acmicpc.net/problem/12162) 

### 성능 요약

메모리: 110760 KB, 시간: 100 ms

### 분류

이분 탐색, 매개 변수 탐색

### 제출 일자

2025년 5월 3일 19:44:16

### 문제 설명

<p>You are waiting in a long line to get a haircut at a trendy barber shop. The shop has <strong>B</strong>barbers on duty, and they are numbered 1 through <strong>B</strong>. It always takes the <strong>k</strong>th barber exactly <strong>M<sub>k</sub></strong> minutes to cut a customer's hair, and a barber can only cut one customer's hair at a time. Once a barber finishes cutting hair, he is immediately free to help another customer.<br>
<br>
While the shop is open, the customer at the head of the queue always goes to the lowest-numbered barber who is available. When no barber is available, that customer waits until at least one becomes available.<br>
<br>
You are the <strong>N</strong>th person in line, and the shop has just opened. Which barber will cut your hair?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow; each consists of two lines. The first contains two space-separated integers <strong>B</strong> and <strong>N</strong> -- the number of barbers and your place in line. The customer at the head of the line is number 1, the next one is number 2, and so on. The second line contains <strong>M<sub>1</sub></strong>, <strong>M<sub>2</sub></strong>, ..., <strong>M<sub>B</sub></strong>.</p>

<div>
<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>N</strong> ≤ 10<sup>9</sup>.</li>
	<li>1 ≤ <strong>B</strong> ≤ 5.</li>
	<li>1 ≤ <strong>M<sub>k</sub></strong> ≤ 25.</li>
</ul>
</div>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the number of the barber who will cut your hair.</p>

