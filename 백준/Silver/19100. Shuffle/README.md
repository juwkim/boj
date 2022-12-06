# [Silver V] Shuffle - 19100 

[문제 링크](https://www.acmicpc.net/problem/19100) 

### 성능 요약

메모리: 283148 KB, 시간: 556 ms

### 분류

애드 혹(ad_hoc)

### 문제 설명

<p>Byteasar has learnt a fabulous recursive method of shuffling a deck of cards. This algorithm can be described as follows:</p>

<ul>
	<li>In order to shuffle two cards, swap them.</li>
	<li>In order to shuffle $2^k$ cards ($k \geq 2$), split them into two equal parts -- an upper one and a lower one (so that each of them has $2^{k - 1}$ cards). Shuffle each of them recursively and then put the lower half on the top of the upper half.</li>
</ul>

<p>Byteasar has a deck of $2^n$ cards. Each of them has a number written on it. Byteasar now shuffles the deck, running the procedure described above exactly $t$ times. As it might take a great amount of time, he would like to know the final order of the cards beforehand.</p>

### 입력 

 <p>The first line of the input contains two integers $n, t$ ($1 \le n \le 20$, $1 \le t \le 10^9$). The second line contains $2^n$ integers $a_1, \dots, a_{2^n}$ ($1 \le a_i \le 10^9$); $a_i$ is the number written on the $i$-th topmost card in the deck.</p>

### 출력 

 <p>In the first and only line of output print $2^n$ integers -- the numbers written on the cards of Byteasar's deck after $t$ shuffles. Print the numbers in the order from the topmost to the bottommost card.</p>

