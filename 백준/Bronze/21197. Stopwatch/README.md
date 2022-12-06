# [Bronze III] Stopwatch - 21197 

[문제 링크](https://www.acmicpc.net/problem/21197) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>Robin just received a stopwatch from her grandfather. Robin's stopwatch has a single button. Pressing the button alternates between stopping and starting the stopwatch's timer. When the timer is on, the displayed time increases by 1 every second.</p>

<p>Initially the stopwatch is stopped and the timer reads 0 seconds. Given a sequence of times that the stopwatch button is pressed, determine what the stopwatch's timer displays.</p>

### 입력 

 <p>The first line of input contains a single integer $N$ ($1 \leq N \leq 1\,000$), which is the number of times the stopwatch was pressed.</p>

<p>The next $N$ lines describe the times the stopwatch's button was pressed in increasing order. Each line contains a single integer $t$ ($0 \leq t \leq 10^6$), which is the time the button was pressed. No two button presses happen on the same second.</p>

### 출력 

 <p>Display <code>still running</code> if the stopwatch's timer is still running after all button presses were made. Otherwise display the number of seconds displayed on the stopwatch's timer.</p>

