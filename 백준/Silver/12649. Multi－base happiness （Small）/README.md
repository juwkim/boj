# [Silver V] Multi-base happiness (Small) - 12649 

[문제 링크](https://www.acmicpc.net/problem/12649) 

### 성능 요약

메모리: 29052 KB, 시간: 76 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Given an integer N, replace it by the sum of the squares of its digits. A happy number is a number where, if you apply this process repeatedly, it eventually results in the number 1. For example, if you start with 82:</p>

<pre>8*8 + 2*2       = 64 + 4    = 68,  repeat:
6*6 + 8*8       = 36 + 64   = 100, repeat:
1*1 + 0*0 + 0*0 = 1 + 0 + 0 = 1 (happy! :)
</pre>

<p>Since this process resulted in 1, 82 is a happy number.</p>

<p>Notice that a number might be happy in some bases, but not happy in others. For instance, the base 10 number 82 is not a happy number when written in base 3 (as 10001).</p>

<p>You are one of the world's top number detectives. Some of the bases got together (yes, they are organized!) and hired you for an important task: find out what's the smallest integer number that's greater than 1 and is happy in all the given bases.</p>

### 입력 

 <p>The first line of input gives the number of cases <strong>T</strong>. <strong>T</strong> test cases follow. Each case consists of a single line. Each line contains a space separated list of distinct integers, representing the bases. The list of bases is always in increasing order.</p>

<p>Limits</p>

<ul>
	<li>2 ≤ all possible input bases ≤ 10</li>
	<li>1 ≤ <strong>T</strong> ≤ 42</li>
	<li>2 ≤ number of bases on each test case ≤ 3</li>
</ul>

### 출력 

 <p>For each test case, output: </p>

<pre>Case #<strong>X</strong>: <strong>K</strong></pre>

<p>where <strong>X</strong> is the test case number, starting from 1, and <strong>K</strong> is the decimal representation of the smallest integer (greater than 1) which is happy in all of the given bases.</p>

