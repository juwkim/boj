# [Silver III] What's the Order Anyway? - 32309 

[문제 링크](https://www.acmicpc.net/problem/32309) 

### 성능 요약

메모리: 111232 KB, 시간: 1472 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 9월 17일 18:18:51

### 문제 설명

<p>Alice, Bob, Carol, Denise, Eddie and Frank are up to their usual tricks. They're performing in the local comedy show but haven't told you the order in which they are presenting their stand-up routines. Instead, they've given you cryptic clues such as (with A standing for Alice, B for Bob, C for Carol, D for Denise, E for Eddie and F for Frank):</p>

<ul>
	<li>A > B</li>
	<li>F < A</li>
	<li>not C D</li>
</ul>

<p>The first clue means that A is performing before B. The second clue means that F is performing after A. The third clue means that C and D are not performing consecutively. (In essence, if we were treating the acts as numbers, the inequality signs are assuming that the acts are sorted from greatest to least.)</p>

<p>Given the above clues, a possible order for the acts is Alice, Carol, Bob, Denise, Frank, Eddie.</p>

<p>What you've realized is that even with their clues, it might be impossible to pin down the exact order of their acts. Thus, you've settled for figuring out how many orderings are possible given the clues they've given you.</p>

<p>Given clues about the order of comedy acts, determine the number of valid possible orderings for the acts.</p>

### 입력 

 <p>The first input line contains two space-separated integers: n (2 ≤ n ≤ 10), indicating the number of comedy acts, and c (1 ≤ c ≤ 10), indicating the number of clues you've been provided. The acts are denoted by the first n uppercase letters.</p>

<p>The clues are provided in the following input lines, one clue per line. Each of these input lines has three space-separated pieces of information: a (1 ≤ a ≤ 3), x and y, as described below:</p>

<ul>
	<li>x and y are guaranteed to be distinct uppercase letters out of the first n letters,</li>
	<li>a represents the type of restriction where 1 indicates that x's act comes before y's, 2 indicates that x's act comes after y's and 3 indicates that x's act and y's act don't occur consecutively (in either order).</li>
</ul>

<p>It's guaranteed that the input clues won't be contradictory, and that there will be at least one valid ordering of the comedy acts.</p>

### 출력 

 <p>Print the number of different orders in which the comedy acts could be.</p>

