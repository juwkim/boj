# [Bronze I] Leapcow - 27041 

[문제 링크](https://www.acmicpc.net/problem/27041) 

### 성능 요약

메모리: 114328 KB, 시간: 132 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>Like everyone else, the cows like to bury each other in sand while at the beach. On this beach, the cows are only buried on the integer coordinates of a one-dimensional number line. Bessie wants to travel from one end of the beach (i.e., coordinate 0) to the other end (coordinate E, 5 ≤ E ≤ 40,000) without stepping on any buried cows. Bessie travels only by leaps, each of which has some length in the range 1..L (3 ≤ L ≤ 50).</p>

<p>Given the locations (1..E-1) of the B (1 ≤ B ≤ 500) buried cows, figure out the least number of leaps Bessie can use to get from one side to the other. It is guaranteed that an answer exists.</p>

### 입력 

 <ul>
	<li>Line 1: Three space-separated integers: E, L, and B.</li>
	<li>Lines 2..B+1: Each line contains a single integer telling the coordinate of a buried cow.</li>
</ul>

### 출력 

 <p>A single line with an integer that is the smallest number of "legal" leaps that are required for Bessie to reach coordinate E.</p>

