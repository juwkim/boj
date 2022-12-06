# [Gold V] Googol String (Large) - 12075 

[문제 링크](https://www.acmicpc.net/problem/12075) 

### 성능 요약

메모리: 30888 KB, 시간: 72 ms

### 분류

애드 혹(ad_hoc), 구성적(constructive), 수학(math), 재귀(recursion)

### 문제 설명

<p>A "0/1 string" is a string in which every character is either <code>0</code> or <code>1</code>. There are two operations that can be performed on a 0/1 string:</p>

<ul>
	<li><b>switch</b>: Every <code>0</code> becomes <code>1</code> and every <code>1</code> becomes <code>0</code>. For example, "100" becomes "011".</li>
	<li><b>reverse</b>: The string is reversed. For example, "100" becomes "001".</li>
</ul>

<p>Consider this infinite sequence of 0/1 strings:</p>

<ul>
	<li>S<sub>0</sub> = ""</li>
	<li>S<sub>1</sub> = "0"</li>
	<li>S<sub>2</sub> = "001"</li>
	<li>S<sub>3</sub> = "0010011"</li>
	<li>S<sub>4</sub> = "001001100011011"</li>
	<li>...</li>
	<li>S<sub>N</sub> = S<sub>N-1</sub> + "0" + <b>switch</b>(<b>reverse</b>(S<sub>N-1</sub>)).</li>
</ul>

<p>You need to figure out the Kth character of S<sub>googol</sub>, where googol = 10<sup>100</sup>.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. Each of the next <b>T</b> lines contains a number <b>K</b>.</p>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the <strong>K</strong>th character of S<sub>googol</sub>.</p>

