# [Bronze I] Computer Purchase - 6799 

[문제 링크](https://www.acmicpc.net/problem/6799) 

### 성능 요약

메모리: 32884 KB, 시간: 560 ms

### 분류

구현(implementation), 정렬(sorting), 문자열(string)

### 문제 설명

<p>In order to increase your performance on the ABC (Another Buying Contest), you decide that you need a new computer. When determining which computer to buy, you narrow your search categories to:</p>

<ul>
	<li>RAM (in gigabytes), denoted as R;</li>
	<li>CPU speed (in megahertz), denoted as S;</li>
	<li>disk drive space (in gigabytes), denoted as D.</li>
</ul>

<p>You perform some analysis and determine that the most preferred machine is the machine that has the largest value of the formula</p>

<p style="text-align: center;">2 × R + 3 × S + D.</p>

<p>Your task is to read a given list of computers and output the top two computers in order of preference, from highest preference to lowest preference.</p>

### 입력 

 <p>The first line of input will be an integer n (0 ≤ n ≤ 10000). Each of the remaining n lines of input will contain a computer specification. A computer specification is of the form:</p>

<ul>
	<li>computer name (a string of less than 20 characters)</li>
	<li>the RAM available (an integer R with 1 ≤ R ≤ 128)</li>
	<li>the CPU speed (an integer S with 1 ≤ S ≤ 4000)</li>
	<li>the disk drive space (an integer D with 1 ≤ D ≤ 3000)</li>
</ul>

<p>There is one space between the name, RAM, CPU speed and disk drive space on each line.</p>

### 출력 

 <p>The output is the name of the top two preferred computers, one name per line, sorted in decreasing order of preference. If there is a tie in the rankings, pick the computer(s) whose name(s) are lexicographically smallest (i.e., “Apple” is smaller than “Dell”). If there is only one computer, output that computer on one line (i.e., do not print it twice).</p>

