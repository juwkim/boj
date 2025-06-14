# [Silver IV] Counting Rectangles - 7338 

[문제 링크](https://www.acmicpc.net/problem/7338) 

### 성능 요약

메모리: 108384 KB, 시간: 96 ms

### 분류

브루트포스 알고리즘, 기하학

### 제출 일자

2025년 6월 14일 20:02:33

### 문제 설명

<p>We are given a figure consisting of only horizontal and vertical line segments. Our goal is to count the number of all different rectangles formed by these segments. As an example, the number of rectangles in the Figures 1 and 2 are 5 and 0 respectively.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/7338/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-09-22%20%EC%98%A4%EC%A0%84%2010.35.21.png" style="height:207px; width:480px"></p>

<p>There are many intersection points in the figure. An intersection point is a point shared by at least two segments. The input line segments are such that each intersection point comes from the intersection of exactly one horizontal segment and one vertical segment.</p>

### 입력 

 <p>The first line of the file contains a single number M, which is the number of test cases in the file (1 ≤ M ≤ 10), and the rest of the file consists of the data of the test cases. Each test case begins with a line containing s (1 ≤ s ≤= 100), the number of line segments in the figure. It follows by s lines, each containing x and y coordinates of two end points of a segment respectively. The coordinates are integers in the range of 0 to 1000.</p>

### 출력 

 <p>The output for each test case is the number of all different rectangles in the figure described by the test case. The output for each test case must be written on a separate line.</p>

