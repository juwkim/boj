# [Silver V] Work Reduction - 4313 

[문제 링크](https://www.acmicpc.net/problem/4313) 

### 성능 요약

메모리: 116392 KB, 시간: 296 ms

### 분류

정렬

### 문제 설명

<p>Paperwork is beginning to pile up on your desk, and tensions at the workplace are starting to mount. Your boss has threatened to fire you if you don't make any progress by the end of the day. You currently have N units of paperwork on your desk, and your boss demands that you have exactly M units of paperwork left by the end of the day.</p>

<p>The only hope for you now is to hire help. There are various agencies which offer paperwork reduction plans:</p>

<ul>
	<li>For <span>$</span>A they will reduce your paperwork by one unit.</li>
	<li>For <span>$</span>B they will reduce your entire paperwork by half (rounding down when necessary).</li>
</ul>

<p>Note that work can never be reduced to less than 0.</p>

<p>Your task now is to produce a sorted table of agency names and their respective minimum costs to solve your workload problem.</p>

### 입력 

 <p>The first line of input consists of a single positive integer representing the number of cases to follow. Each case begins with three positive integers separated by spaces: N - your starting workload, M - your target workload, and L - the number of work reduction agencies available to you, (1 <= M <= N <= 100000, 1 <= L <= 100). The next L lines have the format "[agency name]:A,B", where A and B are the rates as described above for the given agency. (0 <= A,B <= 10000) The length of the agency name will be between 1 and 16, and will consist only of capital letters. Agency names will be unique.</p>

### 출력 

 <p>For each test case, print "Case X", with X being the case number, on a single line, followed by the table of agency names and their respective minimum costs, sorted in non-decreasing order of minimum costs. Sort job agencies with identical minimum costs in alphabetical order by agency name. For each line of the table, print out the agency name, followed by a space, followed by the minimum required cost for that agency to solve your problem.</p>

