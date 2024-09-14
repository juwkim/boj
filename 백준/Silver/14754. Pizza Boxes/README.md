# [Silver II] Pizza Boxes - 14754 

[문제 링크](https://www.acmicpc.net/problem/14754) 

### 성능 요약

메모리: 121128 KB, 시간: 276 ms

### 분류

그리디 알고리즘

### 제출 일자

2024년 9월 14일 23:16:09

### 문제 설명

<p>There are pizza boxes all of which have the same dimensions. The boxes are stacked in piles, forming a three- dimensional grid where the heights are all different. The view from front shows the height of the tallest pile in each column, the view from the side shows the height of the tallest pile in each row.</p>

<p>What is the maximum number of pizza boxes we can remove without changing the front and side views? In the following example, Figure I.2 shows the solution of Figure I.1(a) case. In Figure I.1(a) and Figure I.2, each number (height) represents the number of boxes stacked.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14754/1.png" style="height:220px; width:583px"></p>

<p style="text-align: center;">Figure I.1. (a) Grid of heights and (b) the corresponding views.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14754/2.png" style="height:136px; width:127px"></p>

<p style="text-align: center;">Figure I.2. Grid of heights after removing boxes.</p>

<p>Your task is to compute the maximum number of pizza boxes that can be removed without changing the original front and side views.</p>

### 입력 

 <p>Your program is to read from standard input. The input contains two integers, n and m (1 ≤ n, m ≤ 1,000), the number of rows and columns in the grid, respectively. Each of the following n lines contain m integers, the number of pizza boxes (heights) in the corresponding row. All heights are between 0 and 10<sup>9</sup> inclusive and the heights are all different.</p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line for the input. The line should contain the maximum number of pizza boxes that can be removed without changing the original views.</p>

