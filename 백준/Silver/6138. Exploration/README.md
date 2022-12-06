# [Silver V] Exploration - 6138 

[문제 링크](https://www.acmicpc.net/problem/6138) 

### 성능 요약

메모리: 119796 KB, 시간: 200 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 정렬(sorting)

### 문제 설명

<p>Bessie is traveling on a road teeming with interesting landmarks. The road is labeled just like a number line, and Bessie starts at the "origin" (x = 0). A total of N (1 <= N <= 50,000) landmarks are located at points x_1, x_2, ..., x_N  (-100,000 <= x_i <= 100,000). Bessie wants to visit as many landmarks as possible before sundown, which occurs in T (1 <= T <= 1,000,000,000) minutes. She travels 1 distance unit in 1 minute.</p>

<p>Bessie will visit the landmarks in a particular order. Since the landmarks closer to the origin are more important to Farmer John, she always heads for the unvisited landmark closest to the origin. No two landmarks will be the same distance away from the origin.</p>

<p>Help Bessie determine the maximum number of landmarks she can visit before the day ends.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: T and N</li>
	<li>Lines 2..N+1: Line i+1 contains a single integer that is the location of the ith landmark: x_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The maximum number of landmarks Bessie can visit.</li>
</ul>

