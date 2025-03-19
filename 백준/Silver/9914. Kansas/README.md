# [Silver II] Kansas - 9914 

[문제 링크](https://www.acmicpc.net/problem/9914) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 3월 20일 07:57:18

### 문제 설명

<p>The road map of Kansas, USA, is a grid where there are straight roads North-South and straight roads East-West each 1 mile apart.  A truck driver gets instructions in the following form.  Drive for two hours north at 45 miles per hour, then for 5 hours west at 65 miles per hour, etc.  The driver will have to take a break of 1 hour after 5 hours of continuous driving.  The aim is to compute, after how many breaks the driver for the first time passes through or finally returns to the place where she started from.</p>

### 입력 

 <p>The first line contains an integer (≤ 1000) which is the number of instructions, followed by one line for each instruction, indicating the direction, the number of hours h (1 ≤ h ≤ 200) and the speed s (1 ≤ s ≤ 200) in miles per hour in this order.  The geographical directions are indicated by the position of the small hand on an analog clock; 12 stands for north, 6 for south, 9 for west, and 3 for east.</p>

### 출력 

 <p>The output contains an integer which is the number of breaks taken before the driver for the first time passes through or finally returns to the place where she started from.  If the driver does not reach or pass through the place where she started from after following all instructions, the output file should contain the number -1.</p>

