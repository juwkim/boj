# [Bronze II] Buffon's Needle - 20575 

[문제 링크](https://www.acmicpc.net/problem/20575) 

### 성능 요약

메모리: 124508 KB, 시간: 212 ms

### 분류

수학(math), 파싱(parsing), 문자열(string)

### 문제 설명

<p>For millenia, people have been interested in approximating $\pi$. One famous method is known as Buffon's Needle: drop a bunch of needles of length $1$ on a coordiate plane with a vertical line drawn at each integer $x$ coordinate (so there are lines $x = 0$, $x = 1$, $x = -1$, and so on). Each needle either intersects a vertical line, or lies entirely between two vertical lines. It turns out that, if the needles are dropped randomly, the fraction of needles that intersect a vertical line can be used to approximate $\pi$! (The specific assumptions about exactly how the needles are dropped in the experiment are not important for this problem.)</p>

<p>In particular, let $x$ be the fraction of needles that intersect a vertical line. Then</p>

<p>$$\pi \approx \frac{2}{x}.$$</p>

<p>You are given the positions of $N$ needles (not necessarily random), and it is guaranteed that at least one of them intersects a vertical line. What is the corresponding approximation of $\pi$, using the above formula?</p>

### 입력 

 <p>The first line of input contains a single integer $N$ ($1 \leq N \leq 10^4$), the number of needles. $N$ lines follow.</p>

<p>The $i$-th such line describes the $i$-th needle. It contains four real numbers: $x_{i1}, y_{i1}, x_{i2}, y_{i2}$. This means that the $i$-th needle has one endpoint at $(x_{i1}, y_{i1})$ in the plane and the other endpoint at $(x_{i2}, y_{i2})$.</p>

<p>All real numbers in the input are given with exactly $6$ digits after the decimal point and have absolute value at most $10$. Furthermore, it is guaranteed that no $x$ coordinates in the input are within $10^{-6}$ of an integer.</p>

<p>Since all the needles are of length $1$, for each $i$ it is guaranteed that</p>

<p>$$|(x_{i1} - x_{i2})^2 + (y_{i1} - y_{i2})^2 - 1| < 10^{-3}.$$</p>

### 출력 

 <p>Output a single real number, the approximation of $\pi$ described above. Your answer is considered correct if its absolute or relative error is at most $10^{-6}$.</p>

