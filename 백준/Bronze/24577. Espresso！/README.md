# [Bronze II] Espresso! - 24577 

[문제 링크](https://www.acmicpc.net/problem/24577) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>John is a student working as a part-time barista at the micro kitchen of his school department. He operates the espresso machine at the kitchen to make espresso and latte for students seeking energy to study.</p>

<p>Today, there are n students coming to the micro kitchen to place an order. An order is noted with an espresso shot number x ranging between 1 and 4, and an optional letter <code>L</code> that indicates that the student wants to have a x-shot latte. For example, an order <code>2</code> means a 2-shot espresso, and an order <code>3L</code> means a 3-shot latte.</p>

<p>Making an x-shot espresso consumes x ounces of water. Making a latte requires steaming milk and consumes one additional ounce of water, e.g. making a 3-shot latte consumes 4 ounces of water. The espresso machine at the micro kitchen has a water tank of s ounces that is full at the beginning of the day. John refills the water tank to s ounces whenever the remaining water in the tank is not enough to fulfill the next student’s order. John fulfills the n orders one by one without changing their order.</p>

<p>How many times do John have to refill the water tank today in order to serve all the n students?</p>

### 입력 

 <p>The first line of input has two integers n (1 ≤ n ≤ 100) and s (10 ≤ s ≤ 200). The next n lines each contain a digit between 1 and 4 followed by an optional letter <code>L</code> to describe an order. The orders are to be fulfilled in the given order as they appear in the input.</p>

### 출력 

 <p>Output the number of times John has to refill the water tank of the espresso machine.</p>

