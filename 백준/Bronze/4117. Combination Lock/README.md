# [Bronze II] Combination Lock - 4117 

[문제 링크](https://www.acmicpc.net/problem/4117) 

### 성능 요약

메모리: 30840 KB, 시간: 88 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p><img alt="" src="" style="float:right; height:226px; width:324px">A combination lock consists of a circular dial, which can be turned (clockwise or counterclockwise) and is embedded into the "fixed" part of the lock. The dial has N evenly spaced "ticks". The ticks are numbered from 0 to N-1, increasing in the clockwise direction. The fixed part of the lock has a "mark" which always "points to" a particular tick on the dial. Of course, the mark points to different ticks as the dial is turned.</p>

<p>The lock comes with three code numbers T1, T2, T3. These are non-negative integers and each of them is less than N. No two of the three are the same.</p>

<p>The lock is opened in three stages of operations:</p>

<ol>
	<li>Turn the dial clockwise exactly two full revolutions, and continue to turn it clockwise until the mark points to tick T1.</li>
	<li>Turn the dial one full revolution counterclockwise and continue to turn it counterclockwise until the mark points to tick T2.</li>
	<li>Turn the dial clockwise until the mark points to tick T3. The lock should now open.</li>
</ol>

<p>You must find the maximum possible number of ticks the dial must be turned in order to open the lock. The number of ticks turned is defined to be the sum of the ticks turned in the three stages outlined above, and is always positive regardless of direction. </p>

### 입력 

 <p>The input file consists of a number of test cases, one test case per line. Each line of the input file contains four integers: N, T1, T2, T3, in this order, separated by blank spaces. The integer N is a multiple of 5, 25 <= N <= 100. The numbers T1, T2 and T3 satisfy the constraints stated under the description above. The input will be terminated by a line with four blank-separated 0’s. </p>

### 출력 

 <p>For each test case, print the maximum possible number of ticks the dial must be turned in order to open the lock. Print each on its own line. There should be no blank lines between outputs. </p>

