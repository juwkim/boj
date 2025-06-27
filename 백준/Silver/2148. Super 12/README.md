# [Silver I] Super 12 - 2148 

[문제 링크](https://www.acmicpc.net/problem/2148) 

### 성능 요약

메모리: 112308 KB, 시간: 112 ms

### 분류

구현, 정렬

### 제출 일자

2025년 6월 27일 15:15:06

### 문제 설명

<p>In a rugby-mad country such as New Zealand, fans eagerly await the ranking of the teams in league tables such as the Super 12 (soon to be the Super 14). These rankings are really only meaningful at the end of a round, when all teams have played the same number of games.</p>

<p>A team is awarded 4 points for each win, 2 points for each draw and 0 for each loss. Any team scoring 4 or more tries in a game is awarded a bonus point, as is any team that loses a game by less than 8 points. At the end of a round we can produce a table showing the relative standings of each team, i.e. a table sorted in descending order of points. If two or more teams have the same number of points, then apply the following rules there are no tied teams:</p>

<ul>
	<li>Sort in descending order of spread, i.e. the cumulative difference between total points scored and total points against.</li>
	<li>Sort in descending order of the total number of tries they scored.</li>
	<li>Sort in ascending alphabetic sequence.</li>
</ul>

### 입력 

 <p>Input will consist of the results for a single league and will consist of the names of the competing teams and details of each game. The list of competing teams will be a series of no more than 20 lines each containing a single name(20) and terminated by a line consisting of a single ‘#’. This will be followed by a series of lines giving the results of each game, also terminated by a line consisting of a single ‘#’. Each game will start with the names of the two teams (home side first) followed by 4 integers representing, in order: the score of the home team, the score of the away team, the number of tries scored by the home team, and the number of tries scored by the away team (see the sample input). Note that there will not be any indication of the end of a round, it is determined by the number of competing teams (which will always be even), i.e. a round will end when every team has played exactly one game.</p>

### 출력 

 <p>Output will consist of a league table for each round. The first line of the league table will consist of the word ‘Round’ followed by a space and the number of the round (a running number starting at 1). This will be followed by the teams listed in order of their standing, according to the rules outlined above. Each line consists of the name of the team, followed by, starting in column 22 and right justified in fields of widths as specified in parentheses, their points (2), their cumulative score since the beginning of the league (4), the cumulative score of the teams they have played (4), the total number of tries that they have scored (3) and the total number of tries scored against them (3). Leave a blank line between rounds. See the sample output below.</p>

