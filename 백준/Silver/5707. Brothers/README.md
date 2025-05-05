# [Silver I] Brothers - 5707 

[문제 링크](https://www.acmicpc.net/problem/5707) 

### 성능 요약

메모리: 131412 KB, 시간: 976 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 5월 5일 21:49:54

### 문제 설명

<p>In the land of ACM ruled a great King who became obsessed with order. The kingdom had a rectangular form, and the King divided the territory into a grid of small rectangular counties. Before dying, the King distributed the counties among his sons.</p>

<p>However, he was unaware that his children had developed a strange rivalry: the first heir hated the second heir, but not the rest; the second heir hated the third heir, but not the rest, and so on . . . Finally, the last heir hated the first heir, but not the other heirs.</p>

<p>As soon as the King died, the strange rivalry among the King’s sons sparked off a generalized war in the kingdom. Attacks only took place between pairs of adjacent counties (adjacent counties are those that share one vertical or horizontal border). A county X attacked an adjacent county Y whenever the owner of X hated the owner of Y . The attacked county was always conquered by the attacking brother. By a rule of honor all the attacks were carried out simultaneously, and a set of simultaneous attacks was called a battle. After a certain number of battles, the surviving sons made a truce and never battled again.</p>

<p>For example, if the King had three sons, named 0, 1 and 2, the figure below shows what happens in the first battle for a given initial land distribution:</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images2/bro.png" style="height:162px; width:423px"></p>

<p>You were hired to help an ACM historian determining, given the number of heirs, the initial land distribution and the number of battles, what was the land distribution after all battles.</p>

### 입력 

 <p>The input contains several test cases. The first line of a test case contains four integers N, R, C and K, separated by single spaces. N is the number of heirs (2 ≤ N ≤ 100), R and C are the dimensions of the kingdom (2 ≤ R, C ≤ 100), and K is the number of battles (1 ≤ K ≤ 100). Heirs are identified by sequential integers starting from zero (0 is the first heir, 1 is the second heir, . . ., N − 1 is the last heir). Each of the next R lines contains C integers Hr,c separated by single spaces, representing initial land distribution: H<sub>r,c</sub> is the initial owner of the county in row r and column c (0 ≤ H<sub>r,c</sub> ≤ N − 1).</p>

<p>The last test case is followed by a line containing four zeroes separated by single spaces.</p>

### 출력 

 <p>For each test case, your program must print R lines with C integers each, separated by single spaces in the same format as the input, representing the land distribution after all battles.</p>

