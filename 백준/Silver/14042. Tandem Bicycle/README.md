# [Silver IV] Tandem Bicycle - 14042 

[문제 링크](https://www.acmicpc.net/problem/14042) 

### 성능 요약

메모리: 113248 KB, 시간: 116 ms

### 분류

그리디 알고리즘(greedy), 정렬(sorting)

### 문제 설명

<p>Since time immemorial, the citizens of Dmojistan and Pegland have been at war. Now, they have finally signed a truce. They have decided to participate in a tandem bicycle ride to celebrate the truce. There are N citizens from each country. They must be assigned to pairs so that each pair contains one person from Dmojistan and one person from Pegland.</p>

<p>Each citizen has a cycling speed. In a pair, the fastest person will always operate the tandem bicycle while the slower person simply enjoys the ride. In other words, if the members of a pair have speeds a and b, then the bike speed of the pair is max(a, b). The total speed is the sum of the N individual bike speeds.</p>

<p>For this problem, in each test case, you will be asked to answer one of two questions:</p>

<ul>
	<li>Question 1: what is the minimum total speed, out of all possible assignments into pairs?</li>
	<li>Question 2: what is the maximum total speed, out of all possible assignments into pairs?</li>
</ul>

### 입력 

 <p>The first line will contain the type of question you are to solve, which is either 1 or 2.</p>

<p>The second line contains N (1 ≤ N ≤ 100).</p>

<p>The third line contains N space-separated integers: the speeds of the citizens of Dmojistan.</p>

<p>The fourth line contains N space-separated integers: the speeds of the citizens of Pegland.</p>

<p>Each person’s speed will be an integer between 1 and 1 000 000.</p>

### 출력 

 <p>Output the maximum or minimum total speed that answers the question asked.</p>

