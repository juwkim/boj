# [Silver I] Milestone Counter - 11492 

[문제 링크](https://www.acmicpc.net/problem/11492) 

### 성능 요약

메모리: 110736 KB, 시간: 104 ms

### 분류

수학, 브루트포스 알고리즘, 정수론, 유클리드 호제법

### 제출 일자

2025년 6월 28일 20:51:32

### 문제 설명

<p>Driving through the Irish countryside, one frequently sees enigmatic small grey stones sitting by the wayside, spaced about a kilometre and a half apart. As it turns out, these stones once had a purpose: they were milestones, intended to demarcate this venerable unit of measurement.</p>

<p>Being so old and, crucially, collectible by magpies and larger scamps alike, not all of these stones have remained.</p>

<p>Passing by some more of these tattered markers at a constant but unknown speed, you may still be able to gain some information from their placements. For example, since you started counting you have passed exactly M remaining stones; how fast could you have been driving?</p>

### 입력 

 <ul>
	<li>One line containing two positive integers, M and N (2 ≤ M ≤ N ≤ 10<sup>3</sup>): the number of consecutive stones you noticed and the total number of stones along the road respectively.</li>
	<li>One line containing M distinct non-negative integers T<sub>1..M</sub> in ascending order — the times at which you passed stones in hours (0 ≤ T<sub>i</sub> ≤ 10<sup>15</sup>).</li>
	<li>One line containing N distinct non-negative integers X<sub>1..N</sub> in ascending order — the distances along the road of each milestone (0 ≤ X<sub>i</sub> ≤ 10<sup>15</sup>) in miles.</li>
</ul>

### 출력 

 <p>Output two lines:</p>

<ul>
	<li>First, the number of distinct possible speeds at which the car could have been travelling.</li>
	<li>Second, a space-separated list of all of the possible distances between the first milestone you saw and the second milestone you saw, in increasing order.</li>
</ul>

