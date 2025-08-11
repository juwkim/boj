# [Silver I] Aqualin - 25788 

[문제 링크](https://www.acmicpc.net/problem/25788) 

### 성능 요약

메모리: 114200 KB, 시간: 120 ms

### 분류

구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 플러드 필

### 제출 일자

2025년 8월 11일 22:33:24

### 문제 설명

<p>The board game Aqualin is played on an n × n grid, where each grid cell is filled with a piece. Each piece is an animal of a particular color, i.e., each piece represents two properties: animal type and animal color. For simplicity, we assign letters 'A' through 'Z' for animal types and number the different colors 1 to n.</p>

<p>After each of the n<sup>2</sup> cells of the grid are filled, the game is scored. There are two teams.</p>

<p>The first team gets points for the largest connected component of animals of the same type that are size 2 or greater. Specifically, for each of the largest connected components of the same type of animals, the first player gets 1 + 2 + … + (c-1) points, where c is the number of animals in the component. For example, if there are connected components of 3 starfish ('A'), 4 octopi ('B'), 1 whale ('C'), and 2 starfish ('A'), then points would be awarded for only the first two groups of animals. Note that no score is awarded to a component of size 1 and, when there are several connected components of the same animal type, only the largest connected component is awarded points. Thus, in the case discussed above, the first team would get 1 + 2 = 3 points for the starfish, and 1 + 2 + 3 = 6 points for the octopi, for a total of 9 points. A connected component of animals is the set of animals you can reach directly or indirectly by traveling up, down, left or right in the grid by only going through animals of the same type.</p>

<p>The second team gets points for the largest connected component of animals of the same color. The scoring is the same as previously described, based on component size.</p>

<p>Here is an example 5 × 5 grid, filled out. In each cell, an ordered pair (x, y) indicates that the animal in that cell is of type x, color y.</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td>(B,3)</td>
			<td>(A,1)</td>
			<td>(C,1)</td>
			<td>(A,2)</td>
			<td>(A,5)</td>
		</tr>
		<tr>
			<td>(B,4)</td>
			<td>(B,1)</td>
			<td>(B,5)</td>
			<td>(E,4)</td>
			<td>(E,3)</td>
		</tr>
		<tr>
			<td>(C,3)</td>
			<td>(C,2)</td>
			<td>(B,2)</td>
			<td>(D,2)</td>
			<td>(E,2)</td>
		</tr>
		<tr>
			<td>(A,3)</td>
			<td>(C,4)</td>
			<td>(A,4)</td>
			<td>(E,5)</td>
			<td>(D,1)</td>
		</tr>
		<tr>
			<td>(D,3)</td>
			<td>(C,5)</td>
			<td>(D,4)</td>
			<td>(D,5)</td>
			<td>(E,1)</td>
		</tr>
	</tbody>
</table>

<p>First, let's consider the score by animal type. There are two animals of type 'A' in the top right corner for a score of 1. All five animals of type 'B' are connected (look at top left) for a score of 10. Four animals of type 'C' are connected, starting from the animal (C, 3) for a score of 6. Two animals of type 'D' are connected, (D, 4) and (D, 5), for a score of 1. Three animals of type 'E' are connected, (E, 4), (E, 3) and (E, 2), for a score of 3. The total score for the first team is 1 + 10 + 6 + 1 + 3 = 21.</p>

<p>There are three animals of color 1 connected at the top for a score of 3. Note that there are 2 other animals of color 1 connected in the bottom right corner, but this score doesn't count because we only count the largest connected component of a single type (or color) of an animal. There are 4 animals of color 2 connected (all on row 3) for a score of 6. There are 3 animals of color 3 connected (all on column 1) for a score of 3. There are 3 animals of color 4 connected, (C, 4), (A, 4) and (D, 4), for a score of 3. There are 2 animals of color 5 connected, (E, 5) and (D, 5), for a score of 1. The total score for the second team is 3 + 6 + 3 + 3 + 1 = 16.</p>

<p>Note: In the given example, there are five animal types and five animal colors. Although each of the 25 possible animal type/color combinations appeared exactly once in this example, this is not guaranteed to be true for all input grids. That is, some animal type/color combinations may appear more than once and some animal type/color combinations may not appear at all.</p>

<p>Given the contents of the grid at the end of a game, determine the score for both teams.</p>

### 입력 

 <p>The first input line contains a single integer: n (2 ≤ n ≤ 26), indicating the number of rows and columns in the game grid. Each of the following n input lines provides the contents of one row in the grid. Each row is represented by n terms, each term providing the type x ('A' ≤ x ≤ 'Z') and color y (1 ≤ y ≤ n) of the corresponding animal on the grid. Assume that the input rows start in column one and there is exactly one space separating different values on these input lines.</p>

### 출력 

 <p>Print, on a line by itself, the score for the first team, followed by a space, followed by the score for the second team.</p>

