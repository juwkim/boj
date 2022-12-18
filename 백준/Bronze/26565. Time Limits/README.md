# [Bronze II] Time Limits - 26565 

[문제 링크](https://www.acmicpc.net/problem/26565) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>A contest setter wants to determine the time limits for a given problem. There are n model solutions, and solution k takes t<sub>k</sub> milliseconds to run on the test data. The contest setter wants the time limit to be an integer number of seconds, and wants the time limit to be at least s times larger than the slowest model solution. Compute the minimum time limit the contest setter can set.</p>

### 입력 

 <p>The first line of input will contain a single integer m that indicates the number datasets to follow. Each dataset is comprised of two lines. The first line of input contains two space-separated integers n and s (1 ≤ n ≤ 100 and 1 ≤ s ≤ 20). The second line of input contains n space-separated integers t<sub>1</sub>, . . . , t<sub>n</sub> (1 ≤ tk ≤ 2000 for all k = 1, . . . , n).</p>

### 출력 

 <p>For each dataset print, on one line, the minimum time limit (in seconds) as a single integer.</p>

