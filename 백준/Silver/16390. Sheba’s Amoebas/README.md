# [Silver II] Sheba’s Amoebas - 16390 

[문제 링크](https://www.acmicpc.net/problem/16390) 

### 성능 요약

메모리: 114368 KB, 시간: 136 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 12월 14일 20:59:43

### 문제 설명

<p>After a successful Kickstarter campaign, Sheba Arriba has raised enough money for her mail-order biology supply company. “Sheba’s Amoebas” can ship Petri dishes already populated with a colony of those tiny one-celled organisms. However, Sheba needs to be able to verify the number of amoebas her company sends out. For each dish she has a black-and-white image that has been pre-processed to show each amoeba as a simple closed loop of black pixels. (A loop is a minimal set of black pixels in which each pixel is adjacent to exactly two other pixels in the set; adjacent means sharing an edge or corner of a pixel.) All black pixels in the image belong to some loop.</p>

<p>Sheba would like you to write a program that counts the closed loops in a rectangular array of black and white pixels. No two closed loops in the image touch or overlap. One particularly nasty species of cannibalistic amoeba is known to surround and engulf its neighbors; consequently there may be amoebas within amoebas. For instance, each of the images in Figure G.1 contains four amoebas.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/10d1900a-1988-4679-b9dc-e451888e3da5/-/preview/" style="width: 300px; height: 154px;"></p>

<p style="text-align: center;">Figure G.1: Two Petri dishes, each with four amoebas.</p>

### 입력 

 <p>The first line of input contains two integers m and n, (1 ≤ m, n ≤ 100). This is followed by m lines, each containing n characters. A ‘<code>#</code>’ denotes a black pixel, a ‘<code>.</code>’ denotes a white pixel. For every black pixel, exactly two of its eight neighbors are also black.</p>

### 출력 

 <p>Display a single integer representing the number of loops in the input.</p>

