# [Silver IV] Rather Perplexing Showdown (Small) - 14355 

[문제 링크](https://www.acmicpc.net/problem/14355) 

### 성능 요약

메모리: 115952 KB, 시간: 240 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>You've been asked to organize a Rock-Paper-Scissors tournament. The tournament will have a single-elimination format and will run for N rounds; 2<sup>N</sup> players will participate.</p>

<p>Initially, the players will be lined up from left to right in some order that you specify. In each round, the first and second players in the lineup (starting from the left) will play a match against each other, and the third and fourth players in the lineup (if they exist) will play a match against each other, and so on; all of these matches will occur simultaneously. The winners of these matches will remain in the lineup, in the same relative order, and the losers will leave the lineup and go home. Then a new round will begin. This will continue until only one player remains in the lineup; that player will be declared the winner.</p>

<p>In each Rock-Paper-Scissors match, each of the two players secretly chooses one of Rock, Paper, or Scissors, and then they compare their choices. Rock beats Scissors, Scissors beats Paper, and Paper beats Rock. If one player's choice beats the other players's choice, then that player wins and the match is over. However, if the players make the same choice, then it is a tie, and they must choose again and keep playing until there is a winner.</p>

<p>You know that the players this year are stubborn and not very strategic. Each one has a preferred move and will only play that move in every match, regardless of what the opponent does. Because of this, if two players with the same move go up against each other, they will keep tying and their match will go on forever! If this happens, the tournament will never end and you will be a laughingstock.</p>

<p>This year, there are R players who prefer Rock, P players who prefer Paper, and S players who prefer Scissors. Knowing this, you want to create a lineup that guarantees that the tournament will go to completion and produce a single winner — that is, no match will ever be a tie. Your boss has asked you to produce a list of all such lineups (written in left to right order, with <code>R</code>, <code>P</code>, and <code>S</code> standing for players who prefer Rock, Paper, and Scissors, respectively), and then put that list in alphabetical order.</p>

<p>You know that the boss will lazily pick the first lineup on the list; what will that be? Or do you have to tell your boss that it is <code>IMPOSSIBLE</code> to prevent a tie?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T lines follow; each represents one test case. Each test case consists of four integers: N, R, P, and S, as described in the statement above.</p>

<h3>Limits</h3>

<ul>
	<li>R + P + S = 2<sup>N</sup>.</li>
	<li>0 ≤ R ≤ 2<sup>N</sup>.</li>
	<li>0 ≤ P ≤ 2<sup>N</sup>.</li>
	<li>0 ≤ S ≤ 2<sup>N</sup>.</li>
	<li>1 ≤ T ≤ 25.</li>
	<li>1 ≤ N ≤ 3.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is either <code>IMPOSSIBLE</code> or a string of length 2<sup>N</sup> representing the alphabetically earliest starting lineup that solves the problem. Every character in a lineup must be <code>R</code>, <code>P</code>, or <code>S</code>, and there must be R <code>R</code>s, P <code>P</code>s, and S <code>S</code>s.</p>

