# [Bronze I] The Next Number (Small) - 12645 

[문제 링크](https://www.acmicpc.net/problem/12645) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

브루트포스 알고리즘(bruteforcing), 그리디 알고리즘(greedy)

### 문제 설명

<p>You are writing out a list of numbers. Your list contains all numbers with exactly <strong>D<sub>i</sub></strong> digits in its decimal representation which are equal to <strong>i</strong>, for each <strong>i</strong> between 1 and 9, inclusive. You are writing them out in ascending order.</p>

<p>For example, you might be writing every number with two '1's and one '5'. Your list would begin 115, 151, 511, 1015, 1051.</p>

<p>Given <strong>N</strong>, the last number you wrote, compute what the next number in the list will be.</p>

### 입력 

 <p>The first line of input contains an integer <strong>T</strong>, the number of test cases in the input. <strong>T</strong> lines follow, one for each test case, each containing a single integer <strong>N</strong>.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ T ≤ 50</li>
	<li>1 ≤ N ≤ 10<sup>6</sup></li>
</ul>

### 출력 

 <p>For each test case, output </p>

<pre>Case #<strong>X</strong>: <strong>K</strong></pre>

<p>where <strong>X</strong> is the test case number, starting from 1, and <strong>K</strong> is the next integer in the list.</p>

