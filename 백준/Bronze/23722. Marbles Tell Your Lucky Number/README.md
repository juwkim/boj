# [Bronze I] Marbles Tell Your Lucky Number - 23722 

[문제 링크](https://www.acmicpc.net/problem/23722) 

### 성능 요약

메모리: 30840 KB, 시간: 80 ms

### 분류

구현(implementation), 수학(math), 정수론(number_theory), 시뮬레이션(simulation)

### 문제 설명

<p style="text-align: center;"><img alt="" src="" style="width: 748px; height: 220px;"></p>

<p>You can find your lucky number of the day in the following way.</p>

<p>Prepare four bowls and plenty of marbles. Line up the bowls from left to right, and, after deep meditation, put some arbitrary numbers of marbles in the bowls. Numbers of marbles in the bowls may vary; some bowls may be empty, but at least one of them should be non-empty.</p>

<p>Among non-empty bowls, choose one with the least number of marbles in it. If more than one bowl has the least number of marbles, choose the leftmost. From all the other non-empty bowls, remove the same number of marbles as in the chosen bowl. The marbles in the chosen bowl are left there.</p>

<p>This procedure should be repeated until only one non-empty bowl remains. The number of marbles in the non-empty bowl is your lucky number today.</p>

<p><img alt="" src="" style="width: 400px; height: 308px; float: right;">The figure to the right shows an example corresponding to the first dataset of the Sample Input.</p>

<ol>
	<li>The bowl second from the right contains the least number of marbles, four.</li>
	<li>Four marbles each have been taken out from other bowls. Now the rightmost bowl has two marbles, which are the least.</li>
	<li>Two marbles each have been taken out from other bowls. Three bowls except the leftmost have two marbles, which are the least. The leftmost bowl of the three, that is, the second from the left, is chosen.</li>
	<li>Two marbles each have been taken out from other bowls. Now only two bowls have marbles in them and both have two marbles. Thus, the leftmost bowl is chosen.</li>
	<li>Two marbles from the second bowl have been taken out, leaving only one bowl non-empty, which is the leftmost bowl with two marbles. Yes, your lucky number of the day is <em>two!</em></li>
</ol>

### 입력 

 <p>The input consists of multiple datasets, each in the following format.</p>

<pre><var>a</var><sub>1</sub> <var>a</var><sub>2</sub> <var>a</var><sub>3</sub> <var>a</var><sub>4</sub></pre>

<p>Each of the datasets consists of one line containing four integers, <var>a</var><sub>1</sub> through <var>a</var><sub>4</sub>. These four integers are the numbers of marbles initially in the four bowls. All of these four integers are between 0 and 100, inclusive, and at least one of them is non-zero.</p>

<p>The end of the input is indicated by a line containing four zeros.</p>

<p>The number of datasets does not exceed 100.</p>

### 출력 

 <p>For each of the datasets, output the lucky number decided by the procedure described above in a line.</p>

