# [Bronze III] And Then There Was 5 - 11520 

[문제 링크](https://www.acmicpc.net/problem/11520) 

### 성능 요약

메모리: 30840 KB, 시간: 912 ms

### 분류

구현(implementation)

### 문제 설명

<p>Your friend Mike is arguing with a classmate Chris over what the last digit in π is. (You and I know there is no such thing, but Chris simply isn't to be dissuaded.) Mike's argument is as flawed as it is entertaining: given any digit in π that you look at, either the number itself is a 5 or there is a 5 that occurs after that digit.</p>

<p>Cute, but that same argument is true of any digit, at least for the portion of π that has been calculated. Luckily, you're not being asked to actually prove anything; Mike just wants you to use your "computer skills" to give him some sample data for him to use to support his case.</p>

<p>Your friend wants a large sampling of places of π and wants to show that his argument holds true. For each test case, you will be given an offset into the digits of π (P) and a single digit (D).</p>

<p>He wants to you find the Qth and Rth digits of π given that:</p>

<ul>
	<li>Q is the lowest offset such that Q >= P and the Qth digit of π equals D</li>
	<li>R is the lowest offset such that R > Q and the Rth digit of π equals 5</li>
</ul>

<p>For example, if P is 3 and D is 2, Q would be 6 and R would be 8, and the Qth and Rth digits of π would be 2 and 5 respectively.</p>

<pre>              P     Q   R
Offset: 0 1 2 3 4 5 6 7 8 9 10 11 ...
Value:  3 1 4 1 5 9 2 6 5 3  5  8 ...
</pre>

### 입력 

 <p>The first line contains the number of test cases N (1 <= N <= 10,000).</p>

<p>Each of the following N lines contains two integers:</p>

<ul>
	<li>P (1 <= P <= 1,000,000), an offset into the digits of π</li>
	<li>D (0 <= D <= 9), a digit to find in π</li>
</ul>

### 출력 

 <p>For each test case, you are to output a single line containing the Qth and Rth digits of π as described above.</p>

