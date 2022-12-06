# [Bronze III] Overdraft - 24609 

[문제 링크](https://www.acmicpc.net/problem/24609) 

### 성능 요약

메모리: 30840 KB, 시간: 108 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Banks often charge overdraft fees if you attempt to withdraw more money from your account than is available in your current balance. Given a sequence of deposits and withdrawals (and assuming each deposit and withdrawal is immediately reflected in your balance), determine the minimum (non-negative) starting balance you need to ensure that you will not be charged any overdraft fees over the course of the sequence.</p>

### 입력 

 <p>The first line of input contains a single integer $n$ ($1 \le n \le 1{,}000$), which is the number of transactions.</p>

<p>Each of the next $n$ lines contains a single integer $t$ ($-10^6 \le t \le 10^6$, $t \neq 0$). These are the transactions, in the order that they occur. A positive number represents a deposit, a negative number represents a withdrawal. No two transactions occur simultaneously.</p>

### 출력 

 <p>Output a single non-negative integer, which is the minimum non-negative balance you must start with in your account in order to avoid any overdraft fees.</p>

