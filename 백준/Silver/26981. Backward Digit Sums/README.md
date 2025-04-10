# [Silver I] Backward Digit Sums - 26981 

[문제 링크](https://www.acmicpc.net/problem/26981) 

### 성능 요약

메모리: 110960 KB, 시간: 160 ms

### 분류

브루트포스 알고리즘, 수학

### 제출 일자

2025년 4월 10일 11:51:27

### 문제 설명

<p>FJ and his cows enjoy playing a mental game. They write down the numbers from 1 to N (1 ≤ N ≤ 10) in a certain order and then sum adjacent numbers to produce a new list with one fewer number. They repeat this until only a single number is left. For example, one instance of the game (when N=4) might go like this:</p>

<pre>    3   1   2   4

      4   3   6

        7   9

         16</pre>

<p>Behind FJ's back, the cows have started playing a more difficult game, in which they try to determine the starting sequence from only the final total and the number N. Unfortunately, the game is a bit above FJ's mental arithmetic capabilities.</p>

<p>Write a program to help FJ play the game and keep up with the cows.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and the final sum.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: An ordering of the integers 1..N that leads to the given sum. If there are multiple solutions, choose the one that is lexicographically least, i.e., that puts smaller numbers first.</li>
</ul>

