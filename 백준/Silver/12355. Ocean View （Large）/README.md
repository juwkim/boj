# [Silver II] Ocean View (Large) - 12355 

[문제 링크](https://www.acmicpc.net/problem/12355) 

### 성능 요약

메모리: 32904 KB, 시간: 76 ms

### 분류

다이나믹 프로그래밍(dp), 가장 긴 증가하는 부분 수열: O(n log n)(lis)

### 문제 설명

<p>Ocean View is a small town on the edge of a small lake, populated by people with high self-esteem. There is only one street in this town, Awesome Boulevard, running away from the lake on the west towards the hill in the east. All of the houses in Ocean View are situated along one side of Awesome Boulevard and are numbered starting at #1 on the edge of the lake all the way up to #<strong>N</strong> at the foot of the hill.</p>

<p>Each resident of Ocean View wants to be able to see the lake. Unfortunately, some of the houses may be blocking the view for some of the higher numbered houses. House #A blocks the view for house #B whenever A is smaller than B, but house #A is as tall as or taller than house #B.</p>

<p>Tired of hearing complaints about obstructed views, the Supreme Ruler of Ocean View has decided to solve the problem using his favorite tool of governance -- violence. He will order his guards to destroy some of the houses on Awesome Boulevard in order to ensure that every remaining house has a view of the lake. Of course, if he destroys too many houses, he might have a rebellion to deal with, so he would like to destroy as few houses as possible.</p>

<p>What is the smallest number of houses that need to be destroyed in order to ensure that every remaining house has an unobstructed view of the lake?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case will consist of two lines. The first line will contain a single integer <strong>N</strong>, the number of houses on Awesome Boulevard. The next line will list the height of each house, from west to east, all positive integers separated by single spaces.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>The height of each house will be between 1 and 1000, inclusive.</li>
	<li><span style="line-height:1.6em">1 ≤ </span><strong style="line-height:1.6em">N</strong><span style="line-height:1.6em"> ≤ 1000;</span></li>
	<li>The answer may be larger than 4.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the minimum number of houses that need to be destroyed.</p>

