# [Bronze I] Greedily Increasing Subsequence - 17931 

[문제 링크](https://www.acmicpc.net/problem/17931) 

### 성능 요약

메모리: 149436 KB, 시간: 916 ms

### 분류

자료 구조(data_structures), 그리디 알고리즘(greedy), 구현(implementation), 스택(stack)

### 문제 설명

<p>Given a permutation $A = (a_1, a_2, \dots, a_N)$ of the integers $1, 2, \dots, N$, we define the <em>greedily increasing subsequence</em> (GIS) in the following way.</p>

<p>Let $g_1 = a_1$. For every $i > 1$, let $g_i$ be the leftmost integer in $A$ that is strictly larger than $g_{i-1}$. If there for a given $i$ is no such integer, we say that the GIS of the sequence is the sequence $(g_1, g_2, ..., g_{i - 1})$.</p>

<p>Your task is to, given a permutation $A$, compute the GIS of $A$.</p>

### 입력 

 <p>The first line of input contains an integer $1 \le N \le 10^6$, the number of elements of the permutation $A$. The next line contains $N$ distinct integers between $1$ and $N$, the elements $a_1, \dots, a_N$ of the permutation $A$.</p>

### 출력 

 <p>First, output a line containing the length $l$ of the GIS of $A$. Then, output $l$ integers, containing (in order) the elements of the GIS.</p>

