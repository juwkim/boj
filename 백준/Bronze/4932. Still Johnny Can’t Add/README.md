# [Bronze I] Still Johnny Can’t Add - 4932 

[문제 링크](https://www.acmicpc.net/problem/4932) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>One way for young children in elementary schools to practice addition is to make them write down an addition table. An addition table of size N is an (N +1)∗(N +1) square matrix, where the top row and the left column are labeled with some random integers, (except for their intersection cell where we normally put the plus sign.) The child’s task is now to put in each cell the result of adding the label of the row, and the label of the column. For example, the table on the right is an addition table of size 3.</p>

<table border="1" cellpadding="1" cellspacing="1" style="width:100px">
	<tbody>
		<tr>
			<td style="text-align:center">+</td>
			<td style="text-align:center"><strong>3 </strong></td>
			<td style="text-align:center"><strong>-2</strong></td>
			<td style="text-align:center"><strong>5</strong></td>
		</tr>
		<tr>
			<td style="text-align:center"><strong>1</strong></td>
			<td style="text-align:center">4</td>
			<td style="text-align:center">-1</td>
			<td style="text-align:center">6</td>
		</tr>
		<tr>
			<td style="text-align:center"><strong>4</strong></td>
			<td style="text-align:center">7</td>
			<td style="text-align:center">2</td>
			<td style="text-align:center">9</td>
		</tr>
		<tr>
			<td style="text-align:center"><strong>-2</strong></td>
			<td style="text-align:center">1</td>
			<td style="text-align:center">-4</td>
			<td style="text-align:center">3</td>
		</tr>
	</tbody>
</table>

<p>Once students grow up and enter intermediate-level schools, we can give them the opposite. Give them an N ∗ N table, and let them decide how to add labels for it to be a valid addition table (if it is indeed an addition table.) Given an N ∗ N table, which does not include any labels, your job is to decide whether it is possible to properly label it or not. We’re not interested in the labels themselves, just decide if it is an addition table or not. For example, the 2 ∗ 2 table on the left is not an addition table, while the one on the right is.</p>

<table border="1" cellpadding="1" cellspacing="1" style="width:50px">
	<tbody>
		<tr>
			<td style="text-align:center">1</td>
			<td style="text-align:center">4</td>
		</tr>
		<tr>
			<td style="text-align:center">3</td>
			<td style="text-align:center">5</td>
		</tr>
	</tbody>
</table>

<p> </p>

<table border="1" cellpadding="1" cellspacing="1" style="width:50px">
	<tbody>
		<tr>
			<td style="text-align:center">3</td>
			<td style="text-align:center">6</td>
		</tr>
		<tr>
			<td style="text-align:center">2</td>
			<td style="text-align:center">5</td>
		</tr>
	</tbody>
</table>

<p> </p>

### 입력 

 <p>Your program will be tested on one or more test cases. The first line in the input is an integer D representing the number of cases. The first line of each test case is an integer N, where N ≤ 10, representing the size of the table. Following that, there will be N lines, each with N integers representing the N ∗ N table in a row-major format. Each number in the table is between -10,000 and 10,000 (inclusive).</p>

### 출력 

 <p>For each test case, output the result on a single line using the following format:</p>

<p>k.␣result</p>

<p>Where k is the test case number (starting at 1,) and result is "YES" if the test case is an addition table, or "NO" if it’s not.</p>

