# [Bronze I] Streets Ahead - 27589 

[문제 링크](https://www.acmicpc.net/problem/27589) 

### 성능 요약

메모리: 134428 KB, 시간: 372 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵

### 문제 설명

<p>International Connecting Passage Causeway is a long, rutted two-way country road crossed by streets at different points.</p>

<p>There are many drivers, and each will drive along the country road starting at some intersection and ending at some other intersection. For each driver, how many intersections will they drive through?</p>

### 입력 

 <p>The first line contains two integers, $n$ $(2 \le n \le 10^5)$ and $q$ $(1 \le q \le 10^5)$, where $n$ is the number of cross streets and $q$ is the number of drivers.</p>

<p>Each of the next $n$ lines contains a string of at most ten lowercase letters representing the name of one of the streets that crosses the country road. All street names are unique. Driving along the country road in some direction, one sees these streets in exactly the order provided.</p>

<p>Each of the next $q$ lines contains two strings of at most ten lowercase letters representing the start and end intersection for each driver. Queries will be between distinct streets.</p>

### 출력 

 <p>Output $q$ lines, the $i$th line containing the number of intersections that the $i$th driver drives through.</p>

