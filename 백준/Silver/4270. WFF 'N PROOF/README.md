# [Silver III] WFF 'N PROOF - 4270 

[문제 링크](https://www.acmicpc.net/problem/4270) 

### 성능 요약

메모리: 109240 KB, 시간: 116 ms

### 분류

그리디 알고리즘

### 제출 일자

2024년 6월 22일 00:23:55

### 문제 설명

<p>WFF 'N PROOF is a logic game played with dice. Each die has six faces representing some subset of the possible symbols K, A, N, C, E, p, q, r, s, t. A Well-formed formula (WFF) is any string of these symbols obeying the following rules:</p>

<ul>
	<li>p, q, r, s, and t are WFFs</li>
	<li>if <i>w</i> is a WFF, N<i>w</i> is a WFF</li>
	<li>if <i>w</i> and <i>x</i> are WFFs, K<i>wx</i>, A<i>wx</i>, C<i>wx</i>, and E<i>wx</i> are WFFs.</li>
</ul>

<p>The meaning of a WFF is defined as follows:</p>

<ul>
	<li>p, q, r, s, and t are logical variables that may take on the value 0 (false) or 1 (true).</li>
	<li>K, A, N, C, E mean <i>and, or, not, implies,</i> and <i>equals</i> as defined in the truth table below.</li>
</ul>

<table class="table table-bordered td-center th-center">
	<thead>
		<tr>
			<th colspan="6">Definitions of K, A, N, C, and E</th>
		</tr>
		<tr>
			<th><code>w x</code></th>
			<th><code>Kwx</code></th>
			<th><code>Awx</code></th>
			<th><code>Nw</code></th>
			<th><code>Cwx</code></th>
			<th><code>Ewx</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>1 1</code></td>
			<td><code>1</code></td>
			<td><code>1</code></td>
			<td><code>0</code></td>
			<td><code>1</code></td>
			<td><code>1</code></td>
		</tr>
		<tr>
			<td><code>1 0</code></td>
			<td><code>0</code></td>
			<td><code>1</code></td>
			<td><code>0</code></td>
			<td><code>0</code></td>
			<td><code>0</code></td>
		</tr>
		<tr>
			<td><code>0 1</code></td>
			<td><code>0</code></td>
			<td><code>1</code></td>
			<td><code>1</code></td>
			<td><code>1</code></td>
			<td><code>0</code></td>
		</tr>
		<tr>
			<td><code>0 0</code></td>
			<td><code>0</code></td>
			<td><code>0</code></td>
			<td><code>1</code></td>
			<td><code>1</code></td>
			<td><code>1</code></td>
		</tr>
	</tbody>
</table>

<p>Given a collection of symbols resulting from throwing a set of dice, determine the longest WFF that can be formed from those symbols.</p>

### 입력 

 <p>Input consists of several test cases. Each test case is a single line containing a string containing between 1 and 100 of the characters. A line containing 0 follows the last case.</p>

### 출력 

 <p>For each test case, output a line containing the longest WFF that can be formed using some subset of the letters in the string. If there are several such WFFs, any one will do. If no WFF can be constructed, output a line containing "no WFF possible" as shown below.</p>

