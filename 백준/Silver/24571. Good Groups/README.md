# [Silver IV] Good Groups - 24571 

[문제 링크](https://www.acmicpc.net/problem/24571) 

### 성능 요약

메모리: 366264 KB, 시간: 1608 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set)

### 문제 설명

<p>A class has been divided into groups of three. This division into groups might violate two types of constraints: some students must work together in the same group, and some students must work in separate groups.</p>

<p>Your job is to determine how many of the constraints are violated.</p>

### 입력 

 <p>The first line will contain an integer X with X ≥ 0. The next X lines will each consist of two different names, separated by a single space. These two students must be in the same group.</p>

<p>The next line will contain an integer Y with Y ≥ 0. The next Y lines will each consist of two different names, separated by a single space. These two students must not be in the same group.</p>

<p>Among these X + Y lines representing constraints, each possible pair of students appears at most once.</p>

<p>The next line will contain an integer G with G ≥ 1. The last G lines will each consist of three different names, separated by single spaces. These three students have been placed in the same group.</p>

<p>Each name will consist of between 1 and 10 uppercase letters. No two students will have the same name and each name appearing in a constraint will appear in exactly one of the G groups.</p>

### 출력 

 <p>Output an integer between 0 and X +Y which is the number of constraints that are violated.</p>

