# [Bronze II] Six Sides - 13987 

[문제 링크](https://www.acmicpc.net/problem/13987) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 조합론(combinatorics), 수학(math), 확률론(probability)

### 문제 설명

<p>Two players play a simple game. Each brings their own six-sided die with specified values on the six faces. Each die is fair; that is, when it is thrown, each of its six faces is equally likely to come up on top.</p>

<p>The first player throws the first die and the second throws the second die. If the values shown on the top of the dice differ, the player with the higher value wins. If the values are the same, both players throw the dice again.</p>

<p>Given two dice with specific values, what is the probability that the first player wins?</p>

### 입력 

 <p>The first line of input contains six space-separated integers, representing the values written on the first player’s die.</p>

<p>The second line of input contains the values on the second player’s die in the same format.</p>

<p>It is guaranteed that all the values are between 1 and 6, inclusive.</p>

### 출력 

 <p>Print, on a single line, a floating-point value representing the probability that the first player wins, rounded and displayed to exactly five decimal places. The value should be printed with one digit before the decimal point and five digits after the decimal point. The sixth digit after the decimal point of the exact answer will never be 4 or 5 (eliminating complex rounding considerations).</p>

