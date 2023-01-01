# [Silver IV] Bribe the Prisoners (Small) - 12641 

[문제 링크](https://www.acmicpc.net/problem/12641) 

### 성능 요약

메모리: 117240 KB, 시간: 172 ms

### 분류

백트래킹(backtracking), 브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>In a kingdom there are prison cells (numbered 1 to <strong>P</strong>) built to form a straight line segment. Cells number <strong>i</strong> and <strong>i+1</strong> are adjacent, and prisoners in adjacent cells are called "neighbours." A wall with a window separates adjacent cells, and neighbours can communicate through that window. </p>

<p>All prisoners live in peace until a prisoner is released. When that happens, the released prisoner's neighbours find out, and each communicates this to his other neighbour. That prisoner passes it on to <em>his</em> other neighbour, and so on until they reach a prisoner with no other neighbour (because he is in cell 1, or in cell <strong>P</strong>, or the other adjacent cell is empty). A prisoner who discovers that another prisoner has been released will angrily break everything in his cell, unless he is bribed with a gold coin. So, after releasing a prisoner in cell <strong>A</strong>, all prisoners housed on either side of cell <strong>A</strong> - until cell 1, cell <strong>P</strong> or an empty cell - need to be bribed.</p>

<p>Assume that each prison cell is initially occupied by exactly one prisoner, and that only one prisoner can be released per day. Given the list of <strong>Q</strong> prisoners to be released in <strong>Q</strong>days, find the minimum total number of gold coins needed as bribes if the prisoners may be released in any order.</p>

<p>Note that each bribe only has an effect for one day. If a prisoner who was bribed yesterday hears about another released prisoner today, then he needs to be bribed again.</p>

### 입력 

 <p>The first line of input gives the number of cases, <strong>N</strong>. <strong>N</strong> test cases follow. Each case consists of 2 lines. The first line is formatted as</p>

<pre>P Q</pre>

<p>where <strong>P</strong> is the number of prison cells and <strong>Q</strong> is the number of prisoners to be released.<br>
This will be followed by a line with <strong>Q</strong> distinct cell numbers (of the prisoners to be released), space separated, sorted in ascending order.</p>

<p> </p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>N</strong> ≤ 100</li>
	<li><strong>Q</strong> ≤ <strong>P</strong></li>
	<li>Each cell number is between 1 and <strong>P</strong>, inclusive.</li>
	<li>1 ≤ <strong>P</strong> ≤ 100</li>
	<li>1 ≤ <strong>Q</strong> ≤ 5</li>
</ul>

### 출력 

 <p>For each test case, output one line in the format</p>

<pre>Case #X: C</pre>

<p>where <strong>X</strong> is the case number, starting from 1, and <strong>C</strong> is the minimum number of gold coins needed as bribes.</p>

