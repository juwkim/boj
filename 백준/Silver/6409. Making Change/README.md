# [Silver II] Making Change - 6409 

[문제 링크](https://www.acmicpc.net/problem/6409) 

### 성능 요약

메모리: 109544 KB, 시간: 88 ms

### 분류

브루트포스 알고리즘, 다이나믹 프로그래밍, 그리디 알고리즘, 구현

### 제출 일자

2025년 3월 14일 00:28:11

### 문제 설명

<p>Given an amount of money and unlimited (almost) numbers of coins (we will ignore notes for this problem) we know that an amount of money may be made up in a variety of ways. A more interesting problem arises when goods are bought and need to be paid for, with the possibility that change may need to be given. Given the finite resources of most wallets nowadays, we are constrained in the number of ways in which we can make up an amount to pay for our purchases---assuming that we can make up the amount in the first place, but that is another story.</p>

<p>The problem we will be concerned with will be to minimise the number of coins that change hands at such a transaction, given that the shopkeeper has an adequate supply of all coins. (The set of New Zealand coins comprises 5c, 10c, 20c, 50c, <span>$</span>1 and <span>$</span>2.) Thus if we need to pay 55c, and we do not hold a 50c coin, we could pay this as 2*20c + 10c + 5c to make a total of 4 coins. If we tender <span>$</span>1 we will receive 45c in change which also involves 4 coins, but if we tender <span>$</span>1.05 (<span>$</span>1 + 5c), we get 50c change and the total number of coins that changes hands is only 3.</p>

<p>Write a program that will read in the resources available to you and the amount of the purchase and will determine the minimum number of coins that change hands.</p>

### 입력 

 <p>Input will consist of a series of lines, each line defining a different situation. Each line will consist of 6 integers representing the numbers of coins available to you in the order given above, followed by a real number representing the value of the transaction, which will always be less than <span>$</span>5.00. The file will be terminated by six zeroes (0 0 0 0 0 0). The total value of the coins will always be sufficient to make up the amount and the amount will always be achievable, that is it will always be a multiple of 5c.</p>

### 출력 

 <p>Output will consist of a series of lines, one for each situation defined in the input. Each line will consist of the minimum number of coins that change hands right justified in a field 3 characters wide.</p>

