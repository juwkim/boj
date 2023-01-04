# [Silver IV] Hanafuda Shuffle - 4992 

[문제 링크](https://www.acmicpc.net/problem/4992) 

### 성능 요약

메모리: 114976 KB, 시간: 152 ms

### 분류

자료 구조(data_structures), 구현(implementation), 스택(stack)

### 문제 설명

<p>There are a number of ways to shuffle a deck of cards. Hanafuda shuffling for Japanese card game 'Hanafuda' is one such example. The following is how to perform Hanafuda shuffling.</p>

<p>There is a deck of n cards. Starting from the p-th card from the top of the deck, c cards are pulled out and put on the top of the deck, as shown in Figure 1. This operation, called a cutting operation, is repeated.</p>

<p>Write a program that simulates Hanafuda shuffling and answers which card will be finally placed on the top of the deck.</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images3/A.gif" style="height:380px; width:574px"></p>

<p style="text-align: center;">Figure 1: Cutting operation</p>

### 입력 

 <p>The input consists of multiple data sets. Each data set starts with a line containing two positive integers n (1 <= n <= 50) and r (1 <= r <= 50); n and r are the number of cards in the deck and the number of cutting operations, respectively.</p>

<p>There are r more lines in the data set, each of which represents a cutting operation. These cutting operations are performed in the listed order. Each line contains two positive integers p and c (p + c <= n + 1). Starting from the p-th card from the top of the deck, c cards should be pulled out and put on the top.</p>

<p>The end of the input is indicated by a line which contains two zeros.</p>

<p>Each input line contains exactly two integers separated by a space character. There are no other characters in the line.</p>

### 출력 

 <p>For each data set in the input, your program should write the number of the top card after the shuffle. Assume that at the beginning the cards are numbered from 1 to n, from the bottom to the top. Each number should be written in a separate line without any superfluous characters such as leading or following spaces.</p>

