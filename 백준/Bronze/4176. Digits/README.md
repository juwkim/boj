# [Bronze II] Digits - 4176 

[문제 링크](https://www.acmicpc.net/problem/4176) 

### 성능 요약

메모리: 19104 KB, 시간: 228 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p><img alt="" src="" style="float:right; height:164px; width:270px">A googol written out in decimal has 101 digits. A googolplex has one plus a googol digits. That's a lot of digits!</p>

<p>Given any number x<sub>0</sub>, define a sequence using the following recurrence:</p>

<blockquote>
<p>x<sub>i+1</sub> = the number of digits in the decimal representation of x<sub>i</sub></p>
</blockquote>

<p>Your task is to determine the smallest positive i such that x<sub>i</sub> = x<sub>i-1</sub>.</p>

### 입력 

 <p>Input consists of several lines. Each line contains a value of x<sub>0</sub>. Every value of x<sub>0</sub> is non-negative and has no more than one million digits. The last line of input contains the word END.</p>

### 출력 

 <p>For each value of x<sub>0</sub> given in the input, output one line containing the smallest positive i such that x<sub>i</sub> = x<sub>i-1</sub>.</p>

