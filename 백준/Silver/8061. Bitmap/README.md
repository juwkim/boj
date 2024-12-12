# [Silver II] Bitmap - 8061 

[문제 링크](https://www.acmicpc.net/problem/8061) 

### 성능 요약

메모리: 115492 KB, 시간: 364 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 12월 12일 20:25:21

### 문제 설명

<p>There is given a rectangular bitmap of size n x m. Each pixel of the bitmap is either white or black, but at least one is white. The pixel in i-th line and j-th column is called the pixel (i,j). The distance between two pixels p1=(i<sub>1</sub>,j<sub>1</sub>) and p2=(i<sub>2</sub>,j<sub>2</sub>) is defined as:</p>

<p>d(p<sub>1</sub>,p<sub>2</sub>)=|i<sub>1</sub>-i<sub>2</sub>|+|j<sub>1</sub>-j<sub>2</sub>|.</p>

<p>Write a program which:</p>

<ul>
	<li>reads the description of the bitmap from standard input,</li>
	<li>for each pixel, computes the distance to the nearest white pixel,</li>
	<li>writes the results to the standard output.</li>
</ul>

### 입력 

 <p>First line of the standard input there is a pair of integer numbers n, m separated by a single space, 1 ≤ n ≤ 182, 1 ≤ m ≤ 182. In each of the following n lines of the input exactly one zero-one word of length m, the description of one line of the bitmap, is written. On the j-th position in the line (i+1), 1 ≤ i ≤ n, 1 ≤ j ≤ m, is 1 if, and only if the pixel (i,j) is white.</p>

### 출력 

 <p>In the i-th line of the standard output, 1 ≤ i ≤ n, there should be written m integers f(i,1),…,f(i,m) separated by single spaces, where f(i,j) is the distance from the pixel (i,j) to the nearest white pixel.</p>

