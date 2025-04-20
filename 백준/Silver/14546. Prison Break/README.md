# [Silver I] Prison Break - 14546 

[문제 링크](https://www.acmicpc.net/problem/14546) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 20일 17:45:40

### 문제 설명

<p>A prison has been built as a labyrinth.</p>

<p>The labyrinth is composed of huts labelled + or *. If you are in hut +, you can only move to another hut + near your hut. One hut is considered near one another if the two huts have a side in common. If you are in hut *, you can only move to another hut * near your hut.</p>

<p>The labyrinth can be seen as a rectangle of huts of width W and length L. W and L are integers.</p>

<p>A hut is identified by its position on the horizontal side and by its position on the vertical side of the labyrinth.</p>

<p>In this prison, all huts are “entry huts” but there is only one “exit hut”.</p>

<p>Given the labyrinth, the hut of the prisoner (called entry hut) and the exit hut, your task is to determine if the prisoner can escape.</p>

<p>In the example of Prison A (labyrinth of length 4 and width 2), the prisoner can escape. In the second example (labyrinth of length 3 and width 2), the prisoner cannot escape.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14546/1.png" style="height:159px; width:339px"></p>

<p style="text-align: center;">Prison A</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14546/2.png" style="height:182px; width:260px"></p>

<p style="text-align: center;">Prison B (Typo: Entry hut: (2, 2))</p>

### 입력 

 <p>The input will begin with a single integer P on the first line, indicating the number of cases that will follow.</p>

<p>Each case begins with a single line made of 6 natural numbers with the following format:</p>

<p>L W A B C D where :</p>

<ul>
	<li>L is the length of the labyrinth and W is the width of the labyrinth</li>
	<li>A is the length of the entry hut and B is the width of the entry hut of the prisoner</li>
	<li>C is the length of the exit hut and D is the width of the exit hut</li>
</ul>

<p>followed by W lines containing L characters. Each character will be + or *.</p>

### 출력 

 <p>For each prison, print YES if the prisoner can escape and NO if not.</p>

