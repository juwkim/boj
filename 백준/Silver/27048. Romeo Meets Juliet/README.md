# [Silver V] Romeo Meets Juliet - 27048 

[문제 링크](https://www.acmicpc.net/problem/27048) 

### 성능 요약

메모리: 114328 KB, 시간: 140 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>Farmer John has two feuding herds of cattle, the Moontagues and the Cowpulets.  One of the bulls in the Moontague herd, Romeo, has fallen in love with Juliet, a Cowpulet.  Romeo would like to meet with Juliet, but he doesn't want the other members of the Cowpulet herd to find out.</p>

<p>Romeo and Juliet want to meet and graze in as large a region as possible along the pasture fence.  However, this region should not contain too many Cowpulets, otherwise the chance of the two being caught is too great.  Romeo has determined where along the fence each of the N (1 ≤ N ≤ 1000) members of the Cowpulet herd grazes.  The long straight fence contains P (1 ≤ P ≤ 1000) equally-spaced posts numbered 1..P. Each Cowpulet grazes between some pair of adjacent posts.  Help Romeo determine the length of the largest contiguous region along the fence containing no more than C (0 ≤ C ≤ 1000) members of the Cowpulet herd.</p>

### 입력 

 <ul>
	<li>Line 1: Three separated integers: N, P, and C</li>
	<li>Lines 2..N+1: Each line contains an integer X, in the range 1..P-1, specifying that a  member of the Cowpulet herd grazes between fence posts X and X+1.  Multiple Cowpulets can graze between any given pair of fence posts.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer specifying the size (the number of gaps between  fence posts) of the largest contiguous region containing at most C  Cowpulets.</li>
</ul>

