# [Bronze III] Retype - 23925 

[문제 링크](https://www.acmicpc.net/problem/23925) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>After spending many hours studying for programming competitions, you decided to take a rest and play video games. You are currently playing an adventure game called Quick Start.</p>

<p>This game has <b>N</b> levels, and you are currently on the <b>K</b>-th level. Unfortunately, you just realized that to beat the boss at the final level, you will need a special sword, which can be picked up at level <b>S</b>. You have already completed that level, but you forgot to pick up the sword at that level.</p>

<p>Now you want to pick up the sword and finish the game in the least amount of time possible, and for that you have two options:</p>

<ol>
	<li>Restart the game and complete all levels again, starting from level 1.</li>
	<li>Move to previous levels until you reach level <b>S</b>, pick up the sword and complete all the remaining levels, starting from level <b>S</b>.</li>
</ol>

<p>Every time you enter a level you have to exit it, either by completing it and going to the next level or by moving to a previous level or by finishing / exiting the game. Exiting any level takes 1 minute. That means, for example, that it took you L minutes to complete the first L levels.</p>

<p>Your task is to discover which option would result in the least amount of total time to finish the game (including the time you have already spent).</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> test cases follow.</p>

<p>The first (and only) line of each test case contains three integers <b>N</b>, <b>K</b> and <b>S</b>: the number of levels in the game, the current level you are in, and the level where you have to pick up the sword, respectively.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the least amount of total time to finish the game.</p>

