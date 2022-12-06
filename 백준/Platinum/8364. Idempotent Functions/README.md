# [Platinum V] Idempotent Functions - 8364 

[문제 링크](https://www.acmicpc.net/problem/8364) 

### 성능 요약

메모리: 170620 KB, 시간: 236 ms

### 분류

조합론(combinatorics), 수학(math)

### 문제 설명

<p>You are given a positive integer <em>n</em>. By <em>A</em> we mean the set {1, 2, 3, ..., <em>n</em>}. Function <em>f</em> : <em>A</em> → <em>A</em> is called a <i>permutation</i> if it is injective (for distinct arguments returns distinct values). Function <em>f</em> : <em>A</em> → <em>A</em> is called <i>idempotent</i> if for every <em>i</em> ∈ <em>A</em> holds <em>f</em>(<em>f</em>(<em>i</em>)) = <em>f</em>(<em>i</em>).</p>

<p>You are given a function <em>f</em> : <em>A</em> → <em>A</em>. How many pairs of functions (<em>g</em>, <em>h</em>) satisfy following conditions:</p>

<ul>
	<li><em>g</em> : <em>A</em> → <em>A</em> is a permutation,</li>
	<li><em>h</em> : <em>A</em> → <em>A</em> is idempotent,</li>
	<li>for every <em>i</em> ∈ <em>A</em> holds <em>f</em>(<em>i</em>) = <em>h</em>(<em>g</em>(<em>i</em>))?</li>
</ul>

<p>Write a program which:</p>

<ul>
	<li>reads number <em>n</em> and description of function <em>f</em> from the standard input ,</li>
	<li>determines the number of pairs of functions (<em>g</em>, <em>h</em>) satisfying the requirement described above,</li>
	<li>writes the result to the standard output.</li>
</ul>

### 입력 

 <p>In the first line of input there is one integer <em>n</em> (1 ≤ <em>n</em> ≤ 200 000). Second line contains a description of function <em>f</em> : <em>f</em>(<em>i</em>) (1 ≤ <em>f</em>(<em>i</em>) ≤ <em>n</em>) for <em>i</em> = 1, ..., <em>n</em>, separated with single spaces.</p>

### 출력 

 <p>In the first line of output there should be a single integer: the remainder of the division by 1 000 000 007 of the number of different pairs of functions (<em>g</em>, <em>h</em>) satisfying the requirement.</p>

