# [Silver II] Hippity Hopscotch - 4421 

[문제 링크](https://www.acmicpc.net/problem/4421) 

### 성능 요약

메모리: 5020 KB, 시간: 4 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 2월 8일 03:10:05

### 문제 설명

<p>The game of hopscotch involves chalk, sidewalks, jumping, and picking things up. Our variant of hopscotch involves money as well. The game is played on a square grid of dimension n: each grid location is labelled (p,q) where 0 <= p < n and 0 <= q < n. Each grid location has on it a stack of between 0 and 100 pennies.</p>

<p>A contestant begins by standing at location (0,0). The contestant collects the money where he or she stands and then jumps either horizontally or vertically to another square. That square must be within the jumping capability of the contestant (say, k locations) and must have more pennies than those that were on the current square.</p>

<p>Given n, k, and the number of pennies at each grid location, compute the maximum number of pennies that the contestant can pick up before being unable to move.</p>

### 입력 

 <ul>
	<li>a line containing two integers between 1 and 100: n and k</li>
	<li>n lines, each with n numbers: the first line contains the number of pennies at locations (0,0) (0,1) ... (0,n-1); the next line contains the number of pennies at locations (1,0), (1,1), ... (1,n-1), and so on.</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>a single integer giving the number of pennies collected</li>
</ul>

