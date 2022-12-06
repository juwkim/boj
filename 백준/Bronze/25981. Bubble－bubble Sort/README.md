# [Bronze I] Bubble-bubble Sort - 25981 

[문제 링크](https://www.acmicpc.net/problem/25981) 

### 성능 요약

메모리: 115268 KB, 시간: 648 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 정렬(sorting)

### 문제 설명

<p>Bubbles! As a fanatical supporter of the Bubbles Are Perfect Creatures movement, you have accumulated a large collection of bubbles in all colours and sizes. Being a long time member, your bubbles are among the best in the world, and now is the time to show this. Tomorrow, the yearly Bubble Exposition will be held, and your goal is to win the Bubble Prize and become the Bubble Champion!</p>

<p>However, this is not an easy competition. In order to win, you do not only need the most beautiful bubbles, you also need the best-looking placement of bubbles. You have decided to order the bubbles by bubbliness: less bubblier bubbles to the left, more bubblier bubbles to the right. However, it is hard to compare all the bubbles in your collection at once. In fact, you can only compare up to $k$ bubbles by eye before losing track of all the bubbles. Since your collection consists of more than $k$ bubbles, you need a fancier sorting algorithm.</p>

<p>Your first thought is to use the best sorting algorithm for bubbly purposes, namely Bubble Sort. However, this is the most prestigious bubble competition, so you decide to do better: Bubble-bubble Sort. It works as follows.</p>

<p>Initially, your bubbles are placed in an arbitrary order. Every hour, you do the following: you look at the first $k$ bubbles and place them in the optimal order. Then, you look at bubbles $2$ to $k+1$ and place those in the correct order. Then, you look at bubbles $3$ to $k+2$, and so on, until you have placed the last $k$ bubbles in the correct order. You then admire how the bubble collection looks so far until the next hour begins and you start at the first bubbles again.</p>

<p>Is this algorithm fast enough to place all your bubbles, or do you need to go further and invent a Bubble-bubble-bubble Sort algorithm? To be precise, after how many hours are the bubbles in the optimal positions?</p>

### 입력 

 <ul>
	<li>One line with two integers $n$ and $k$ ($2 \leq k < n \leq 2500$), the number of bubbles and the number of bubbles you can sort at once.</li>
	<li>One line with $n$ integers $a$ ($0 \leq a \leq 10^9$), the bubbliness of each bubble in the initial placement of your bubble collection.</li>
</ul>

### 출력 

 <p>Output the number of hours needed to sort your bubble collection.</p>

