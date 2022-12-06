# [Bronze III] Contest Struggles - 21339 

[문제 링크](https://www.acmicpc.net/problem/21339) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Lotte is competing in a programming contest. Her team has already solved $k$ out of the $n$ problems in the problem set, but as the problems become harder, she begins to lose focus and her mind starts to wander.</p>

<p>She recalls hearing the judges talk about the difficulty of the problems, which they rate on an integer scale from $0$ to $100$, inclusive. In fact, one of the judges said that "<em>the problem set has never been so tough, the average difficulty of the problems in the problem set is $d$!</em>"</p>

<p>She starts thinking about the problems her team has solved so far, and comes up with an estimate $s$ for their average difficulty. In hope of gaining some motivation, Lotte wonders if she can use this information to determine the average difficulty of the remaining problems.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with two integers $n$ and $k$ ($2\leq n\leq 10^6$, $0 < k < n$), the total number of problems and the number of problems Lotte's team has solved so far.</li>
	<li>One line with two integers $d$ and $s$ ($0\leq d,s \leq 100$), the average difficulty of all the problems and Lotte's estimate of the average difficulty of the problems her team has solved.</li>
</ul>

### 출력 

 <p>Assuming Lotte's estimate is correct, output the average difficulty of the unsolved problems, or "<code>impossible</code>" if the average difficulty does not exist. Your answer should have an absolute or relative error of at most $10^{-6}$.</p>

