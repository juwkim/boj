# [Silver III] Pack - 7159 

[문제 링크](https://www.acmicpc.net/problem/7159) 

### 성능 요약

메모리: 134652 KB, 시간: 588 ms

### 분류

자료 구조, 덱, 구현, 시뮬레이션

### 제출 일자

2024년 4월 12일 11:01:49

### 문제 설명

<p>There is a pack of cards on the table, containing n cards placed one on another. Each card has a positive integer written on one side and nothing on the other. On the top card the number 1 is written, on the second from top number 2, etc., and on the bottom card the number n is written. In the beginning all the cards in the pack are placed so that numbers are facing up. Archibald makes m turns. In the i-th turn he takes the upper ki cards, holding them together turns them upside down and places back on top of the pack. Your task is to write a program that determines the place and state of a card (upside up or down) in the pack after m moves made by Archibald!</p>

### 입력 

 <p>The first line of the standard input contains two positive integers – n (the number of cards in the pack, n≤100000) and m (the number of turns done by Archibald, m≤1000) – which are separated using a space symbol. Each of the following m lines contains one positive integer ki (1≤ki≤n) – the number of cards used in each turn.</p>

<p>The next line of the standard input contains one positive integer s (s≤10000) – the number of cards, the final position and state of which must be determined. Each of the following s lines contains one positive integer – the number written on the card, the final position and state of which must be determined. </p>

### 출력 

 <p>The standard output must contain excatly s lines. Each line must contain one integer. If in the end the p-th card has the number that the m+i+1st line of the standrard input contains, the i-th line of the output file must contain the number</p>

<ul>
	<li>+p if the card has its number written on the side facing up or</li>
	<li>-p if the card has its number written on the side facing down. </li>
</ul>

