# [Silver I] Friendship Graph - 9789 

[문제 링크](https://www.acmicpc.net/problem/9789) 

### 성능 요약

메모리: 185264 KB, 시간: 576 ms

### 분류

그래프 이론, 그래프 탐색

### 제출 일자

2025년 5월 5일 21:10:21

### 문제 설명

<p>Friendship between two persons is usually mutual, but not always.</p>

<p>If person A trusts person B, we have a directed edge A → B in the friendship graph G.</p>

<p>There may be a case that we have directed edge A → B in G but not directed edge B → A.</p>

<p>A person X wants to deliver a secret message to another person Y, either directly or via a chain of trusted friendships in G.</p>

<p>Can this secret message be successfully delivered?</p>

<p>Answer: 1 for a successful delivery, or 0 otherwise. There will be Q such queries with different X and Y in G.</p>

### 입력 

 <p>The first section of the input is for the friendship graph G.</p>

<p>The first line of input contains two integers in one line: V and E (1 ≤ V ≤ 2000; 0 ≤ E ≤ 100000). Then, we have a list of E lines that contains two integers: A and B that implies the existence of directed edge A → B in G.</p>

<p>Vertices are numbered from [0..V-1], i.e. 0 ≤ A, B < V.</p>

<p>The second section of the input is for the queries. The first and the second section of the input is separated by a blank line for clarity.</p>

<p>The query section starts with one line containing an integer Q (1 ≤ Q ≤ 200000).</p>

<p>Afterward, we have a list of Q lines that also contains two integers: X and Y (0 ≤ X, Y < V). Note that it is possible that X = Y.</p>

### 출력 

 <p>For each query, simply output one line containing either "1" or "0" (without the quotes) according to the problem description above.</p>

<p>Important Note: There is something interesting with this particular friendship graph G that you can probably use. In at least 99% of the Q queries, if a person X can send a secret message to another person Y, then Y can also send a secret message (that is, a reply) back to X.</p>

