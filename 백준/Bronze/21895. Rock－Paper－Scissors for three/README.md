# [Bronze II] Rock-Paper-Scissors for three - 21895 

[문제 링크](https://www.acmicpc.net/problem/21895) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Jury of Innopolis Open really like problems about "Rock-Paper-Scissors" game. They even built two special robots to play against each other in this game. As the time passed, robots became so good at this game, so they invited Dasha to play with them.</p>

<p>Rules of "Rock-Paper-Scissors" for three players are as follows:</p>

<ul>
	<li>In each round all players simultaneously show one of three followings signs: Rock, Paper or Scissors.</li>
	<li>Rock beats Scissors, Scissors beats Paper and Paper beats Rock.</li>
	<li>If one player showed the sign which beats both other players' signs, then he is the winner of the round.</li>
	<li>If two players showed the sign which beats the third player's sign, then they both are winners of the round.</li>
	<li>If all players showed either all different signs or all equal signs, then it's impossible to determine a winner and that round ends with a draw.</li>
</ul>

<p>What robots didn't know is that Dasha programmed them and knows every move they are going to make in each round. Help Dasha show them who's boss and win as many rounds as possible.</p>

### 입력 

 <p>First line of input contains $n$ --- number of rounds in Dasha's and robots' game ($1 \le n \le 100$).</p>

<p>Second line contains a string of length $n$, which consists of letters "<code>R</code>" (Rock), "<code>S</code>" (Scissors) and "<code>P</code>" (Paper), $i$-th letter is the first robot's move in the $i$-th round of the game.</p>

<p>Third line contains description of second robot's moves in the same format.</p>

### 출력 

 <p>Output a string of $n$ characters "<code>R</code>", "<code>P</code>" and "<code>S</code>", describing Dasha's moves in each round, that allows her to win as many rounds as possible.</p>

