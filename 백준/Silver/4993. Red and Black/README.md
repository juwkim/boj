# [Silver I] Red and Black - 4993 

[문제 링크](https://www.acmicpc.net/problem/4993) 

### 성능 요약

메모리: 110736 KB, 시간: 108 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 9일 17:22:25

### 문제 설명

<p>There is a rectangular room, covered with square tiles. Each tile is colored either red or black. A man is standing on a black tile. From a tile, he can move to one of four adjacent tiles. But he can't move on red tiles, he can move only on black tiles.</p>

<p>Write a program to count the number of black tiles which he can reach by repeating the moves described above.</p>

### 입력 

 <p>The input consists of multiple data sets. A data set starts with a line containing two positive integers W and H; W and H are the numbers of tiles in the x- and y- directions, respectively. W and H are not more than 20.</p>

<p>There are H more lines in the data set, each of which includes W characters. Each character represents the color of a tile as follows.</p>

<ul>
	<li>'.' - a black tile</li>
	<li>'#' - a red tile</li>
	<li>'@' - a man on a black tile(appears exactly once in a data set)</li>
</ul>

<p>The end of the input is indicated by a line consisting of two zeros.</p>

### 출력 

 <p>For each data set, your program should output a line which contains the number of tiles he can reach from the initial tile (including itself).</p>

