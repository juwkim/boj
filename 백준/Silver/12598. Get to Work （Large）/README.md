# [Silver IV] Get to Work (Large) - 12598 

[문제 링크](https://www.acmicpc.net/problem/12598) 

### 성능 요약

메모리: 115444 KB, 시간: 204 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation), 정렬(sorting)

### 문제 설명

<p>You work for a company that has <strong>E</strong> employees working in town <strong>T</strong>. There are <strong>N</strong> towns in the area where the employees live. You want to ensure that everyone will be able to make it to work. Some of the employees are drivers and can drive <strong>P</strong> passengers. A capacity of <code>P == 1</code> indicates that the driver can only transport themselves to work. You want to ensure that everyone will be able to make it to work and you would like to minimize the number of cars on the road.</p>

<p>You want to calculate the number of cars on the road, with these requirements:</p>

<ul>
	<li>Every employee can get to town <strong>T</strong>.</li>
	<li>The only way an employee may travel between towns is in a car belonging to an employee.</li>
	<li>Employees can only take rides from other employees that live in the same town.</li>
	<li>The minimum number of cars is used.</li>
</ul>

<p>Find whether it is possible for everyone to make it to work, and if it is, how many cars will end up driving to the office.</p>

### 입력 

 <p>One line containing an integer <strong>C</strong>, the number of test cases in the input file.</p>

<p>For each test case there will be:</p>

<ul>
	<li>One line containing the integer <strong>N</strong>, the number of towns in your area and the integer <strong>T</strong>, the town where the office is located.</li>
	<li>One line containing the integer <strong>E</strong>, the number of employees.</li>
	<li><code>E</code> lines, one for each employee, each containing:
	<ul>
		<li>An integer H >= 1, the home town of the employee, followed by</li>
		<li>An integer P >= 0, the number of passengers they can drive. If the employee is not licensed to drive the number will be 0.</li>
	</ul>
	</li>
</ul>

<p>Limits</p>

<ul>
	<li>1 ≤ T ≤ N</li>
	<li>1 ≤ H ≤ N</li>
	<li>0 ≤ P ≤ 6</li>
	<li>C = 100</li>
	<li>1 ≤ N ≤ 100</li>
	<li>1 ≤ E ≤ 500</li>
</ul>

### 출력 

 <ul>
	<li><strong>C</strong> lines, one for each test case in the order they occur in the input file, each containing the string "Case #<strong>X</strong>: " where <strong>X</strong> is the number of the test case, starting from 1, followed by:
	<ul>
		<li>The string <strong>IMPOSSIBLE</strong>, if there are not enough drivers for everyone to commute; <strong>OR</strong></li>
		<li><strong>N</strong> space-separated integers, one for each town from <strong>1</strong> to <strong>N</strong>, which indicate the number of vehicles commuting from the town.</li>
	</ul>
	</li>
</ul>

