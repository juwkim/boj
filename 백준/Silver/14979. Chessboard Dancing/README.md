# [Silver II] Chessboard Dancing - 14979 

[문제 링크](https://www.acmicpc.net/problem/14979) 

### 성능 요약

메모리: 111532 KB, 시간: 116 ms

### 분류

애드 혹, 많은 조건 분기

### 제출 일자

2025년 1월 8일 05:50:40

### 문제 설명

<p>Amusement park anniversary organizing group invited a prominent dance company to perform surprise theme dances at the anniversary celebrations. The company prepared four dances with chess theme, conveniently named King performance, Knight performance, Bishop performance and Rook performance.</p>

<p>Each dance is performed by a number of teams of dancers. The unusual setting in the amusement park seems to cause difficulties to a few sensitive company members, however. The main choreographer holds that if a dancer, during a performance, has in his/her sight another dancer of the same team it might sometimes confuse the dancer and tempt him/her to follow erroneously the movements of the teammate. The implication is that the dancers of the same team should be suitably dispersed over the dancing area to be mutually obscured by the members of other teams. Moreover, any arrangement of this kind cannot be shared among the performances, because their styles and movements differ dramatically from each other.</p>

<p>For each of the four dances, the organizing group eventually managed to formulate exact limiting conditions based on company demands:</p>

<p>The performance takes place on a regular S × S square grid of markers on the floor.</p>

<p>Each dancer occupies one marker, no marker is left unoccupied, no two dancers share a common marker and each dancer remains at the same marker during the performance. Each dancer belongs to exactly one team.</p>

<p>Suppose that the center of each marker coincides with some integer lattice point in a Cartesian grid and that the distance between the center of any marker and the center of its closest neighbour marker is 1.</p>

<p>Let us consider two different markers A and B with their respective centers located at Cartesian coordinates (x<sub>1</sub>, y<sub>1</sub>) and (x<sub>2</sub>, y<sub>2</sub>).</p>

<ul>
	<li>In the King performance, if |x<sub>1</sub>−x<sub>2</sub>| < 2 and |y<sub>1</sub>−y<sub>2</sub>| < 2, then A and B must be occupied by members of different teams.</li>
	<li>In the Knight performance, if |x<sub>1</sub> − x<sub>2</sub>| · |y<sub>1</sub> − y<sub>2</sub>| = 2, then A and B must be occupied by members of different teams.</li>
	<li>In the Bishop performance, if |x<sub>1</sub> − x<sub>2</sub>| = |y<sub>1</sub> − y<sub>2</sub>|, then A and B must be occupied by members of different teams.</li>
	<li>In the Rook performance, if |x<sub>1</sub> − x<sub>2</sub>| · |y<sub>1</sub> − y<sub>2</sub>| = 0, then A and B must be occupied by members of different teams.</li>
</ul>

<p>For each of the four dances, the organizing group wants to know the minimum possible number of teams needed to perform the dance.</p>

### 입력 

 <p>There are more test cases. Each test case consists of a single line with integer S (1 ≤ S ≤ 1000) followed by a space and one of four capital letters “K”, “N”, “B”, “R”. S specifies the size of the marker grid and letters denote King performance, Knight performance, Bishop performance, or Rook performance, respectively.</p>

### 출력 

 <p>For each test case, print a single line with one integer denoting the minimum number of teams which are necessary to perform the given dance on a marker grid of the given size.</p>

