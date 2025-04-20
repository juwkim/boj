# [Silver I] Shopping - 10332 

[문제 링크](https://www.acmicpc.net/problem/10332) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

그리디 알고리즘, 정렬, 스위핑

### 제출 일자

2025년 4월 20일 21:16:39

### 문제 설명

<p>Your friend will enjoy shopping. She will walk through a mall along a straight street, where N individual shops (numbered from 1 to N) are aligned at regular intervals. Each shop has one door and is located at the one side of the street. The distances between the doors of the adjacent shops are the same length, i.e. a unit length. Starting shopping at the entrance of the mall, she visits shops in order to purchase goods. She has to go to the exit of the mall after shopping.</p>

<p>She requires some restrictions on visiting order of shops. Each of the restrictions indicates that she shall visit a shop before visiting another shop. For example, when she wants to buy a nice dress before choosing heels, she shall visit a boutique before visiting a shoe store. When the boutique is farther than the shoe store, she must pass the shoe store before visiting the boutique, and go back to the shoe store after visiting the boutique.</p>

<p>If only the order of the visiting shops satisfies all the restrictions, she can visit other shops in any order she likes.</p>

<p>Write a program to determine the minimum required walking length for her to move from the entrance to the exit.</p>

<p>Assume that the position of the door of the shop numbered k is k units far from the entrance, where the position of the exit is N + 1 units far from the entrance.</p>

### 입력 

 <p>The input consists of a single test case.</p>

<pre>N m
c<sub>1</sub> d<sub>1</sub>
.
.
.
c<sub>m</sub> d<sub>m</sub></pre>

<p>The first line contains two integers N and m, where N (1 ≤ N ≤ 1000) is the number of shops, and m (0 ≤ m ≤ 500) is the number of restrictions. Each of the next m lines contains two integers c<sub>i</sub> and d<sub>i</sub> (1 ≤ c<sub>i</sub> < d<sub>i</sub> ≤ N) indicating the i-th restriction on the visiting order, where she must visit the shop numbered c<sub>i</sub> after she visits the shop numbered d<sub>i</sub> (i = 1, ... , m).</p>

<p>There are no pair of j and k that satisfy c<sub>j</sub> = c<sub>k</sub> and d<sub>j</sub> = d<sub>k</sub>.</p>

### 출력 

 <p>Output the minimum required walking length for her to move from the entrance to the exit. You should omit the length of her walk in the insides of shops.</p>

