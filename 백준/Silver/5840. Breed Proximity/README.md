# [Silver V] Breed Proximity - 5840 

[문제 링크](https://www.acmicpc.net/problem/5840) 

### 성능 요약

메모리: 214644 KB, 시간: 2048 ms

### 분류

구현(implementation)

### 문제 설명

<p>Farmer John's N cows (1 <= N <= 50,000) are standing in a line, each described by an integer breed ID.</p><p>Cows of the same breed are at risk for getting into an argument with each-other if they are standing too close.  Specifically, two cows of the same breed are said to be "crowded" if their positions within the line differ by no more than K (1 <= K < N).</p><p>Please compute the maximum breed ID of a pair of crowded cows.</p>

### 입력 

 <ul><li>Line 1: Two space-separated integers: N and K.</li><li>Lines 2..1+N: Each line contains the breed ID of a single cow in the line.  All breed IDs are integers in the range 0..1,000,000.</li></ul>

### 출력 

 <ul><li>Line 1: The maximum breed ID of a crowded pair of cows, or -1 if there is no crowded pair of cows.</li></ul>

