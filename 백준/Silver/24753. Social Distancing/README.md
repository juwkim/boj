# [Silver V] Social Distancing - 24753 

[문제 링크](https://www.acmicpc.net/problem/24753) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>It's time for a social distancing party! A group of friends are sitting around a circular table where some seats are filled and some seats are empty. In particular, to maintain social distancing protocols, no two people are sitting directly beside each other.</p>

<p>They want to expand the party and include more friends, but no one is willing to move out of their current seat. Given the current table seating, determine the maximum number of additional people that can be seated such that there is still at least one empty seat between all pairs of people seated.</p>

### 입력 

 <p>The first line of input contains two integers $S$ ($3 \leq S \leq 1\,000$), which is the number of seats at the table, and $N$ ($1 \leq N \leq S/2$), which is the number of people that are already seated at the table.</p>

<p>Note that the seats of the table are numbered $1, 2, \ldots, S$ in a circular fashion: for each $1 \leq i < S$, seats numbered $i$ and $i+1$ are directly beside each other. Seats $S$ and $1$ are also directly beside each other.</p>

<p>The second line contains $N$ integers $a_1, a_2, \ldots, a_N$ ($1 \leq a_1 < a_2 < \cdots < a_N \leq S$), which indicates that seat number $a_{i}$ is currently occupied. No two occupied seats are directly beside each other.</p>

### 출력 

 <p>Display the maximum number of additional friends that can be seated at the table such that there is still at least one empty seat between all pairs of people seated.</p>

