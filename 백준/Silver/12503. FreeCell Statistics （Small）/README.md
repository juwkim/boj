# [Silver V] FreeCell Statistics (Small) - 12503 

[문제 링크](https://www.acmicpc.net/problem/12503) 

### 성능 요약

메모리: 30888 KB, 시간: 76 ms

### 분류

많은 조건 분기(case_work), 수학(math), 정수론(number_theory)

### 문제 설명

<p>I played <strong>D</strong> (<strong>D</strong> > 0) games of FreeCell today. Each game of FreeCell ends in one of two ways -- I either win, or I lose. I've been playing for many years, and have so far played <strong>G</strong>games in total (obviously, <strong>G</strong> ≥ <strong>D</strong>).</p>

<p>At the end of the day, I look at the game statistics to see how well I have played. It turns out that I have won exactly <strong>P<sub>D</sub></strong> percent of the <strong>D</strong> games today, and exactly <strong>P<sub>G</sub></strong> percent of <strong>G</strong>total games I had ever played. Miraculously, there is no rounding necessary -- both percentages are exact! Unfortunately, I don't remember the exact number of games that I have played today (<strong>D</strong>), or the exact number of games that I have played in total (<strong>G</strong>). I do know that I could not have played more than <strong>N</strong> games today (<strong>D</strong> ≤ <strong>N</strong>).</p>

<p>Are the percentages displayed possible, or is the game statistics calculator broken?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> lines follow. Each line contains 3 integers -- <strong>N</strong>, <strong>P<sub>D</sub></strong> and <strong>P<sub>G</sub></strong>.</p>

<h3>Limits</h3>

<ul>
	<li>0 ≤ <strong>P<sub>D</sub></strong> ≤ 100;</li>
	<li>0 ≤ <strong>P<sub>G</sub></strong> ≤ 100.</li>
	<li>1 ≤ <strong>T</strong> ≤ 100;</li>
	<li>1 ≤ <strong>N</strong> ≤ 10.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is either "Possible" or "Broken".</p>

