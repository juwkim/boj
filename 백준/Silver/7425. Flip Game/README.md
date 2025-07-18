# [Silver I] Flip Game - 7425 

[문제 링크](https://www.acmicpc.net/problem/7425) 

### 성능 요약

메모리: 114016 KB, 시간: 148 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 6월 19일 04:24:26

### 문제 설명

<p>Flip game is played on a rectangular 4x4 field with two-sided pieces placed on each of its 16 squares. One side of each piece is white and the other one is black and each piece is lying either it's black or white side up. Each round you flip 3 to 5 pieces, thus changing the color of their upper side from black to white and vice versa. The pieces to be flipped are chosen every round according to the following rules:</p>

<ol>
	<li>Choose any one of the 16 pieces.</li>
	<li>Flip the chosen piece and also all adjacent pieces to the left, to the right, to the top, and to the bottom of the chosen piece (if there are any).</li>
</ol>

<p><img alt="" src="https://upload.acmicpc.net/e98541f7-ba5e-4d6c-9fd1-55b2b2f1b66e/-/preview/" style="width: 227px; height: 203px; float: right;">Consider the following position as an example:</p>

<pre>bwbw
wwww
bbwb
bwwb</pre>

<p>Here "b" denotes pieces lying their black side up and "w" denotes pieces lying their white side up. If we choose to flip the 1st piece from the 3rd row (this choice is shown at the picture), then the field will become:</p>

<pre>bwbw
bwww
wwwb
wwwb</pre>

<p>The goal of the game is to flip either all pieces white side up or all pieces black side up. You are to write a program that will search for the minimum number of rounds needed to achieve this goal.</p>

### 입력 

 <p>The input file consists of 4 lines with 4 characters "w" or "b" each that denote game field position.</p>

### 출력 

 <p>Write to the output file a single integer number - the minimum number of rounds needed to achieve the goal of the game from the given position. If the goal is initially achieved, then write 0. If it's impossible to achieve the goal, then write the word "Impossible" (without quotes).</p>

