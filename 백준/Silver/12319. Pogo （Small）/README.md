# [Silver II] Pogo (Small) - 12319 

[문제 링크](https://www.acmicpc.net/problem/12319) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

해 구성하기, 그리디 알고리즘

### 제출 일자

2025년 1월 8일 04:40:59

### 문제 설명

<p>You have just got the best gift ever, a Pogo stick. The pogo stick is something you use to jump off the ground while standing on it. </p>

<p>This Pogo stick is a special one: the first jump will move you a distance of 1 unit, the second jump will move you 2 units, the third jump will move you 3 units and so on. You can jump in only four directions using this stick: north (increasing y), south (decreasing y), east (increasing x) or west (decreasing x). </p>

<p>Now you want to play a game in your backyard, which we model as an infinite plane. You are standing with your stick in at point (0, 0) and you want to go to point (X, Y). </p>

<p>The point (X, Y) will never be (0, 0), and it will always be reachable from your starting point. </p>

<p>Check the output section carefully, because the required outputs for the small and large datasets are not the same.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow, one per line. Each line consists of 2 integers separated by a single space, <strong>X</strong> and <strong>Y</strong>, the coordinates of the point you want to reach.</p>

<p>Limits</p>

<ul>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">T</strong><span style="line-height:1.6em"> ≤ 50.</span></li>
	<li>0 ≤ |<strong>X</strong>|, |<strong>Y</strong>| ≤ 100.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is a string represents the directions of the moves, for example if you are going to move north then south then east then west, this string should be NSEW. </p>

<p>For the small dataset, the output is considered correct if it does not take more than 500 moves to reach the destination in each test case. </p>

<p>For the large dataset, the output is considered correct if it reaches the destination point in the minimum possible number of moves. </p>

<p>If there are multiple correct solutions, print any of them.</p>

