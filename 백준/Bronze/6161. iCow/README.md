# [Bronze I] iCow - 6161 

[문제 링크](https://www.acmicpc.net/problem/6161) 

### 성능 요약

메모리: 28776 KB, 시간: 264 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Fatigued by the endless toils of farming, Farmer John has decided to try his hand in the MP3 player market with the new iCow. It is an MP3 player that stores N songs (1 <= N <= 1,000) indexed 1 through N that plays songs in a "shuffled" order, as determined by Farmer John's own algorithm:</p>

<p>Each song i has an initial rating R_i (1 <= R_i <= 10,000).</p>

<p>The next song to be played is always the one with the highest rating (or, if two or more are tied, the highest rated song with the lowest index is chosen).</p>

<p>After being played, a song's rating is set to zero, and its rating points are distributed evenly among the other N-1 songs.</p>

<p>If the rating points cannot be distributed evenly (i.e., they are not divisible by N-1), then the extra points are parceled out one at a time to the first songs on the list (i.e., R_1, R_2, etc. -- but not the played song) until no more extra points remain.</p>

<p>This process is repeated with the new ratings after the next song is played.</p>

<p>Determine the first T songs (1 <= T <= 1000) that are played by the iCow.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and T</li>
	<li>Lines 2..N+1: Line i+1 contains a single integer: R_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1..T: Line i contains a single integer that is the i-th song that the iCow plays.</li>
</ul>

<p> </p>

