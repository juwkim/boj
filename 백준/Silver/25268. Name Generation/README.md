# [Silver V] Name Generation - 25268 

[문제 링크](https://www.acmicpc.net/problem/25268) 

### 성능 요약

메모리: 117732 KB, 시간: 156 ms

### 분류

구성적(constructive), 무작위화(randomization), 문자열(string)

### 문제 설명

<p>Ingrid is the founder and CEO of bicycle retailer BIKEA. The company sells bicycles for customers to assemble themselves.</p>

<p>BIKEA has $N$ different bicycles to offer. Ingrid wants to give each of them a human-readable name, to make it easy to remember. But doing this by hand is a very time consuming task. </p>

<p>You are given the number $N$, and your task is to generate $N$ different names. To make the names readable, they must satisfy the following:</p>

<ol>
	<li>Each name has length between $3$ and $20$, and only consists of lowercase  English letters.</li>
	<li>Three consecutive letters of a name cannot all be vowels or consonants.  Here we consider <code>a</code>, <code>e</code>, <code>i</code>, <code>o</code>, <code>u</code> vowels, while the remaining $21$ letters are consonants.</li>
</ol>

<p>For example, <code>hello</code>, <code>abc</code>, and <code>lkab</code> are all valid names, whereas <code>ingrid</code>, <code>bo</code> and <code>louise</code> are invalid. </p>

### 입력 

 <p>The input consists of one integer $N$ ($1 \leq N \leq 30000$), the number of names to generate.</p>

### 출력 

 <p>Print $N$ lines, each of them containing a name. It can be proven that it is possible to generate $N$ different names.</p>

