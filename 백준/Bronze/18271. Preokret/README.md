# [Bronze I] Preokret - 18271 

[문제 링크](https://www.acmicpc.net/problem/18271) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>It’s <em>Saint Stephen’s Day</em>, the day after Christmas. The secular version of the same holiday in England is known as <em>Boxing day</em>. While people in Croatia celebrate Saint Stephen’s Day by stuffing themselves with ridiculous amounts of food, our British friends traditionally play football. Premier league, Championship, amateur leagues – everybody plays football on Boxing day.</p>

<p>This year, Pep ate too much roast beef on Christmas and decided to take a break from Boxing day football. He stayed in bed that day, analyzing an old City fixture against an unknown opponent.</p>

<p>Pep knows that there were N goals scored during the match and he also knows in which order were they scored. He watches the game and wishes to answer the following questions</p>

<ol>
	<li>What was the final score, i.e., how many goals did City score and how many goals did their opponents score?</li>
	<li>How many different ties were featured during the course of the game? We say that the game is tied if both teams have scored the same number of goals. The starting score 0:0 is also considered a tie.</li>
	<li>Let’s define a <em>turnover</em> as a situation in which a losing team, i.e. the team that scored less goals than its opponent, scores a certain number of successive goals and takes the lead after those goals have been scored. Pep wonders what is the largest turnover in the game. In other words, he wants to know what was the largest number of successive goals scored by one team such that before those goals they were losing and after those goals they were winning. Pep knows that this specific game had at least one turnover.</li>
</ol>

### 입력 

 <p>First line contains an integer N (1 ≤ N ≤ 250) from the task description.</p>

<p>In the next N lines there is a single number 1 or 2 which represents a team that scored a goal (in order of goals scored in the game). City is denoted by number 1 and their opponents by number 2.</p>

### 출력 

 <p>In the first line you should output two space-separated integers, the number of goals scored by City and the number of goals scored by the opposing team.</p>

<p>In the second line you should output the number of different ties featured during the course of the game.</p>

<p>In the third line you should output the largest turnover in the game.</p>

