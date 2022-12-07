# [Silver IV] Fire on Field - 17968 

[문제 링크](https://www.acmicpc.net/problem/17968) 

### 성능 요약

메모리: 115136 KB, 시간: 160 ms

### 분류

브루트포스 알고리즘(bruteforcing), 다이나믹 프로그래밍(dp), 구현(implementation)

### 문제 설명

<p>We define <em>A</em> as a sequence of positive integers like the following.</p>

<blockquote>
<p>Let <em>A</em>[0] = 1, <em>A</em>[1] = 1. For a positive integer <em>i</em> ≥ 2, <em>A</em>[<em>i</em>] is the smallest positive integer under the condition that no three terms <em>A</em>[<em>i</em> − 2<em>k</em>], <em>A</em>[<em>i</em> − <em>k</em>], and <em>A</em>[<em>i</em>] form an arithmetic progression for any integer <em>k</em> > 0 such that <em>i</em> − 2<em>k</em> ≥ 0, that is, <em>A</em>[<em>i</em>] − <em>A</em>[<em>i</em> − <em>k</em>] ≠ <em>A</em>[<em>i</em> − <em>k</em>] − <em>A</em>[<em>i</em> − 2<em>k</em>].</p>
</blockquote>

<p>The sequence is uniquely determined like the following sequence: <em>A</em>[0] = 1, <em>A</em>[1] = 1, <em>A</em>[2] = 2, <em>A</em>[3] = 1, <em>A</em>[4] = 1, <em>A</em>[5] = 2, <em>A</em>[6] = 2, <em>A</em>[7] = 4, <em>A</em>[8] = 4, etc. The sequence element <em>A</em>[2] cannot be 1 since otherwise <em>A</em>[0] = 1, <em>A</em>[1] = 1, <em>A</em>[2] = 1 form an arithmetic progression; here <em>i</em> = 2 and <em>k</em> = 1. If <em>A</em>[2] is any integer larger than one, then the condition is satisfied. Therefore, <em>A</em>[2] should be 2 which is the smallest positive integer among the possible ones. Similarly, it is easy to know that <em>A</em>[3] = 1. The sequence element <em>A</em>[4] cannot be 3 since otherwise <em>A</em>[4] − <em>A</em>[4 − 2] = <em>A</em>[4 − 2] − <em>A</em>[4 − 2 × 2] ; here <em>i</em> = 4 and <em>k</em> = 2 . Other natural numbers like 1, 2 and 4 are also possible for <em>A</em>[4], but the smallest one is 1. Therefore, <em>A</em>[4] = 1.</p>

<p>This sequence is called “fire on field” or “forest fire” since the scatter plot of the sequence looks like spreading fire on a field. See the figure below.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/54909aee-bd6b-4c80-899e-2b11fbc75251/-/preview/" style="width: 464px; height: 324px;"></p>

<p>Given a non-negative integer <em>n</em>, write a program to output <em>A</em>[<em>n</em>].</p>

### 입력 

 <p>Your program is to read from standard input. The input consists of one line containing one non-negative integer <em>n</em> (0 ≤ <em>n</em> ≤ 1,000).</p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line. The line should contain <em>A</em>[<em>n</em>].</p>

