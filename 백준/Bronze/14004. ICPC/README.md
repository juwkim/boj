# [Bronze II] ICPC - 14004 

[문제 링크](https://www.acmicpc.net/problem/14004) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p><strong>"I once met an interesting guy who had a phone with two batteries."</strong> - Dudu, 2014</p>

<p>Dudu once met an interesting chap who had a phone with two batteries. With that in mind he decided to create a phone that would have a pair of batteries for his upcoming trip to Thailand.</p>

<p>His company, Interesting Chap Phone Charging (ICPC), created an advanced dual battery technology. While one battery is being used to supply the phone the other is being recharged via a solar receptor.</p>

<p>Unfortunately the rate that the phone uses energy is higher than the rate a battery can be recharged. ICPC is interested to know how long a system will last until being completely out of charge.</p>

### 입력 

 <p>The input will consist of 4 integers A, B, C and D. They are respectively the rate a phone uses energy in Amperes (Coulombs per second), the rate in which a battery can be recharged in Amperes, the initial charge of the first battery in Coulombs and the initial charge of the second battery in Coulombs.</p>

<p>ICPC's batteries have infinite capacity and the phone changes from using one battery to using the other instantaneously.</p>

<ul>
	<li>0 ≤ A,B,C,D < 2<sup>31</sup></li>
	<li>A > B</li>
</ul>

### 출력 

 <p>Output one integer with the number of seconds a phone will last given an ICPC dual battery as described in the statement. Round down your answer in case it's nonintegral.</p>

