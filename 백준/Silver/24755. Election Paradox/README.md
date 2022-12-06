# [Silver V] Election Paradox - 24755 

[문제 링크](https://www.acmicpc.net/problem/24755) 

### 성능 요약

메모리: 30864 KB, 시간: 68 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting)

### 문제 설명

<p>In Oddland, the leader of the country is determined by a democratic election.  The country is divided into an odd number of regions, in which each region has an odd number of voters.</p>

<p>There are two (an even number!) political parties in Oddland, and the winning party is the one that wins the most number of regions.  A party wins a region if it receives more votes than the other party in that region.</p>

<p>Under this system, it is possible that the losing party receives more votes than the winning party.  For example, if there are three regions with $11$, $3$, and $3$ people, respectively, then a party could receive $8$, $1$, and $1$ votes and lose the election.  In this case, the losing party received the majority of the votes in the total population.</p>

<p>Determine the largest number of votes a party can receive and still lose the election.</p>

### 입력 

 <p>The first line of input contains an odd integer $N$ ($3 \leq N \leq 999$), which is the number of regions in Oddland. </p>

<p>The next line contains $N$ odd integers $p_i$ ($1 \leq p_i \leq 999$), which are the populations of the $N$ cities.</p>

### 출력 

 <p>Display the largest number of votes a party can receive and still lose the election.</p>

