# [Bronze III] Who Has Seen The Wind - 6779 

[문제 링크](https://www.acmicpc.net/problem/6779) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math)

### 문제 설명

<p>Margaret has looked at the wind floating over the prairies for a long time. After these observations, she has created a formula that will describe the altitude of a weather balloon launched from her house. In particular, her equation predicts the altitude A (in metres above the ground) at hour t after launching her balloon is:</p>

<p style="text-align: center;">A = −6t<sup>4</sup> + ht<sup>3</sup> + 2t<sup>2</sup> + t</p>

<p>where h is an integer value representing the humidity as a value between 0 and 100 inclusive.</p>

<p>Margaret is curious at what the earliest hour is (if any) that her weather balloon will hit the ground after launch, so long as it is no more than the maximum time, M, that Margaret is willing to wait. You can assume that the weather balloon touches ground when A ≤ 0.</p>

<p>In order to do this, your program should use the formula to calculate the altitude when t = 1, t = 2, and so on, until the balloon touches the ground or t = M is reached.</p>

### 입력 

 <p>The input is two non-negative integers: h, the humidity factor, followed by M, the maximum number of hours Margaret will wait for the weather balloon to return to ground. You can assume 0 ≤ h ≤ 100 and 0 < M < 240.</p>

### 출력 

 <p>The output will be one of the following possibilities:</p>

<ul>
	<li><code>The balloon does not touch ground in the given time.</code></li>
	<li><code>The balloon first touches ground at hour: T</code></li>
</ul>

<p>where T is a positive integer value representing the earliest hour when the balloon has altitude less than or equal to zero.</p>

