# [Silver II] Tower Climbing - 25820 

[문제 링크](https://www.acmicpc.net/problem/25820) 

### 성능 요약

메모리: 113052 KB, 시간: 120 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 2월 22일 23:09:07

### 문제 설명

<p>You are speed running a game where you need to jump on various platforms and reach the top of the tower. The tower has multiple uniformly spaced layers. Each layer contains a single platform. The platform is so narrow that it can be thought of as a point. Depending on upgrades, your character can jump at most k layers up (in a single jump). The time it takes to jump from one point (platform) to another point is defined by the following equation:</p>

<p>Time((x1, y1), (x2, y2)) = |x1 - x2| + (y1 - y2)<sup>2</sup></p>

<p>where x1 and x2 represent (respectively) the x location of your starting and ending points (platforms) in a jump, and y1 and y2 represent (respectively) the layer for the starting and ending platforms for the jump.</p>

<p>Note that the layers are numbered sequentially starting at 1, i.e., the y coordinate of platforms going up are 1, 2, 3, etc. Note also that, as indicated by the Time formula and shown in the picture, the time it takes to jump to a nearby layer is less than the time it takes to jump to a layer farther away.</p>

<p>You start at the first layer and finish at the last layer. You’d like to confirm that you have the optimal strategy, time wise.</p>

<p>Given the x location of the platforms and the maximum height you can jump, determine the least amount of time to reach the top of the tower.</p>

### 입력 

 <p>The first input line contains two integers: n (2 ≤ n ≤ 20,000), indicating the number of layers, and k (1 ≤ k ≤ 8), indicating the maximum height you can jump. Each of the next n input lines contains an integer (between 1 and 1,000,000,000, inclusive), indicating the x coordinate of a platform. The platforms are provided in order from starting point to ending point (going up the tower), i.e., the y coordinate for platforms will be 1, 2, 3, etc. (so the y coordinates are provided in the input implicitly rather than explicitly).</p>

### 출력 

 <p>Print the total amount of time it takes to reach the top (last) platform from the bottom (first) platform.</p>

