# [Silver II] Satellite Photographs - 26999 

[문제 링크](https://www.acmicpc.net/problem/26999) 

### 성능 요약

메모리: 111492 KB, 시간: 120 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 12월 15일 04:16:39

### 문제 설명

<p>Farmer John purchased satellite photos of W x H pixels of his farm (1 ≤ W ≤ 80, 1 ≤ H ≤ 1000) and wishes to determine the largest 'contiguous' (connected) pasture. Pastures are contiguous when any pair of pixels in a pasture can be connected by traversing adjacent vertical or horizontal pixels that are part of the pasture. (It is easy to create pastures with very strange shapes, even circles that surround other circles.)</p>

<p>Each photo has been digitally enhanced to show pasture area as an asterisk ('*') and non-pasture area as a period ('.'). Here is a 10 x 5 sample satellite photo:</p>

<pre>..*.....**
.**..*****
.*...*....
..****.***
..****.***</pre>

<p>This photo shows three contiguous pastures of 4, 16, and 6 pixels. Help FJ find the largest contiguous pasture in each of his satellite photos.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: W and H</li>
	<li>Lines 2..H+1: Each line contains W "*" or "." characters representing one raster line of a satellite photograph.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: The size of the largest contiguous field in the satellite photo.</li>
</ul>

