# [Silver V] Soccer Standings - 26315 

[문제 링크](https://www.acmicpc.net/problem/26315) 

### 성능 요약

메모리: 114328 KB, 시간: 124 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>In a soccer match, a team either earns a win, tie or loss. A win is worth 3 points, a tie is worth 1 point, and a loss is worth 0 points. Unfortunately, due to poor record-keeping, some leagues have only saved the number of total matches played and the number of points each team has earned. One of these leagues has asked you to write a program to recreate the possible combinations of wins, ties and losses for certain teams in the league.</p>

<p>Given the number of games played by a soccer team in a season and the number of points earned by the team, list each possible combination of wins, ties and losses that the team could have gotten to achieve the given total points.</p>

### 입력 

 <p>The first input line contains a positive integer, n, indicating the number of teams for which you are to reconstruct possible records. The teams’ information are on the following n input lines, one team per line. Each of these lines contains two space separated integers: g (0 < g ≤ 100), and p (0 ≤ p ≤ 300), representing the number of games played and the total points earned by the team, respectively. It is guaranteed that there is at least one possible combination of wins, ties and losses that is consistent with the given information for each team.</p>

### 출력 

 <p>For each team, first output header info with the following format:</p>

<pre>Team #k
Games: g
Points: p
Possible records:</pre>

<p>where k is the team number (starting with 1), g is the number of games, and p is the total points earned. Following the above header info, output the possible records, each on a separate line with the format:</p>

<p>w-t-l</p>

<p>where w is the number of wins, t is the number of ties and l is the number of losses. Print these by descending order of wins.</p>

<p>Leave a blank line after the output for each team. Follow the format illustrated in Sample Output.</p>

