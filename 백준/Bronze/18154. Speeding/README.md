# [Bronze II] Speeding - 18154 

[문제 링크](https://www.acmicpc.net/problem/18154) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>You’d like to figure out whether a car was speeding while it was driving down a straight road. Unfortunately you don’t have any radar guns or related instruments for measuring speed directly; all you have are photographs taken of the car at various checkpoints on the road at various times. Given when and where these photographs were taken, what is the fastest speed that you can prove the car must have been going at some point along the road?</p>

### 입력 

 <p>The first line contains an integer N, the number of photographs taken, with 2 ≤ N ≤ 100. The following N lines each contain two integers t<sub>i</sub> and d<sub>i</sub>, with 0 ≤ t<sub>i</sub> ≤ 10 000 and 0 ≤ d<sub>i</sub> ≤ 1 000 000. The first photograph is always taken at time 0 with distance 0. Both the times and distances strictly increase. That is, t<sub>i+1</sub> > t<sub>i</sub> and d<sub>i+1</sub> > d<sub>i</sub>.</p>

### 출력 

 <p>Output the greatest integral speed that you can be certain the car was going at some point.</p>

