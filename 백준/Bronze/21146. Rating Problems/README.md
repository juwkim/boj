# [Bronze III] Rating Problems - 21146 

[문제 링크](https://www.acmicpc.net/problem/21146) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 그리디 알고리즘(greedy), 수학(math)

### 문제 설명

<p>Your judges are preparing a problem set, and they’re trying to evaluate a problem for inclusion in the set. Each judge rates the problem with an integer between $-3$ and $3$, where:</p>

<ul>
	<li>$3$ means: I <em>really</em> like this problem!</li>
	<li>$-3$ means: I <em>really don’t</em> like this problem!</li>
	<li>$0$ means: Meh. I don’t care if we use this problem or not.</li>
</ul>

<p>The overall rating of the problem is the average of all of the judges’ ratings—that is, the sum of the ratings divided by the number of judges providing a rating.</p>

<p>Some judges have already rated the problem. Compute the minimum and maximum possible overall rating that the problem can end up with after the other judges submit their ratings.</p>

### 입력 

 <p>The first line of input contains two integers $n$ ($1 \le n \le 10$) and $k$ ($0 \le k \le n$), where $n$ is the total number of judges, and $k$ is the number of judges who have already rated the problem.</p>

<p>Each of the next $k$ lines contains a single integer $r$ ($-3 \le r \le 3$). These are the ratings of the $k$ judges that have already rated the problem.</p>

### 출력 

 <p>Output two space-separated floating point numbers on a single line, which are the minimum and maximum overall rating the problem could achieve after the remaining judges rate the problem, minimum first. These values must be accurate to an absolute or relative error of $10^{-4}$.</p>

