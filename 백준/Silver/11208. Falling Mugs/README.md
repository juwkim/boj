# [Silver V] Falling Mugs - 11208 

[문제 링크](https://www.acmicpc.net/problem/11208) 

### 성능 요약

메모리: 114328 KB, 시간: 116 ms

### 분류

브루트포스 알고리즘, 수학

### 문제 설명

<p>Susan is making high-speed videos of falling coffee mugs. When analyzing the videos she wants to know how big the mugs are, but unfortunately they all got destroyed during filming. Susan knows some physics though, so she has figured out how far they moved between different video frames. The camera was filming at a speed of 70 frames per second, which means that at frame n, counted from when the mug was released, the number of millimeters it has moved is d = n<sup>2</sup>. The counting of the frames starts at 0.</p>

<p>Susan thinks a certain mug is D millimeters high, but to verify this she needs to find two frames between which the mug has moved exactly this distance. Can you help her do this?</p>

### 입력 

 <p>The input file contains the single positive integer D ≤ 200 000, the distance to be measured.</p>

### 출력 

 <p>Output two non-negative integers n<sub>1</sub> and n<sub>2</sub>, the numbers of the frames that Susan should compare. They should fulfill n<sub>2</sub><sup>2</sup> − n<sub>1</sub><sup>2</sup> = D. If no two such integers exist, instead output “impossible”.</p>

