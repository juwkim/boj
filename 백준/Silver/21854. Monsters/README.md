# [Silver II] Monsters - 21854 

[문제 링크](https://www.acmicpc.net/problem/21854) 

### 성능 요약

메모리: 139776 KB, 시간: 208 ms

### 분류

분할 정복을 이용한 거듭제곱, 수학

### 제출 일자

2024년 12월 17일 04:55:24

### 문제 설명

<p>The 2017 International Congress of Monsters gathers n monsters coming from all over the world. Their chairman has to solve the following problem: if the i<sup>th</sup> monster (1 ≤ i ≤ n) has k<sub>i</sub> fingers, indexed from 0 to k<sub>i</sub> - 1, so he can lift j of those fingers (0 ≤ j ≤ k<sub>i</sub>), obtaining a certain number, in the following way: if a certain finger is lifted, 2<sup>finger index</sup> is added to the current number. As a result, the i<sup>th</sup> monster can count on his fingers nr<sub>i</sub> distinct numbers. Therefore, the demanded result is nr<sub>1</sub> + nr<sub>2</sub> + … + nr<sub>n</sub>, modulo 10<sup>9</sup>+7.</p>

<p>Compute the required sum, modulo 10<sup>9</sup>+7.</p>

### 입력 

 <p>The first line of the input contains the number n.</p>

<p>The second line contains n positive integers, k<sub>1</sub>, k<sub>2</sub>, …, k<sub>n</sub>, representing the numbers of fingers of each monster.</p>

### 출력 

 <p>The output must contain a single positive integer, the requested sum, modulo 10<sup>9</sup>+7.</p>

