# [Silver V] Preokret - 16750 

[문제 링크](https://www.acmicpc.net/problem/16750) 

### 성능 요약

메모리: 116688 KB, 시간: 160 ms

### 분류

구현(implementation)

### 문제 설명

<p>If they continue playing like this, soon the basketball players of the world's best league, the NBA, will put a ball in the basket every second. So there will no longer be any defense, tactics nor basketball.</p>

<p>Let's imagine observing one of these future matches between Team A and Team B. We know how many points both Team A and Team B have scored and the exact second when it happened. Within a second, it will not be possible to score more than one point.</p>

<p>King James is observing the task input and wants to answer the following two questions:</p>

<ol>
	<li>How many points have been scored during the first half-time, that is in the first half of the game, if we know that the entire game lasts 4 × 12 minutes?</li>
	<li>How many "turnarounds" have happened during the match, i.e. how many times has a team come from a losing situation (has strictly fewer points scored than the other team) to a leading one (has strictly more points scored than the other team)?</li>
</ol>

### 입력 

 <p>The first line contains a positive integer A (1 ≤ A ≤ 2879), the number of points Team A has scored. In the following A lines there are positive integers As (1 ≤ As ≤ 2880), the seconds in which Team A was scoring points ordered from the smallest to the largest number.</p>

<p>In the (A + 2)<sup>th</sup> line there is a positive integer B (1 ≤ B ≤ 2879), the number of points Team B has scored. In the following B lines there are positive integers Bs (1 ≤ Bs ≤ 2880), the seconds in which Team B was scoring points ordered from the smallest to the largest number.</p>

### 출력 

 <p>In the first line print an integer value, the answer to the first question from the text of the task. In the second line print an integer value, the answer to the second question from the text of the task.</p>

