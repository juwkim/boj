# [Silver III] Hiding Nuts - 18306 

[문제 링크](https://www.acmicpc.net/problem/18306) 

### 성능 요약

메모리: 110548 KB, 시간: 128 ms

### 분류

브루트포스 알고리즘, 누적 합

### 제출 일자

2024년 4월 2일 11:49:26

### 문제 설명

<p>Bob, a squirrel, has set up N hiding places throughout his territory, where he stores nuts before the winter. The hiding places are placed at integer coordinates on a grid. He would like to select one of those hiding places as his main den. He is very worried about his nuts being eaten by other animals. He would therefore like to choose a den that minimizes the average distance of the paths between the den and the N − 1 remaining hiding places.</p>

<p>Bob has kind of a poor sense of direction. In order not to get lost between his den and each hiding place, he decides that he will only travel using the horizontal and vertical lines of the grid at integer coordinates.</p>

<p>For instance, the distance between the points D and E in the following grid is 4 (one path of minimal length between D and E is drawn in red below), and the average distance between D and the other points is 13/5 .</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/cbbe3c94-ecd1-4897-802e-e0c17c6ce4f0/-/preview/" style="width: 279px; height: 236px;"></p>

### 입력 

 <p>The input consists of the following lines:</p>

<ul>
	<li>on the first line: the total number N of hiding places, an integer;</li>
	<li>on the next N lines: X<sub>i</sub> and Y<sub>i</sub>, the integer coordinates of the i-th hiding place, separated by a space.</li>
</ul>

### 출력 

 <p>The coordinates of a hiding place that minimizes the distance to the other hiding places. In case of equality, that hiding place must be the one with the smallest X coordinate and, in case there is still equality, with the smallest Y coordinate.</p>

