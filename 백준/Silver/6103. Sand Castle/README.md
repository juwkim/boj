# [Silver I] Sand Castle - 6103 

[문제 링크](https://www.acmicpc.net/problem/6103) 

### 성능 요약

메모리: 115444 KB, 시간: 120 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 5월 6일 18:54:24

### 문제 설명

<p>Farmer John has built a sand castle! Like all good castles, the walls have crennelations, that nifty pattern of embrasures (gaps) and merlons (filled spaces); see the diagram below. The N (1 <= N <= 25,000) merlons of his castle wall are conveniently numbered 1..N; merlon i has height M_i (1 <= M_i <= 100,000); his merlons often have varying heights, unlike so many.</p>

<p>He wishes to modify the castle design in the following fashion: he has a list of numbers B_1 through B_N (1 <= B_i <= 100,000), and wants to change the merlon heights to those heights B_1, ..., B_N in some order (not necessarily the order given or any other order derived from the data).</p>

<p>To do this, he has hired some bovine craftsmen to raise and lower the merlons' heights. Craftsmen, of course, cost a lot of money. In particular, they charge FJ a total X (1 <= X <= 100) money per unit height added and Y (1 <= Y <= 100) money per unit height reduced.</p>

<p>FJ would like to know the cheapest possible cost of modifying his sand castle if he picks the best permutation of heights. The answer is guaranteed to fit within a 32-bit signed integer.</p>

### 입력 

 <ul>
	<li>Line 1: Three space-separated integers: N, X, and Y</li>
	<li>Lines 2..N+1: Line i+1 contains the two space-separated integers: M_i and B_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer, the minimum cost needed to rebuild the castle</li>
</ul>

<p> </p>

