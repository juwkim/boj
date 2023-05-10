# [Silver IV] Fence Height - 27024 

[문제 링크](https://www.acmicpc.net/problem/27024) 

### 성능 요약

메모리: 115536 KB, 시간: 148 ms

### 분류

슬라이딩 윈도우, 정렬

### 문제 설명

<p>Cows have very strong feelings about how high fences should be.  A cow wants the fence high enough so that she feels safe and protected, but not so high so that she can not see over it and moo at passing cars.  Though a cow could stand on her tip-hooves or squat down to get to the right height, she naturally wants the fence to be the right height in the first place.  Each of the N (1 ≤ N ≤ 10,000) cows expresses a height preference (1 ≤ preference ≤ 10,000), which may vary from cow to cow.</p>

<p>This presents a predicament for Farmer John.  As a man of great esthetics, he wants his fence to of a uniform height everywhere. But as a man of great empathy, he sincerely wants to satisfy the demands of his cows.  (Or maybe he's just selfish and knows that the cows would give more milk if they got what they wanted.)</p>

<p>To compromise, he agreed to build portions of the fence using posts of different heights in order to appease the majority (strictly greater than half) of the cow population.  A cow is satisfied if there is some part of the fence at her height preference.  However, FJ really wants to minimize the range of fence posts heights used, i.e., the difference between the highest fence post and the lowest fence post. Help him do that.</p>

<p>Note that the height of a fence post determines the fence height, not some fancy continuous function that connects two fence posts of different height.</p>

### 입력 

 <ul>
	<li>Line 1: An integer, N</li>
	<li>Lines 2..N+1: An integer fence post height preference of a cow</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer representing the minimum range of fence post heights.</li>
</ul>

