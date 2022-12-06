# [Silver V] Frame - 10353 

[문제 링크](https://www.acmicpc.net/problem/10353) 

### 성능 요약

메모리: 28776 KB, 시간: 76 ms

### 분류

많은 조건 분기(case_work), 수학(math), 정수론(number_theory)

### 문제 설명

<p>Let's consider a X×Y rectangle with the middle (X – 2)×(Y – 2) rectangle cut out. We will call this figure a frame with size X×Y. Picture 1 shows the frame 5 × 6.</p>

<p><img alt="" src="" style="height:191px; width:559px"></p>

<p>Let's assume that we have unlimited number of tiles with size A×1. We consider the following problem: is it possible to completely pave a frame with size X×Y using these tiles (tiles can be rotated by 90 degrees). For example, frame 5×6 from Picture 1 can be paved completely with tiles of size 3×1 (one way to do so is shown in Picture 2), but can’t be paved with tiles of size 4×1.</p>

### 입력 

 <p>The first input line contains 2 integers – X and Y (3 ≤ X ≤ 10<sup>6</sup>, 3 ≤ Y ≤ 10<sup>6</sup>). The second line contains integer N – the number of tile types to be analyzed (1 ≤ N ≤ 1000). Each of following N lines contains one integer, not exceeding 10<sup>6</sup>. We designate with A<sub>K</sub> the integer on the (k+2)-th line of the input file.</p>

### 출력 

 <p>Your goal is to print N lines, where the K-th line should contain the word "YES", if it is possible to tile the frame with size X × Y with tiles A<sub>K</sub> × 1, and the word "NO" otherwise.</p>

