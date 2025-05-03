# [Silver I] Intelligence in Perpendicularia - 15139 

[문제 링크](https://www.acmicpc.net/problem/15139) 

### 성능 요약

메모리: 110576 KB, 시간: 104 ms

### 분류

애드 혹, 기하학

### 제출 일자

2025년 5월 4일 01:59:50

### 문제 설명

<p>There are only two directions in Perpendicularia: vertical and horizontal. Perpendicularia government are going to build a new secret service facility. They have some proposed facility plans and want to calculate total secured perimeter for each of them.</p>

<p>The total secured perimeter is calculated as the total length of the facility walls invisible for the perpendicularly-looking outside observer. The figure below shows one of the proposed plans and corresponding secured perimeter.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15139/1.png" style="height:181px; width:238px"></p>

<p>Write a program that calculates the total secured perimeter for the given plan of the secret service facility.</p>

### 입력 

 <p>The plan of the secret service facility is specified as a polygon.</p>

<p>The first line of the input contains one integer n — the number of vertices of the polygon (4 ≤ n ≤ 1000). Each of the following n lines contains two integers x<sub>i</sub> and y<sub>i</sub> – the coordinates of the i-th vertex (−10<sup>6</sup> ≤ x<sub>i</sub>, y<sub>i</sub> ≤ 10<sup>6</sup>). Vertices are listed in the consecutive order.</p>

<p>All polygon vertices are distinct and none of them lie at the polygon’s edge. All polygon edges are either vertical (x<sub>i</sub> = x<sub>i+1</sub> or horizontal (y<sub>i</sub> = y<sub>i+1</sub>) and none of them intersect each other.</p>

### 출력 

 <p>Output a single integer — the total secured perimeter of the secret service facility.</p>

