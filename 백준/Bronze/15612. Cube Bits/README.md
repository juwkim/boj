# [Bronze II] Cube Bits - 15612 

[문제 링크](https://www.acmicpc.net/problem/15612) 

### 성능 요약

메모리: 196348 KB, 시간: 1164 ms

### 분류

수학(math)

### 문제 설명

<p>The new computers are here! However, we made a mistake during the order: we thought we were ordering machines with qubits; in fact, we ordered several hundred computers powered by cube-bits.</p>

<p>The programs and data we had ready were prepared in base 10. To feed the data into the new computer, which uses a cubic system of counting, we will need to convert it to base 3 first.</p>

<p>Write a program to convert a stream of decimal numbers into ternary format, so they fit the new system’s input bus.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with an integer n (1 ≤ n ≤ 10<sup>6</sup>), the size of the data stream.</li>
	<li>n lines with one decimal integer v<sub>i</sub> (0 ≤ v < 3<sup>20</sup>), the decimal representation of the i-th integer in the data stream.</li>
</ul>

### 출력 

 <p>Output n lines, giving the numbers converted to base-3, in the same order as given. In the interest of conserving disk space, do not print leading zeroes.</p>

