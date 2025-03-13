# [Silver II] Balanced Change - 7589 

[문제 링크](https://www.acmicpc.net/problem/7589) 

### 성능 요약

메모리: 110904 KB, 시간: 100 ms

### 분류

브루트포스 알고리즘, 많은 조건 분기, 구현, 파싱, 문자열

### 제출 일자

2025년 3월 14일 01:01:53

### 문제 설명

<p>When giving change to a customer in a shop, clerks are careful to hand over the minimum number of coins – so unless they have run out of coins of the appropriate denomination they will, for example, always give a customer needing <span>$</span>2 in change, one <span>$</span>2 coin rather than 2 <span>$</span>1 coins or 4 50c coins. It might be that this is not always the best strategy however, when there is an imbalance in the stock of coins. If you have an excess of <span>$</span>1 coins in the cash drawer, it might be better to give 2 <span>$</span>1 coins to a customer, if only to prevent the <span>$</span>1 coin bucket from overflowing. Your task is to devise and test an algorithm to decide what coins to give in change, which tries to balance the stock of coins of each denomination. </p>

<p>More precisely: you have a cash draw with buckets for <span>$</span>2, <span>$</span>1, 50c, 20c and 10c coins. We define imbalance as follows: Let min be the minimum number of coins in any bucket. Then the imbalance is the sum of the squares of the number of coins above the minimum in each bucket. If we have 2, 3, 4, 3, 5 of <span>$</span>2, <span>$</span>1, 50c, 20c and 10c coins respectively: the minimum is 2 and the imbalance is (2-2)<sup>2</sup> +(3-2)<sup>2</sup> +(4-2)<sup>2</sup> +(3-2)<sup>2</sup> +(5-2)<sup>2</sup> = 0 + 1 + 4 + 1 + 9 = 15. Your task is to write a program to give change in such a way as to minimize the imbalance of the cash remaining in the cash draw. If more than one way of giving cash gives the same imbalance you should use the one which gives the greater number of <span>$</span>2 coins. If the number of <span>$</span>2 coins is the same, then prefer the one with the largest number of <span>$</span>1 coins, then 50c, etc. </p>

### 입력 

 <p>The input file contains several change giving problems. Each problem is described on one line of input by 5 integers and a dollar amount. The first 5 are the numbers of <span>$</span>2, <span>$</span>1, 50c, 20c, and 10c coins in the cash drawer. The dollar amount takes the form ‘<span>$</span>n.m’ where n is always present, but may be zero and m is always two digits. It is the amount of change to be given. Input ends with a line holding 5 zeroes and ‘<span>$</span>0.00’. The amount of change to be given is always greater than zero and never more than <span>$</span>5. </p>

### 출력 

 <p>For each problem output a line with ‘Problem #n:’, followed by the number of <span>$</span>2, <span>$</span>1, 50c, 20c and 10c coins respectively. This should be formatted as illustrated below with correct use of commas, and the word ‘and’. If it is not possible to provide exact change, output ‘not possible’. </p>

