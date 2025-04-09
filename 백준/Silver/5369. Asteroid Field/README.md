# [Silver I] Asteroid Field - 5369 

[문제 링크](https://www.acmicpc.net/problem/5369) 

### 성능 요약

메모리: 113496 KB, 시간: 116 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 9일 10:50:15

### 문제 설명

<p>Plot a path through the asteroid field. Given a starting location, final destination, and a description of the asteroid fields plot a shortest path that takes you from the starting location to the final destination without running into any asteroids. The asteroid field is described using a mxm grid of characters with</p>

<ul>
	<li>s: for starting location</li>
	<li>d: for final location</li>
	<li>-: for open space</li>
	<li>*: asteroid</li>
</ul>

<p>Here is an example of a 4x4 grid.</p>

<pre>s*-*
-*-*
----
*-*d</pre>

<p>Your ship can move up, down, left, and right (not diagonally). Each position in a mxm grid will be assigned an integer between 0 and m<sup>2</sup>-1 as follows.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b44cd4a5-7baf-4560-b59d-1d7e3a8205da/-/preview/" style="width: 128px; height: 85px;"></p>

### 입력 

 <p>The first line will have a positive integer n representing the number of data sets. The first line of each data set will contain an integer m, followed by m lines, and each line will contain m characters. The character s will always be in the top left corner and d will always be in the bottom right corner.</p>

### 출력 

 <p>For each data set print the minimal number of moves needed to reach the destination or -1 if there is no solution.</p>

