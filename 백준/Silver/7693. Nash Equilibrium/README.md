# [Silver V] Nash Equilibrium - 7693 

[문제 링크](https://www.acmicpc.net/problem/7693) 

### 성능 요약

메모리: 115388 KB, 시간: 172 ms

### 분류

구현

### 문제 설명

<p>A two-player normal form game between two individuals A and B is completely specified by</p>

<ul>
	<li>{a<sub>1</sub>, . . . , a<sub>m</sub>}, a set of actions for player A,</li>
	<li>{b<sub>1</sub>, . . . , b<sub>n</sub>}, a set of actions for player B,</li>
	<li>PA, an m × n payoff matrix for player A, and</li>
	<li>PB, an m × n payoff matrix for player B.</li>
</ul>

<p>In such a game, both players simultaneously select actions to be played (say ai and bj for players A and B, respectively). Then payoffs for each player are determined according to the payoff matrices (PA[i,j] and PB[i,j] for players A and B, respectively). The goal of each player is to maximize his or her payoff.</p>

<p>For player A, the set of best responses to a particular action b<sub>j</sub> by player B consists of any action a<sub>i</sub> which maximizes A’s payoff, that is, whose payoff is max<sub>i'</sub>PA[i',j]. Similarly, for player B, the set of best responses to a particular action a<sub>i</sub> by player A is any action b<sub>j</sub> whose payoff is max<sub>j'</sub>PB[i,j']. A pair of strategies (a<sub>i</sub>, b<sub>j</sub>) is said to be a pure strategy Nash equilibrium if a<sub>i</sub> is a best response to b<sub>j</sub> and b<sub>j</sub> is a best response to a<sub>i</sub>.</p>

<p>In this problem, you are given the payoff matrices for two players A and B, and your task is to find and list all pure strategy Nash equilibria.</p>

### 입력 

 <p>The input test file will contain multiple test cases. Each test case begins with a single line containing two integers, m and n, where 1 ≤ m, n ≤ 20. The next m lines specify the m rows of payoff matrix PA. The m lines after that specify the m rows of payoff matrix PB. All payoff matrix values will be integers between -100 and 100, inclusive. The end-of-file is marked by a test case with m = n = 0 and should not be processed.</p>

### 출력 

 <p>For each input case, suppose that N is the number of Nash equilibria for the described normal form game. Then, the output of the program consists of (1) a line containing the single integer N, and (2) N lines containing two integers i and j, where (a<sub>i</sub>, b<sub>j</sub>) is the corresponding Nash equilibrium. Note that the program must list all Nash equilibria in lexicographical order, i.e., (a<sub>i<sub>1</sub></sub>, b<sub>j<sub>1</sub></sub>) is listed before (a<sub>i<sub>2</sub></sub>, b<sub>j<sub>2</sub></sub>) if i<sub>1</sub> < i<sub>2</sub> or if i<sub>1</sub> = i<sub>2</sub> and j<sub>1</sub> < j<sub>2</sub>.</p>

