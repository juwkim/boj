# [Silver IV] Physics Experiment - 23731 

[문제 링크](https://www.acmicpc.net/problem/23731) 

### 성능 요약

메모리: 134336 KB, 시간: 284 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation), 수학(math)

### 문제 설명

<p>Yunee is taking a physics lab class. One day, after an experiment, Yunee noticed that some figures in the experiment result came out lower than expected. So Yunee decided to manipulate the result by rounding the values several times.</p>

<p>When rounding a number to the $i$-th place, it is rounded down if the digit one place right to the $i$-th place is less than $5$. Otherwise, it is rounded up. For example, rounding $454$ to the nearest tens gives $450$. On the other hand, rounding $454$ to the nearest hundreds gives $500$.</p>

<p>By rounding $454$ to the nearest hundreds and then thousands, we get $454 \rightarrow 500 \rightarrow 1000$. This is the maximum value we can get by rounding $454$ zero or more times.</p>

<p>Help Yunee maximize the value in the experiment result by rounding it zero or more times.</p>

### 입력 

 <p>The first line contains an integer $N$ representing the value in the experiment result $(1\le N \le 10^{15})$. <strong>Note that $N$ may exceed the 32-bit integer limit.</strong></p>

### 출력 

 <p>Output the maximized value by rounding $N$ zero or more times. The output should not have leading zeros.</p>

