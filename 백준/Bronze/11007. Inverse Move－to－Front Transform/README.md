# [Bronze II] Inverse Move-to-Front Transform - 11007 

[문제 링크](https://www.acmicpc.net/problem/11007) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>The Move-to-Front (MTF) transform is an encoding scheme which maps the input data into a sequence of numbers. Entropy encoding schemes often achieve better compression ratio on the data encoded by the MTF transform. The MTF transform is quite simple. The following scheme is the MTF transform on string consisting of only characters in lowercase.</p>

<ol>
	<li>Maintain a list of characters in lowercase. Initially, the list is sorted in the lexicographic order. I.e., the list is [abcdefghijklmnopqrstuvwxyz] at the beginning.</li>
	<li>Read a character α from the string. Output the index of α in the list, then move α to the front of the list.</li>
	<li>Repeat the previous step until all characters in the string are read.</li>
</ol>

<p>For example, the following is how the transform above works on the string hakka.</p>

<ol>
	<li>The first character h has index 7 in [abcdefghijklmnopqrstuvwxyz]. Output 7, then move h to the front of the list.</li>
	<li>The second character a has index 1 in [habcdefgijklmnopqrstuvwxyz]. Output 1, then move a to the front of the list.</li>
	<li>The third character k has index 10 in [ahbcdefgijklmnopqrstuvwxyz]. Output 10, then move k to the front of the list.</li>
	<li>The fourth character k has index 0 in [kahbcdefgijlmnopqrstuvwxyz]. Output 0, then move k to the front of the list.</li>
	<li>The fourth character a has index 1 in [kahbcdefgijlmnopqrstuvwxyz]. Output 1, then move a to the front of the list.</li>
</ol>

<p>The MTF transform maps hakka into the sequence (7, 1, 10, 0, 1). Please write a program to inverse the MTF transform. In other words, your program reads a sequence of numbers (a<sub>1</sub>,...,a<sub>n</sub>), then compute the string s such that the MTF transform maps s into (a<sub>1</sub>,...,a<sub>n</sub>).</p>

### 입력 

 <p>The first line of the input contains an integer T, T ≤ 50, which indicates the number of test cases. Each test case consists of two lines. The first one contains a positive integer n, 1 ≤ n ≤ 100, which indicates the length of the sequence. The second line contains n integers a<sub>1</sub>,...,a<sub>n</sub> separated by blanks. The input sequence is (a<sub>1</sub>,...,a<sub>n</sub>), and a<sub>i</sub> ∈ {0, 1,..., 25} for i ∈ {1,...,n}.</p>

### 출력 

 <p>For each test case, output the string s such that the MTF transform maps s into (a<sub>1</sub>,...,a<sub>n</sub>).</p>

