# [Silver IV] Telefoni - 12110 

[문제 링크](https://www.acmicpc.net/problem/12110) 

### 성능 요약

메모리: 154672 KB, 시간: 164 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>There are N desks in a room, placed from left to right, one next to each other. Some desks have phones on them, whereas some desks are empty. All phones are broken, so the phone on the ith desk will ring if the phone at jth desk rings, which is at most D desks away from the ith desk. In other words, it holds |j - i| ≤ D. The first and the last desk will always have a phone on them. In the beginning the leftmost phone rings. What is the minimal amount of new phones to be placed on the desks so that the last phone rings?</p>

### 입력 

 <p>The first line of input contains two positive integers, N (1 ≤ N ≤ 300 000) and D (1 ≤ D ≤ N). The following line contains N numbers 0 or 1. If the ith number is 1, then the ith desk from the left has a phone on it, otherwise the ith desk is empty.</p>

### 출력 

 <p>The first and only line of output must contain the required minimal number of phones.</p>

