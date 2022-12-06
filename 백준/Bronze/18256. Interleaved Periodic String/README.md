# [Bronze II] Interleaved Periodic String - 18256 

[문제 링크](https://www.acmicpc.net/problem/18256) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

애드 혹(ad_hoc), 문자열(string)

### 문제 설명

<p>An interleaved periodic string S can be written down using the following procedure:</p>

<ol>
	<li>Write down any two strings s<sub>1</sub> and s<sub>2</sub> of lengths p<sub>1</sub> and p<sub>2</sub> respectively. The strings must consist of only 0s and 1s, and can possibly be empty.</li>
	<li>Concatenate some copies of the string s<sub>1</sub> to obtain string S<sub>1</sub>.</li>
	<li>Concatenate some copies of the string s<sub>2</sub> to obtain string S<sub>2</sub>.</li>
	<li>Interleave the strings S<sub>1</sub> and S<sub>2</sub> to obtain S.</li>
</ol>

<p>To interleave two strings, merge their characters arbitrarily, maintaining the relative order in which they occur in both strings. For example, the strings “101” and “011” can be interleaved to get “011011” or “101011”, however they cannot be interleaved to form “110110”. Given S, find the minimum possible value of (p<sub>1</sub> + p<sub>2</sub>).</p>

### 입력 

 <p>The input consists of multiple test cases. The first line contains the number of test cases T. Each of the next T lines contain a string S consisting of only ‘0’s and ‘1’s.</p>

### 출력 

 <p>Output T lines, one corresponding to each test case, containing the minimum value of (p<sub>1</sub> + p<sub>2</sub>) for the corresponding test case.</p>

