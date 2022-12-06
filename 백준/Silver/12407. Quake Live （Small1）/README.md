# [Silver IV] Quake Live (Small1) - 12407 

[문제 링크](https://www.acmicpc.net/problem/12407) 

### 성능 요약

메모리: 115268 KB, 시간: 148 ms

### 분류

Empty

### 문제 설명

<p>Quake Live is a first-person shooter game that supports several types of matches. One of the most popular types is the 4-on-4 team deathmatch. Eight players enter. They are split into two teams of 4. The teams fight to the death. The team whose players all die first loses.</p>

<p>The Quake Live servers maintain a history of matches for each player, which is used to estimate each player's <em>skill level</em> -- an integer between 1 and 1000. To keep the game as fair as possible, whenever 8 players connect to the server, the server assigns players to teams to keep the skill balance as fair as possible. To do this, the server looks at the skill levels of the 8 players and finds a way to split the players into two teams of 4 in a way that minimizes the difference between the sum of skills on team A and the sum of skills on team B.</p>

<p>You think that something is fishy in this logic and would like to verify that the server is doing its job correctly. Given the skill levels of the players who enter, can you find the smallest possible difference between the total team skills? Note that the two teams must always have the same number of players.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> lines follow. Each line starts with the integer <strong>N</strong> -- the number of players who enter. The next <strong>N</strong> integers on the line are the skill levels of the players in no particular order.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li><strong>N</strong> = 8.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>X</strong>: <strong>Y</strong>", where <strong>X</strong> is the case number (starting from 1) and <strong>Y</strong> is the smallest possible difference between the sum of skill levels of the players on team A and the sum of skill levels of the players on team B.</p>

