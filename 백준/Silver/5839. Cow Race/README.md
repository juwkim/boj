# [Silver V] Cow Race - 5839 

[문제 링크](https://www.acmicpc.net/problem/5839) 

### 성능 요약

메모리: 115404 KB, 시간: 152 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>In order to finally settle their long-running dispute over who is the faster cow, Bessie and her friend Elsie decide to hold a race across the farm.</p>

<p>The two cows start at the same location and begin running in the same direction at the same time. The progress of each cow is described by a series of "segments", during each of which the cow runs at a constant speed. For example, Bessie might run at a speed of 5 for 3 units of time, then at a speed of 10 for 6 units of time. Bessie and Elsie both run for the same total amount of time.</p>

<p>The cows would like your help in counting the number of leadership changes during their race. A leadership change happens at a point in time when cow A pulls into the lead of cow B, whereas the last time one cow was in the lead, it was cow B. For example, if B is in the lead and then A pulls ahead, then this is a leadership change. If B is in the lead, and then A becomes even with B for some time and then finally pulls ahead, then this also counts as a leadership change.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers, N and M. (1 <= N, M <= 1000)</li>
	<li>Lines 2..1+N: Each line contains one of the N segments of Bessie's run, described by two integers: Bessie's speed and the amount of time she runs at that speed (both integers are in the range 1..1000).</li>
	<li>Lines 2+N..1+N+M: Each line contains one of the M segments of Elsie's run, described by two integers: Elsie's speed and the amount of time she runs at that speed (both integers are in the range 1..1000).</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: The number of leadership changes during the race.</li>
</ul>

