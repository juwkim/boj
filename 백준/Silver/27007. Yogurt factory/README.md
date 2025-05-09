# [Silver I] Yogurt factory - 27007 

[문제 링크](https://www.acmicpc.net/problem/27007) 

### 성능 요약

메모리: 110576 KB, 시간: 96 ms

### 분류

그리디 알고리즘

### 제출 일자

2025년 5월 10일 01:44:35

### 문제 설명

<p>The cows have purchased a yogurt factory that makes world-famous Yucky Yogurt. Over the next N (1 ≤ N ≤ 10,000) weeks, the price of milk and labor will fluctuate weekly such that it will cost the company C_i (1 ≤ C_i ≤ 5,000) cents to produce one unit of yogurt in week i. Yucky's factory, being well-designed, can produce arbitrarily many units of yogurt each week.</p>

<p>Yucky Yogurt owns a warehouse that can store unused yogurt at a constant fee of S (1 ≤ S ≤ 100) cents per unit of yogurt per week. Fortuitously, yogurt does not spoil. Yucky Yogurt's warehouse is enormous, so it can hold arbitrarily many units of yogurt.</p>

<p>Yucky wants to find a way to make weekly deliveries of Y_i (0 ≤ Y_i ≤ 10,000) units of yogurt to its clientele (Y_i is the delivery quantity in week i). Help Yucky minimize its costs over the entire N-week period. Yogurt produced in week i, as well as any yogurt already in storage, can be used to meet Yucky's demand for that week.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers, N and S.</li>
	<li>Lines 2..N+1: Line i+1 contains two space-separated integers: C_i and Y_i.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: Line 1 contains a single integer: the minimum total cost to satisfy the yogurt schedule. Note that the total might be too large for a 32-bit integer.</li>
</ul>

