# [Bronze II] Speed Reading - 6139 

[문제 링크](https://www.acmicpc.net/problem/6139) 

### 성능 요약

메모리: 123152 KB, 시간: 212 ms

### 분류

구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>All K (1 <= K <= 1,000) of the cows are participating in Farmer John's annual reading contest. The competition consists of reading a single book with N (1 <= N <= 100,000) pages as fast as possible while understanding it.</p>

<p>Cow i has a reading speed S_i (1 <= S_i <= 100) pages per minute, a maximum consecutive reading time T_i (1 <= T_i <= 100) minutes, and a minimum rest time R_i (1 <= R_i <= 100) minutes.  The cow can read at a rate of S_i pages per minute, but only for T_i minute sat a time. After she stops reading to rest, she must rest for R_i minutes before commencing reading again.</p>

<p>Determine the number of minutes (rounded up to the nearest full minute) that it will take for each cow to read the book.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and K</li>
	<li>Lines 2..K+1: Line i+1 contains three space-separated integers: S_i, T_i, and R_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..K: Line i should indicate how many minutes (rounded up to the nearest full minute) are required for cow i to read the whole book.</li>
</ul>

