# [Silver I] Mouse Journey - 6771 

[문제 링크](https://www.acmicpc.net/problem/6771) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 5월 4일 03:32:16

### 문제 설명

<p>You are a mouse that lives in a cage in a large laboratory. The laboratory is composed of one rectangular grid of square cages, with a total of R rows and C columns of cages (1 ≤ R, C ≤ 25).</p>

<p>To get your exercise, the laboratory owners allow you to move between cages. You can move between cages either by moving right between two adjacent cages in the same row, or by moving down between two adjacent cages in the same column. You cannot move diagonally, left or up.</p>

<p>Your cage is in one corner of the laboratory, which has the label (1, 1) (to indicate top-most row, left-most column). You would like to visit your brother who lives in the cage labelled (R, C) (bottom-most row, right-most column), which is in the other corner diagonally. However, there are some cages which you cannot pass through, since they contain cats.</p>

<p>Your brother, who loves numbers, would like to know how many different paths there are between your cage and his that do not pass through any cat cage. Write a program to compute this number of cat-free paths.</p>

### 입력 

 <p>The first line of input contains two integers R and C, separated by one space representing the number of rows and columns (respectively). On the second line of input is the integer K, the number of cages that contain cats. The next K lines each contain the row and column positions (in that order) for a cage that contains a cat. None of the K cat cages are repeated, and all cages are valid positions. Note also that (1, 1) and (R, C) will not be cat cages.</p>

### 출력 

 <p>Output the non-negative integer value representing the number of paths between your cage at position (1, 1) and your brother’s cage at position (R, C). You can assume the output will be strictly less than 1 000 000 000.</p>

