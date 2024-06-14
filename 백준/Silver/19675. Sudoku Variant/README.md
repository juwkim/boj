# [Silver III] Sudoku Variant - 19675 

[문제 링크](https://www.acmicpc.net/problem/19675) 

### 성능 요약

메모리: 108080 KB, 시간: 116 ms

### 분류

백트래킹, 브루트포스 알고리즘

### 제출 일자

2024년 6월 14일 19:48:06

### 문제 설명

<p>Sudoku is a famous logic puzzle game that is played on a 9x9 grid. In it, the player is required to fill in the grid so that every row, column and 3x3 box contains the digits 1 through 9. In this problem, you will be working on a variant of this puzzle which is played on a 3x3 grid.</p>

<p>Similar to Sudoku, the 3x3 grid you are given is already partially filled with the digits 1 through 9. Your job is to fill in the remaining empty grid positions with the digits 1 through 9 such that the numbers that appear in every row and every column are distinct, i.e. a number cannot be repeated along a row or column.</p>

<p>In the given grid there are at least 1 empty grid position and at most 3 empty grid positions, you may assume that the partially filled grid is consistent with the rules, i.e. no number is duplicated on any row or column. You are required to determine the number of ways the empty positions can be filled.</p>

### 입력 

 <p>The input consists of 3 lines of 3 digits each, the digits are separated by a single space. Each line contains the configuration of one row of the 3x3 grid. The first line represents the first row of the grid; the second line represents the second row and so on. The digit 1 through 9 in the input indicates that the particular grid position is already filled with the digit while the digit 0 indicates that the particular position is empty</p>

### 출력 

 <p>Output the number of ways in which the given puzzle can be solved.</p>

