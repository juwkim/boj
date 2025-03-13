# [Silver II] Binary Witch - 7864 

[문제 링크](https://www.acmicpc.net/problem/7864) 

### 성능 요약

메모리: 115516 KB, 시간: 196 ms

### 분류

자료 구조, 다이나믹 프로그래밍, 해시를 사용한 집합과 맵, 구현, 시뮬레이션, 문자열

### 제출 일자

2025년 3월 14일 02:09:00

### 문제 설명

<p>Once upon a time in the silent depths of digital forests there lived a Binary Witch. She was able to forecast weather, telling for any day in the future whether it will be rainy or sunny.</p>

<p>Her magic was based on the following ancient rule: let a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>N</sub> be the sequence of binary digits, where a<sub>i</sub> = 0 indicates that i-th day was rainy, and a<sub>i</sub> = 1  that it was sunny. To predict the weather in day N + 1, consider the t-postfix a<sub>N-t+1</sub>, a<sub>N-t+2</sub>, ..., a<sub>N</sub> consisting of the last t elements. If that postfix is encountered somewhere before the position N - t + 1, i.e. if there is such k ≤ N - t, that a<sub>k</sub>= a<sub>N-t+1</sub>, a<sub>k+1</sub> = a<sub>N-t+2</sub>, ..., a<sub>k+t-1</sub> = a<sub>N</sub> then the predicted value will be a<sub>k+t</sub>.</p>

<p>If there is more than one occurrence of t-postfix, then the rightmost one (with maximal k) will be taken. So, to make a prediction, she tried t-postfixes, consequently for t = 13, 12, ..., 1, stopping after the first prediction. If neither postfix was found, she predicted rain (0). If prediction for more than one day is needed, it is assumed that all previous days are predicted correctly, so if first predicted value is b, then we make forecast for day N + 2 based on N + 1 values, where a<sub>N+1</sub> = b.</p>

<p>Because the witch was burned long ago, your task is to write a program to perform her arcane job.</p>

### 입력 

 <p>First line of input file contains two integers N (1 ≤ N ≤ 1000000) and L (1 ≤ L ≤ 1000), separated by space. Second line contains a string of N characters 0 and 1.</p>

### 출력 

 <p>Output file must contain a single string of L characters, which are forecasts for days N + 1, N + 2, ..., N + L.</p>

