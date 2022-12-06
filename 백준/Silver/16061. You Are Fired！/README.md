# [Silver V] You Are Fired! - 16061 

[문제 링크](https://www.acmicpc.net/problem/16061) 

### 성능 요약

메모리: 118216 KB, 시간: 160 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting)

### 문제 설명

<p>The latest quarterly report of the Pump Organization does not look promising at all: the costs exploded while the revenue decreased by 42%. Taking a closer look at the numbers, CEO Dagobert J. Pump comes to the conclusion that the only way to save the company is to fire some of the employees.</p>

<p>The problem is that CEO Pump just recently claimed in an interview that "he is the greatest job creator that God ever created". So if he fired too many people, the dishonest corrupted left-wing media would certainly report about it, which would make him look extremely unreliable. The PR experts of the Pump Organization already estimated a number of employees that CEO Pump may fire without raising any attention in the media. To be on the safe side, CEO Pump further decides to fire as few employees as possible.</p>

<p>Taking a list of all employees of his company and their respective salary, CEO Pump has to save at least d Dollars by firing not more than k employees. If this is possible, CEO Pump wants to personally tell each and every one of them: YOU ARE FIRED!</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>one line with three integers n, d, and k, where
	<ul>
		<li>n (1 ≤ n ≤ 10 000) is the number of employees of the Pump Organization;</li>
		<li>d (1 ≤ d ≤ 10<sup>9</sup>) is the amount of money that CEO Pump needs to save at least;</li>
		<li>k (1 ≤ k ≤ n) is the maximum number of employees that CEO Pump can fire without raising attention in the media.</li>
	</ul>
	</li>
	<li>n lines each containing a string s<sub>i</sub> and an integer c<sub>i</sub>, where
	<ul>
		<li>s<sub>i</sub> (1 ≤ |s<sub>i</sub>| ≤ 7) is the name of the i-th employee;</li>
		<li>c<sub>i</sub> (1 ≤ c<sub>i</sub> ≤ 100 000) is the salary of the i-th employee.</li>
	</ul>
	</li>
</ul>

<p>All s<sub>i</sub> are distinct and only contain lowercase and uppercase letters of the English alphabet.</p>

### 출력 

 <p>If there is no way to save at least d Dollars by firing not more than k employees, output impossible.</p>

<p>If there is a way to save at least d Dollars by firing not more than k employees, then the output consists of:</p>

<ul>
	<li>one line containing a single integer x (1 ≤ x ≤ k), where x is the number of people to be fired.</li>
	<li>x lines each containing the string s<sub>i</sub>, YOU ARE FIRED!, where s<sub>i</sub> is the name of the i-th employee to be fired.</li>
</ul>

<p>If there are multiple solutions, any of them will be accepted.</p>

