# [Silver V] Election - 14762 

[문제 링크](https://www.acmicpc.net/problem/14762) 

### 성능 요약

메모리: 114328 KB, 시간: 128 ms

### 분류

조합론(combinatorics), 수학(math)

### 문제 설명

<p>After all the fundraising, campaigning and debating, the election day has finally arrived. Only two candidates remain on the ballot and you work as an aide to one of them.</p>

<p>Reports from the voting stations are starting to trickle in and you hope that you can soon declare a victory.</p>

<p>There are N voters and everyone votes for one of the two candidates (there are no spoiled ballots). In order to win, a candidate needs more than half of the votes. A certain number M ≤ N of ballots have been counted, and there are V<sub>i</sub> votes for candidate i (V<sub>1</sub>+V<sub>2</sub> = M), where V<sub>1</sub> is the number of votes your candidate received.</p>

<p>Due to the historical data and results of highly scientific polls, you know that each of the remaining votes has a 50% chance to go to your candidate. That makes you think that you could announce the win before all the votes are counted. So, if the probability of winning strictly exceeds a certain threshold W, the victory is yours! We just hope you are sure of this, we don’t want any scandals...</p>

### 입력 

 <p>The first line of input contains a single positive integer T ≤ 100 indicating the number of test cases. Next T lines each contain four integers: N, V<sub>1</sub>, V<sub>2</sub> and W as described above.</p>

<p>The input limits are as follows:</p>

<ul>
	<li>1 ≤ N ≤ 50</li>
	<li>50 ≤ W < 100</li>
	<li>V<sub>1</sub>, V<sub>2</sub> ≥ 0</li>
	<li>V<sub>1</sub> + V<sub>2</sub> ≤ N</li>
</ul>

### 출력 

 <p>For each test case print a single line containing the appropriate action:</p>

<ul>
	<li>If the probability that your candidate will win is strictly greater than W%, print <code>GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!</code></li>
	<li>If your candidate has no chance of winning, print <code>RECOUNT!</code></li>
	<li>Otherwise, print <code>PATIENCE, EVERYONE!</code></li>
</ul>

