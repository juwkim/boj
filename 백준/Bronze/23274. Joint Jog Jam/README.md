# [Bronze I] Joint Jog Jam - 23274 

[문제 링크](https://www.acmicpc.net/problem/23274) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

기하학(geometry), 수학(math), 피타고라스 정리(pythagoras)

### 문제 설명

<p>Like so many good stories, this one begins with a claim that Kari is a faster runner than Ola, who of course challenges Kari to a run-down.</p>

<p>Dubbed (rather ironically) Non-Competitive Pace Challenge,</p>

<p>they want to see who can run the furthest in a certain amount of time $t$.  Clearly they both choose to run in straight lines with constant speed.</p>

<p>Kari wrote an app to make sure that Ola does not cheat, but the app requires that their phones constantly communicate over Bluetooth.</p>

<p>After their run, Kari needs to ensure that they were never too far apart from each other at any time during the run.  Write a program that computes the maximum distance between Kari and Ola at any point during the run.</p>

### 입력 

 <p>The input consists of a single line containing eight integers describing four points:</p>

<ul>
	<li>the starting position of Kari,</li>
	<li>the starting position of Ola,</li>
	<li>the ending position of Kari, and</li>
	<li>the ending position of Ola,</li>
</ul>

<p>in that order.  Each point is given by two integers $x$ and $y$ ($0 \le x, y \le 10^4$), the coordinates of the point.</p>

### 출력 

 <p>Output the maximum distance between Kari and Ola during their run, with an absolute or relative error of at most $10^{-6}$.</p>

