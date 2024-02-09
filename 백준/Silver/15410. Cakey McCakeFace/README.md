# [Silver III] Cakey McCakeFace - 15410 

[문제 링크](https://www.acmicpc.net/problem/15410) 

### 성능 요약

메모리: 428584 KB, 시간: 2380 ms

### 분류

정렬

### 제출 일자

2024년 2월 9일 18:56:01

### 문제 설명

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15410/1.png" style="height:291px; width:270px"></p>

<p>Cakey McCakeFace’s signature pastry, the Unknowable Cake, is baked daily in their Paris facility. The make-or-break trick for this cake is the cooking time, which is a very well-kept secret. Eve, the well-known spy, wants to steal this secret, and your job is to help her.</p>

<p>Cakes are cooked in a single huge oven that has exactly one front and one back door. The uncooked cakes are inserted through the front door. After the exact and very secret cooking time has passed, the cakes exit the oven through the back door. Only one cake can go through the front or back door at any given time.</p>

<p>Eve has secretly installed detectors at the front and back of the oven. They record a signal every time a cake passes through the doors. A cake will therefore trigger the entry detector at some time t when it goes through the front door, and then trigger the exit detector at time exactly t + cooking_time when it goes through the back door (all cakes at Cakey McCakeFace are always perfectly cooked).</p>

<p>After a few days, she receives two sets of timestamps (in ms) corresponding to entry and exit detectors. Unfortunately, the detectors are faulty: they are sometimes triggered when no cake has passed, or they may fail to be triggered when a cake passes. Eve noticed that she could make a good guess of the secret cooking_time by finding the time difference that maximizes the number of correspondences of entry and exit detection times. Help Eve compute this.</p>

### 입력 

 <ul>
	<li>Line 1: the number N of times the entry detector was triggered.</li>
	<li>Line 2: the number M of times the exit detector was triggered.</li>
	<li>Line 3: the N integer timestamps at which the entry detector was triggered, sorted in ascending order, with no repetition, space-separated.</li>
	<li>Line 4: the M integer timestamps at which the exit detector was triggered, sorted in ascending order, with no repetition, space-separated.</li>
</ul>

<p>Limits</p>

<ul>
	<li>1 ≤ N, M ≤ 2 000;</li>
	<li>each timestamp is between 0 and 1 000 000 000 (inclusive).</li>
</ul>

### 출력 

 <p>A single integer: your best guess of the secret cooking_time, the (positive or zero) time difference that maximizes the number of correspondences of entry and exit detection times. If multiple such values exist, the smallest one should be returned.</p>

