# [Silver I] Longest Contiguous Subsequence - 6042 

[문제 링크](https://www.acmicpc.net/problem/6042) 

### 성능 요약

메모리: 109544 KB, 시간: 96 ms

### 분류

브루트포스 알고리즘, 다이나믹 프로그래밍

### 제출 일자

2025년 4월 27일 17:00:11

### 문제 설명

<p>Bessie's friend Jessie wanted to enter a programming contest. "What are the tasks like?" she asked.</p>

<p>Bessie, known to be knowledgeable about so many things, said "Here is a typical problem that folks solve early in their competitive career. See if you can solve it."</p>

<p>Perhaps you can solve it, too.</p>

<p>You are given two sequences of integers, S1 and S2. S1 has length L1 (1 <= L1 <= 180) and S2 has length L2 (1 <= L2 <= 180). Your job is to print out the length of the longest contiguous subsequence of numbers common to both S1 and S2. Ordered sequence S1 has elements S1_1, S1_2, ..., S1_L1 (-100 <= S1_i <= 100); S2 has elements S2_i (-100 <= S2_i <= 100).</p>

<p>A contiguous subsequence is a consecutive run of numbers in that sequence. The subsequences of 1 2 3 1 are: the empty sequence, "1", "1 2", "1 2 3", "1 2 3 1", "2", "2 3", "2 3 1", "3", "3 1", and a repeat occurrence of "1".</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: L1 and L2</li>
	<li>Lines 2..L1+1: Line i+1 contains a single integer: S1_i</li>
	<li>Lines L1+2..L1+L2+1: Line L1+i+1 contains a integer: S2_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer, the length of the longest contiguous subsequence of S1 and S2</li>
</ul>

<p> </p>

