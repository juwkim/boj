# [Silver I] You Shall Not Pass!! - 9353 

[문제 링크](https://www.acmicpc.net/problem/9353) 

### 성능 요약

메모리: 145168 KB, 시간: 616 ms

### 분류

그래프 이론, 그래프 탐색, 그리디 알고리즘, 정렬, 트리

### 제출 일자

2025년 6월 17일 03:17:34

### 문제 설명

<p>Ahmed Aly is the problem architect for this year’s regional contest, and he knows a lot about the participating teams and their coaches. More precisely, each participating university has a coach who coaches some seniors; each of them might be coaching some juniors where each junior might be coaching another junior, and so on. You can think of this as a hierarchy relation, where each team coaches those who are directly beneath it in the hierarchy. Ahmed, of course, knows these relations precisely and knows who coaches whom.</p>

<p>Ahmed also knows that, for each team, he can write a problem that he knows neither this team nor its trainees nor anyone beneath them in the hierarchy can solve and everyone else will solve it, but he has a limited number of problems he can put in the problem set of the contest. He wants to use all that for the sole purpose of maximizing the number of teams who will not solve at least one problem.</p>

<p>Ahmed needs your help, write a program that given the number of problems Ahmed can write in the problem set and the relations between the teams, prints the maximum number of those who will not solve at least one problem.</p>

<p>Note that a team can only be coached by one other team</p>

### 입력 

 <p>The first line of input contains an integer T, the number of test cases. T test cases follow, the first line of each test case contains three integers A, B, C, the number of teams, the number of relations and the number of problems available in the problem set respectively. Then follows B lines, each in the format F T, where F and T are contestants and F coaches T where contestants are numbered from 0 to A-1.</p>

<ul>
	<li>0 < T ≤ 100</li>
	<li>0 < A ≤ 10000 </li>
	<li>0 ≤ B < A</li>
	<li>0 ≤ C ≤ A</li>
	<li>0 ≤ F, T <A</li>
</ul>

### 출력 

 <p>For each test case, on a separate line, output the maximum number of those who will not solve at least one problem.</p>

