# [Silver IV] Multi-key Sorting - 3340 

[문제 링크](https://www.acmicpc.net/problem/3340) 

### 성능 요약

메모리: 209176 KB, 시간: 348 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 정렬(sorting)

### 문제 설명

<p>Consider a table with rows and columns. The columns are numbered from 1 to C. For simplicity's sake, the items in the table are strings consisting of lower case letters.</p>

<table class="table table-bordered td-center th-center">
	<tbody>
		<tr>
			<td>
			<table class="table table-bordered td-center th-center">
				<thead>
					<tr>
						<th>Col. 1</th>
						<th>Col. 2</th>
						<th>Col. 3</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>apple</td>
						<td>red</td>
						<td>sweet</td>
					</tr>
					<tr>
						<td>apple</td>
						<td>green</td>
						<td>sour</td>
					</tr>
					<tr>
						<td>pear</td>
						<td>green</td>
						<td>sweet</td>
					</tr>
					<tr>
						<td>banana</td>
						<td>yellow</td>
						<td>sweet</td>
					</tr>
					<tr>
						<td>banana</td>
						<td>brown</td>
						<td>rotten</td>
					</tr>
				</tbody>
			</table>
			</td>
			<td>
			<table class="table table-bordered td-center th-center">
				<thead>
					<tr>
						<th>Col. 1</th>
						<th>Col. 2</th>
						<th>Col. 3</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>banana</td>
						<td>brown</td>
						<td>rotten</td>
					</tr>
					<tr>
						<td>apple</td>
						<td>green</td>
						<td>sour</td>
					</tr>
					<tr>
						<td>pear</td>
						<td>green</td>
						<td>sweet</td>
					</tr>
					<tr>
						<td>apple</td>
						<td>red</td>
						<td>sweet</td>
					</tr>
					<tr>
						<td>banana</td>
						<td>yellow</td>
						<td>sweer</td>
					</tr>
				</tbody>
			</table>
			</td>
			<td>
			<table class="table table-bordered td-center th-center">
				<thead>
					<tr>
						<th>Col. 1</th>
						<th>Col. 2</th>
						<th>Col. 3</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>apple</td>
						<td>green</td>
						<td>sour</td>
					</tr>
					<tr>
						<td>apple</td>
						<td>red</td>
						<td>sweet</td>
					</tr>
					<tr>
						<td>banana</td>
						<td>brown</td>
						<td>rotten</td>
					</tr>
					<tr>
						<td>banana</td>
						<td>yellow</td>
						<td>sweet</td>
					</tr>
					<tr>
						<td>pear</td>
						<td>green</td>
						<td>sweet</td>
					</tr>
				</tbody>
			</table>
			</td>
		</tr>
	</tbody>
	<tfoot>
		<tr>
			<th>Table 1</th>
			<th>Table 2</th>
			<th>Table 3</th>
		</tr>
	</tfoot>
</table>

<p>You are given the operation Sort(k) on such tables: Sort(k) sorts the rows of a table in the order of the values in column k (while the order of the columns does not change). The sort is stable, that is, rows that have equal values in column k, remain in their original order. For example, applying Sort(2) to Table 1 yields Table 2.</p>

<p>We are interested in sequences of such sort operations. These operations are successively applied to the same table. For example, applying the sequence Sort(2); Sort(1) to Table 1 yields Table 3.</p>

<p>Two sequences of sort operations are called equivalent if, for any table, they have the same effect. For example, Sort(2); Sort(2); Sort(1) is equivalent to Sort(2); Sort(1). However, it is not equivalent to Sort(1); Sort(2), because the effect on Table 1 is different.</p>

<p>Given a sequence of sort operations, determine a shortest equivalent sequence.</p>

### 입력 

 <p>The first line of input contains two integers, C and N. C (1 ≤ C ≤ 1 000 000) is the number of columns and N (1 ≤ N ≤ 3 000 000) is the number of sort operations. The second line contains N integers, k<sub>i</sub> (1 ≤ k<sub>i</sub> ≤ C). It defines the sequence of sort operations Sort(k<sub>1</sub>); ...; Sort(k<sub>N</sub>).</p>

### 출력 

 <p>The first line of output contains one integer, M, the length of the shortest sequence of sort operations equivalent to the input sequence. The second line contains exactly M integers, representing a shortest sequence.</p>

