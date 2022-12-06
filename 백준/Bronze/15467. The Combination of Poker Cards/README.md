# [Bronze I] The Combination of Poker Cards - 15467 

[문제 링크](https://www.acmicpc.net/problem/15467) 

### 성능 요약

메모리: 45224 KB, 시간: 172 ms

### 분류

구현(implementation)

### 문제 설명

<p>Poker is a popular card game worldwide, which was played from the 18th century in a variety of forms. A standard deck of poker cards has 52 cards divided into four suits, with each suit having the 13 ranks. In the Chinese area, “Big Two” and “Thirteen Cards” are two popular poker games based on the ranking of different combinations of cards. If we want to design such computer poker games, we need to write a program that can recognize card combinations. Suppose that we simplify the requirement as follows: Without considering the types of suits but only concerning about the ranks of cards, try to determine the card combination from any six given cards. If we use integer numbers to represent card ranks, the possible card combinations are described below:</p>

<ul>
	<li>single: six different numbers, e.g., 2 5 7 10 9 8</li>
	<li>one pair: one pair of equal numbers, e.g., 4 4 7 10 8 9</li>
	<li>two pairs: two pairs of equal numbers, e.g., 8 8 3 3 6 7</li>
	<li>three pairs: three pairs of equal numbers, e.g., 8 8 3 3 7 7</li>
	<li>one triple: three equal numbers, e.g., 2 2 2 7 5 6</li>
	<li>two triples: two suits of three equal numbers, e.g., 2 2 2 7 7 7</li>
	<li>tiki: four equal numbers, e.g., 5 5 5 5 9 8</li>
	<li>tiki pair: four equal numbers and another one pair, e.g., 5 5 5 5 9 9</li>
	<li>full house: three equal numbers and another one pair, e.g., 3 3 3 9 9 7</li>
</ul>

<p>Suppose that we use integer numbers from 1 to 13 to represent the card ranks. Please write a program to determine the card combination from six input numbers.</p>

### 입력 

 <p>The first input line contains one integer number T, indicating the number of test cases. Each test case includes six integer numbers (with each number from 1 to 13) that are separated by a single white space.</p>

<p>You may assume:</p>

<ul>
	<li>1 ≤ T ≤ 25</li>
	<li>In every test case, any number appears at most 4 times.</li>
</ul>

### 출력 

 <p>Show the name of the card combination for each input test case using the namespace of single, one pair, two pairs, three pairs, one triple, two triples, tiki, tiki pair, and full house.</p>

