# [Silver III] Oversized Pancake Flipper (Large) - 14789 

[문제 링크](https://www.acmicpc.net/problem/14789) 

### 성능 요약

메모리: 30840 KB, 시간: 268 ms

### 분류

브루트포스 알고리즘(bruteforcing), 그리디 알고리즘(greedy)

### 문제 설명

<p>Last year, the Infinite House of Pancakes introduced a new kind of pancake. It has a happy face made of chocolate chips on one side (the "happy side"), and nothing on the other side (the "blank side").</p>

<p>You are the head cook on duty. The pancakes are cooked in a single row over a hot surface. As part of its infinite efforts to maximize efficiency, the House has recently given you an oversized pancake flipper that flips exactly <strong>K</strong> consecutive pancakes. That is, in that range of <strong>K</strong> pancakes, it changes every happy-side pancake to a blank-side pancake, and vice versa; it does <em>not</em> change the left-to-right order of those pancakes.</p>

<p>You cannot flip fewer than <strong>K</strong> pancakes at a time with the flipper, even at the ends of the row (since there are raised borders on both sides of the cooking surface). For example, you can flip the first <strong>K</strong> pancakes, but not the first <strong>K</strong> - 1 pancakes.</p>

<p>Your apprentice cook, who is still learning the job, just used the old-fashioned single-pancake flipper to flip some individual pancakes and then ran to the restroom with it, right before the time when customers come to visit the kitchen. You only have the oversized pancake flipper left, and you need to use it quickly to leave all the cooking pancakes happy side up, so that the customers leave feeling happy with their visit.</p>

<p>Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper needed to leave all pancakes happy side up, or state that there is no way to do it.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each consists of one line with a string <strong>S</strong> and an integer <strong>K</strong>. <strong>S</strong> represents the row of pancakes: each of its characters is either <code>+</code> (which represents a pancake that is initially happy side up) or <code>-</code> (which represents a pancake that is initially blank side up).</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>Every character in <strong>S</strong> is either <code>+</code> or <code>-</code>.</li>
	<li>2 ≤ <strong>K</strong> ≤ length of <strong>S</strong>.</li>
	<li>2 ≤ length of <strong>S</strong> ≤ 1000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is either <code>IMPOSSIBLE</code> if there is no way to get all the pancakes happy side up, or an integer representing the the minimum number of times you will need to use the oversized pancake flipper to do it.</p>

