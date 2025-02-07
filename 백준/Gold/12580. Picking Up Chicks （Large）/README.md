# [Gold IV] Picking Up Chicks (Large) - 12580 

[문제 링크](https://www.acmicpc.net/problem/12580) 

### 성능 요약

메모리: 109544 KB, 시간: 100 ms

### 분류

그리디 알고리즘

### 제출 일자

2025년 2월 7일 20:01:09

### 문제 설명

<p>A flock of chickens are running east along a straight, narrow road. Each one is running with its own constant speed. Whenever a chick catches up to the one in front of it, it has to slow down and follow at the speed of the other chick. You are in a mobile crane behind the flock, chasing the chicks towards the barn at the end of the road. The arm of the crane allows you to pick up any chick momentarily, let the chick behind it pass underneath and place the picked up chick back down. This operation takes no time and can only be performed on a pair of chicks that are immediately next to each other, even if 3 or more chicks are in a row, one after the other.</p>

<p>Given the initial locations (<strong>X<sub>i</sub></strong>) at time 0 and natural speeds (<strong>V<sub>i</sub></strong>) of the chicks, as well as the location of the barn (<strong>B</strong>), what is the minimum number of swaps you need to perform with your crane in order to have at least <strong>K</strong> of the <strong>N</strong> chicks arrive at the barn no later than time <strong>T</strong>?</p>

<p>You may think of the chicks as points moving along a line. Even if 3 or more chicks are at the same location, next to each other, picking up one of them will only let one of the other two pass through. Any swap is instantaneous, which means that you may perform multiple swaps at the same time, but each one will count as a separate swap.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>C</strong>.  <strong>C</strong> test cases follow. Each test case starts with 4 integers on a line -- <strong>N</strong>, <strong>K</strong>, <strong>B</strong> and <strong>T</strong>. The next line contains the <strong>N</strong> different integers <strong>X<sub>i</sub></strong>, in increasing order. The line after that contains the <strong>N</strong> integers <strong>V<sub>i</sub></strong>. All distances are in meters; all speeds are in meters per second; all times are in seconds.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>C</strong> ≤ 100;</li>
	<li>1 ≤ <strong>B</strong> ≤ 1,000,000,000;</li>
	<li>1 ≤ <strong>T</strong> ≤ 1,000;</li>
	<li>0 ≤ <strong>X<sub>i</sub></strong> < <strong>B</strong>;</li>
	<li>1 ≤ <strong>V<sub>i</sub></strong> ≤ 100;</li>
	<li>All the <strong>X<sub>i</sub></strong>'s will be distinct and in increasing order.</li>
	<li>1 ≤ <strong>N</strong> ≤ 50;</li>
	<li>0 ≤ <strong>K</strong> ≤ <strong>N</strong>;</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: <strong>S</strong>", where x is the case number (starting from 1) and <strong>S</strong> is the smallest number of required swaps, or the word "IMPOSSIBLE".</p>

