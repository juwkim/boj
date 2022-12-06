# [Bronze I] Visible Trees - 21009 

[문제 링크](https://www.acmicpc.net/problem/21009) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>There is a legend about a magical park with N × N trees. The trees are positioned in a square grid with N rows (numbered from 1 to N from north to south) and N columns (numbered from 1 to N from west to east). The height (in metres) of each tree is an integer between 1 and N × N, inclusive. Magically, the height of all trees is unique.</p>

<p>Bunga is standing on the northmost point of the park and wants to count the number of visible trees for each column. Similarly, Lestari is standing on the westmost point of the park and wants to count the number of visible trees for each row. A tree X is visible if all other trees in front of the tree X are shorter than the tree X.</p>

<p>For example, let N = 3 and the height (in metres) of the trees are as follows.</p>

<pre>6 1 8
7 5 3
2 9 4</pre>

<ul>
	<li>On the first column, Bunga can see two trees, as the tree on the third row is obstructed by the other trees.</li>
	<li>On the second column, Bunga can see all three trees.</li>
	<li>On the third column, Bunga can see only the tree on the first row, as the other trees are obstructed by the tree on the first row.</li>
	<li>On the first row, Lestari can see two trees, as the tree on the second column is obstructed by the tree on the first column.</li>
	<li>On the second row, Lestari can see only the tree on the first column, as the other trees are obstructed by the tree on the first column.</li>
	<li>On the third row, Lestari can see two trees, as the tree on the third column is obstructed by the tree on the second column.</li>
</ul>

<p>Your task is to determine the numbers reported by Bunga and Lestari.</p>

### 입력 

 <p>Input begins with a line containing an integer: N (1 ≤ N ≤ 10) representing the number of trees on each row and column. The next N lines each contains N integers representing the height (in metres) of the trees. The j<sup>th</sup> integer on the i<sup>th</sup> line is the height of the tree on the i<sup>th</sup> row and j<sup>th</sup> column between 1 to N × N, inclusive. It is guaranteed that all trees have different heights.</p>

### 출력 

 <p>Output begins with a line containing N integers representing the number of trees visible by Bunga. The j<sup>th</sup> integer is the number of visible trees on the j<sup>th</sup> column. The next N lines each contains an integer representing the number of trees visible by Lestari. The integer on the i<sup>th</sup> line is the number of visible trees on the i<sup>th</sup> row.</p>

