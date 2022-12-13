# [Bronze III] Desni klik - 26392 

[문제 링크](https://www.acmicpc.net/problem/26392) 

### 성능 요약

메모리: 114328 KB, 시간: 124 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>NFP is the future!, this is something all Noa’s friends can expect him to say when finance topics come up.</p>

<p>NFP is one of the cryptocurrencies. The value of NFP over the course of s days can be represented with a matrix with r rows and s columns, consisting only of characters <code>.</code> and <code>#</code>. The character <code>#</code> in the i-th column represents the value of NFP on the i-th day, with the value being the number of the row, counted bottom-up.</p>

<pre style="text-align: center;">....##.
#..#...
.##....
......#</pre>

<p style="text-align: center;">The value of NFP from the second example over the course of 7 days was: 3, 2, 2, 3, 4, 4, 1. The insecurity of this NFP is 3.</p>

<p>The insecurity of NFP is defined as the difference between the maximum and minimum value it achieves over the course of s days.</p>

<p>Noa wants to determine the insecurity for n NFPs, whose values are represented by matrices with r rows and s columns.</p>

<p>Help him determine the insecurity of each of the n NFPs.</p>

### 입력 

 <p>The first line contains integers n, r and s (1 ≤ n ≤ 20, 2 ≤ r, s ≤ 50), the number of NFPs, and the number of rows and colums of the matrices.</p>

<p>n matrices follows, one below another, each with r rows and s columns, representing NFP values. Each column consists only of characters <code>.</code>, except for exactly one character <code>#</code>.</p>

### 출력 

 <p>Print n lines. In the i-th of n lines print the insecurity od the i-th NFP.</p>

