# [Silver III] Connected or Not Connected - 5237 

[문제 링크](https://www.acmicpc.net/problem/5237) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 1월 28일 20:10:05

### 문제 설명

<p>Sam and Quorra are trying to build a map of a secret base in the Grid world that contains a number of (virtual) sites interconnected by (virtual) pathways. Although they know the number of sites (n), their knowledge of interconnections between the sites is sparse. Several different programs that have been inside the base are able to give them some information about the connections between the sites, and Sam and Quorra need to put it together. In particular, they would like to make sure that they have enough information to know how to go from every site to every other site.</p>

<p>Your goal is to help them decide if a specified set of connections is enough to ensure that there is a path from every site to every other site. Assume that the connections are bi-directional, i.e., if we know that there is a connection between site 1 and site 2, then we can go from site 1 to site 2, and vice versa.</p>

### 입력 

 <p>The first line in the test data file contains the number of test cases (≤ 50). After that, each line contains a test case. The first number in each test case is the number of sites, n (≤ 100). The sites are numbered from 0 to n − 1. The second number is the number of connections between the sites, k (≤ 200). After that there are k pairs of numbers, one for each connection. The connections might repeat and further, there may be self-connections (i.e., a connection from a site to itself).</p>

### 출력 

 <p>For each test case, you are to check whether there is path from every site to every other site, and output “Connected.” or “Not connected.” accordingly.</p>

