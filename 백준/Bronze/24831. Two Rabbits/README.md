# [Bronze II] Two Rabbits - 24831 

[문제 링크](https://www.acmicpc.net/problem/24831) 

### 성능 요약

메모리: 30840 KB, 시간: 156 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Being tired of participating in too many Codeforces rounds, Gildong decided to take some rest in a park. He sat down on a bench, and soon he found two rabbits hopping around. One of the rabbits was taller than the other.</p>

<p>He noticed that the two rabbits were hopping <em>towards each other</em>. The positions of the two rabbits can be represented as integer coordinates on a horizontal line. The taller rabbit is currently on position $x$, and the shorter rabbit is currently on position $y$ ($x \lt y$). Every second, each rabbit hops to another position. The taller rabbit hops to the positive direction by $a$, and the shorter rabbit hops to the negative direction by $b$.</p>

<p style="text-align: center;"><img alt="" src=""></p>

<p>For example, let's say $x=0$, $y=10$, $a=2$, and $b=3$. At the $1$-st second, each rabbit will be at position $2$ and $7$. At the $2$-nd second, both rabbits will be at position $4$.</p>

<p>Gildong is now wondering: <em>Will the two rabbits be at the same position <strong>at the same moment</strong>? If so, how long will it take?</em> Let's find a moment in time (in seconds) after which the rabbits will be at the same point.</p>

### 입력 

 <p>Each test contains one or more test cases. The first line contains the number of test cases $t$ ($1 \le t \le 1000$).</p>

<p>Each test case contains exactly one line. The line consists of four integers $x$, $y$, $a$, $b$ ($0 \le x \lt y \le 10^9$, $1 \le a,b \le 10^9$) — the current position of the taller rabbit, the current position of the shorter rabbit, the hopping distance of the taller rabbit, and the hopping distance of the shorter rabbit, respectively.</p>

### 출력 

 <p>For each test case, print the single integer: number of seconds the two rabbits will take to be at the same position.</p>

<p>If the two rabbits will never be at the same position simultaneously, print $-1$.</p>

