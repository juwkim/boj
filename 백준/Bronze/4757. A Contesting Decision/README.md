# [Bronze II] A Contesting Decision - 4757 

[문제 링크](https://www.acmicpc.net/problem/4757) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p>Judging a programming contest is hard work, with demanding contestants, tedious decisions, and monotonous work. Not to mention the nutritional problems of spending 12 hours with only donuts, pizza, and soda for food. Still, it can be a lot of fun.</p>

<p>Software that automates the judging process is a great help, but the notorious unreliability of some contest software makes people wish that something better were available. You are part of a group trying to develop better, open source, contest management software, based on the principle of modular design.</p>

<p>Your component is to be used for calculating the scores of programming contest teams and determining a winner. You will be given the results from several teams and must determine the winner.</p>

<p>Scoring</p>

<p>There are two components to a team’s score. The first is the number of problems solved. The second is penalty points, which reflects the amount of time and incorrect submissions made before the problem is solved. For each problem solved correctly, penalty points are charged equal to the time at which the problem was solved plus 20 minutes for each incorrect submission. No penalty points are added for problems that are never solved.</p>

<p>So if a team solved problem one on their second submission at twenty minutes, they are charged 40 penalty points. If they submit problem 2 three times, but do not solve it, they are charged no penalty points. If they submit problem 3 once and solve it at 120 minutes, they are charged 120 penalty points. Their total score is two problems solved with 160 penalty points.</p>

<p>The winner is the team that solves the most problems. If teams tie for solving the most problems, then the winner is the team with the fewest penalty points.</p>

### 입력 

 <p>For the programming contest your program is judging, there are four problems. You are guaranteed that the input will not result in a tie between teams after counting penalty points.</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td>Line 1</td>
			<td><nTeams></td>
		</tr>
		<tr>
			<td>Line 2–n+1</td>
			<td>
			<p><Name><p1Sub><p1Time><p2Sub><p2Time>...<p4Time></p>

			<p>The first element on the line is the team name, which contains no whitespace. Following that, for each of the four problems, is the number of times the team submitted a run for that problem and the time at which it was solved correctly (both integers). If a team did not solve a problem, the time will be zero. The number of submissions will be at least one if the problem was solved.</p>

			<p> </p>
			</td>
		</tr>
	</tbody>
</table>

<p> </p>

### 출력 

 <p>The output consists of a single line listing the name of the team that won, the number of problems they solved, and their penalty points.</p>

