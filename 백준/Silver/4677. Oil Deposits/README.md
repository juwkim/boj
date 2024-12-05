# [Silver II] Oil Deposits - 4677 

[문제 링크](https://www.acmicpc.net/problem/4677) 

### 성능 요약

메모리: 114036 KB, 시간: 140 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 12월 6일 04:28:37

### 문제 설명

<p>The GeoSurvComp geologic survey company is responsible for detecting underground oil de- posits. GeoSurvComp works with one large rectangular region of land at a time, and creates a grid that divides the land into numerous square plots. It then analyzes each plot separately, using sensing equipment to determine whether or not the plot contains oil. A plot containing oil is called a pocket. If two pockets are adjacent, then they are part of the same oil deposit. Oil deposits can be quite large and may contain numerous pockets. Your job is to determine how many different oil deposits are contained in a grid.</p>

### 입력 

 <p>The input file contains one or more grids. Each grid begins with a line containing m and n, the number of rows and columns in the grid, separated by a single space. If m = 0 it signals the end of the input; otherwise 1 ≤ m ≤ 100 and 1 ≤ n ≤ 100. Following this are m lines of n characters each (not counting the end-of-line characters). Each character corresponds to one plot, and is either ‘*’, representing the absence of oil, or ‘@’, representing an oil pocket.</p>

### 출력 

 <p>For each grid, output the number of distinct oil deposits. Two different pockets are part of the same oil deposit if they are adjacent horizontally, vertically, or diagonally. An oil deposit will not contain more than 100 pockets.</p>

