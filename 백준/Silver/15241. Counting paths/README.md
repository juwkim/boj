# [Silver II] Counting paths - 15241 

[문제 링크](https://www.acmicpc.net/problem/15241) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 12월 15일 03:10:11

### 문제 설명

<p dir="ltr">Every afternoon, Jack runs from his house to John's. Their houses are in an open field of size N x M. Jack is trying to use a different path each day but he is not sure how many different ways to reach John's house exist.</p>

<p dir="ltr">We will represent the field using a grid of N rows and M columns like the following:</p>

<pre><strong>....
..X.
....</strong>
</pre>

<p>Jack lives in the top-left position and John in the bottom-right. Jack wants to use a different route every day but does not want to waste time he will only walk down and/or right. Also, some parts of the fields have obstacles such as rocks or houses and Jack cannot go through them (they are marked with an X in the grid).</p>

<p>In the previous field, the 4 valid routes are:</p>

<table class="table table-bordered" style="width:100%">
	<tbody>
		<tr>
			<td style="width:25%">
			<pre><strong>****
..X*
...*</strong></pre>
			</td>
			<td style="width:25%">
			<pre><strong>*...
*.X.
****</strong></pre>
			</td>
			<td style="width:25%">
			<pre><strong>*...
**X.
.***</strong></pre>
			</td>
			<td style="width:25%">
			<pre><strong>**..
.*X.
.***</strong></pre>
			</td>
		</tr>
	</tbody>
</table>

<p>Notice that all the valid routes will always have the same length (N + M - 1).</p>

<p>The number of possible paths can be very large so print the result modulo 1000000007 (10^9 + 7).</p>

### 입력 

 <p dir="ltr">The first line will contain two integers N and M. The rows and columns of the map.</p>

<p>Each of the following N lines will contain M characters. If the character is a dot (.), this position is empty. If the character is an X, it means that there is an obstacle and Jack cannot use this cell.</p>

<p>The top-left and bottom-right cells will never have an obstacle on them.</p>

<p dir="ltr">2 <= N <= 200</p>

<p dir="ltr">2 <= M <= 200</p>

### 출력 

 <p dir="ltr">Print the number of possible path between the top-left and bottom-right positions. Remember to print the result modulo 1000000007.</p>

<p>In most languages the modulus operator is %.</p>

