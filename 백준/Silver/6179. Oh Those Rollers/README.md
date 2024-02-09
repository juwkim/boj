# [Silver III] Oh Those Rollers - 6179 

[문제 링크](https://www.acmicpc.net/problem/6179) 

### 성능 요약

메모리: 110680 KB, 시간: 128 ms

### 분류

브루트포스 알고리즘, 깊이 우선 탐색, 기하학, 그래프 이론, 그래프 탐색, 피타고라스 정리

### 제출 일자

2024년 2월 9일 16:46:45

### 문제 설명

<p>Farmer John has installed a new winch that gives him mechanical advantage when lifting bales of hay into the barn. The winch was manufactured by the Rube Goldberg Winch Company and has way too many rollers to make any sense at all. The winch has a huge steel plate with a number of rollers whose ultimate source of power is the drive-roller whose location FJ has denoted as the origin (0,0). This roller drives a roller that drives another roller, etc. etc. until the final roller is driven. FJ is trying to find that final roller and wants to know which one it is.</p>

<p>FJ has recorded the x_i,y_i (-5,000 <= x_i <= 5,000; -5,000 <= y_i <= 5,000) coordinates and the radius r_i (3 <= r_i <= 1024) of each of the N (2 <= N <= 1080) rollers. Tell him the x,y coordinate of the last roller in the chain (the roller that is driven but drives no other roller). Every roller except the drive-roller is driven by exactly one other roller.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N+1: Line i+1 describes roller i with three space separated integers: x_i, y_i, and r_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single line with two space-separated integers that are respectively the x,y coordinates of the last roller in the chain of driven rollers.</li>
</ul>

