# [Silver II] gBalloon (Small) - 12052 

[문제 링크](https://www.acmicpc.net/problem/12052) 

### 성능 요약

메모리: 112636 KB, 시간: 192 ms

### 분류

백트래킹, 브루트포스 알고리즘

### 제출 일자

2025년 3월 10일 17:37:14

### 문제 설명

<p>The G tech company has deployed many balloons. Sometimes, they need to be collected for maintenance at the company's tower, which is located at horizontal position 0. Each balloon is currently at horizontal position <strong>P<sub>i</sub></strong> and height <strong>H<sub>i</sub></strong>.</p>

<p>G engineers can move a balloon up and down by sending radio signals to tell it to drop ballast or let out air. But they can't move the balloon horizontally; they have to rely on existing winds to do that.</p>

<p>There are <strong>M</strong> different heights where the balloons could be. The winds at different heights may blow in different directions and at different velocities. Specifically, at height j, the wind has velocity <strong>V<sub>j</sub></strong>, with positive velocities meaning that the wind blows left to right, and negative velocities meaning that the wind blows right to left. A balloon at position P at a height with wind velocity V will be at position P+V after one time unit, P+2V after two time units, etc. If a balloon touches the tower, it is immediately collected.</p>

<p>It costs | H<sub>original</sub> - H<sub>new</sub> | points of energy to move one balloon between two different heights. (This transfer takes no time.) You have <strong>Q</strong> points of energy to spend, although you do not need to spend all of it. What is the least amount of time it will take to collect all the balloons, if you spend energy optimally?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follows. The first line of each case has three integers <strong>N</strong>, <strong>M</strong>, and <strong>Q</strong>, representing the number of balloons, the number of height levels, and the amount of energy available. <br>
The second line has <strong>M</strong> integers; the jth value on this line (counting starting from 0) is the wind velocity at height j. <br>
Then, <strong>N</strong> more lines follow. The ith of these lines consists of two integers, <strong>P<sub>i</sub></strong> and <strong>H<sub>i</sub></strong>, representing the position and height of the ith balloon.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>N</strong> ≤ 10.</li>
	<li>1 ≤ <strong>M</strong> ≤ 10.</li>
	<li>-10 ≤ <strong>V<sub>j</sub></strong> ≤ 10.</li>
	<li>1 ≤ <strong>Q</strong> ≤ 10.</li>
	<li>0 ≤ <strong>H<sub>i</sub></strong> <<strong>M</strong>.</li>
	<li>-10 ≤ <strong>P<sub>i</sub></strong> ≤ 10.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of time units needed to collect all of the balloons, returns IMPOSSIBLE if it's impossible to collect all the balloons using the energy given.</p>

