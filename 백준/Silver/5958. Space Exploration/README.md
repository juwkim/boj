# [Silver II] Space Exploration - 5958 

[문제 링크](https://www.acmicpc.net/problem/5958) 

### 성능 요약

메모리: 122276 KB, 시간: 264 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 12월 12일 20:33:36

### 문제 설명

<p>Farmer John's cows have finally blasted off from earth and are now floating around space in their Moocraft. The cows want to reach their fiery kin on Jupiter's moon of Io, but to do this they must first navigate through the dangerous asteroid belt.</p>

<p>Bessie is piloting the craft through this treacherous N x N (1 <= N <= 1,000) sector of space. Asteroids in this sector comprise some number of 1 x 1 squares of space-rock connected along their edges (two squares sharing only a corner count as two distinct asteroids). Please help Bessie maneuver through the field by counting the number of distinct asteroids in the entire sector.</p>

<p>Consider the 10 x 10 space shown below on the left. The '*'s represent asteroid chunks, and each '.' represents a .vast void of empty space. The diagram on the right shows an arbitrary numbering applied to the asteroids.</p>

<pre>               ...**.....           ...11.....
               .*........           .2........
               ......*...           ......3...
               ...*..*...           ...3..3...
               ..*****...           ..33333...
               ...*......           ...3......
               ....***...           ....444...
               .*..***...           .5..444...
               .....*...*          ......4...6
               ..*.......          ..7........</pre>

<p>It's easy to see there are 7 asteroids in this sector.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N+1: Line i+1 contains row i of the asteroid field: N characters</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer indicating the number of asteroids in the field.</li>
</ul>

<p> </p>

