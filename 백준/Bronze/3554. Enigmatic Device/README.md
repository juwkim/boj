# [Bronze III] Enigmatic Device - 3554 

[문제 링크](https://www.acmicpc.net/problem/3554) 

### 성능 요약

메모리: 213744 KB, 시간: 7924 ms

### 분류

구현(implementation)

### 문제 설명

<p>Yes, it happened! The first contact! Aliens will visit the Earth in 2010! And they promised to bring an enigmatic device which cannot be constructed using existing Earth technologies. Most of the scientists of the world think so! All newspapers already published their leading articles about it. </p>

<p>This device will accept an integer sequence $\{a_i\}$ as its initial input. After that, it can perform the following two operations:</p>

<ol>
	<li>Take an interval $[l; r]$ and perform $a_i \leftarrow a_i^2 \bmod 2010$ for all $a_i$ such that $l \le i \le r$.</li>
	<li>Take an interval $[l; r]$ and output the sum of all $a_i$ such that $l\le i\le r$. Note that the sum is <em>not</em> taken modulo 2010.</li>
</ol>

<p>The amazing thing about this device is that it is able to perform $50\,000$ operations of this kind with a sequence of $50\,000$ numbers within 3 seconds. Nobody could do it before!</p>

<p>But Roman does not believe in aliens and thinks that it is only a great hoax made by somebody just to win another million bucks on the stock exchange. His goal is to prove this. So he hired you to write a program to simulate this device.</p>

<p>Given an integer sequence $a_i$ and a sequence of operations, write a program which simulates the behaviour of the strange alien device.</p>

### 입력 

 <p>The first line of the input contains the length of the sequence $n$ ($1\le n\le 50\,000$). The second line contains $n$ numbers $a_i$ forming the initial sequence ($0\le a_i\le 2009$). The third line contains the number of operations $m$ ($1\le m\le 50\,000$). The rest of file contains $m$ lines, each describing one operation. The $j$-th operation is described by its kind $k_j$ (<code>1</code> for squaring, <code>2</code> for calculating the sum), followed by two integers $l_j$ and $r_j$ ($1\le l_j \le r_j\le n$).</p>

### 출력 

 <p>For each operation of the second kind, write their output on the separate line, in order they appear in the input.</p>

