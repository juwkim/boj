# [Silver I] Pascal's Travels - 4620 

[문제 링크](https://www.acmicpc.net/problem/4620) 

### 성능 요약

메모리: 110760 KB, 시간: 100 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 4월 7일 20:54:04

### 문제 설명

<p>An n x n game board is populated with integers, one nonnegative integer per square. The goal is to travel along any legitimate path from the upper left corner to the lower right corner of the board. The integer in any one square dictates how large a step away from that location must be. If the step size would advance travel off the game board, then a step in that particular direction is forbidden. All steps must be either to the right or toward the bottom. Note that a 0 is a dead end which prevents any further progress.</p>

<p>Consider the 4 x 4 board shown in Figure 1, where the solid circle identifies the start position and the dashed circle identifies the target. Figure 2 shows the three paths from the start to the target, with the irrelevant numbers in each removed.</p>

<p style="text-align:center"><img alt="" src="https://www.acmicpc.net/upload/images2/image001.gif" style="height:147px; width:147px"></p>

<p style="text-align:center">Figure 1</p>

<p style="text-align:center"><img alt="" src="https://www.acmicpc.net/upload/images2/image002.gif" style="height:147px; width:460px"></p>

<p style="text-align:center">Figure 2</p>

### 입력 

 <p>The input contains data for one to thirty boards, followed by a final line containing only the integer -1. The data for a board starts with a line containing a single positive integer n, 4 ≤ n ≤ 34, which is the number of rows in this board. This is followed by n rows of data. Each row contains n single digits, 0-9, with no spaces between them. </p>

### 출력 

 <p>The output consists of one line for each board, containing a single integer, which is the number of paths from the upper left corner to the lower right corner. There will be fewer than 2<sup>63</sup> paths for any board.</p>

