# [Silver I] Cow Picnic - 6207 

[문제 링크](https://www.acmicpc.net/problem/6207) 

### 성능 요약

메모리: 111336 KB, 시간: 128 ms

### 분류

너비 우선 탐색, 브루트포스 알고리즘, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 11일 00:45:28

### 문제 설명

<p>The cows are having a picnic! Each of Farmer John's K (1 <= K <= 100) cows is grazing in one of N (1 <= N <= 1,000) pastures, conveniently numbered 1...N. The pastures are connected by M (1 <= M <= 10,000) one-way paths (no path connects a pasture to itself).</p>

<p>The cows want to gather in the same pasture for their picnic, but (because of the one-way paths) some cows may only be able to get to some pastures. Help the cows out by figuring out how many pastures are reachable by all cows, and hence are possible picnic locations.</p>

### 입력 

 <ul>
	<li>Line 1: Three space-separated integers, respectively: K, N, and M</li>
	<li>Lines 2..K+1: Line i+1 contains a single integer (1..N) which is the number of the pasture in which cow i is grazing.</li>
	<li>Lines K+2..M+K+1: Each line contains two space-separated integers, respectively A and B (both 1..N and A != B), representing a one-way path from pasture A to pasture B.</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The single integer that is the number of pastures that are reachable by all cows via the one-way paths.</li>
</ul>

