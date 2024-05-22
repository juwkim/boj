# [Silver III] Rectangles 2 - 8312 

[문제 링크](https://www.acmicpc.net/problem/8312) 

### 성능 요약

메모리: 109240 KB, 시간: 108 ms

### 분류

사칙연산, 브루트포스 알고리즘, 조합론, 수학

### 제출 일자

2024년 5월 23일 01:29:32

### 문제 설명

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/8312/1.gif" style="height:100px; width:150px"></p>

<p>We have found: 6 rectangles 1 × 1, 4 rectangles 2 × 1, 3 rectangles 1 × 2, 2 rectangles 2 × 2, 2 rectangles 3 × 1 and one rectangle 3 × 2, what gives 18 in total. Clearly, we are interested in rectangles with vertices in grid points, i.e., the points located at the intersections of vertical and horizontal line segments, and having vertical or horizontal sides. The above grid has dimensions 3 × 2.</p>

<p>And how many such rectangles of perimeter at least 6 can be found in the figure? You can find the answer in the Example section.</p>

### 입력 

 <p>The first and only line of the standard input contains three integers: n, m and p (1 ≤ n, m ≤ 5,000, 4 ≤ p ≤ 2(n+m)), representing the dimensions of the grid and the lower bound for the perimeter of the rectangles.</p>

### 출력 

 <p>In the first line of the standard output your program should output one integer: the number of rectangles with vertices in grid points of the grid n × m, having vertical or horizontal sides and which perimeter is at least p.</p>

