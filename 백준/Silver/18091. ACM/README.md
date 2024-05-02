# [Silver III] ACM - 18091 

[문제 링크](https://www.acmicpc.net/problem/18091) 

### 성능 요약

메모리: 110592 KB, 시간: 132 ms

### 분류

파싱, 문자열

### 제출 일자

2024년 5월 2일 19:05:29

### 문제 설명

<p>An ancient programming competition is getting near and it is organized by none other than ACM (<em>Aeronautic Centre of Metković</em>). Exactly N teams will compete for the grand prize and among them is a golden Croatian trio: Paula, Marin and Josip. The contest format is standard, while the pilot is performing aerobatic maneuvers, the co-pilot reads the problem statements and attempts to transmit the solutions to the <s>code monkey</s> main programmer who is securely taped to the aircraft’s exterior.</p>

<p>The contest consists of M different tasks and the teams are (non-increasingly) ordered by the number of solved tasks.</p>

<p>The teams that have the same number of solved tasks are ordered (non-decreasingly) by so-called penalty time. Penalty time of a certain team is the sum of penalty time they achieved on each of their correctly solved tasks. Penalty time of a correctly solved task equals to the time it took for the team to solve that task (from the beginning of the contest) increased by additional <strong>20 minutes</strong> for each of the wrongly submitted solutions for that task. No teams will attempt to submit a solution for a problem that they have already solved and the maximum number of submissions for a certain task is <strong>9 for each team</strong>. If some teams have the same number of solved problems and the same penalty time, they will be ordered alphabetically in the final standings.</p>

<p>The competition lasts for <strong>five hours</strong>. During the first four hours the standings are available to all teams and contain information about the status of each task for each team (number of submissions, whether it was solved and when). During those four hours, the order of the teams will be automatically updated after each submission. In the last hour though, the standings become frozen, i.e., the order of the teams is not updated after a new submission is judged. During that time, each team knows the judgement of their own submissions, but they don’t know the judgement of submissions made by other teams. They only know which tasks were submitted by other teams, how many times were they submitted and when was the last submission for each task.</p>

<p>The contest is over and the standings should be unfrozen soon. Our heroes, team named <code>NijeZivotJedanACM</code> need your help. They want to know what is the worst possible position on the scoreboard they could end up in after the standings become unfrozen. Help them!</p>

### 입력 

 <p>The first line contains integers N (1 ≤ N ≤ 1000) and M (1 ≤ M ≤ 15) from the task description.</p>

<p>The next N lines represent the frozen standings. Each line begins by a team name (string made up of lowercase and uppercase English letters which consists of at most 20 characters, names of all teams will be different) which is separated by a space from M (also space-separated) strings that hold the information about the status of each task for that team.</p>

<p>Those strings are of the form <code>SX/V</code>, where:</p>

<ul>
	<li><code>S</code> represents the status of the task – ‘<code>+</code>’ means the task is solved correctly, ‘<code>-</code>’ means it is solved incorrectly and ‘<code>?</code>’ means that the last submission was sent when the standings were already frozen.</li>
	<li><code>X</code> represents the number of submissions that were sent by that team for this specific task. It is omitted if no submissions were made for that task.</li>
	<li><code>V</code> represents the time when the last submission was sent by that team for this specific task. It is given in the format <code>HH:MM:SS</code> (with leading zeroes) and is less than 5 hours. The whole <code>/V</code> part is omitted if the task is not solved correctly (status ’<code>-</code>’)</li>
</ul>

<p>The last line contains the unfrozen standings of our heroes, team named <code>NijeZivotJedanACM</code>.</p>

### 출력 

 <p>In the first and only line you should output the worst possible position in the standings where our heroes might end up in after the standings become unfrozen.</p>

