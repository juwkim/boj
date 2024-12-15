# [Silver II] To the Max - 6374 

[문제 링크](https://www.acmicpc.net/problem/6374) 

### 성능 요약

메모리: 110880 KB, 시간: 320 ms

### 분류

브루트포스 알고리즘, 다이나믹 프로그래밍, 누적 합

### 제출 일자

2024년 12월 15일 10:28:09

### 문제 설명

<p>Given a two-dimensional array of positive and negative integers, a sub-rectangle is any contiguous sub-array of size 1 × 1 or greater located within the whole array. The sum of a rectangle is the sum of all the elements in that rectangle. In this problem the sub-rectangle with the largest sum is referred to as the maximal sub-rectangle.</p>

<p>As an example, the maximal sub-rectangle of the array:</p>

<pre> 0 -2 -7 0
 9  2 -6 2
-4  1 -4 1
-1  8 0 -2</pre>

<p>is in the lower left corner:</p>

<pre> 9 2
-4 1
-1 8</pre>

<p>and has a sum of 15.</p>

### 입력 

 <p>The input consists of an N × N array of integers. The input begins with a single positive integer N on a line by itself, indicating the size of the square two-dimensional array. This is followed by N<sup>2</sup> integers separated by whitespace (spaces and newlines). These are the N<sup>2</sup> integers of the array, presented in row-major order. That is, all numbers in the first row, left to right, then all numbers in the second row, left to right, etc. N may be as large as 100. The numbers in the array will be in the range [-127,127].</p>

### 출력 

 <p>Output the sum of the maximal sub-rectangle.</p>

