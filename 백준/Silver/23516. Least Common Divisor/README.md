# [Silver IV] Least Common Divisor - 23516 

[문제 링크](https://www.acmicpc.net/problem/23516) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

브루트포스 알고리즘(bruteforcing), 문자열(string)

### 문제 설명

<p>A <em>divisor</em> of string $A$ is a string $D$ which can be repeated an integer number of times to obtain $A$. For example, divisors of string "<code>aaaa</code>" are strings "<code>a</code>", "<code>aa</code>", and "<code>aaaa</code>", and divisors of string "<code>ababab</code>" are strings "<code>ab</code>" and "<code>ababab</code>".</p>

<p>Consider two strings $S$ and $T$. Find the shortest of strings which are simultaneously divisors of $S$ and divisors of $T$, or determine that there are no such strings.</p>

### 입력 

 <p>The first line contains string $S$, and the second line contains string $T$. Each of these strings has length from $1$ to $50$ characters, inclusive, and consists only of lowercase English letters.</p>

### 출력 

 <p>Print the least common divisor of strings $S$ and $T$, or the string "<code>No solution</code>" in case the least common divisor does not exist.</p>

