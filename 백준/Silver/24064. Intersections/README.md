# [Silver V] Intersections - 24064 

[문제 링크](https://www.acmicpc.net/problem/24064) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

수학(math)

### 문제 설명

<p>You are given the following two functions. ($\mathbb{N}_0$ denotes the set of non-negative integers.)</p>

<p>$$f(x)= \begin{cases} 0, & \mbox{if } x < 0 \\ x - 2k, & \mbox{if } 2k \le x < 2k+1 \, (k \in \mathbb{N}_0) \\ -x + 2(k+1) & \mbox{if } 2k + 1 \le x < 2k+2 \, (k \in \mathbb{N}_0) \end{cases}$$</p>

<p>$$g(x) = {x \over a}$$</p>

<p>How many intersections between the graphs of $y=f(x)$ and $y=g(x)$ exist on the XY-plane?</p>

### 입력 

 <p>The first and only line of the input contains a single integer $a$.</p>

### 출력 

 <p>Print the number of intersections between the graphs of $y = f(x)$ and $y = g(x)$. If there are infinitely many intersections, print <code>INF</code>.</p>

