# [Bronze II] Law 11 - 15129 

[문제 링크](https://www.acmicpc.net/problem/15129) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>Of the seventeen enumerated laws of Soccer, Offside as described by Law 11 is perhaps the most contentious. In short, offside consists of two conditions: the offside position, and a state of play that turns the offside position into an offense. In an attempt to consistently enforce offside offenses (and generally ratchet down the poor sportsmanship of parents who consider themselves smarter than the referees, but too selfish to serve as referees themselves), your team has been contacted to implement the analysis algorithm for Offside Enforcement Technology, soon to be known as OET. This phase of OET will focus solely on the Offside Position, which may be stated as:</p>

<ul>
	<li>Any part of a player’s head, body, or feet (but not hands or arms) is in the opponents' side of the field (excluding the halfway line), AND</li>
	<li>Any part of a player’s head, body, or feet (but not hands or arms) is closer to the opponents' goal line than BOTH the ball AND all but 1 opponent</li>
</ul>

<p>For the purposes of OET, consider each player to be a single point, and determine if the offense is in an offside position. The field will be 100m × 80m, with the point (0,0) being the center of the halfway line, and the opponent’s goal line running from (50,-40) to (50,40).</p>

<p style="text-align:center"><img alt="" src="" style="height:209px; width:333px"></p>

### 입력 

 <p>Each input will consist of a single test case. Note that your program may be run multiple times on different inputs. Each test case will have exactly 23 lines of input. Each line will contain two integers, x and y (-50 ≤ x ≤ 50, -40 ≤ y ≤ 40), which indicate the position of the ball or a player on the field in meters. The first line will indicate the position of the ball, then the next 11 will be the offense and the last 11 will be the defense. No two players will be in the same position.</p>

### 출력 

 <p>Output a single integer, 1 of the play is offside, and 0 if it is not.</p>

