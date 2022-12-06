# [Bronze I] Archaeological Digs - 5088 

[문제 링크](https://www.acmicpc.net/problem/5088) 

### 성능 요약

메모리: 30840 KB, 시간: 488 ms

### 분류

구현(implementation)

### 문제 설명

<p>Archaeologists at a dig typically divide up the area they are examining into a grid, and will record in which grid cell each item is found. It is thus quite easy to tell how many items were found in a given cell.</p>

### 입력 

 <p>In this problem you will be given a number of scenarios. Each scenario begins with a line containing two digits X and Y (separated by a space) representing the length and width of the grid (0 < X, Y <= 100). A scenario in which X and Y are both 0 marks the end of input.</p>

<p>The second line of the scenario is a single digit M (0 < M <= 10000) which gives the number of items located by the archaeologists. This is followed by M lines each containing the X and Y coordinates of the grid cell in which an item was found. Note that the grid coordinate system starts at 0, 0 and that several items may be found in a particular cell, so cell coordinates may be repeated.</p>

<p>Following the M lines of item locations there is a list of cell references for which the total number of found items is required. The first line of this section is a single integer, N, which gives the number of cells (0 < N <= (X * Y)). There follows N lines each containing the X and Y coordinates of a cell.</p>

### 출력 

 <p>Output consists of a single line for each scenario. It contains the total number of items found in the N cells listed.</p>

