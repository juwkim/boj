# [Silver II] Large PhD Restaurant - 14012 

[문제 링크](https://www.acmicpc.net/problem/14012) 

### 성능 요약

메모리: 136580 KB, 시간: 352 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2024년 2월 9일 09:16:37

### 문제 설명

<p><strong>"There is probably a place where all waiters have a PhD in, I don't know, some stuff."</strong> - Dudu, 2014</p>

<p><strong>Note:</strong> This problem is identical to Small PhD Restaurant, but with larger bounds.</p>

<p>Dudu is hungry. He sat down in a nice Thai restaurant. To his amazement, he realized that he is in the <em>PhD restaurant</em>, a wonderful place where every staff member has a PhD in <em>some stuff</em>.</p>

<p>Even more, each staff member has arranged a challenge related to his or her field of study for Dudu to attempt while he waits for his food. The challenge arranged by staff member i costs A<sub>i</sub> to attempt and will award Dudu B<sub>i</sub>when he completes it successfully.</p>

<p>Each challenge can be completed at most once and they can be attempted in any order. Dudu is very smart and can complete any challenge, but he must have enough money to pay A<sub>i</sub> before he attempts challenge i. If Dudu starts with M money, determine the maximum amount he can obtain.</p>

### 입력 

 <p>Input begins with a line containing two integers N and M, the number of challenges and the amount of money Dudu begins with, respectively.</p>

<p>The following line contains N numbers A<sub>1</sub>,A<sub>2</sub>, ..., A<sub>N</sub>, indicating the costs to attempt each challenge.</p>

<p>Finally, the last line contains the N numbers B<sub>1</sub>, B<sub>2</sub>, ..., B<sub>N</sub> indicating the payoff from each challenge.</p>

<ul>
	<li>1 ≤ N ≤ 10<sup>5</sup></li>
	<li>0 ≤ M, A<sub>i</sub>, B<sub>i</sub> ≤ 10<sup>6</sup></li>
</ul>

### 출력 

 <p>Output a single integer indicating the maximum amount of money Dudu can obtain.</p>

