# [Silver I] grad - 3170 

[문제 링크](https://www.acmicpc.net/problem/3170) 

### 성능 요약

메모리: 113500 KB, 시간: 120 ms

### 분류

기하학, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 5월 14일 04:15:32

### 문제 설명

<p>A construction site is defined as a rectangle in the coordinate system with sides parallel to the coordinate axes, with one corner in (0,0) and the opposite corner in (X,Y). </p>

<p>The entrance to the site is in the middle of the bottom side. There are N cranes on the construction site. Each crane is situated in a point on the site, it can rotate 360 degrees and the maximum reach is known for each crane. </p>

<p>The truck unloads heavy equipment on the entrance of the site and after that the equipment is carried across the site by a sequence of crane movements. In each step, one crane picks up the equipment and leaves it at any place within the maximum reach of that crane. </p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/783c37d6-6d83-4619-8cc0-78f1cfd098fe/-/preview/" style="width: 237px; height: 387px;"></p>

<p>Write a program that, given a list of K destinations within the site, determines for each destination if it is possible to carry the equipment to this destination. </p>

### 입력 

 <p>The first line of input contains two integers X and Y, 2 ≤ X,Y ≤ 200, X is even. </p>

<p>Next line contains an integer N, 1 ≤ N ≤ 50, the number of cranes. </p>

<p>Each of the following N lines contains three integers A, B and C – (A,B) is the position of the crane, and C is its maximum reach, 0 ≤ A ≤ X, 0 ≤ B ≤ Y, 0 ≤ C ≤ 200. </p>

<p>The next line contains an integer K, 3 ≤ K ≤ 30, the number of destinations. </p>

<p>Each of the following N lines contains two integers D and E – (D,E) is the position of one destination, 0 ≤ D ≤ X, 0 ≤ E ≤ Y. </p>

### 출력 

 <p>Each of the K lines should contain the word 'DA' or 'NE' – 'DA' means that it is possible to deliver the equipment to that destination, and 'NE' means that it is not possible. </p>

