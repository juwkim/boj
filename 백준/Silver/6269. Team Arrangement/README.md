# [Silver III] Team Arrangement - 6269 

[문제 링크](https://www.acmicpc.net/problem/6269) 

### 성능 요약

메모리: 112008 KB, 시간: 136 ms

### 분류

구현, 정렬

### 제출 일자

2024년 6월 13일 13:52:42

### 문제 설명

<p>Barry Bennett, the coach of the Bings football team, wants to arrange his team for an important match against the Bangs. He decides on the formation he wants to play, for example 4-4-2, meaning that there will be four defenders, four midfielders, and two strikers (and of course, one goalkeeper). Your task is to determine the players who will play. For each available player, we know his role (e.g. midfielder). For each role, the players are selected in ascending order of their numbers. When the players are selected, you must determine the captain too, who is the player with the longest record in the team play. In case two players have the same record, the one with bigger number is chosen. Note that the captain is chosen among the players that are selected in the arrange.</p>

<p> </p>

### 입력 

 <p>The input consists of multiple test cases. The first 22 lines of each test case contain the data for the 22 available players in this format:</p>

<p><br>
number name role year<sub>1</sub> - year'<sub>1</sub> year<sub>2</sub> - year'<sub>2</sub> ...</p>

<p><br>
number is the player number (unique positive integer less than 100). name is a string of at most 20 letters. role is a single character among G, D, M, S, for goalkeeper, defender, midfielder, and striker respectively. Each year<sub>i</sub> - year'<sub>i</sub> pair (year<sub>i</sub> ≤ year'<sub>i</sub>) shows the player has been a member of the team between the specified years (inclusive). The years are in four-digit format. There is at least one and at most 20 such pairs, and the same year is not repeated more than once in the list. There is a 23-rd line describing the desired formation, like 4-4-2 in that format. Note that there are only three numbers in the formation (so, 4-3-2-1 is not valid), none of them is zero, and their sum is always 10. The input is terminated by a line containing a single `0'.</p>

### 출력 

 <p>For each test case, output a list of 11 players chosen in the arrange. Each line must contain the player number, his name and his role, separated by single blank characters. The players must be sorted according to their role, in the order of goalkeeper, defenders, midfielders, and strikers. The players with the same role are sorted according to ascending order of their numbers. There is an exception that the captain always comes as the first player in the entire list. If it is not possible to arrange the team conforming to the desired formation, write a single line containing `IMPOSSIBLE TO ARRANGE' in the output. There should be a blank line after the output for each test case.</p>

<p> </p>

