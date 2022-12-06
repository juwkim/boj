# [Silver V] Soccer Bets - 3982 

[문제 링크](https://www.acmicpc.net/problem/3982) 

### 성능 요약

메모리: 32412 KB, 시간: 88 ms

### 분류

구현(implementation)

### 문제 설명

<p>The teams have finished the group stage of the FIFA World Cup and the teams that are in the round of the last sixteen are known. My boss has all of the games analyzed and bet on the whole rest of the tournament – writing the outcome of each match on a single sheet of paper. It was my job to bring his bets to the next betting office and set 1 000\$. Being nervous with so much cash in my pockets I fell over (I am a bit clumsy) and the bets got shuffled. So I don’t know if a bet corresponds to the final match or the semi-final or something else.</p>

<p>I do not want to disappoint my boss, so I decided to place only one bet on the winner of the tournament. Everything I know is that in each round the teams that win (a team wins if it shoots more goals than the opposing team) are in the next round, the other teams are eliminated from the tournament. This is not true for the semi-finals where the losers also play for the third place. So we have in total 16 matches.</p>

<p>Can you please tell me which team will win the World Cup based on the bets of my boss?</p>

### 입력 

 <p>The first line of the input is the number of test cases c (1 ≤ c ≤ 100). Each test case consists of 16 lines describing the matches in random order. A match description looks as follows: t<sub>1</sub> t<sub>2</sub> g<sub>1</sub> g<sub>2</sub>. t<sub>1</sub> and t<sub>2</sub> are the names of teams (abbreviated as exactly three uppercase letters), g<sub>1</sub> and g<sub>2</sub> (0 ≤ g<sub>1</sub>, g<sub>2</sub> ≤ 10; g<sub>1</sub> ≠ g<sub>2</sub>) are the goals of the two teams.</p>

### 출력 

 <p>For each test case, print one line containing the team that will win the FIFA World Cup (based on the analysis of my boss which is always correct!).</p>

