# [Bronze II] Accurate Movement - 18067 

[문제 링크](https://www.acmicpc.net/problem/18067) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>Amelia is studying modeling. She is interested in models with moving parts.</p>

<p>As her first task, she made a rectangular box of size 2 × n, which contains two parallel rails and a rectangular bar on each of them. The short bar has size 1 × a, and the long one has size 1 × b. The long bar has a stopper at each end, and the short one is always between these two stoppers.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 424px; height: 105px;"></p>

<p>The bars can be moved along the rails, one bar at a time, as long as the short bar is between the stoppers. So, on each move Amelia selects one of the bars and moves it, while the other one stays in place.</p>

<p>Initially, both bars are aligned to one side of the box, and Amelia wants them to be aligned to the other side in as few moves as possible. What is the minimal number of moves she should do to achieve her goal?</p>

### 입력 

 <p>The only input line contains three integers a, b, and n (1 ≤ a < b ≤ n ≤ 10<sup>7</sup>).</p>

### 출력 

 <p>The only output line should contain a single integer — the minimal number of moves Amelia needs to do.</p>

