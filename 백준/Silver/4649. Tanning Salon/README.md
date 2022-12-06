# [Silver V] Tanning Salon - 4649 

[문제 링크](https://www.acmicpc.net/problem/4649) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

비트마스킹(bitmask), 자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Tan Your Hide, Inc., owns several coin-operated tanning salons. Research has shown that if a customer arrives and there are no beds available, the customer will turn around and leave, thus costing the company a sale. Your task is to write a program that tells the company how many customers left without tanning.</p>

### 입력 

 <p>The input consists of data for one or more salons, followed by a line containing the number 0 that signals the end of the input. Data for each salon is a single line containing a positive integer, representing the number of tanning beds in the salon, followed by a space, followed by a sequence of uppercase letters. Letters in the sequence occur in pairs. The first occurrence indicates the arrival of a customer, the second indicates the departure of that same customer. No letter will occur in more than one pair. Customers who leave without tanning always depart before customers who are currently tanning. There are at most 20 beds per salon.</p>

### 출력 

 <p>For each salon, output a sentence telling how many customers, if any, walked away. Use the exact format shown below.</p>

