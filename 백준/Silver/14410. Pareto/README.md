# [Silver V] Pareto - 14410 

[문제 링크](https://www.acmicpc.net/problem/14410) 

### 성능 요약

메모리: 168792 KB, 시간: 248 ms

### 분류

정렬(sorting)

### 문제 설명

<p>Paret’s principle, also known as the “80/20 rule”, states that in many situations 80% of results come from 20% of (the most important) causes. For instance, Microsoft found that, by fixing 20% of most commonly reported bugs, they would eliminate 80% of downtime in their systems. In the business world, it is often said that 80% of income comes from 20% of the most important clients. In the world of mobile games, when it comes to games with free basic functionality, 50% of profit comes from 0.5% of players. Some say that 80% of your success will come from 20% of your activities.</p>

<p>It is a known fact that 80% of the world’s goods is owned by 20% of (the richest) people. Your task is to check the validity of this rule based on the bank accounts owned by clients of a single bank. Is it true that 20% of accounts hold 80% of the total money? Does a stronger claim hold, for instance, that only 10% of accounts hold 85% of the total money?</p>

<p>More precisely: based on the given account balances of N bank clients, your task is to find ​ numbers ​A and ​B with the maximal difference ​B - A such that we can say that ​ precisely ​A% of accounts hold ​ ​B% of the total money​ of all clients of the bank.</p>

### 입력 

 <p>The first line of input contains the integer N (1 ≤ N ≤ 300 000), the number of clients in the bank.</p>

<p>The following line contains N integers from the interval [0, 100 000 000], the balances of bank accounts in euros.</p>

### 출력 

 <p>In two lines, you must output two real numbers from the task, A and B, omitting the percentage sign. Solution with the greatest B - A difference will be unique​. A deviation from the official solution for less than 0.01 will be tolerated.</p>

