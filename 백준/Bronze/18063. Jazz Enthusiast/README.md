# [Bronze III] Jazz Enthusiast - 18063 

[문제 링크](https://www.acmicpc.net/problem/18063) 

### 성능 요약

메모리: 121220 KB, 시간: 100 ms

### 분류

사칙연산(arithmetic), 수학(math), 문자열(string)

### 문제 설명

<p>Kai is listening to his favourite jazz playlist. He likes to turn on crossfading between songs, so during the last seconds of a song, it will slowly fade out while the next one fades in. This happens between any two consecutive songs, but the beginning of the first song and the end of the last song will be played normally.</p>

<p>Determine the total amount of time it takes Kai to listen to the whole playlist.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>Two integers n and c (1 ≤ n ≤ 100, 1 ≤ c ≤ 10), giving the number of songs and the crossfade time in seconds.</li>
	<li>n lines of the form m:ss (0:30 ≤ m:ss ≤ 9:59), giving the song lengths (with one digit for the number of whole minutes and two digits for the remaining seconds).</li>
</ul>

### 출력 

 <p>Output a string of the form hh:mm:ss, giving the total time it takes to listen through the whole playlist (with two digits for the number of whole hours, two digits for the number of remaining whole minutes, and two digits for the remaining seconds).</p>

