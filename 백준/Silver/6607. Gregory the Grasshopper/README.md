# [Silver I] Gregory the Grasshopper - 6607 

[문제 링크](https://www.acmicpc.net/problem/6607) 

### 성능 요약

메모리: 114756 KB, 시간: 540 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 5월 4일 04:48:18

### 문제 설명

<p>Gregory is a grasshopper. His favourite food are clover leafs — he can simply never have enough of them. Whenever he spots such a leaf, he wants to eat it as quickly as possible. Gregory is also lazy, so he wants to move to the leaf with minimal effort. Your task is to help him to find the shortest way to a clover leaf.</p>

<p>For simplicity, we will assume that Gregory lives on a rectangular grid consisting of unit squares. As a grasshopper, he prefers to move by jumping (or, more exactly, hopping) from one square to the other. Each hop takes him to a square that is in the adjacent row or column in one direction, and two columns or rows away in the other direction. So, his hops resemble the moves of a knight on a chessboard.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images2/grass.png" style="height:248px; width:246px"></p>

### 입력 

 <p>The input consists of several test cases, each of them specified by six integer numbers on one line: R, C, G<sub>R</sub>, G<sub>C</sub>, L<sub>R</sub>, and L<sub>C</sub>. R and C specify the size of the grid in unit squares, 1 ≤ R, C ≤ 100. Gregory cannot hop outside a rectangle of this size, because it would be too dangerous. The values of G<sub>R</sub>, G<sub>C</sub> are the coordinates of the square that Gregory is standing on, and L<sub>R</sub>, L<sub>C</sub> are the coordinates of the square with the delicious clover leaf. (1 ≤ G<sub>R</sub>, L<sub>R</sub> ≤ R; 1 ≤ G<sub>C</sub>, L<sub>C</sub> ≤ C)</p>

### 출력 

 <p>For each test case, print one integer number — the minimal number of hops that Gregory needs to reach the square with his beloved delicacy. If it is not possible to reach that square at all, print the word “impossible” instead.</p>

