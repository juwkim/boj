# [Bronze I] Suspicious Event - 27622 

[문제 링크](https://www.acmicpc.net/problem/27622) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현(implementation)

### 문제 설명

<p>Before you graduate from your beloved university, you managed to secure an internship at a security company. Your first task is to analyze a login/logout sequence.</p>

<p>You are given a sequence of integers A that represents a record for users login/logout events in chronological order. Each user is represented by a unique integer. A positive integer x indicates a login event while a negative integer −x indicates a logout event by user |x|. You are guaranteed that there are no two events that are the same in A.</p>

<p>Once in a while, you might find from the record, a user who logs out even though that user has never been logged in previously. This can be due to a bug in the system or a hacking attempt. Nevertheless, it’s suspicious!</p>

<p>For example, let A<sub>1..8</sub> = (8, 3, −8, −6, 7, −3, −1, 6). There are 8 events from 5 distinct users (the users are 1, 3, 6, 7, and 8). The events are as follows.</p>

<ul>
	<li>A<sub>1</sub> = 8 → user 8 log in.</li>
	<li>A<sub>2</sub> = 3 → user 3 log in.</li>
	<li>A<sub>3</sub> = −8 → user 8 log out.</li>
	<li>A<sub>4</sub> = −6 → user 6 log out – suspicious event! (user 6 has not logged in)</li>
	<li>A<sub>5</sub> = 7 → user 7 log in.</li>
	<li>A<sub>6</sub> = −3 → user 3 log out.</li>
	<li>A<sub>7</sub> = −1 → user 1 log out – suspicious event! (user 1 has not logged in)</li>
	<li>A<sub>8</sub> = 6 → user 6 log in.</li>
</ul>

<p>In total, there are 2 suspicious logout events, i.e. A<sub>4</sub> = −6 and A<sub>7</sub> = −1. Note that although user 6 logs in at A<sub>8</sub>, he has not logged in when he logs out at A<sub>4</sub>.</p>

<p>Your task in this problem is to count how many logout suspicious events are there given the login/logout record.</p>

### 입력 

 <p>Input begins with a line containing an integer N (1 ≤ N ≤ 1000) representing the number of events in the given record. The next line contains N integers A<sub>i</sub> (−1000 ≤ A<sub>i</sub> ≤ 1000; A<sub>i</sub> ≠ 0) each representing an event in chronological order. It is guaranteed that all integers in A are distinct.</p>

### 출력 

 <p>Output contains an integer in a line representing the number of suspicious logout events.</p>

