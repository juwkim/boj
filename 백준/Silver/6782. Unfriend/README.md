# [Silver III] Unfriend - 6782 

[문제 링크](https://www.acmicpc.net/problem/6782) 

### 성능 요약

메모리: 108080 KB, 시간: 104 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 4월 7일 09:03:31

### 문제 설명

<p>Mark invited some people to join his social network. Some of them invited new people, who invited new people, and so on. Now there are N people in the network, numbered from 1 to N. Mark has decided to remove some people and keep others. There is one restriction: when removing a person, he will also remove the people s/he invited, and the people they invited, and so on. Mark will never remove himself, and we do not allow people to be invited by more than one person. Mark can also decide to not remove anyone.</p>

<p>How many different sets of people can be removed?</p>

### 입력 

 <p>The first line contains a single integer N (N ≤ 6), the number of people in the network. Next are N − 1 lines telling us who invited each person. To be precise, line i in this set (1 ≤ i ≤ N − 1) contains a single integer j (with j > i), which indicates that person j is the person who invited person i. Person N is Mark.</p>

### 출력 

 <p>Output a single integer, the number of possible sets of people that can be removed.</p>

