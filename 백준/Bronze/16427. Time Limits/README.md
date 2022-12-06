# [Bronze III] Time Limits - 16427 

[문제 링크](https://www.acmicpc.net/problem/16427) 

### 성능 요약

메모리: 121220 KB, 시간: 112 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Your Chief Judge needs help! He needs to set the time limit for a problem in the problem set. He has n solutions written by his judges. He knows how long each runs in the contest environment, in milliseconds. He wants to set the time limit to be at least s times the slowest solution from his judges, but as small as possible, and he wants it to be an integral number of seconds. Can you help him?</p>

### 입력 

 <p>Each input will consist of a single test case. Note that your program may be run multiple times on different inputs.</p>

<p>Each test case will begin with a line containing two space-separated integers n (1 ≤ n ≤ 100) and s (1 ≤ s ≤ 20), where n is the number of solutions from judges, and s is the multiplying factor.</p>

<p>The next line will contain n space-separated integers m (1 ≤ m ≤ 2,000), which are the number of milliseconds it takes for some judge’s solution to run in the contest environment.</p>

### 출력 

 <p>Output a single integer, which is the time limit to set for this problem. It should be in seconds, and the smallest time that is at least s times the slowest judge’s solution.</p>

