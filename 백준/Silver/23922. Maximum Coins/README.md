# [Silver V] Maximum Coins - 23922 

[문제 링크](https://www.acmicpc.net/problem/23922) 

### 성능 요약

메모리: 214652 KB, 시간: 1980 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>Mike has a square matrix with <b>N</b> rows and <b>N</b> columns. Cell (i,j) denotes the cell present at row i and column j. Cell (1,1) denotes the top left corner of the matrix. Each cell has some amount of coins associated with it and Mike can collect them only if he visits that cell. <b>C<sub>i,j</sub></b> represents the number of coins in cell with row i and column j. From a cell (i,j), Mike can decide to go to cell (i+1,j+1) or cell (i-1,j-1), as long as the cell lies within the boundaries of the matrix and has not been visited yet. He can choose to start the journey from any cell and choose to stop at any point. Mike wants to maximize the number of coins he can collect. Please help him determine the maximum number of coins he can collect.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow. Each test case begins with a line containing the integer <b>N</b>. The next <b>N</b> lines contain <b>N</b> integers each. The j-th integer in the i-th line represents the number of coins <b>C<sub>i,j</sub></b> in cell (i,j).</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the maximum number of coins Mike can collect.</p>

