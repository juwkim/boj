# [Silver IV] Guest Student - 16666 

[문제 링크](https://www.acmicpc.net/problem/16666) 

### 성능 요약

메모리: 122736 KB, 시간: 896 ms

### 분류

구현(implementation)

### 문제 설명

<p>Berland State University invites people from all over the world as guest students. You can come to the capital of Berland and study with the best teachers in the country.</p>

<p>Berland State University works every day of the week, but classes for guest students are held on the following schedule. You know the sequence of seven integers a<sub>1</sub>, a<sub>2</sub>, . . . , a<sub>7</sub> (a<sub>i</sub> = 0 or a<sub>i</sub> = 1):</p>

<ul>
	<li>a<sub>1</sub> = 1 if and only if there are classes for guest students on Sundays;</li>
	<li>a<sub>2</sub> = 1 if and only if there are classes for guest students on Mondays;</li>
	<li>. . .</li>
	<li>a<sub>7</sub> = 1 if and only if there are classes for guest students on Saturdays.</li>
</ul>

<p>The classes for guest students are held in at least one day of a week.</p>

<p>You want to visit the capital of Berland and spend the minimum number of days in it to study k days as a guest student in Berland State University. Write a program to find the length of the shortest continuous period of days to stay in the capital to study exactly k days as a guest student.</p>

### 입력 

 <p>The first line of the input contains integer t (1 ≤ t ≤ 10 000) — the number of test cases to process. For each test case independently solve the problem and print the answer.</p>

<p>Each test case consists of two lines. The first of them contains integer k (1 ≤ k ≤ 10<sup>8</sup>) — the required number of days to study as a guest student. The second line contains exactly seven integers a<sub>1</sub>, a<sub>2</sub>, . . . , a<sub>7</sub> (a<sub>i</sub> = 0 or a<sub>i</sub> = 1) where a<sub>i</sub> = 1 if and only if classes for guest students are held on the i-th day of a week.</p>

### 출력 

 <p>Print t lines, the i-th line should contain the answer for the i-th test case — the length of the shortest continuous period of days you need to stay to study exactly k days as a guest student.</p>

