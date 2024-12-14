# [Silver II] RAINFOREST CANOPY - 9700 

[문제 링크](https://www.acmicpc.net/problem/9700) 

### 성능 요약

메모리: 110760 KB, 시간: 112 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 12월 15일 07:48:01

### 문제 설명

<p>A tropical rainforest is typically divided into four main layers: the emergent, canopy, understory, and forest floor layers. Of the four, it is quite tricky to distinguish the emergent layer from the canopy layer. The emergent layer contains a small number of very large trees, which grow above the general canopy, reaching heights of 45 to 55 metres. The canopy layer is the richest layer of the diverse rainforest, and ranges in heights of 30 to 45 metres tall. Because of bio- diversity crisis, monitoring rainforest canopy is the mission of Whole Forest Observatory, which is trying to identify suitable canopy research sites.</p>

<p>A group of engineers have found a simple satellite imagery technique that can mark canopy layers on a spot image of a wide rainforest area. The spot image is a square and is stored as pixels, i.e., small cells containing either a 1 or a 0. Each pixel carries some information about a particular 1 km<sup>2</sup> region. A pixel location contains a 1 if part or its entire represented region is a canopy layer and a 0 if otherwise. </p>

<p>The following assumptions hold: </p>

<ul>
	<li>A canopy layer is represented by at least a single 1. </li>
	<li>Cells with adjacent sides on a common pixel that contains a 1, comprise the canopy layer. A single large canopy layer image will contain all 1’s. </li>
	<li>Distinct canopy layers do not touch one another. </li>
	<li>There is no wrap-around, i.e., the pixels on the bottom are not adjacent to the top, and the left is not adjacent to the right.</li>
</ul>

<p>Write a program that reads spot images and correctly counts the number of canopy layers in these images.</p>

### 입력 

 <p>The input consists of up to 1000 test cases. Each test case describes a spot image of a rainforest area, which starts on a new line with a positive integer N, (1 <= N <= 40) indicating the dimension of the image. The next N lines of each test case delineate the pixelated representation of the image.</p>

### 출력 

 <p>For each test case, produce a single line of output that starts with the prefix “Case #x:” where x represents the case number (starting from one and incrementing at each new test case), followed by a single space, and then the result, i.e., the number of canopy layers in the spot image.</p>

