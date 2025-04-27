# [Silver I] Bellevue - 25993 

[문제 링크](https://www.acmicpc.net/problem/25993) 

### 성능 요약

메모리: 120572 KB, 시간: 132 ms

### 분류

기하학, 그리디 알고리즘

### 제출 일자

2025년 4월 27일 16:38:46

### 문제 설명

<p>As any photographer knows, any good sunset photo has the sun setting over the sea. In fact, the more sea that is visible in the photo, the prettier it is!</p>

<p>You are currently visiting the island Bellevue, and you would like to take a photo of either the sunrise to the east or the sunset to the west to submit it to Bellevue's Astonishing Photography Competition. By carefully studying the topographic maps, you managed to find the east-west profile of the island. Now you would like to know the maximal amount of sea that you could capture in a photo, measured as the viewing angle covered by water.</p>

<p>The profile of the island is given as a piecewise linear function consisting of $n-1$ segments between $n$ points. The island starts and ends at sea level. As an example, Figure B.1 shows the profile of the first sample case.</p>

<p>Note that the viewing angle of your lens is not large enough to capture the ocean to the east and west of the island in one shot. Also, the viewing angle of sea at sea level is $0$ degrees.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/49969b43-f152-404f-ba57-2f2aabc35928/-/preview/" style="width: 400px; height: 188px;"></p>

<p style="text-align: center;">Figure B.1: The east-west profile of the island in the first sample case.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with an integer $n$ ($3\leq n\leq 50\,000$), the number of points.</li>
	<li>$n$ lines with two integers $x_i$ and $y_i$ ($0\leq x_i, y_i \leq 50\,000$), a point in the east-west profile of the island.</li>
</ul>

<p>It is guaranteed that the points are given from left to right ($x_1<x_2<\dots<x_n$) and that the island starts and ends at sea level ($y_1 = y_n = 0$). The interior of the island is all above sea level ($y_i > 0$ for $1<i<n$).</p>

### 출력 

 <p>Output the maximal viewing angle of sea you can see, in degrees.</p>

<p>Your answer should have an absolute or relative error of at most $10^{-6}$.</p>

