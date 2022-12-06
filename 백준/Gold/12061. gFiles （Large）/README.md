# [Gold V] gFiles (Large) - 12061 

[문제 링크](https://www.acmicpc.net/problem/12061) 

### 성능 요약

메모리: 115464 KB, 시간: 156 ms

### 분류

이분 탐색(binary_search), 많은 조건 분기(case_work), 수학(math), 매개 변수 탐색(parametric_search)

### 문제 설명

<p>Alien tech company G has a very old file transfer tool that is still in use today. While the tool is running, it reassures users by giving status updates on both the percentage of files transferred so far and the number of files transferred so far. The status updates during the process might look like this:</p>

<pre> 20% |==>-------|     1 files transferred
100% |==========|     5 files transferred
</pre>

<p>But the percentage isn't precise; it is simply truncated before the decimal point (i.e. floored to the next lowest or equal 1%). That is, both 1.2% and 1.7% would be displayed as 1%.</p>

<p>Some users may want to know the exact total number of files, so you want to modify the tool so that the status updates look like this:</p>

<pre> 20% |==>-------|     1 out of <strong>5</strong> files transferred
100% |==========|     5 out of <strong>5</strong> files transferred
</pre>

<p>But you've realized that it may or may not be possible to know the number of files. Given the status updates that the tool displays, either figure out how many files there are, or determine that it can't be done (i.e., there are multiple possible values for the number of files). The status updates are not guaranteed to occur at regular intervals and are not guaranteed to occur whenever a file is transferred.</p>

### 입력 

 <p>The first line contains <strong>T</strong>, the number of test cases. <strong>T</strong> test cases follow. Each test case consists of one line with an integer <strong>N</strong>, the number of status updates output by the tool, followed by <strong>N</strong> lines with the format P<sub>i</sub> K<sub>i</sub>, where P<sub>i</sub> and K<sub>i</sub> are integers representing the percentage and number of files transferred at some point in the process. The updates are given listed in chronological order -- that is, both the P<sub>i</sub> values and the K<sub>i</sub> values are nondecreasing throughout a test case.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 50.</li>
	<li>1 ≤ <strong>N</strong> ≤ 100.</li>
	<li>0 ≤ P<sub>i</sub> ≤ 100</li>
	<li>0 ≤ K<sub>i</sub> ≤ 10<sup>15</sup></li>
	<li>The answer is guaranteed not to exceed 10<sup>15</sup>.</li>
</ul>

### 출력 

 <p>For each case, output a line starts with "Case #x: y", where x is the number of the case (starting from 1), and y is either the total number of files, or <code>-1</code> if that number is ambiguous.</p>

