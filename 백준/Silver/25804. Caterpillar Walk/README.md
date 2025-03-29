# [Silver IV] Caterpillar Walk - 25804 

[문제 링크](https://www.acmicpc.net/problem/25804) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 3월 30일 02:50:32

### 문제 설명

<p>Consider a city where each building is a rectangle with its base on the positive x-axis, its two walls parallel to the positive y-axis, and its roof parallel to x-axis. The walls of two buildings can touch each other, i.e., the buildings can be right next to each other. The buildings do not, however, have any area in common, i.e., no two buildings intersect/overlap.</p>

<p>Lulu (our beloved caterpillar) lives at coordinates (0,0) and works at coordinates (100,0). Every morning, Lulu crawls from home to office. Without any buildings, this is a distance of 100 but, unfortunately, the buildings force Lulu to crawl up and down of the building walls and they add to the distance Lulu has to travel. Note that Lulu starts at home, ends at the office, and is always crawling on x-axis, side of a wall going up (parallel to y-axis), top of a building (parallel to x-axis), or side of a wall coming down (parallel to y-axis).</p>

<p>Given the description of all the buildings, compute the total distance travelled by Lulu.</p>

### 입력 

 <p>The first input line contains an integer, n (1 ≤ n ≤ 50), indicating the number of buildings. Each of the next n input lines describes a building. A building is described by three integers: s (1 ≤ s ≤ 98), indicating the lower-left corner of the building, w (1 ≤ w ≤ 98), indicating the width of the building, and h (1 ≤ h ≤ 100), indicating the height of the building. Assume s + w ≤ 99, i.e., no building will end beyond (99,0).</p>

### 출력 

 <p>Print the total distance travelled by Lulu.</p>

