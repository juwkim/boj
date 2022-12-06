# [Silver V] Architecture - 17542 

[문제 링크](https://www.acmicpc.net/problem/17542) 

### 성능 요약

메모리: 113248 KB, 시간: 112 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>Your brother has won an award at the recent Breakthroughs in Architectural Problems Conference and has been given the once in a lifetime opportunity of redesigning the city center of his favorite city Nijmegen. Since the most striking parts of a city’s layout are the skylines, your brother has started by drawing ideas for how he wants the northern and eastern skylines of Nijmegen to look. However, some of his proposals look rather outlandish, and you are starting to wonder whether his designs are possible.</p>

<p>For his design, your brother has put an R × C grid on the city. Each cell of the city will contain a building of a certain height. The eastern skyline is given by the tallest building in each of the R rows, and the northern skyline is given by the tallest building in each of the C columns.</p>

<p>A pair of your brother’s drawings of skylines is possible if and only if there exists some way of assigning building heights to the grid cells such that the resulting skylines match these drawings.</p>

<p>Figure A.1 shows a possible city with the northern and eastern skylines exactly as given in the input of the first sample.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 108px; height: 85px;"></p>

<p style="text-align: center;">Figure A.1: Example city showing sample 1 has a valid solution.</p>

### 입력 

 <ul>
	<li>The first line consists of two integers 1 ≤ R, C ≤ 100, the number of rows and columns in the grid.</li>
	<li>The second line consists of R integers x<sub>1</sub>, . . . , x<sub>R</sub> describing the eastern skyline (0 ≤ x<sub>i</sub> ≤ 1000 for all i).</li>
	<li>The third line consists of C integers y<sub>1</sub>, . . . , y<sub>C</sub> describing the northern skyline (0 ≤ y<sub>j</sub> ≤ 1000 for all j).</li>
</ul>

### 출력 

 <p>Output one line containing the string possible if there exists a city design that produces the specified skyline, and impossible otherwise.</p>

