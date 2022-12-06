# [Silver V] Calvinball championship, again 1 - 10960 

[문제 링크](https://www.acmicpc.net/problem/10960) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구성적(constructive), 그래프 이론(graphs), 런타임 전의 전처리(precomputation)

### 문제 설명

<p>Recall that a Calvinball championship is being held in Czech Republic this year. A game of Calvinball is played by n players with distinct names, divided into any number of non-empty teams. Some players dislike each other; disliking is symmetric: if player a dislikes player b, then also b dislikes a.</p>

<p>The International Calvinball Disorganization decided to make a last-minute change to the team selection procedure: no two people who dislike each other may be on the same team, and subject to that, the number of teams must be as small as possible.</p>

<p>For example, if Calvin, Hobbes, Susie, Tom, Jerry, and Batman play in the game, Batman dislikes everyone else and Tom does not like Jerry and Hobbes, it is possible to play the game with three teams (for example, Batman alone, Tom with Susie, and Calvin with Hobbes and Jerry), but not with two teams (since Batman, Tom, and Jerry dislike each other and must be in different teams), and not with four teams (since a smaller number of teams is possible).</p>

<p>Given the description of which players dislike each other, determine some allowed division of the players into teams (an arbitrary one, if several exist).</p>

### 입력 

 <p><span style="line-height:1.6em">The first line contains two non-negative integers n and m, giving the number of players and the number of distinct pairs of players that dislike each other, respectively. The players are numbered from 1 to n. The i-th of the m following lines contains two distinct positive integers a</span><sub style="line-height:1.6em">i</sub><span style="line-height:1.6em"> and b</span><sub style="line-height:1.6em">i</sub><span style="line-height:1.6em"> (1 ≤ a</span><sub style="line-height:1.6em">i</sub><span style="line-height:1.6em">, b</span><sub style="line-height:1.6em">i</sub><span style="line-height:1.6em"> ≤ n), showing that the players a</span><sub style="line-height:1.6em">i</sub><span style="line-height:1.6em"> and b</span><sub style="line-height:1.6em">i</sub><span style="line-height:1.6em"> dislike each other.</span></p>

### 출력 

 <p>The first line contains a non-negative integer t, giving the number of teams to which the players are divided. The i-th of the following t lines contains a space-separated list of numbers of players belonging to the i-th team. The teams as well as the players in each team can be listed in any order.</p>

<p>The output files should be submitted through the contest interface. In case your submission lacks some of the output files, these are copied from the previous submission (if there is any). It is therefore also possible to submit the output files one by one.</p>

