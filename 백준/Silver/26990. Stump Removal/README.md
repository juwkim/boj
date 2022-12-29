# [Silver V] Stump Removal - 26990 

[문제 링크](https://www.acmicpc.net/problem/26990) 

### 성능 요약

메모리: 31924 KB, 시간: 60 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>Always thinking of the cows' grazing experience, FJ has found that he must remove N (1 ≤ N ≤ 50,000) unsightly stumps from the pasture. The stumps are conveniently arranged in a straight line and numbered 1..N with each stump having some height H_i (1 ≤ H_i ≤ 10,000).</p>

<p>FJ will use the traditional high explosives to destroy the stumps. These high explosives are formulated to destroy adjacent stumps as long as those adjacent stumps are strictly shorter than the nearest stump being destroyed. The blast can continue past the closest adjacent stump to the next adjacent stump if it is even shorter than the nearest stump just destroyed. As soon as a stump encountered by the blast wave is not shorter, though, no more destruction occurs on that side of the target stump (the other side follows the same rules with whatever stumps might appear there).</p>

<p>Consider a line of nine stumps with these heights:</p>

<pre>              1 2 5 4 3 3 6 6 2
</pre>

<p>If FJ blows up the third stump (with height 5), then the second stump will also be destroyed (height 2) and the first stump (height 1) will also be destroyed. Likewise, the fourth stump (height 4) and fifth stump (height 3) will be destroyed since they are successively shorter, leaving the line like this:</p>

<pre>              * * * * * 3 6 6 2</pre>

<p>Two more explosives (at stumps 7 and 8) will destroy the rest.</p>

<p>Help FJ determine the minimum number of explosive charges he needs to destroy the stumps.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer, N</li>
	<li>Lines 2..N+1: Line i+1 contains H_i</li>
</ul>

### 출력 

 <ul>
	<li>Lines 1..?: Each line contains one integer which is the index of a stump to blow up. The indices must be listed in increasing order.</li>
</ul>

