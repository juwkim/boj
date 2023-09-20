# [Silver IV] Defense of a Kingdom - 3532 

[문제 링크](https://www.acmicpc.net/problem/3532) 

### 성능 요약

메모리: 118408 KB, 시간: 164 ms

### 분류

정렬

### 문제 설명

<p>Theodore implements a new strategy game “Defense of a Kingdom”. On each level player defends the Kingdom that is represented by a rectangular grid of cells. The player builds crossbow towers in some cells of the grid. The tower defends all the cells in the same row and the same column. No two towers share a row or a column.</p>

<p>The penalty of the position is a number of cells in the largest undefended rectangle. For example, the position shown on the picture has penalty 12.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6c6ebc3d-5343-4ec0-b9b7-68a137d18591/-/preview/" style="width: 569px; height: 200px;"></p>

<p>Help Theodore write a program that calculates the penalty of the given position.</p>

### 입력 

 <p>The first line of the input file contains three integer numbers: w — width of the grid, h — height of the grid and n — number of crossbow towers (1 ≤ w, h ≤ 40 000; 0 ≤ n ≤ min(w, h)).</p>

<p>Each of the following n lines of the input file contains two integer numbers x<sub>i</sub> and y<sub>i</sub> — the coordinates of the cell occupied by a tower (1 ≤ x<sub>i</sub> ≤ w; 1 ≤ y<sub>i</sub> ≤ h).</p>

### 출력 

 <p>Output a single integer number — the number of cells in the largest rectangle that is not defended by the towers.</p>

