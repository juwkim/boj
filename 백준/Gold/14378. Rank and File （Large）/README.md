# [Gold V] Rank and File (Large) - 14378 

[문제 링크](https://www.acmicpc.net/problem/14378) 

### 성능 요약

메모리: 115372 KB, 시간: 200 ms

### 분류

조합론, 수학

### 제출 일자

2024년 2월 9일 21:11:37

### 문제 설명

<p>When Sergeant Argus's army assembles for drilling, they stand in the shape of an N by Nsquare grid, with exactly one soldier in each cell. Each soldier has a certain height.</p>

<p>Argus believes that it is important to keep an eye on all of his soldiers at all times. Since he likes to look at the grid from the upper left, he requires that:</p>

<ul>
	<li>Within every row of the grid, the soldiers' heights must be in strictly increasing order, from left to right.</li>
	<li>Within every column of the grid, the soldiers' heights must be in strictly increasing order, from top to bottom.</li>
</ul>

<p>Although no two soldiers in the same row or column may have the same height, it is possible for multiple soldiers in the grid to have the same height.</p>

<p>Since soldiers sometimes train separately with their row or their column, Argus has asked you to make a report consisting of 2*N lists of the soldiers' heights: one representing each row (in left-to-right order) and column (in top-to-bottom order). As you surveyed the soldiers, you only had small pieces of paper to write on, so you wrote each list on a separate piece of paper. However, on your way back to your office, you were startled by a loud bugle blast and you dropped all of the pieces of paper, and the wind blew one away before you could recover it! The other pieces of paper are now in no particular order, and you can't even remember which lists represent rows and which represent columns, since you didn't write that down.</p>

<p>You know that Argus will make you do hundreds of push-ups if you give him an incomplete report. Can you figure out what the missing list is?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with an integer N, followed by 2*N-1 lines of N integers each, representing the lists you have, as described in the statement. It is guaranteed that these lists represent all but one of the rows and columns from a valid grid, as described in the statement.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ T ≤ 50.</li>
	<li>1 ≤ all heights ≤ 2500.</li>
	<li>The integers on each line will be in strictly increasing order.</li>
	<li>It is guaranteed that a unique valid answer exists.</li>
	<li>2 ≤ N ≤ 50.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and y is a list of N integers in strictly increasing order, representing the missing list.</p>

