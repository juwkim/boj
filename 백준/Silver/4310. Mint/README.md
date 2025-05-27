# [Silver I] Mint - 4310 

[문제 링크](https://www.acmicpc.net/problem/4310) 

### 성능 요약

메모리: 110896 KB, 시간: 804 ms

### 분류

브루트포스 알고리즘, 유클리드 호제법, 수학, 정수론

### 제출 일자

2025년 5월 27일 17:10:33

### 문제 설명

<p>The Royal Canadian Mint has commissioned a new series of designer coffee tables, with legs that are constructed from stacks of coins. Each table has four legs, each of which uses a different type of coin. For example, one leg might be a stack of quarters, another nickels, another loonies, and another twonies. Each leg must be exactly the same length.</p>

<p>Many coins are available for these tables, including foreign and special commemorative coins. Given an inventory of available coins and a desired table height, compute the lengths nearest to the desired height for which four legs of equal length may be constructed using a different coin for each leg.</p>

### 입력 

 <p>Input consists of several test cases. Each case begins with two integers: 4 ≤ n ≤ 50 giving the number of types of coins available, and 1 ≤ t ≤ 10 giving the number of tables to be designed. n lines follow; each gives the thickness of a coin in hundredths of millimetres. t lines follow; each gives the height of a table to be designed (also in hundredths of millimetres). A line containing 0 0 follows the last test case.</p>

### 출력 

 <p>For each table, output a line with two integers: the greatest leg length not exceeding the desired length, and the smallest leg length not less than the desired length.</p>

