# [Bronze I] Weekend Lottery - 5742 

[문제 링크](https://www.acmicpc.net/problem/5742) 

### 성능 요약

메모리: 115004 KB, 시간: 160 ms

### 분류

구현(implementation)

### 문제 설명

<p>Some people are against lotteries on moral grounds, some governments forbid lotteries, but with the advent of Internet this popular form of gambling, which started in China and helped finance the Great Wall, is thriving.</p>

<p>But the odds of winning a national lottery are tiny, and therefore your college classmates decided to organize a private lottery, with draws every Friday. The lottery is based on a popular style: a student who wants to bet chooses C distinct numbers from 1 to K and pays US\$ 1.00 (notice that traditional lotteries such as US National Lotto use C = 6 and K = 49). On Friday during lunch C numbers (also from 1 to K) are drawn. The student whose bet has the largest number of correct guesses receives the amount collected in the bets. This amount is shared in case of ties and accumulates to next week if no one guessed any of the numbers drawn.</p>

<p>Some of your colleagues do not believe in the laws of probability and asked you to write a program that determines the numbers that have been drawn the fewest times considering all previous draws, so that they can bet on those numbers.</p>

### 입력 

 <p>The input contains several test cases. The first line of a test case contains three integers N, C and K which indicate respectively the number of draws that have already happened (1 ≤ N ≤ 10000), how many numbers comprises a bet (1 ≤ C ≤ 10) and the maximum value of the numbers to be chosen in a bet (C < K ≤ 100). Each of the next N lines contains C distinct integers X<sub>i</sub> indicating the numbers drawn in each previous contest (1 ≤ X<sub>i</sub> ≤ K, for 1 ≤ i ≤ C). The end of input is indicated by N = C = K = 0.</p>

### 출력 

 <p>For each test case in the input your program must write one line of output, containing the set of numbers that have been drawn the fewest times. This set must be printed as a list, in increasing order of numbers. Leave one blank space between two consecutive numbers in the list.</p>

