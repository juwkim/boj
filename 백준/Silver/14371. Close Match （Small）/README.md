# [Silver V] Close Match (Small) - 14371 

[문제 링크](https://www.acmicpc.net/problem/14371) 

### 성능 요약

메모리: 111736 KB, 시간: 784 ms

### 분류

브루트포스 알고리즘, 문자열

### 제출 일자

2024년 9월 20일 14:45:44

### 문제 설명

<p>You are attending the most important game in sports history. The Oceania Coders are playing the Eurasia Jammers in the Centrifugal Bumble-Puppy world finals. Unfortunately, you were sleep deprived from all the anticipation, so you fell asleep during the game!</p>

<p>The scoreboard is currently displaying both scores, perhaps with one or more leading zeroes (because the scoreboard displays a fixed number of digits). While you were asleep, some of the lights on the scoreboard were damaged by strong ball hits, so one or more of the digits in one or both scores are not being displayed.</p>

<p>You think close games are more exciting, and you would like to imagine that the scores are as close as possible. Can you fill in all of the missing digits in a way that minimizes the absolute difference between the scores? If there is more than one way to attain the minimum absolute difference, choose the way that minimizes the Coders' score. If there is more than one way to attain the minimum absolute difference while also minimizing the Coders' score, choose the way that minimizes the Jammers' score.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T cases follow. Each case consists of one line with two non-empty strings C and J of the same length, composed only of decimal digits and question marks, representing the score as you see it for the Coders and the Jammers, respectively. There will be at least one question mark in each test case.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ T ≤ 200.</li>
	<li>C and J have the same length.</li>
	<li>1 ≤ the length of C and J ≤ 3.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: c j</code>, where <code>x</code> is the test case number (starting from 1), <code>c</code> is C with the question marks replaced by digits, and <code>j</code> is J with the question marks replaced by digits, such that the absolute difference between the integers represented by <code>c</code> and <code>j</code> is minimized. If there are multiple solutions with the same absolute difference, use the one in which <code>c</code> is minimized; if there are multiple solutions with the same absolute difference and the same value of <code>c</code>, use the one in which <code>j</code> is minimized.</p>

