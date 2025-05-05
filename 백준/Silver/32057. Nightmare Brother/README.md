# [Silver I] Nightmare Brother - 32057 

[문제 링크](https://www.acmicpc.net/problem/32057) 

### 성능 요약

메모리: 110760 KB, 시간: 100 ms

### 분류

브루트포스 알고리즘, 구현, 문자열

### 제출 일자

2025년 5월 5일 23:30:18

### 문제 설명

<p>Your brother has a string $S$ of length $M$ with indices from $1$ to $M$. You want to know exactly what string $S$ is. To help you, he gives you $N$ hints that might help you to figure out $S$. Hint $i$ is represented by an integer $X_i$ and a string $T_i$, indicating that the string $T_i$ appears as a substring of $S$ starting from index $X_i$ of $S$. All the hints are unique, that is, there are no hints $i$ and $j$ such that $i \ne j$ while $X_i = X_j$ and $T_i = T_j$.</p>

<p>However, your brother is known to be mischievous and tells you that there might be <strong>at most</strong> one false hint among all $N$ hints he has given, but he didn’t tell you which.</p>

<p>A string $S$ is a possible solution if and only if there exists a set of at least $N - 1$ hints (that are assumed to be true) where string $S$ is the <strong>only</strong> string consistent with all of the hints in the set.</p>

<p>You would like to find a possible solution. If there is no possible solution, you should output <code>-1</code>. If there is more than one possible solution, you should output <code>-2</code>.</p>

### 입력 

 <p>Input begins with two integers $N$ $M$ ($1 ≤ N ≤ 100$; $1 ≤ M ≤ 100$) representing the number of hints and the length of the scary string, respectively. Each of the next $N$ lines contains an integer and a string $X_i$ $T_i$ ($1 ≤ X_i , |T_i |$; $X_i + |T_i | - 1 ≤ M$) representing hint $i$. The string $T_i$ consists of only uppercase characters. It is guaranteed that there are no hints $i$ and $j$ such that $i \ne j$ while $X_i = X_j$ and $T_i = T_j$.</p>

### 출력 

 <p>If there is exactly one possible solution as explained in the problem description above, then output the string $S$ in a single line. If there is no possible solution, then output <code>-1</code> in a single line. If there is more than one possible solution, then output <code>-2</code> in a single line.</p>

