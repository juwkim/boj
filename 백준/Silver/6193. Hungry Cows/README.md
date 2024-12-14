# [Silver II] Hungry Cows - 6193 

[문제 링크](https://www.acmicpc.net/problem/6193) 

### 성능 요약

메모리: 111400 KB, 시간: 100 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 12월 15일 06:14:10

### 문제 설명

<p>Each of Farmer John's N (1 <= N <= 5,000) cows has a unique positive integer brand that fits nicely into 32 signed bits. He wishes the cows would line up in numerical order for feeding, but they never cooperate. To encourage good behavior, he allows a cow to eat only if it is the first cow to be chosen to eat or if its number is greater than the cow that ate before it.</p>

<p>Given a listing of the ordering of cow brands for the cows standing in line, what is the largest number of cows that can be fed using FJ rules?</p>

<p>Consider this line of 11 cows:</p>

<pre>2 5 18 3 4 7 10 9 11 8 15</pre>

<p>One could feed cows in the order 2, 3, 4, 7, 10 11, and 15 for a total of seven fed, the largest number possible.</p>

<p>One could not feed cows in the order 2, 5, 3, 10 15 since cow 3's brand is not greater than its predecessor, 5.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer, N </li>
	<li>Lines 2..?: Each line except potentially the last contains 20 space-separated integers that are successively the brands of the cows in line. The last line might have fewer than 20 integers if N is not an exact multiple of 20.</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The length of the largest chain of cows where each brand is greater than its predecessor.</li>
</ul>

