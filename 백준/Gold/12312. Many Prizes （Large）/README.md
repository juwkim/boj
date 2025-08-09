# [Gold III] Many Prizes (Large) - 12312 

[문제 링크](https://www.acmicpc.net/problem/12312) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

그리디 알고리즘, 재귀

### 제출 일자

2025년 8월 10일 02:13:20

### 문제 설명

<p>We're going to run a tournament with 2N teams, and give out P identical prizes to the teams with ranks 0..P-1.</p>

<p>The teams are numbered 0 through 2N-1. When team i and team j play against each other in a game, team i will win iff i<j.</p>

<p>The teams for a tournament are organized in some order, called the tournament's tournament list, which contains all 2N teams in the tournament. The tournament list will affect which teams play each other, and in what order.</p>

<p>Your job will be to find the largest-numbered team that is guaranteed to win a prize, independent of how the tournament list is ordered; and to find the largest-numbered team that could win a prize, depending on how the tournament list is ordered.</p>

<p>Tournament Resolution</p>

<p>The tournament is conducted in N rounds.</p>

<p>Each team has a record: the list of the results of the games it has played so far. For example, if a team has played three games, and won the first, lost the second and won the third, its record is [W, L, W]. If a team has played zero games, its record is [].</p>

<p>In each round, every team plays a game against a team with the same record. The first team in the tournament list with a particular record will play against the second team with that record; the third team with the same record will play against the fourth; and so on.</p>

<p>After N rounds, each team has a different record. The teams are ranked in reverse lexicographical order of their records; so [W, W, W] > [W, W, L] > [W, L, W] ... > [L, L, L].</p>

<p>Here is an example of a tournament with N=3, and the tournament list [2, 4, 5, 3, 6, 7, 1, 0], where the columns represent different rounds, and the teams are grouped by their records. The winner of each game in the example has been marked with a *.</p>

<p>Round 1    Round 2    Round 3    Final Result<br>
                                               (best rank at top)<br>
[]              [W]           [W,W]<br>
2  *           2  *            2              0  [W,W,W]<br>
4              3               0  *           2  [W,W,L]<br>
                                 [W,L]<br>
5              6               3  *           3  [W,L,W]<br>
3  *          0  *            6              6  [W,L,L]<br>
               [L]             [L,W]<br>
6  *          4  *            4              1  [L,W,W]<br>
7              5                1  *          4  [L,W,L]<br>
                                 [L,L]<br>
1              7                5  *          5  [L,L,W]<br>
0  *          1  *             7             7  [L,L,L]<br>
If we give out 4 prizes (N=3, P=4), the prizes will go to teams 0, 2, 3 and 6.</p>

<p>The largest-numbered team that was guaranteed to win a prize with N=3, P=4, independent of the order of the tournament list, was team 0: this tournament list demonstrated that it's possible for team 1 not to win a prize, and it turns out that team 0 will always win one, regardless of the order of the tournament list.</p>

<p>The largest-numbered team that could win a prize with N=3, P=4, depending on how the tournament list was ordered, was team 6: this tournament list demonstrated that it's possible for team 6 to win a prize, and it turns out that team 7 will never win one, regardless of the order of the tournament list.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case consists of two space-separated integers: <strong>N</strong>, which indicates the tournament has 2<strong><sup>N</sup></strong> teams, and <strong>P</strong>, the number of prizes.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>P</strong> ≤ 2<strong><sup>N</sup></strong>.</li>
	<li>1 ≤ <strong>N</strong> ≤ 50.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y z", where x is the case number (starting from 1), y is the largest-numbered team that is <em>guaranteed</em> to win a prize, independent of how the tournament list is ordered; and z is the largest-numbered team that <em>could</em> win a prize, depending on how the tournament list is ordered.</p>

