# [Silver I] Izbori - 15361 

[문제 링크](https://www.acmicpc.net/problem/15361) 

### 성능 요약

메모리: 121772 KB, 시간: 260 ms

### 분류

백트래킹, 비트마스킹, 브루트포스 알고리즘, 구현

### 제출 일자

2025년 5월 11일 20:11:37

### 문제 설명

<p>In a land with developed democracy far, far away, presidential elections for the football association are taking place. This land consists of N counties, and each county has its own football association. There are M presidential candidates labeled with 1, 2, … M. Each of the football associations will select exactly one candidate to cast their vote for. The winner of the election is the candidate with the most votes. If multiple candidates get the most amount of votes, the winner is the one with the smallest label.</p>

<p>During the election campaign, candidates visited the counties and tried to gain their sympathies. After having met all the candidates, each county’s football association determined the order in which they would cast their vote for each candidate.</p>

<p>For example, let’s assume that there are four candidates in the election and that one county’s order is 2, 1, 4, 3. This means that, unless they revoke their candidacy, the candidate with label 2 will get the county’s vote. If candidate 2 revokes their candidacy, and candidate 1 is still in the race, then they will get the vote, and so on.</p>

<p>Zdravko is a passionate football fan, and also a close friend of candidate with label K. He wants to know which candidate will win if neither of the candidates revokes their candidacy.</p>

<p>He also wants to know what is the minimal number of candidates he must persuade to revoke their candidacy in order for his friend, candidate K, to become the president of the football association.</p>

<p>Zdravko is currently dealing with other problems, so he is hoping that you will answer these questions.</p>

### 입력 

 <p>The first line of input contains the numbers N (1 ≤ N ≤ 100), M (1 ≤ M ≤ 15) and K (1 ≤ K ≤ M) from the task.</p>

<p>Each of the following N lines contains the orders given by the counties’ football associations, i.e. a permutation of the first M natural numbers.</p>

### 출력 

 <p>You must output the answers to the questions from the task, each in its own line.</p>

