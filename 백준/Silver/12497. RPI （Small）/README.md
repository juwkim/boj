# [Silver V] RPI (Small) - 12497 

[문제 링크](https://www.acmicpc.net/problem/12497) 

### 성능 요약

메모리: 115164 KB, 시간: 140 ms

### 분류

구현, 시뮬레이션

### 문제 설명

<p>In the United States, 350 schools compete every year for an invitation to the NCAA College Basketball Tournament. With so many schools, how do you decide who should be invited? Most teams never play each other, and some teams have a much more difficult schedule than others.</p>

<p>Here is an example schedule for 4 teams named A, B, C, D:</p>

<pre>    |ABCD
  -+----
  A| . 1 1 .
  B|0 . 00
  C|0 1 . 1
  D| . 1 0 .
</pre>

<p>Each 1 in a team's row represents a win, and each 0 represents a loss. So team C has wins against B and D, and a loss against A. Team A has wins against B and C, but has not played D.</p>

<p>The NCAA tournament committee uses a formula called the RPI (Ratings Percentage Index) to help rank teams. Traditionally, it has been defined as follows:</p>

<pre>  RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
</pre>

<p>WP, OWP, and OOWP are defined for each team as follows:</p>

<ul>
	<li>WP (Winning Percentage) is the fraction of your games that you have won.<br>
	In the example schedule, team A has WP = 1, team B has WP = 0, team C has WP = 2/3, and team D has WP = 0.5.</li>
	<li>OWP (Opponents' Winning Percentage) is the average WP of all your opponents, after first throwing out the games they played against you.<br>
	For example, if you throw out games played against team D, then team B has WP = 0 and team C has WP = 0.5. Therefore team D has OWP = 0.5 * (0 + 0.5) = 0.25. Similarly, team A has OWP = 0.5, team B has OWP = 0.5, and team C has OWP = 2/3.</li>
	<li>OOWP (Opponents' Opponents' Winning Percentage) is the average OWP of all your opponents. OWP is exactly the number computed in the previous step.<br>
	For example, team A has OOWP = 0.5 * (0.5 + 2/3) = 7/12.</li>
</ul>

<p>Putting it all together, we see team A has RPI = (0.25 * 1) + (0.5 * 0.5) + (0.25 * 7 / 12) = 0.6458333...</p>

<p>There are some pretty interesting questions you can ask about the RPI. Is it a reasonable measure of team's ability? Is it more important for teams to win games, or to schedule strong opponents? These are all good questions, but for this problem, your task is more straightforward: given a schedule of games, can you calculate every team's RPI?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case begins with a single line containing the number of teams <strong>N</strong>.</p>

<p>The next <strong>N</strong> lines each contain exactly <strong>N</strong> characters (either '0', '1', or '.') representing a schedule in the same format as the example schedule above. A '1' in row i, column j indicates team i beat team j, a '0' in row i, column j indicates team i lost to team j, and a '.' in row i, column j indicates team i never played against team j.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 20.</li>
	<li>If the schedule contains a '1' in row i, column j, then it contains a '0' in row j, column i.</li>
	<li>If the schedule contains a '0' in row i, column j, then it contains a '1' in row j, column i.</li>
	<li>If the schedule contains a '.' in row i, column j, then it contains a '.' in row j, column i.</li>
	<li>Every team plays at least two other teams.</li>
	<li>No two teams play each other twice.</li>
	<li>No team plays itself.</li>
	<li>3 ≤ <strong>N</strong> ≤ 10.</li>
</ul>

### 출력 

 <p>For each test case, output <strong>N</strong> + 1 lines. The first line should be "Case #x:" where x is the case number (starting from 1). The next <strong>N</strong> lines should contain the RPI of each team, one per line, in the same order as the schedule.</p>

<p>Answers with a relative or absolute error of at most 10<sup>-6</sup> will be considered correct.</p>

