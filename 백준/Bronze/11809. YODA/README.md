# [Bronze I] YODA - 11809 

[문제 링크](https://www.acmicpc.net/problem/11809) 

### 성능 요약

메모리: 113248 KB, 시간: 108 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>A long, long time ago in a galaxy far, far away a big collision of integers is taking place right now. What happens when two integers collide? During collision, each digit of one number compares itself to the corresponding digit of the other number (the least significant digit with the other’s least significant digit, and so on). The smaller digit “falls out” of the number containing it. Additionally, if the digits are the same, nothing happens. If a number doesn’t consist of a corresponding digit, then we consider it to be zero. After all comparisons of corresponding digits, the leftover digits in the number come closer and create a new number. For example:</p>

<p style="text-align: center;"><img alt="" src="" style="height:100px; width:517px"></p>

<p>Write a programme that will, for two given integers, determine their values after collision. If it happens that all the digits of one number fell out, then for that number output the message “YODA”.</p>

### 입력 

 <p>The first line of input contains the integer N (1 ≤ N ≤ 10<sup>9</sup>), one of the integers from the task. The second line of input contains the integer M (1 ≤ N ≤ 10<sup>9</sup>), one of the integers from the task.</p>

### 출력 

 <p>The first line of output must contain the new value of the first given integer from the task. The second line of output must contain the new value of the second given integer from the task.</p>

