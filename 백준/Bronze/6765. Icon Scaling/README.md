# [Bronze II] Icon Scaling - 6765 

[문제 링크](https://www.acmicpc.net/problem/6765) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>You have been asked to take a small icon that appears on the screen of a smart telephone and scale it up so it looks bigger on a regular computer screen.</p>

<p>The icon will be encoded as characters (x and *) in a 3 × 3 grid as follows:</p>

<pre><code>*x*
 xx 
* * </code></pre>

<p>Write a program that accepts a positive integer scaling factor and outputs the scaled icon. A scaling factor of k means that each character is replaced by a k × k grid consisting only of that character.</p>

### 입력 

 <p>The input will be a positive integer k such that k < 25.</p>

### 출력 

 <p>The output will be 3k lines, which represent each individual line scaled by a factor of k and repeated k times. A line is scaled by a factor of k by replacing each character in the line with k copies of the character.</p>

