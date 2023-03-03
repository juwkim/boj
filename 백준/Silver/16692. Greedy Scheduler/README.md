# [Silver IV] Greedy Scheduler - 16692 

[문제 링크](https://www.acmicpc.net/problem/16692) 

### 성능 요약

메모리: 115108 KB, 시간: 144 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>A store has n cashiers numbered sequentially from 1 to n, with c customers in a queue. A customer at the front of the queue is constantly assigned to the first unoccupied cashier, i.e., cashier with the smallest number. The ith customer’s shopping cart takes t<sub>i</sub> seconds to process.</p>

<p>Find which cashier will process each customer’s shopping cart.</p>

### 입력 

 <p>The first line of input contains two space-separated integers n and c (1 ≤ n ≤ c ≤ 1000). The second line of input contains c space-separated integers t<sub>1</sub>, . . . , t<sub>c</sub> (1 ≤ t<sub>i</sub> ≤ 1,000), representing the length of time required to handle that customer.</p>

### 출력 

 <p>Output a single line containing c space-separated integers, each with the cashier number that handles that customer.</p>

