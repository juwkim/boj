# [Silver V] Election Time - 6160 

[문제 링크](https://www.acmicpc.net/problem/6160) 

### 성능 요약

메모리: 40248 KB, 시간: 2228 ms

### 분류

구현(implementation), 수학(math), 정렬(sorting)

### 문제 설명

<p>The cows are having their first election after overthrowing the tyrannical Farmer John, and Bessie is one of N cows (1 <= N <= 50,000) running for President. Before the election actually happens, however, Bessie wants to determine who has the best chance of winning.</p>

<p>The election consists of two rounds. In the first round, the K cows (1 <= K <= N) cows with the most votes advance to the second round. In the second round, the cow with the most votes becomes President.</p>

<p>Given that cow i expects to get A_i votes (1 <= A_i <= 1,000,000,000) in the first round and B_i votes (1 <= B_i <= 1,000,000,000) in the second round (if he or she makes it), determine which cow is expected to win the election. Happily for you, no vote count appears twice in the A_i list; likewise, no vote count appears twice in the B_i list.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and K</li>
	<li>Lines 2..N+1: Line i+1 contains two space-separated integers: A_i and B_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The index of the cow that is expected to win the election.</li>
</ul>

<p> </p>

