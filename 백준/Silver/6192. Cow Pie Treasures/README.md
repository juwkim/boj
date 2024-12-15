# [Silver II] Cow Pie Treasures - 6192 

[문제 링크](https://www.acmicpc.net/problem/6192) 

### 성능 요약

메모리: 110884 KB, 시간: 108 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 12월 16일 03:36:05

### 문제 설명

<p>The cows have been busily baking pies that contain gold coins! Each pie has some number Ni (1 <= Ni <= 25) of gold coins and is neatly labeled on its crust with the number of gold coins inside.</p>

<p>The cows have placed the pies very precisely in an array of R rows and C columns (1 <= R <= C <= 100) out in the pasture.  You have been placed in the pasture at the location (R=1,C=1) and have gathered the gold coins in that pie. You must make your way to the other side of the pasture, moving one column closer to the end point (which is location (R,C)) with each move you make. As you step to the new column, you may stay on the same row or change your row by no more than 1 (i.e., from (r,c) you can move to (r-1,c+1), (r, c+1), or (r+1,c+1).  Of course, you would not want to leave the field and fail to get some gold coins, and you must end up at (R,C).</p>

<p>Given a map of the pasture, what is the greatest number of gold coins you can gather?</p>

<p>By way of example, consider this field of gold-bearing cow pies:</p>

<pre>start-> 6 5 3 7 9 2 7
        2 4 3 5 6 8 6
        4 9 9 9 1 5 8 <-end</pre>

<p>Here's one path:</p>

<pre>start-> 6 5 3 7 9 2 7
         \
        2 4 3 5 6 8 6
           \   / \
        4 9 9-9 1 5-8 <-end</pre>

<p>The path above yields 6+4+9+9+6+5+8 = 47 gold coins. The path below is even better and yields 50 coins, which is the best possible:</p>

<pre>start->6 5 3 7 9 2 7
         \
        2 4 3 5 6-8 6
           \   /   \
        4 9 9-9 1 5 8 <-end</pre>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers, respectively R and C</li>
	<li>Lines 2..R+1: Each line contains C space-separated integers in the obvious order</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the maximum number of gold coins that can be gathered</li>
</ul>

