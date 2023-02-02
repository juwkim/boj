# [Silver IV] Faulty Odometer - 4861 

[문제 링크](https://www.acmicpc.net/problem/4861) 

### 성능 요약

메모리: 115252 KB, 시간: 1272 ms

### 분류

수학(math), 정수론(number_theory)

### 문제 설명

<p>You are given a car odometer which displays the miles traveled as an integer. The odometer has a defect, however: it proceeds from the digit 3 to the digit 5, always skipping over the digit 4. This defect shows up in all positions (the one's, the ten's, the hundred's, etc.). For example, if the odometer displays 15339 and the car travels one mile, odometer reading changes to 15350 (instead of 15340).</p>

### 입력 

 <p>Each line of input contains a positive integer in the range 1..999999999 which represents an odometer reading. (Leading zeros will not appear in the input.) The end of input is indicated by a line containing a single 0. You may assume that no odometer reading will contain the digit 4.</p>

### 출력 

 <p>Each line of input will produce exactly one line of output, which will contain: the odometer reading from the input, a colon, one blank space, and the actual number of miles traveled by the car.</p>

