# [Bronze I] SPIN - 4872 

[문제 링크](https://www.acmicpc.net/problem/4872) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Simulate a locked spinner puzzle.</p>

<p>A locked spinner puzzle is a puzzle where you can only change wheels in groups. It is a common puzzle to achieve some value on the spinners with by only changing them in the allowed groups.</p>

<p>Imagine a row of D numbered wheels, each labeled sequentially with the digits 0 through 9. This is similar to what is on a briefcase combination lock.</p>

<p>Below this are a series of B buttons with labels that are D digits long. For example, D may be 4 and the labels are 1000 1200 1002 0111 and 0100. Pressing the button labeled 1000 moves the first wheel once, but leaves the others alone, while pressing the button labeled 1002 moves the first wheel once and the fourth wheel twice, leaving the center button unchanged.</p>

<p>Your task is to simulate such a locked spinner puzzle giving the final readout of the wheels.</p>

### 입력 

 <p>The input to your program will be a line containing D digits (at most 10) representing the starting positions of the wheels. Following this, each line will have the button label for which button is pressed next.</p>

### 출력 

 <p>The output file should have the standard header, followed by the final positions of the wheels, followed by the standard trailer.</p>

