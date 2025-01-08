# [Silver II] Harvest Waterloo - 32330 

[문제 링크](https://www.acmicpc.net/problem/32330) 

### 성능 요약

메모리: 112592 KB, 시간: 116 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 1월 8일 21:29:56

### 문제 설명

<p>There is a wildly popular new harvest simulation game called Harvest Waterloo. The game is played on a rectangular pumpkin patch which contains bales of hay and pumpkins of different sizes. To begin the game, a farmer is placed at the location of a pumpkin.</p>

<p>The farmer harvests all pumpkins they can reach by moving left, right, up, and down throughout the patch. The farmer cannot move diagonally. The farmer can also not move through a bale of hay nor move outside of the patch.</p>

<p>Your job is to determine the total value of all the pumpkins harvested by the farmer. A small pumpkin is worth <span>$</span>1, a medium pumpkin is worth <span>$</span>5, and a large pumpkin is worth <span>$</span>10 dollars.</p>

### 입력 

 <p>The first line of input is an integer R > 0 which is the number of rows within the patch.</p>

<p>The second line of input is an integer C > 0 which is the number of columns within the patch.</p>

<p>The next R lines describe the patch. Each line will contain C characters and each character will either represent a pumpkin size or a bale of hay: <code>S</code> for a small pumpkin, <code>M</code> for a medium pumpkin, <code>L</code> for a large pumpkin, or <code>*</code> for a bale of hay.</p>

<p>The next line of input is an integer A where 0 ≤ A < R, and the last line of input is an integer B where 0 ≤ B < C. Row A and column B is the starting location of the farmer and the top-left corner of the patch is row 0 and column 0.</p>

### 출력 

 <p>Output the integer, V , which is the total value in dollars of all the pumpkins harvested by the farmer.</p>

