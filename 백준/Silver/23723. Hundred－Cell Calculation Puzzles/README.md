# [Silver I] Hundred-Cell Calculation Puzzles - 23723 

[문제 링크](https://www.acmicpc.net/problem/23723) 

### 성능 요약

메모리: 111488 KB, 시간: 128 ms

### 분류

그래프 이론, 그래프 탐색

### 제출 일자

2025년 5월 9일 21:48:36

### 문제 설명

<p>The <i>hundred-cell calculation</i> is a kind of calculation training. In hundred-cell calculation, a sheet with ten by ten empty cells is given. Numbers, 0 through 9, are written on the top of the ten columns in an arbitrary order. 0 through 9 are also written at the left of the ten rows in an arbitrary order. You are to fill the empty cells with the sums of the top and left numbers, as an example shown in the figure below.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/fc80f0ac-a9c5-4cf7-b74e-5b38e2726643/-/preview/" style="width: 400px; height: 400px;"></p>

<p>You may think of more generalized drills. Such a drill has different numbers of the columns and rows, say <i>w</i> × <i>h.</i> The numbers to be written on the top and the left can be any integers.</p>

<p>Hideo is designing a puzzle based on the generalized hundred-cell calculation. A sheet is given in which some of answer cells are filled with numbers, but numbers on the top and the left are omitted. The puzzle is to find these omitted numbers consistent with the filled numbers.</p>

<p>Hideo decided to construct puzzles by preparing sheets filled with all the correct sums and then removing some of these sums. This guarantees that the puzzle has at least one solution. The existence of the solution, however, is not enough; it should be unique.</p>

<p>Hideo has found through many trials that, when the leftmost of the numbers on the top is fixed to be 0, puzzles with <i>w</i> × <i>h</i> cells may have a unique solution when <i>w</i> + <i>h</i> − 1 sums are kept. He, however, could not figure out which cells to keep for a single unique solution.</p>

<p>Your task is to help Hideo by writing a program that judges solution uniqueness for each of the puzzle candidates he has made.</p>

### 입력 

 <p>The input consists of at most 100 datasets, each in the following format.</p>

<pre><i>w</i> <i>h</i>
<i>x</i><sub>1</sub> <i>y</i><sub>1</sub> <i>n</i><sub>1</sub>
...
<i>x</i><sub><i>k</i></sub> <i>y</i><sub><i>k</i></sub> <i>n</i><sub><i>k</i></sub></pre>

<p><i>w</i> and <i>h</i> in the first line are the numbers of answer cells in one row and in one column, respectively (2 ≤ <i>w</i> ≤ 100 and 2 ≤ <i>h</i> ≤ 100). There remain <i>k</i> numbers (<i>k</i> = <i>w</i> + <i>h</i> − 1) in the answer cells. The <i>k</i> lines starting from the second show that the number <i>n<sub>i</sub></i> is in the cell <i>x<sub>i</sub></i>-th from the left and <i>y<sub>i</sub></i>-th from the top. <i>x<sub>i</sub></i>, <i>y<sub>i</sub></i>, <i>n<sub>i</sub></i> are integers satisfying 1 ≤ <i>x<sub>i</sub></i> ≤ <i>w</i>, 1 ≤ <i>y<sub>i</sub></i> ≤ <i>h</i>, and −100 ≤ <i>n<sub>i</sub></i> ≤ 100. Here, <i>x</i> = 1 means the leftmost and <i>y</i> = 1 means the topmost. Either of <i>x<sub>i</sub></i> ≠ <i>x<sub>j</sub></i> or <i>y<sub>i</sub></i> ≠ <i>y<sub>j</sub></i> holds for different <i>i</i> and <i>j</i>.</p>

<p>The end of the input is indicated by a line containing two zeros separated by a space.</p>

### 출력 

 <p>For each dataset, output YES if the puzzle has a unique solution, and NO otherwise, in a line.</p>

