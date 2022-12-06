# [Bronze I] Investing at the Market (Small) - 12539 

[문제 링크](https://www.acmicpc.net/problem/12539) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>You have money <strong>M</strong> to invest and a forecast of a commodity price <strong>P</strong> for each month in the coming year. Of course you want profit! Figure out when to buy and sell in order to maximize your profit. You cannot buy a fraction of an item. You can assume that the price will be different each month. If two scenarios exist that result in the same profit, you should choose to buy at the lowest price per unit. You can only make a single purchase. If it is impossible to make a profit given the market trends, you should output <code>IMPOSSIBLE</code>.</p>

### 입력 

 <p>The first line of input gives the number of cases, <strong>N</strong>.<br>
<strong>N</strong> test cases follow. For each test case there will be:</p>

<ul>
	<li>One line containing the amount of money <strong>M</strong> that you have to invest.</li>
	<li>One line containing a space separated list of 12 integers <strong>P</strong> indicating the price at the beginning of each month.</li>
</ul>

<h3>Limits</h3>

<ul>
	<li>100 ≤ <strong>M</strong> ≤ 500</li>
	<li>1 ≤ <strong>P</strong> ≤ 250</li>
	<li><strong>N</strong> ≤ 10</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>x</strong>: " followed by either the word "IMPOSSIBLE" or three space separated integers:</p>

<ul>
	<li>The index <strong>B</strong> of the month when you should buy the goods. An integer between 1 and 11 (inclusive).</li>
	<li>The index of the month when you should sell the goods. An integer between (<strong>B</strong> + 1) and 12 (inclusive).</li>
	<li>The amount of profit that your investment plan will return.</li>
</ul>

