# [Silver II] Jumping Cows - 27053 

[문제 링크](https://www.acmicpc.net/problem/27053) 

### 성능 요약

메모리: 120504 KB, 시간: 128 ms

### 분류

다이나믹 프로그래밍, 그리디 알고리즘

### 제출 일자

2025년 1월 13일 07:06:54

### 문제 설명

<p>Farmer John's cows would like to jump over the moon, just like the cows in their favorite nursery rhyme. Unfortunately, cows can not jump.</p>

<p>The local witch doctor has mixed up P (1 ≤ P ≤ 150,000) potions to aid the cows in their quest to jump. These potions must be administered exactly in the order they were created, though some may be skipped.</p>

<p>Each potion has a 'strength' (1 ≤ strength ≤ 500) that enhances the cows' jumping ability. Taking a potion during an odd time step increases the cows' jump; taking a potion during an even time step decreases the jump. Before taking any potions the cows' jumping ability is, of course, 0.</p>

<p>No potion can be taken twice, and once the cow has begun taking potions, one potion must be taken during each time step, starting at time 1. One or more potions may be skipped in each turn.</p>

<p>Determine which potions to take to get the highest jump.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer, P</li>
	<li>Lines 2..P+1: Each line contains a single integer that is the strength of a potion. Line 2 gives the strength of the first potion; line 3 gives the strength of the second potion; and so on.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the maximum possible jump.</li>
</ul>

