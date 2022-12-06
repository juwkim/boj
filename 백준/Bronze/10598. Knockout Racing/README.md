# [Bronze I] Knockout Racing - 10598 

[문제 링크](https://www.acmicpc.net/problem/10598) 

### 성능 요약

메모리: 29028 KB, 시간: 828 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>The races became more popular than ever at Pandora planet. But these races are quite unusual. There are n cars participating in a race on the long straight track. Each car moves with a speed of 1 meter per second. Track has coordinates in meters.</p>

<p>The car number i moves between two points on the track with coordinates a<sub>i</sub> and b<sub>i</sub> starting at the second 0 in the point a<sub>i</sub>. The car moves from a<sub>i</sub> to b<sub>i</sub>, then from b<sub>i</sub> to a<sub>i</sub>, then from a<sub>i</sub> to b<sub>i</sub> again, and so on.</p>

<p>Handsome Mike wants to knock some cars out of the race using dynamite. Thus he has m questions. The question number j is: what is the number of cars in the coordinates between x<sub>j</sub> and y<sub>j</sub> inclusive after t<sub>j</sub> seconds from the start?</p>

<p>Your task is to answer Mike’s questions.</p>

### 입력 

 <p>The first line of the input file contains two integers n and m (1 ≤ n, m ≤ 1000) — the number of cars in the race and the number of questions.</p>

<p>Each of the following n lines contains a description of the car: two integers a<sub>i</sub> and b<sub>i</sub> (0 ≤ a<sub>i</sub>, b<sub>i</sub> ≤ 10<sup>9</sup>, a<sub>i</sub> ≠ b<sub>i</sub>) — the coordinates of the two points between which the car i moves.</p>

<p>Each of the following m lines contains a description of the question: three integers x<sub>j</sub> , y<sub>j</sub> , and t<sub>j</sub> (0 ≤ x<sub>j</sub> ≤ y<sub>j</sub> ≤ 10<sup>9</sup>, 0 ≤ t<sub>j</sub> ≤ 10<sup>9</sup>) — the coordinate range and the time for the question j.</p>

### 출력 

 <p>Write m lines to the output file. Each line must contain one integer — the answer to the corresponding question in order they are given in the input file.</p>

