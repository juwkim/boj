# [Bronze I] The Easiest Problem is This One - 6627 

[문제 링크](https://www.acmicpc.net/problem/6627) 

### 성능 요약

메모리: 28776 KB, 시간: 200 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math)

### 문제 설명

<p>If you are the lucky one to advance to the ACM-ICPC World Finals, one of the situations you will face is the world finals competition itself. Wait, isn’t that the main reason to go there?</p>

<p>In the beginning of each ACM-ICPC competition, there are two separate goals each team tries to accomplish:</p>

<p>among the given set of problems, find the easiest one,<br>
solve that problem as fast as possible.</p>

<p>To evaluate the performance of all teams in detail, we want to test your abilities for each of these two goals separately. The former goal (finding the easiest problem) is analyzed in another problem (difficult), here we deal with the latter goal (solving the easiest problem).</p>

<p>To isolate other influences, we will tell you clearly which problem is the easiest one to solve in this problem set (CTU Open Contest 2010). It is this one! What more can we do to emphasize that fact? The title says it. The problem name is easy. And believe us, it is true. This is indeed the easiest of all nine problems. We recommend you to do it first.</p>

<p>A positive integer number N can be expressed in the decimal system (numeral system with the base of 10) as the sequence of digits \(d_i\)</p>

<p>\[N = d_1d_2d_3d_4\dots d_k\]</p>

<p>where \(\forall i\), 1 ≤ \(i\) ≤ k : 0 ≤ \(d_i\) ≤ 9.</p>

<p>The digits express the value which has to be multiplied by a power of ten:</p>

<p>\[N = d_1 \cdot 10^{k-1} + d_2 \cdot 10^{k-2} + \dots + d_{k-1} \cdot 10 + d_k = \sum_{i=0} ^{k-1} {d_{i+1} \cdot 10^{k-i-1}}\]</p>

<p>The sum of the digits \(S(N)\) is then defined as the plain sum of all individual digits without multiplying them by powers of ten:</p>

<p>\[S(N) = d_1 + d_2 + d_3 + \dots + d_k = \sum_{i=0}^{k-1}{d_{i+1}}\]</p>

<p>For example:</p>

<p>\[N = 3029 = 3 \cdot 10^3 + 2 \cdot 10 + 9 \\ S(N) = 3 + 0 + 2 + 9 = 14\]</p>

<p>If we multiply the original number \(N\) with another number \(m\), the sum of the digits typically changes. For example, if \(m_1 = 26\):</p>

<p>\[N \cdot m_1 = 78754 = 7 \cdot 10^4 + 8 \cdot 10^3 + 7 \cdot 10^2 + 5 \cdot 10 + 4 \\ S(N \cdot m_1) = 7+8+7+5+4 = 31\]</p>

<p>However, there are some numbers that, if multiplied by \(N\), will result in the same sum of the digits as the original number \(N\). For example, consider \(m_2 = 37\):</p>

<p>\[N \cdot m_2 = 112073 = 10^5 + 10^4 + 2 \cdot 10^3 + 7 \cdot 10 + 3 \\ S(N \cdot m_2) = 1 + 1 + 2+0+7+3 = 14 = S(N)\]</p>

<p>Your task is to find the smallest positive integer \(p\) among those that will result in the same sum of the digits when multiplied by \(N\). To make the task a little bit more challenging, the number must also be higher than ten.</p>

### 입력 

 <p>The input consists of several test cases. Each case is described by a single line containing one positive integer number \(N\), 1 ≤ \(N\) ≤ 100 000. The last test case is followed by a line containing zero.</p>

### 출력 

 <p>For each test case, print one line with a single integer number \(p\) which satisfies all of the following conditions:</p>

<ul>
	<li>\(p\) > 10</li>
	<li>\(S(N)\) = \(S(N \cdot p)\)</li>
	<li>\(\forall q\in N:\left[ S(N)=S(N\cdot q) \right] \Rightarrow  \left[  (q \ge p) \vee (q \le 10) \right]\)</li>
</ul>

