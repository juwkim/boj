# [Bronze II] Crop Circles - 5959 

[문제 링크](https://www.acmicpc.net/problem/5959) 

### 성능 요약

메모리: 28776 KB, 시간: 336 ms

### 분류

브루트포스 알고리즘(bruteforcing), 기하학(geometry), 피타고라스 정리(pythagoras)

### 문제 설명

<p>Bessie and her fellow herd-mates have become extremely territorial. The N (1 <= N <= 400) cows conveniently numbered 1..N have all staked out a grazing spot in the pasture. Each cow i has a spot on an integer grid (0 <= X_i <= 10,000; 0 <= Y_i <= 10,000) and an integer radius R_i that indicates the circle she is staking out (1 <= R_i <= 500).</p>

<p>The cows are a bit greedy and sometimes stake out territory of their herd-mates. For each cow, calculate the number of other cows whose territory overlaps her territory.</p>

<p>By way of example, consider these six cows with indicated locations and radii (don't confuse radius with diameter!):</p>

<p><img alt="" src="" style="height:153px; width:489px"></p>

<p>By visual inspection, we can see and count the overlaps, as shown.</p>

<p>NOTE: the test data will avoid pathological situations like tangents where the circles just barely touch.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N+1: Three space-separated integers: X_i, Y_i, and R_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..N: Line i contains a single integer that is the number of other fields that overlap with cow i's field.</li>
</ul>

<p> </p>

