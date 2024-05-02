# [Silver III] ACM Rank Table - 7846 

[문제 링크](https://www.acmicpc.net/problem/7846) 

### 성능 요약

메모리: 114492 KB, 시간: 160 ms

### 분류

정렬

### 제출 일자

2024년 5월 3일 02:26:37

### 문제 설명

<p>ACM contests, like the one you are participating in, are hosted by the special software. That software, among other functions, preforms a job of accepting and evaluating teams' solutions (runs), and displaying results in a rank table. The scoring rules are as follows:</p>

<ol>
	<li>Each run is either accepted or rejected.</li>
	<li>The problem is considered solved by the team, if one of the runs submitted for it is accepted.</li>
	<li>The time consumed for a solved problem is the time elapsed from the beginning of the contest to the submission of the first accepted run for this problem (in minutes) plus 20 minutes for every other run for this problem before the accepted one. For an unsolved problem consumed time is not computed.</li>
	<li>The total time is the sum of the time consumed for each problem solved.</li>
	<li>Teams are ranked according to the number of solved problems. Teams that solve the same number of problems are ranked by the least total time.</li>
	<li>While the time shown is in minutes, the actual time is measured to the precision of 1 second, and the the seconds are taken into account when ranking teams.</li>
	<li>Teams with equal rank according to the above rules must be sorted by increasing team number.</li>
</ol>

<p> </p>

<p>Your task is, given the list of <i>N</i> runs with submission time and result of each run, compute the rank table for <i>C</i> teams.</p>

### 입력 

 <p>Input contains integer numbers <i>C</i> <i>N</i>, followed by <i>N</i> quartets of integes <i>c<sub>i</sub></i> <i>p<sub>i</sub></i> <i>t<sub>i</sub></i> <i>r<sub>i</sub></i>, where <i>c<sub>i</sub></i> -- team number, <i>p<sub>i</sub></i> -- problem number, <i>t<sub>i</sub></i> -- submission time <i>in seconds</i>, <i>r<sub>i</sub></i> -- 1, if the run was accepted, 0 otherwise.</p>

### 출력 

 <p>Output file must contain <i>C</i> integers -- team numbers sorted by rank.</p>

