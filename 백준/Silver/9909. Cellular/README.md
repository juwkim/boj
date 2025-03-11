# [Silver II] Cellular - 9909 

[문제 링크](https://www.acmicpc.net/problem/9909) 

### 성능 요약

메모리: 112016 KB, 시간: 172 ms

### 분류

비트마스킹, 브루트포스 알고리즘, 구현, 시뮬레이션

### 제출 일자

2025년 3월 12일 02:44:17

### 문제 설명

<p>A square field is divided up into n × n cells.  Each cell can only take one of two states: 0 or 1.  At regular intervals, called generations, all cells update their state simultaneously, depending on the state that they and their neighbors had in the previous generation.</p>

<p>An interior cell has four neighbors, namely the cells above it and below it, and the cells to its right and to its left.  Corner cells have only two neighbors.  Other cells at the edge of the field have three neighbors.</p>

<p>One possible rule to update a cell is to look at the sum of the states that it and its neighbors had in the previous generation.  This sum has a value in the range 0 through 5.  In this case, the update rule for the cells can be encoded in 6 bits.  For example, an update rule 0 0 1 0 0 1 means that the new state of each cell is</p>

<ul>
	<li>0 if the sum was 5,</li>
	<li>0 if the sum was 4,</li>
	<li>1 if the sum was 3,</li>
	<li>0 if the sum was 2,</li>
	<li>0 if the sum was 1, and</li>
	<li>1 if the sum was 0,</li>
</ul>

<p>where “the sum” means the sum of the old states of the cell and of all its neighbors.  We can use binary code to uniquely identify the rule.  A 6-bit binary number a b c d e f corresponds to the decimal value (a × 32) + (b × 16) + (c × 8) + (d × 4) + (e × 2) + f.  The above rule would have the binary number 001001, which corresponds to the decimal value 9.</p>

<p>For example, if n is 4 we could have the starting state</p>

<pre>1111
1111
1111
1111</pre>

<p>With rule 9, we get after 1 generation the states</p>

<pre>1001
0000
0000
1001</pre>

<p>and after 2 generations</p>

<pre>0000
0110
0110
0000
</pre>

<p>Given a size n, a number of generations g, a starting state s and an ending state e, the goal is to find the rule with smallest decimal value that generates the ending state e from a starting state s after exactly g generations.  The output required is the decimal value of the rule.  If there is no such rule, the output should be –1.</p>

<p>You can assume that n is not bigger than 30 and g is not bigger than 50.</p>

### 입력 

 <p>The input consists of the following lines:</p>

<ol>
	<li>The first line contains two positive integers indicating the size n and number of generations g.</li>
	<li>Each of the next n lines contains n digits which are 0 or 1.  These n lines indicate the starting state s.</li>
	<li>The next line is empty.</li>
	<li>Each of the following n lines contains n digits which are 0 or 1.  These n lines indicate the ending state e.</li>
</ol>

### 출력 

 <p>The output contains a single integer value, which is the smallest decimal value of a rule that generates e from s after exactly g generations.</p>

