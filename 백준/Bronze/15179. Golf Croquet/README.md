# [Bronze III] Golf Croquet - 15179 

[문제 링크](https://www.acmicpc.net/problem/15179) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>In golf croquet doubles, two teams of 2 play each other. Each player has their own ball which they hit when it is their turn. A turn comprises one hit of the ball. </p>

<p>There are 6 hoops which are each played twice, once in each direction, in a prescribed order. A point is scored by the first team to make the current hoop. To make a hoop, one of the team s balls must be knocked through the current hoop in the right direction. The first team to score 7 points wins. If the game reaches 6-6, a final deciding hoop is played. Note that a team cannot score more than 7 points the game ends as soon as the 7th hoop is won. </p>

<p>The balls are played in a fixed order: blue, red, black (blue s partner) then yellow (red s partner). We can record the progress of a match by recording the outcome of each shot. The code we are using is: </p>

<ul>
	<li><strong>S</strong> a standard shot that does not make a hoop</li>
	<li><strong>H</strong> a shot that makes a hoop for the team who played the shot</li>
	<li><strong>D</strong> a shot that makes 2 hoops for the team who played the shot an extremely unlikely scenario but it can happen! A team on 6 points will only score the first of the two hoops, of course.</li>
	<li><strong>O</strong> a shot that makes a hoop for an opponent s ball! </li>
</ul>

<p>The last one is almost certainly an accident, but it happens far more times than players like! </p>

### 입력 

 <p>The input represents part or all of a single game of golf croquet. The first two lines each contain the name of a team, each consisting of one or more words. The name will be no more than 30 characters long. The first named team play blue and black. The third line is a single integer, S, which tells how many strokes are recorded, for a game that has started but which may not yet be completed. (0 < S <= 255) </p>

<p>The fourth line contains S upper case letter characters, each being one of the 4 characters defined above (S, H, D or O). Blue always plays the first shot followed in turn by red, black and yellow.</p>

### 출력 

 <p>Output a single line of text with the current score in the form </p>

<pre>team1name x team2name y.</pre>

<p>Follow this by a space then one of: </p>

<pre>teamname has won.
teamname is winning.
All square.</pre>

