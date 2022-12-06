# [Bronze I] Rummikub - 11453 

[문제 링크](https://www.acmicpc.net/problem/11453) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation)

### 문제 설명

<p>Rummikub is a simple game, often played by elderly people versus their grandchildren. The tile set consists of four suits, represented by the colors blue, green, red and yellow. Each suit consists of N > 0 different tiles, numbered from 1 to N. The number of a tile represents the value of that tile. There are two tiles of each (value, color) combination.</p>

<p>At the start of the game, the referee deals each player a hand of tiles. These are only visible to them. All other tiles that are not dealt to any player are placed face down on the table, and form the pool. The players take turns in playing tiles. Any tile that is played must be an element of either a group or a run. A group is defined as a set of at least three tiles of the same value but a different suit. A run is defined as a set of at least three tiles of the same suit but with consecutive values. If a player cannot play any tiles, the player must take a tile from the pool.</p>

<p>The elderly people like progress a lot. They love to play lots of tiles each turn, and they hate it when they have to pick a tile from the pool, as this retains progress. Sometimes, the elderly people accidentally take a tile from the pool, because they overlook a run or group in their hand. You have been asked to solve this problem for them. Given a hand of tiles, write a program that determines whether they can create a new run or group.</p>

### 입력 

 <p>The input starts with a line containing an integer T, the number of test cases. Then for each test case:</p>

<ul>
	<li>One line with an integer M, satisfying 1 ≤ M ≤ 800: the number of tiles the player has in his hand.</li>
	<li>One line with M space-separated strings, representing the tiles in the hand. Each tile string consists of an integer V satisfying 1 ≤ V ≤ 100 (the value), and a character which is either b, g, r or y (representing the suit).</li>
</ul>

### 출력 

 <p>For each test case, output a single line containing the string YES if the player can form a run or a group; NO otherwise.</p>

