# [Bronze III] Snacks within 300 Yen - 32046 

[문제 링크](https://www.acmicpc.net/problem/32046) 

### 성능 요약

메모리: 109240 KB, 시간: 92 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 7월 15일 06:21:28

### 문제 설명

<p>Your friend, Greedy George, visits a candy store for his snacks for the school excursion, grabbing 300 yen in his hand. In the candy store, one item of each different kind of snack is placed in a line on the shelf. After entering the store, Greedy George picks up a shopping basket and starts checking the snacks on the shelf from left to right. If the sum of the prices of snacks in the basket will not exceed 300 yen, he immediately puts the checked snack into the basket. If the sum should exceed 300 yen, he tearfully skips that snack. After examining all the snacks in this manner to the right end, George heads to the checkout.</p>

<p>Given a list of the prices of the snacks in the store, compute how much money Greedy George will spend.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/295eae5a-541d-4eec-a48f-41625808e7a6/-/preview/" style="width: 512px; height: 205px;"></p>

<p style="text-align: center;">Figure A-1: The first dataset of Sample Input</p>

### 입력 

 <p>The input consists of multiple datasets, each in the following format. The number of datasets does not exceed 50.</p>

<blockquote>
<p><i>n</i></p>

<p><i>a</i><sub>1</sub> <i>a</i><sub>2</sub> ⋯ <i>a<sub>n</sub></i></p>
</blockquote>

<p><i>n</i> (1 ≤ <i>n</i> ≤ 100) is the number of snacks sold in the candy store. <i>a<sub>k</sub></i> (<i>k</i> = 1, …, <i>n</i>) is a positive integer less than or equal to 1000, meaning that the price of the <i>k</i>-th snack from the left is <i>a<sub>k</sub></i> yen.</p>

<p>The end of the input is indicated by a line consisting of a zero.</p>

### 출력 

 <p>For each dataset, output in a line how many yen Greedy George will spend on the snacks.</p>

