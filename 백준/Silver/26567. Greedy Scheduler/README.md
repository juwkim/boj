# [Silver III] Greedy Scheduler - 26567 

[문제 링크](https://www.acmicpc.net/problem/26567) 

### 성능 요약

메모리: 111772 KB, 시간: 172 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2024년 3월 14일 03:04:15

### 문제 설명

<p>A store has n cashiers numbered sequentially from 1 to n, with c customers in a queue. A customer at the front of the queue is constantly assigned to the first unoccupied cashier, (i.e., if more than one cashier is unoccupied select the cashier with the smallest number). The ith customer’s shopping cart takes ti seconds to process.</p>

<p>Find which cashier will process each customer’s shopping cart.</p>

### 입력 

 <p>The first line of input will contain a single integer m that indicates the number datasets to follow. Each dataset is comprised of two lines. The first line of input contains two space-separated integers n and c (1 ≤ n ≤ c ≤ 1000). The second line of input contains c space-separated integers t<sub>1</sub>, . . . , t<sub>c</sub>, representing the length of time required to handle that customer.</p>

### 출력 

 <p>For each dataset print, on a single line c integers separated by one space, where each integer is the cashier number that handles that customer.</p>

