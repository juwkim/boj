# [Silver V] Dire Straights (Small) - 12477 

[문제 링크](https://www.acmicpc.net/problem/12477) 

### 성능 요약

메모리: 116024 KB, 시간: 136 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>You are playing a card game, where each card has an integer number written on it.</p>

<p>To play the game, you are given some cards — your <em>hand</em>. Then you arrange the cards in your hand into <em>straights</em>. A straight is a set of cards with consecutive values; e.g. the three cards {3, 4, 5}, or the single card {7}. You then receive a number of dollars equal to the length of the shortest straight. If you have no cards, you can form no straights, so you get zero dollars.</p>

<p>You will be given a series of test cases, each of which describes the cards you will have in your hand. Find the maximum number of dollars you can receive for each test case.</p>

### 입력 

 <p>The first line of the input contains the number of test cases, <strong>T</strong>. Each test case consists of one line. Each line contains <strong>N</strong>, the number of cards in your hand, followed by <strong>N</strong> integers giving the numbers on those cards. These numbers are all space-separated.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100</li>
	<li>The numbers on the cards are between 1 and 10000.</li>
	<li>0 ≤ <strong>N</strong> ≤ 10</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the maximum number of dollars you can receive.</p>

