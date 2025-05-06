# [Silver I] Collecting Stars - 16614 

[문제 링크](https://www.acmicpc.net/problem/16614) 

### 성능 요약

메모리: 134432 KB, 시간: 352 ms

### 분류

자료 구조, 우선순위 큐

### 제출 일자

2025년 5월 6일 19:04:08

### 문제 설명

<p>You are planning to complete the latest Super Mario game as fast as you can. In this game, there are n stars that can be collected and your objective is to collect any k of them. Each star takes a certain amount of time to get. After collecting a star, Mario will reappear at the start of the game, so the time taken to collect any sequence of stars is the same regardless of the order that they are collected in. However, some stars do not become available for collection until a certain quantity of stars has already been collected.</p>

<p>Given a description of the stars, determine the fastest time in which you could collect k of them or determine that it is impossible to do so.</p>

### 입력 

 <p>The input starts with a line containing two integers n (1 ≤ n ≤ 200 000), which is the number of stars, and k (1 ≤ k ≤ n), which is the number of stars you must collect.</p>

<p>The following n lines describe the stars. Each of these lines contains two integers t (1 ≤ t ≤ 10<sup>9</sup>), which is the amount of time it will take to collect the star, and d (0 ≤ d < n), which is the number of stars that must be collected before the star is available.</p>

### 출력 

 <p>Display the minimum amount of time to collect k stars. If you cannot collect k stars, display <code>IMPOSSIBLE</code>.</p>

