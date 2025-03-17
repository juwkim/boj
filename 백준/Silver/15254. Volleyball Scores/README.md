# [Silver II] Volleyball Scores - 15254 

[문제 링크](https://www.acmicpc.net/problem/15254) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

분류 없음

### 제출 일자

2025년 3월 17일 23:08:40

### 문제 설명

<p>Volleyball has been an Olympic sport since 1964. Teams of 6 players (in beach volleyball: 2 players) hit a ball back and forth, but each team can only touch the ball up to three times until they need to hit it to the other side. There are additional rules, such as the same player not being allowed to touch the ball twice in a row, etc., which make keeping track of the score quite tedious. This is where you come in and write a program to solve this problem for them.</p>

<p>Here’s a more precise refresher of volleyball rules. The two teams each consist of 6 players: Team A’s players are numbered 1–6 in this problem, and Team B’s players are 7–12. The two teams take turns serving. The other team wins the point when one of the following things happen to your team:<sup>3</sup></p>

<ol>
	<li>One of your team’s players touches the ball twice in a row.</li>
	<li>The ball is touched at least four times in a row by players of your team.</li>
	<li>The ball touches the ground in your court.</li>
	<li>The ball touches the ground out of bounds, and one of your team’s players was the last to touch the ball before that.</li>
	<li>One of your team’s players touches the ball right after one of your players has served it.</li>
</ol>

<p>Given a sequence of who touched the ball, your goal is to find out the current score (notice that “touching” the ball may include serving it). You also should output an error message if at any point in time, the wrong team served.</p>

<p><sup>3</sup>We will ignore effects of the net here, as well as a few other details, including the fact that the person serving the ball must normally rotate.</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of a data set contains a number t with 1 ≤ t ≤ 1000. The second line is a sequence of t “ball touches”, separated by one empty space, as follows:</p>

<ul>
	<li>A number i with 1 ≤ i ≤ 12 means that player i touched the ball (this may have been a serve).</li>
	<li>The characters ‘A’ or ‘B’ mean that the ball touched the ground in the court of Team A resp. Team B.</li>
	<li>The character ‘X’ means that the ball touched the ground out of bounds.</li>
</ul>

<p>The first “ball touch” is always a number, representing the person who served first. The point may be ongoing at the end of the sequence. The input will never contain impossible sequences (except wrong serves).</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the score of the two teams, separated by a single white space. If at any point during the sequence, a player from the wrong team served, output “Wrong Serve” instead of the score.</p>

