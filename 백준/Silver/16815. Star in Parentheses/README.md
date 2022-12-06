# [Silver V] Star in Parentheses - 16815 

[문제 링크](https://www.acmicpc.net/problem/16815) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

자료 구조(data_structures), 스택(stack), 문자열(string)

### 문제 설명

<p>You are given a string $S$, which is balanced parentheses with a star symbol <code>*</code> inserted.</p>

<p>Any balanced parentheses can be constructed using the following rules:</p>

<ul>
	<li>An empty string is balanced.</li>
	<li>Concatenation of two balanced parentheses is balanced.</li>
	<li>If $T$ is balanced parentheses, concatenation of <code>(</code>, $T$, and <code>)</code> in this order is balanced.</li>
</ul>

<p>For example, <code>()()</code> and <code>(()())</code> are balanced parentheses. <code>)(</code> and <code>)()(()</code> are not balanced parentheses.</p>

<p>Your task is to count how many matching pairs of parentheses surround the star.</p>

<p>Let $S_i$ be the $i$-th character of a string $S$. The pair of $S_l$ and $S_r$ $(l < r)$ is called a matching pair of parentheses if $S_l$ is <code>(</code>, $S_r$ is <code>)</code> and the surrounded string by them is balanced when ignoring a star symbol.</p>

### 입력 

 <p>The input consists of a single test case formatted as follows.</p>

<pre class="mathjax">$S$</pre>

<p>$S$ is balanced parentheses with exactly one <code>*</code> inserted somewhere. The length of $S$ is between $1$ and $100$, inclusive.</p>

### 출력 

 <p>Print the answer in one line.</p>

