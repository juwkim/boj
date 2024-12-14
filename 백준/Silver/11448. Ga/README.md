# [Silver II] Ga - 11448 

[문제 링크](https://www.acmicpc.net/problem/11448) 

### 성능 요약

메모리: 114172 KB, 시간: 120 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 12월 15일 02:26:29

### 문제 설명

<p>The Dutch version of the game “Go” is called “Ga”. It is played on an N × N board; the N<sup>2</sup> squares are initially empty. Two players, White and Black, take turns; White begins. During a move, the player places one or more stones of his own colour (one by one) on previously empty squares, one per square. The first player that cannot move, loses.</p>

<p>We say that two squares are adjacent if they directly touch each other in a horizontal, vertical or diagonal way. A player must always place his stones on squares that are adjacent to squares that are already occupied by a stone from his own colour. (The very first stone of the first move of a player may be placed at will.)</p>

<p>The number of stones a player is allowed to put on the board during his move is usually determined by local game rules. E.g., in Volendam this number is determined by throwing dice. Specialized shops sell beautifully carved sets of dice (called “gabbers”) with different numbers of sides. Anyway, it is important to have an upper bound on the number of stones a player can put on the board during his move.</p>

<p>We want to have a program that determines how many stones the White player at most can put on the board during his move.</p>

### 입력 

 <p>The input starts with a line containing an integer T, the number of test cases. Then for each test case:</p>

<ul>
	<li>A line containing one integer N (with 2 ≤ N ≤ 100), the height (equal to the width) of the board.</li>
	<li>Then N lines, each containing N characters, describing the state of the gameboard. The characters are: -, w and b, representing an empty square, a White stone and a Black stone, respectively.</li>
</ul>

<p>Every gameboard contains at least one White stone and at least one Black stone. The White stones so far have been placed according to the rules, and so have the Black ones.</p>

### 출력 

 <p>For each test case, output one line containing a single integer: the maximum number of stones that White can put on the given board in one move, according to the rules of “Ga”.</p>

