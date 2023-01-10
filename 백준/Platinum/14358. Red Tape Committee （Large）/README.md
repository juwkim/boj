# [Platinum II] Red Tape Committee (Large) - 14358 

[문제 링크](https://www.acmicpc.net/problem/14358) 

### 성능 요약

메모리: 115664 KB, 시간: 828 ms

### 분류

Empty

### 문제 설명

<p>You are the head of the Department of Redundancy Reduction and Superfluity Shrinkage. Currently, the department cannot agree on whether there is too much "red tape" (inefficiency) in the department itself. They have asked you to form a Red Tape Committee to vote on the issue.</p>

<p>The department has N members. For each member, you know the probability P<sub>i</sub> that that member will vote "Yes". If a member does not vote "Yes", they necessarily vote "No"; nobody abstains.</p>

<p>You must choose exactly K members to be on the committee. The department rules dictate that K must be an even number to allow for ties, which are seen as part of a healthy bureaucracy.</p>

<p>If you choose committee members to maximize the probability of a tie, what is that probability?</p>

<ul>
</ul>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow; each consists of two lines. The first line of a test case consists of two integers N and K, the sizes of the department and the committee. The second line of a test case consists of Ndecimal  values P<sub>i</sub>; each has exactly two decimal places of precision and represents the probability that the i-th department member will vote "Yes".</p>

<p>Limits</p>

<ul>
	<li>1 ≤ T ≤ 100.</li>
	<li>2 ≤ K ≤ N.</li>
	<li>K is even.</li>
	<li>0.00 ≤ each P<sub>i</sub> ≤ 1.00.</li>
	<li>2 ≤ N ≤ 200.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is a floating-point number: the maximum possible probability of a tie. <code>y</code> will be considered correct if it is within an absolute or relative error of 10<sup>-6</sup> of the correct answer.</p>

