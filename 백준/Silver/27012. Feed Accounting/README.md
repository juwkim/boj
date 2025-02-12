# [Silver II] Feed Accounting - 27012 

[문제 링크](https://www.acmicpc.net/problem/27012) 

### 성능 요약

메모리: 109544 KB, 시간: 96 ms

### 분류

자료 구조, 누적 합, 스택

### 제출 일자

2025년 2월 12일 10:34:13

### 문제 설명

<p>Farmer John is trying to figure out when his last shipment of feed arrived. Starting with an empty grain bin, he ordered and received F1 (1 ≤ F1 ≤ 1,000,000) kilograms of feed. Regrettably, he is not certain exactly when the feed arrived. Of the F1 kilograms, F2 (1 ≤ F2 ≤ F1) kilograms of feed remain on day D (1 ≤ D ≤ 2,000). He must determine the most recent day that his shipment could have arrived.</p>

<p>Each of his C (1 ≤ C ≤ 100) cows eats exactly 1 kilogram of feed each day. For various reasons, cows arrive on a certain day and depart on another, so two days might have very different feed consumption. The input data tells which days each cow was present. Every cow ate feed from Farmer John's bin on the day she arrived and also on the day she left.</p>

<p>Given that today is day D, determine the minimum number of days that must have passed since his last shipment. The cows have already eaten today, and the shipment arrived before the cows had eaten.</p>

### 입력 

 <ul>
	<li>Line 1: Four space-separated integers: C, F1, F2, and D</li>
	<li>Lines 2..C+1: Line i+1 contains two space-separated integers describing the presence of a cow. The first integer tells the first day the cow was on the farm; the second tells the final day of the cow's presence. Each day is in the range 1..2,000.</li>
</ul>

### 출력 

 <p>The last day that the shipment might have arrived, an integer that will always be positive.</p>

