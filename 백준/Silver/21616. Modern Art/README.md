# [Silver II] Modern Art - 21616 

[문제 링크](https://www.acmicpc.net/problem/21616) 

### 성능 요약

메모리: 122560 KB, 시간: 296 ms

### 분류

애드 혹, 수학

### 제출 일자

2024년 12월 17일 21:46:11

### 문제 설명

<p>A new and upcoming artist has a unique way to create checkered patterns. The idea is to use an M-by-N canvas which is initially entirely black. Then the artist repeatedly chooses a row or column and runs their magic brush along the row or column. The brush changes the colour of each cell in the row or column from black to gold or gold to black.</p>

<p>Given the artist’s choices, your job is to determine how much gold appears in the pattern determined by these choices.</p>

### 입력 

 <p>The first line of input will be a positive integer M. The second line of input will be a positive integer N. The third line of input will be a positive integer K. The remaining input will be K lines giving the choices made by the artist. Each of these lines will either be R followed by a single space and then an integer which is a row number, or C followed by a single space and then an integer which is a column number. Rows are numbered top down from 1 to M. Columns are numbered left to right from 1 to N.</p>

### 출력 

 <p>Output one non-negative integer which is equal to the number of cells that are gold in the pattern determined by the artist’s choices.</p>

