# [Bronze II] Bakugan - 5678 

[문제 링크](https://www.acmicpc.net/problem/5678) 

### 성능 요약

메모리: 28776 KB, 시간: 100 ms

### 분류

구현(implementation)

### 문제 설명

<p>Mark and Leti love to play with Bakugan balls. These balls are small plastic spheres with a tiny monster toy inside. When dropped to the ground, a Bakugan ball pops open with an incredible sound, liberating a fearsome Bakugan monster. Mark and Leti love to play with the toy monsters, but popping open the balls is also great fun.</p>

<p>Each of them received a bag with Bakugan balls, and they invented a game to pop open the balls. There are 10 different monsters, and for the game Mark and Leti associated each monster with a different integer from 1 to 10, according to the monster’s ugliness. The game is composed of R rounds. At each round:</p>

<ul>
	<li>both players drop simultaneously a ball each;</li>
	<li>each player accumulates a number of points coincident with the number associated with the monster liberated by her/his ball;</li>
	<li>the first (and only the first) player who liberates the same monster in three consecutive rounds earns 30 additional points; if this condition happens in the same round for both players then nobody earns extra points.</li>
</ul>

<p>The winner of the game is the player who accumulates more points. Please help Mark and Leti announce the winner of the game!</p>

### 입력 

 <p>Each test case is described using three lines. The first line contains an integer R representing the number of rounds of the game (1 ≤ R ≤ 10). The second line contains R integers Mi indicating the monsters liberated by Mark at each turn (1 ≤ Mi ≤ 10 for 1 ≤ i ≤ R). The third line contains R integers Li indicating the monsters liberated by Leti at each turn (1 ≤ Li ≤ 10 for 1 ≤ i ≤ R).</p>

<p>The last test case is followed by a line containing one zero.</p>

### 출력 

 <p>For each test case output a line with a character representing the result of the game: ‘M’ (uppercase) if the winner is Mark, ‘L’ (uppercase) if the winner is Leti, or ‘T’ (uppercase) if there is a tie.</p>

