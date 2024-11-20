# [Silver III] Lifting Walls - 11188 

[문제 링크](https://www.acmicpc.net/problem/11188) 

### 성능 요약

메모리: 108080 KB, 시간: 96 ms

### 분류

브루트포스 알고리즘, 기하학

### 제출 일자

2024년 11월 20일 15:20:46

### 문제 설명

<p>The local building firm needs your help. They are building an apartment building where the walls are prefabricated and lifted in place using cranes. The building firm has located n possible locations for cranes, and needs to choose some of these so that the center of each wall can be reached by at least one crane. The cranes are quite expensive, so they want to use as few of them as possible. A crane can reach a wall if the wall’s center is at most a distance r away.</p>

<p>The house that is to be built is rectangular with a length ℓ and width w.</p>

<p>Find the minimum number of cranes required to reach the center of all four walls.</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11188/1.png" style="height:149px; width:179px"></p>

<p style="text-align:center">Figure C.1: This example corresponds to sample input 1.</p>

### 입력 

 <p>The first line of input contains four space-separated positive integers ℓ, w, n and r, all at most 30. ℓ and w denote the length and width of the house, n denotes the number of possible crane locations, and r denotes the reaching distance of each crane.</p>

<p>This is followed by n lines, each containing two integers x and y (−100 ≤ x, y ≤ 100), denoting a possible location for a crane. The coordinate system has its origin in the center of the building and the x-coordinate along the length of the house. The walls thus have their centers at (x, y) = (−ℓ/2, 0),(ℓ/2, 0),(0, −w/2),(0, w/2).</p>

### 출력 

 <p>Output one integer, the minimum number of cranes required to reach all wall segments, or Impossible if not all wall segments can be reached.</p>

