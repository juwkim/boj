# [Silver IV] Dart Scoring - 7532 

[문제 링크](https://www.acmicpc.net/problem/7532) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

많은 조건 분기, 구현, 시뮬레이션

### 제출 일자

2023년 12월 7일 22:56:28

### 문제 설명

<p>The game of darts involves throwing darts at a darts board. A darts board is divided into 20 sector, numbered from 1 to 20. Each segment contains single, double and triple scoring areas, so, for example, in segment number 5 it is possible to score 5, 10 or 15 points depending on the area which the dart lands in. In the centre of the board are two concentric circles: the bull’s eye (worth 50 points) and the outer bull (worth 25).</p>

<p>The game of 301 is played by two players, who take it in turns to throw groups of three darts. For each player, scoring does not start until they score a double (the bull’s eye counts as a double). At the end of each group of three darts the total of those darts is deducted from that player's score (which counts down from 301).</p>

<p>To finish the game, a player must make their score exactly 0 by scoring a double. Hence a turn finishes, and no more darts are thrown, once the score drops below 2. If the final score is 0 and the last dart was a double, then the game is over and that player is the winner, otherwise the game continues and the player’s score reverts to what it was at the beginning of the turn. Thus, if your score at the beginning of your turn is 10, then you should attempt to throw a double 5 and end the game. If you throw triple 3, single 9, single 10, or more than 10 then your turn ends and your score remains at 10. If you throw anything else then that throw is temporarily subtracted from your score and you continue attempting to end the game on a double. If you do then you win, if you don’t and your score drops below 2, then your turn ends and your score remains as it was at the beginning of your turn (in this case 10).</p>

<p>Write a program to score darts games.</p>

### 입력 

 <p>Input consists of details for a series of games, with each game consisting of a series of throws occupying one or more lines. Each line (except possibly the last one in a game) consists of 10 throws where each throw consists of a specifier and a comma. A throw specifier is one of the following:</p>

<ul>
	<li>an S, D or T followed by number in the range 1 to 20 indicating a single, double or triple area in that sector.</li>
	<li>a B (bull’s eye) or OB (outer bull).</li>
	<li>an M if the dart missed (scores 0).</li>
	<li>a # to indicate the end of a game.</li>
</ul>

<p>The sequence of games is terminated by a line consisting of a single ‘#’.</p>

### 출력 

 <p>Output consists of several lines for each game. The first line contains the word ‘Game’, followed by a space and the game number — a running number starting at 1. This is followed by as many lines as necessary, with each line showing the scores at the end of each round. (Assume that the game starts with an empty zeroth round, so the first line is always ‘ 301 301’. Each line shows the scores for the two teams right justified in a field of width 5. The last line will contain the score of the losing team and the word ‘Wins’ right justified in a field of width 5 under the appropriate column. Separate successive games by a blank line.</p>

