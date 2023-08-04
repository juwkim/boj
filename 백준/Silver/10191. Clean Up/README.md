# [Silver V] Clean Up - 10191 

[문제 링크](https://www.acmicpc.net/problem/10191) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘

### 문제 설명

<p>You work for the IT department of a major league baseball team. Baseball has an almost infinite number of stats—what a great job for a computer program!</p>

<p>You will write a program to determine who will bat 4th in the batting order. This is called the “clean-up” position and some managers use the person with the best batting average.</p>

<p>You will be given the roster (with their hits and at bats). The clean-up batter will be fourth and have the highest batting average.</p>

<p>You will also be given a series of hits and at bats which may change the best current batting average. Here are three possibilities:</p>

<ol>
	<li>The clean-up batter still has the greatest average (no change!)</li>
	<li>One of the first 3 batters now has the greatest—switch positions with the clean-up hitter.</li>
	<li>One of the last 5 batters now has the greatest—insert the newest batter at the fourth position and the 4th becomes the 5th, the 5th becomes the 6th… until the old batting position is reached.</li>
</ol>

### 입력 

 <p>The first 9 lines consist of the current roster (last name only) and their past hits and at bats. The next 9 lines consist of the hits and at bats for the next series of games (in the same order as the roster).</p>

### 출력 

 <p>Show the new roster with the highest batting average in the clean-up position.</p>

