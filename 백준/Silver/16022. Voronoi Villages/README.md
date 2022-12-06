# [Silver V] Voronoi Villages - 16022 

[문제 링크](https://www.acmicpc.net/problem/16022) 

### 성능 요약

메모리: 113248 KB, 시간: 112 ms

### 분류

정렬(sorting)

### 문제 설명

<p>In the country of Voronoi, there are N villages, located at distinct points on a straight road. Each of these villages will be represented by an integer position along this road.</p>

<p>Each village defines its neighbourhood as all points along the road which are closer to it than to any other village. A point which is equally close to two distinct villages A and B is in the neighbourhood of A and also in the neighbourhood of B.</p>

<p>Each neighbourhood has a size which is the difference between the minimum (leftmost) point in its neighbourhood and the maximum (rightmost) point in its neighbourhood.</p>

<p>The neighbourhoods of the leftmost and rightmost villages are defined to be of infinite size, while all other neighbourhoods are finite in size.</p>

<p>Determine the smallest size of any of the neighbourhoods (with exactly 1 digit after the decimal point)</p>

### 입력 

 <p>The first line will contain the number N (3 ≤ N ≤ 100), the number of villages. On the next N lines there will be one integer per line, where the ith line contains the integer V<sub>i</sub>, the position of the ith village (−1 000 000 000 ≤ V<sub>i</sub> ≤ 1 000 000 000). All villages are at distinct positions.</p>

### 출력 

 <p>Output the smallest neighbourhood size with exactly one digit after the decimal point.</p>

