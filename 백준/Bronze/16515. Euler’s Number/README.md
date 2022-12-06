# [Bronze II] Euler’s Number - 16515 

[문제 링크](https://www.acmicpc.net/problem/16515) 

### 성능 요약

메모리: 28776 KB, 시간: 96 ms

### 분류

수학(math)

### 문제 설명

<p>Euler’s number (you may know it better as just \(e\)) has a special place in mathematics. You may have encountered \(e\) in calculus or economics (for computing compound interest), or perhaps as the base of the natural logarithm, ln x, on your calculator.</p>

<p>While e can be calculated as a limit, there is a good approximation that can be made using discrete mathematics. The formula for \(e\) is:</p>

<p>\[e = \sum_{i=0}^{n}{\frac{1}{i!}} = \frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \frac{1}{4!} + \cdots\]</p>

<p>Note that 0! = 1. Now as n approaches ∞, the series converges to \(e\). When n is any positive constant, the formula serves as an approximation of the actual value of \(e\). (For example, at n = 10 the approximation is already accurate to 7 decimals.)</p>

<p>You will be given a single input, a value of n, and your job is to compute the approximation of e for that value of n.</p>

### 입력 

 <p>A single integer n, ranging from 0 to 10 000.</p>

### 출력 

 <p>A single real number – the approximation of e computed by the formula with the given n. All output must be accurate to an absolute or relative error of at most 10<sup>−12</sup>.</p>

