# [Silver III] Meeting Time - 10678 

[문제 링크](https://www.acmicpc.net/problem/10678) 

### 성능 요약

메모리: 111820 KB, 시간: 148 ms

### 분류

브루트포스 알고리즘, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 1월 28일 08:35:29

### 문제 설명

<p>Bessie and her sister Elsie want to travel from the barn to their favorite field, such that they leave at exactly the same time from the barn, and also arrive at exactly the same time at their favorite field.</p>

<p>The farm is a collection of N fields (1 <= N <= 16) numbered 1..N, where field 1 contains the barn and field N is the favorite field. The farm is built on the side of a hill, with field X being higher in elevation than field Y if X < Y.  An assortment of M paths connect pairs of fields.  However, since each path is rather steep, it can only be followed in a downhill direction. For example, a path connecting field 5 with field 8 could be followed in the 5 -> 8 direction but not the other way, since this would be uphill.  Each pair of fields is connected by at most one path, so M <= N(N-1)/2.</p>

<p>It might take Bessie and Elsie different amounts of time to follow a path; for example, Bessie might take 10 units of time, and Elsie 20. Moreover, Bessie and Elsie only consume time when traveling on paths between fields -- since they are in a hurry, they always travel through a field in essentially zero time, never waiting around anywhere.</p>

<p>Please help determine the shortest amount of time Bessie and Elsie must take in order to reach their favorite field at exactly the same moment.</p>

### 입력 

 <p>The first input line contains N and M, separated by a space.</p>

<p>Each of the following M lines describes a path using four integers A B C D, where A and B (with A < B) are the fields connected by the path, C is the time required for Bessie to follow the path, and D is the time required for Elsie to follow the path.  Both C and D are in the range 1..1000.</p>

### 출력 

 <p>A single integer, giving the minimum time required for Bessie and Elsie to travel to their favorite field and arrive at the same moment. If this is impossible, or if there is no way for Bessie or Elsie to reach the favorite field at all, output the word IMPOSSIBLE on a single line.</p>

