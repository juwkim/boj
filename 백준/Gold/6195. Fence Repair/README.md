# [Gold IV] Fence Repair - 6195 

[문제 링크](https://www.acmicpc.net/problem/6195) 

### 성능 요약

메모리: 117624 KB, 시간: 248 ms

### 분류

자료 구조(data_structures), 그리디 알고리즘(greedy), 우선순위 큐(priority_queue)

### 문제 설명

<p>Farmer John wants to repair a small length of the fence around the pasture. He measures the fence and finds that he needs N (1 <= N <= 20,000) planks of wood, each having some integer length Li (1 <= Li <= 50,000) units. He then purchases a single long board just long enough to saw into the N planks (i.e., whose length is the sum of the lengths Li). FJ is ignoring the "kerf", the extra length lost to sawdust when a sawcut is made; you should ignore it, too.</p>

<p>FJ sadly realizes that he doesn't own a saw with which to cut the wood, so he mosies over to Farmer Don's Farm with this long board and politely asks if he may borrow a saw.</p>

<p>Farmer Don, a closet capitalist, doesn't lend FJ a saw but instead offers to charge Farmer John for each of the N-1 cuts in the plank. The charge to cut a piece of wood is exactly equal to its length. Cutting a plank of length 21 costs 21 cents.</p>

<p>Farmer Don then lets Farmer John decide the order and locations to cut the plank. Help Farmer John determine the minimum amount of money he can spend to create the N planks. FJ knows that he can cut the board in various different orders which will result in different charges since the resulting intermediate planks are of different lengths.</p>

### 입력 

 <ul>
	<li>Line 1: One integer N, the number of planks</li>
	<li>Lines 2..N+1: Each line contains a single integer describing the length of a needed plank</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: One integer: the minimum amount of money he must spend to make N-1 cuts</li>
</ul>

