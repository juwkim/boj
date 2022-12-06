# [Silver V] Election - 11172 

[문제 링크](https://www.acmicpc.net/problem/11172) 

### 성능 요약

메모리: 30840 KB, 시간: 120 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>In ancient Rome, they used to hold elections by playing a game called Throw the Coin. A quick note for those of you studying Roman history is in order: this is not accurate – in actuality, they held elections by having their cats fight in the arena. Historical accuracy aside, the game of Throw the coin was a game in which the goal was to get as many allies as possible. At the end of the game, the person with the most allies would win. Note that these games were fixed most of the time, and the winner would normally be the one with the fiercest looking cat. With this in mind, it is actually more historically accurate than we meant for this problem statement to be. Also please kindly note that, while this paragraph is very long, we can assure you beyond reasonable as well as unreasonable doubt that it could absolutely have been much, much longer, well beyond the point at which it would be considered ridiculous by anyone possessing any degree of sanity at all.</p>

<p>Each player would bring a coin to the game, any coin, as long as it was perfectly circular and had an integer radius. The players would then throw their coins so that the center of each coin landed on integer coordinates in a coordinate system. They would then mark the area that was covered by each coin, and after everyone had thrown their coin, they would compare the area each coin had covered. A player would become allies with another player if the areas of their coins overlapped. Strangely, the areas were somehow guaranteed to never touch in only one single point.</p>

<p>N players have lined up to play. Your task is to figure out who won, i.e. who got the most allies.</p>

### 입력 

 <p>The first line of the input consists of a single integer, T, the number of test cases.</p>

<p>Each of the following T cases begins with a line with a single integer N.</p>

<p>Each of the next N lines consist of a player’s name, and three integers X, Y and R, representing the x- and y-coordinates of his throw, and the radius of his coin, respectively.</p>

<ul>
	<li>1 ≤ T ≤ 20</li>
	<li>2 ≤ N ≤ 100</li>
	<li>−100 ≤ X, Y ≤ 100</li>
	<li>1 ≤ R ≤ 10</li>
	<li>Each name consists of between 2 and 255 lowercase letters a-z</li>
</ul>

### 출력 

 <p>For each test case output a single line with the name of the winning player or, in case of a tie, output TIE.</p>

