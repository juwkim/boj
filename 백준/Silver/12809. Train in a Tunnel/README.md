# [Silver II] Train in a Tunnel - 12809 

[문제 링크](https://www.acmicpc.net/problem/12809) 

### 성능 요약

메모리: 171076 KB, 시간: 340 ms

### 분류

그리디 알고리즘

### 제출 일자

2025년 3월 14일 18:05:47

### 문제 설명

<p>Peter has decided to take a journey. He is traveling in a train right now. The train has n cars, the length of the i-th car is a<sub>i</sub> meters. Let us ignore distance between the cars.</p>

<p>Peter noticed that some cars have the light on, while some have the light off. The train is approaching a tunnel that has length of h meters. Peter doesn't want there was a moment when only cars with the light off were in the tunnel. Peter calls a moment dark if all cars that have some non-zero length part in a tunnel have the light off. To avoid dark moments, Peter wants to turn the light on in some cars.</p>

<p>Help Peter to turn the light on in the minimal number of cars, that there were no dark moment while the train passes the tunnel.</p>

### 입력 

 <p>Input contains several tests. The first line contains one integer t (1 ≤ t ≤ 100) — the number of tests. The tests follow.</p>

<p>Each test has the following structure. The first line of the test contains two integers: n and h (1 ≤ n ≤ 10<sup>5</sup>, 1 ≤ h ≤ 10<sup>9</sup>) — the number of cars and the length of the tunnel. The second line contains n integers a<sub>i</sub> (1 ≤ a<sub>i</sub> ≤ 10<sup>9</sup>) — the lengths of the cars. The third line contains n integers, the i-th of them is 1 if the i-th car initially has the light on, or 0 if it has the light off. Cars are described in order they would enter the tunnel.</p>

<p>The sum of values of n for all tests doesn't exceed 10<sup>6</sup>.</p>

### 출력 

 <p>For each test case output one integer — the minimal number of cars that Peter must turn the light on so that there were no dark moment.</p>

