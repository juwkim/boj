# [Gold III] Perfect Game (Large) - 12367 

[문제 링크](https://www.acmicpc.net/problem/12367) 

### 성능 요약

메모리: 115004 KB, 시간: 176 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation), 수학(math), 확률론(probability), 정렬(sorting)

### 문제 설명

<p>You're playing a video game, in which you will get an achievement if you complete all of the levels consecutively without dying. You can play the levels in any order, and each time you play a level you'll either complete it or die. Each level has some probability that you'll complete it, and takes some amount of time. In what order should you play the levels so that the expected time it takes you to get the achievement is minimized? Assume that it takes equally long to beat a level or to die in it, and that you will start again from the first level in your ordering as soon as you die.</p>

<p>Note: If you fail to complete a level, you do not personally die—only your character in the game dies. If that were not the case, only a few people would try to earn this achievement.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow, each of which consists of three lines. The first line of each test case contains a single integer <strong>N</strong>, the number of levels. The second line contains <strong>N</strong> space-separated integers <strong>L<sub>i</sub></strong>. <strong>L<sub>i</sub></strong> is the number of seconds level <code>i</code> lasts, which is independent of whether you complete the level or die. The third line contains <strong>N</strong> space-separated integers <strong>P<sub>i</sub></strong>. <strong>P<sub>i</sub></strong> is the percent chance that you will <em><strong>die</strong></em> in any given attempt to complete level <code>i</code>.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>0 ≤ <strong>P<sub>i</sub></strong> < 100.</li>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">N</strong><span style="line-height:1.6em"> ≤ 1000.</span></li>
	<li>1 ≤ <strong>L<sub>i</sub></strong> ≤ 100.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: ", where x is the case number (starting from 1), followed by <strong>N</strong> space-separated integers. The <code>j</code><sup>th</sup> integer in the list should be the index of the <code>j</code><sup>th</sup> level you should attempt to beat in order to minimize the amount of time you expect to spend earning the achievement.</p>

<p>Indices go from <code>0</code> to <code>N-1</code>. If there are multiple orderings that would give the same expected time, output the lexicographically least ordering. Out of two orderings, the lexicographically smaller one is the one with the smaller index at the first location where they differ; out of many orderings, the lexicographically least one is the one that is lexicographically smaller than every other ordering.</p>

