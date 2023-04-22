# [Silver IV] Do the Shuffle - 6826 

[문제 링크](https://www.acmicpc.net/problem/6826) 

### 성능 요약

메모리: 114436 KB, 시간: 144 ms

### 분류

자료 구조, 덱, 구현, 시뮬레이션

### 문제 설명

<p>Those tiny music machines that play your digital music are really computers that keep track of and play music files. The CCC music player (C<sup>3</sup>MP) is currently in development and will be hitting the stores soon! In this problem, you have to simulate a C<sup>3</sup>MP.</p>

<p>The C<sup>3</sup>MP music player will hold 5 songs in memory, whose titles will always be “A”, “B”, “C”, “D” and “E”. The C<sup>3</sup>MP also keeps track of a playlist, which is an ordering of all the songs. The C<sup>3</sup>MP has 4 buttons that the user will press to rearrange the playlist and play the songs.</p>

<p>Initially, the C<sup>3</sup>MP playist is “A, B, C, D, E”. The 4 control buttons do the following:</p>

<ul>
	<li>Button 1: move the first song of the playlist to the end of the playlist. For example: “A, B, C, D, E” will change to “B, C, D, E, A”.</li>
	<li>Button 2: move the last song of the playlist to the start of the playlist. For example, “A, B, C, D, E” will change to “E, A, B, C, D”.</li>
	<li>Button 3: swap the first two songs of the playlist. For example, “A, B, C, D, E” will change to “B, A, C, D, E”.</li>
	<li>Button 4: stop rearranging songs and output the playlist.</li>
</ul>

<p>You need to write a program to simulate a CCC music player. Your program should repeatedly ask for two positive integers b and n. Here b represents the button number that the user wants to press, 1 ≤ b ≤ 4, and n represents the number of times that the user wants to press button b. You can assume that n always satisfies 1 ≤ n ≤ 10.</p>

<p>The input will always finish with the pair of inputs (b = 4, n = 1) when this happens, you should print the order of songs in the current playlist and your program should end. You can assume that the user will only ever press button 4 once</p>

### 입력 

 Empty

### 출력 

 Empty

