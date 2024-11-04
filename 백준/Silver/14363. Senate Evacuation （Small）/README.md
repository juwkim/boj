# [Silver III] Senate Evacuation (Small) - 14363 

[문제 링크](https://www.acmicpc.net/problem/14363) 

### 성능 요약

메모리: 108080 KB, 시간: 116 ms

### 분류

브루트포스 알고리즘, 자료 구조, 그리디 알고리즘, 우선순위 큐

### 제출 일자

2024년 2월 15일 11:35:41

### 문제 설명

<p>A small fire started in the senate room, and it needs to be evacuated!</p>

<p>There are some senators in the senate room, each of whom belongs to of one of N political parties. Those parties are named after the first N (uppercase) letters of the English alphabet.</p>

<p>The emergency door is wide enough for up to two senators, so in each step of the evacuation, you may choose to remove either one or two senators from the room.</p>

<p>The senate rules indicate the senators in the room may vote on any bill at any time, even in the middle of an evacuation! So, the senators must be evacuated in a way that ensures that no party ever has an absolute majority. That is, it can never be the case after any evacuation step that more than half of the senators in the senate room belong to the same party.</p>

<p>Can you construct an evacuation plan? The senate is counting on you!</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of two lines. The first line contains a single integer N, the number of parties. The second line contains N integers, P<sub>1</sub>, P<sub>2</sub>, ..., P<sub>N</sub>, where P<sub>i</sub> represents the number of senators of the party named after the i-th letter of the alphabet.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ T ≤ 50.</li>
	<li>No party will have an absolute majority before the start of the evacuation.</li>
	<li>1 ≤ P<sub>i</sub> ≤ 1000, for all i.</li>
	<li>2 ≤ N ≤ 3.</li>
	<li>sum of all P<sub>i</sub> ≤ 9.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the evacuation plan. The plan must be a space-separated list of instructions, in the order in which they are to be carried out, where each instruction is either one or two characters, representing the parties of the senators to evacuate in each step.</p>

<p>It is guaranteed that at least one valid evacuation plan will exist. If multiple evacuation plans are valid, you may output any of them.</p>

