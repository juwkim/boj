# [Silver IV] The Chosen Sub Matrix - 7800 

[문제 링크](https://www.acmicpc.net/problem/7800) 

### 성능 요약

메모리: 114328 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘(bruteforcing), 자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 정렬(sorting), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>From a given N x N matrix, you should find an M x M sub matrix which has the least distinct element in it. If there are more than one sub matrixes which have the same number of distinct elements then compare each element in descending order and choose one that has the first highest element. If all of distinct elements of all sub matrixes are the same, chose one with the least row index, and then the least column index. The matrix index starts at 1.</p>

<p>For example, given a 4x4 matrix:</p>

<table class="table table-bordered" style="width:10%">
	<tbody>
		<tr>
			<td>3</td>
			<td>9</td>
			<td>9</td>
			<td>9</td>
		</tr>
		<tr>
			<td>3</td>
			<td>9</td>
			<td>9</td>
			<td>2</td>
		</tr>
		<tr>
			<td>3</td>
			<td>9</td>
			<td>9</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>5</td>
			<td>5</td>
			<td>2</td>
		</tr>
	</tbody>
</table>

<p>Then, the possible sub matrixes of 3x3 are:</p>

<table class="table table-bordered" style="width:45%">
	<tbody>
		<tr>
			<td style="width:3%">3</td>
			<td style="width:3%">9</td>
			<td style="width:3%">9</td>
			<td rowspan="4" style="width:3%"> </td>
			<td style="width:3%">9</td>
			<td style="width:3%">9</td>
			<td style="width:3%">9</td>
			<td rowspan="4" style="width:3%"> </td>
			<td style="width:3%">3</td>
			<td style="width:3%">9</td>
			<td style="width:3%">9</td>
			<td rowspan="4" style="width:3%"> </td>
			<td style="width:3%">9</td>
			<td style="width:3%">9</td>
			<td style="width:3%">2</td>
		</tr>
		<tr>
			<td>3</td>
			<td>9</td>
			<td>9</td>
			<td>9</td>
			<td>9</td>
			<td>2</td>
			<td>3</td>
			<td>9</td>
			<td>9</td>
			<td>9</td>
			<td>9</td>
			<td>2</td>
		</tr>
		<tr>
			<td>3</td>
			<td>9</td>
			<td>9</td>
			<td>9</td>
			<td>9</td>
			<td>2</td>
			<td>2</td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>5</td>
			<td>2</td>
		</tr>
		<tr>
			<th colspan="3">S<sub>1</sub></th>
			<th colspan="3">S<sub>2</sub></th>
			<th colspan="3">S<sub>3</sub></th>
			<th colspan="3">S<sub>4</sub></th>
		</tr>
	</tbody>
</table>

<p>Sub matrix S1 has 2 distinct elements: 9 and 3;</p>

<p>Sub matrix S2 has 2 distinct elements: 9 and 2;</p>

<p>Sub matrix S3 has 4 distinct elements: 9, 5, 3, and 2;</p>

<p>Sub matrix S4 has 3 distinct elements: 9, 5, and 2.</p>

<p>Sub matrixes are ranked using the rules above and give result as S1, S2, S4, and then S3.</p>

<p>Which means the chosen sub matrix is S1.</p>

### 입력 

 <p>The first line of each case contains two integers, N (1<=N<=10) the size of matrix, and M (1<=M<=N) the size of sub matrix to be chosen. In the next N lines, each contains N integers (each separated by a space) that represent the matrix. Each element in the matrix should be between 0 and 9 inclusively.</p>

<p> </p>

### 출력 

 <p>For each case you should output in a single line, the top-left index (row and column, separated by a single space) of the chosen sub matrix.</p>

<p> </p>

