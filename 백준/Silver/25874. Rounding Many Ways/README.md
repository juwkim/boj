# [Silver III] Rounding Many Ways - 25874 

[문제 링크](https://www.acmicpc.net/problem/25874) 

### 성능 요약

메모리: 108080 KB, 시간: 128 ms

### 분류

브루트포스 알고리즘, 수학, 정수론, 정렬

### 제출 일자

2024년 5월 4일 04:51:33

### 문제 설명

<p>Timothy and Alex’s hopes and dreams of running for UCF’s Student Government Association have been crushed by the realization that their campaign ticket would not be alliterative. So, they have decided to analyze statistics from many different polls given to students to determine what pair of programming team members would be best situated to win the election. However, there is a problem. All of the statistics have been rounded off. This would not be an issue apart from the fact that the pollsters forgot to mention how the number was rounded! (Math Terminology Note: if we round, say, 198 to 200, then 198 is called the “true value” and 200 is called the “rounded value”.)</p>

<p>For example, the rounded value 750 could have come from a true value rounded to the nearest 10 or maybe even the nearest 250. It may also have come from a true value rounded to the nearest 1 (thus not rounding it at all). Thus, the true value could have been something like 625 or maybe much closer like 748.</p>

<p>Luckily for Timothy and Alex, after some reconnaissance work, they have discovered the general rounding methods used:</p>

<ul>
	<li>The original statistic was a positive integer S</li>
	<li>Then a positive integer X was chosen such that X is a divisor of some power of 10, i.e., there exist non-negative integers Y and Z such that X * Y = 10<sup>Z</sup></li>
	<li>Finally the statistic S was rounded to the nearest positive multiple of X to get the rounded value N, i.e., there exists a positive integer W such that X * W = N and |S – N| is minimized.</li>
</ul>

<p>Given the rounded value, find all the different ways it could have been rounded (derived). In other words, given N and using the above constraints, you are to find all values of X that satisfy both of the following two equations:</p>

<ul>
	<li>X * Y = 10<sup>Z</sup></li>
	<li>X * W = N</li>
</ul>

### 입력 

 <p>The first and only line of input contains an integer, N (1 ≤ N ≤ 10<sup>18</sup>), representing the rounded value.</p>

### 출력 

 <p>First print out a single line containing an integer representing the number of different X values that the rounded value N could have been derived from. Then print out all of these values of X, in increasing order, on separate lines.</p>

