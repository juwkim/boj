# [Silver IV] Super Paintball - 6127 

[문제 링크](https://www.acmicpc.net/problem/6127) 

### 성능 요약

메모리: 115552 KB, 시간: 140 ms

### 분류

구현(implementation)

### 문제 설명

<p>The cows have purchased a Super Paintball Deluxe game set from Tycow, the cow-toy manufacturer. Bessie, knowing you can help, has partitioned the pasture into a set of N x N unit squares (1 <= N <= 100) and compiled a list of the K (1 <= K <= 100,000) locations (1 <= R_i <= N; 1 <= C_i <= N) of every one of her opponents in the Paintball game.</p>

<p>This paintball game features a paintball gun that can shoot paintballs in any of eight directions: north, south, east, west, and the diagonals that split those directions exactly (northeast, southeast, northwest, southwest).</p>

<p>Bessie wants you to tell her the total number of squares she can occupy and still be able to shoot all of her opponents (she can even shoot them if she shares the same square as they occupy!).</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and K</li>
	<li>Lines 2..K+1: Line i+1 describes cow i's location with two space-separated integers: R_i and C_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that tells how many different locations Bessie may occupy if she is to be able to shoot any cow according to the shooting rules.</li>
</ul>

