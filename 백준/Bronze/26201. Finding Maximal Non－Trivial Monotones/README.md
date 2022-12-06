# [Bronze II] Finding Maximal Non-Trivial Monotones - 26201 

[문제 링크](https://www.acmicpc.net/problem/26201) 

### 성능 요약

메모리: 121408 KB, 시간: 128 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>In this problem we will be dealing with character sequences, often called <em>strings</em>. A sequence is <em>non-trivial</em> if it contains at least two elements.</p>

<p>Given a sequence $s$, we say that a chunk $s_i , \dots , s_j$ is <em>monotone</em> if all its characters are equal, and we say that it is <em>maximal</em> if this chunk cannot be extended to left or right without losing the monotonicity.</p>

<p>Given a sequence composed only of characters “<code>a</code>” and “<code>b</code>”, determine how many characters “<code>a</code>” occur in non-trivial maximal monotone chunks.</p>

### 입력 

 <p>The input consists of two lines. The first line contains a single integer $N$, where $1 ≤ N ≤ 10^5$. The second line contains a string with exactly $N$ characters, composed only of the characters “<code>a</code>” and “<code>b</code>”.</p>

### 출력 

 <p>Print a single line containing an integer representing the total number of times the character “<code>a</code>” occurs in non-trivial maximal monotone chunks.</p>

