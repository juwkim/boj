# [Silver II] Hay For Sale - 6076 

[문제 링크](https://www.acmicpc.net/problem/6076) 

### 성능 요약

메모리: 213804 KB, 시간: 3056 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 12월 17일 01:02:50

### 문제 설명

<p>Farmer John suffered a terrible loss when giant Australian cockroaches ate the entirety of his hay inventory, leaving him with nothing to feed the cows. He hitched up his wagon with capacity C (1 <= C <= 50,000) cubic units and sauntered over to Farmer Don's to get some hay before the cows miss a meal.</p>

<p>Farmer Don had a wide variety of H (1 <= H <= 5,000) hay bales for sale, each with its own volume (1 <= V_i <= C). Bales of hay, you know, are somewhat flexible and can be jammed into the oddest of spaces in a wagon.</p>

<p>FJ carefully evaluates the volumes so that he can figure out the largest amount of hay he can purchase for his cows.</p>

<p>Given the volume constraint and a list of bales to buy, what is the greatest volume of hay FJ can purchase?  He can't purchase partial bales, of course. Each input line (after the first) lists a single bale FJ can buy.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: C and H</li>
	<li>Lines 2..H+1: Each line describes the volume of a single bale: V_i</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer which is the greatest volume of hay FJ can purchase given the list of bales for sale and constraints.</li>
</ul>

