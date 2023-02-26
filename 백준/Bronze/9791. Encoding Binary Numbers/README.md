# [Bronze II] Encoding Binary Numbers - 9791 

[문제 링크](https://www.acmicpc.net/problem/9791) 

### 성능 요약

메모리: 116696 KB, 시간: 244 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>A binary number can be encoded into decimal digits by the following counting method.</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<th>Binary number</th>
			<th>Counting</th>
			<th>Decimal digits</th>
		</tr>
		<tr>
			<td><code>000 </code></td>
			<td><code>3x0 </code></td>
			<td><code>30 </code></td>
		</tr>
		<tr>
			<td><code>0111</code></td>
			<td><code>1x0 3x1 </code></td>
			<td><code>1031 </code></td>
		</tr>
		<tr>
			<td><code>111000001 </code></td>
			<td><code>3x1 5x0 1x1</code></td>
			<td><code>315011 </code></td>
		</tr>
		<tr>
			<td><code>1010 </code></td>
			<td><code>1x1 1x0 1x1 1x0 </code></td>
			<td><code>11101110</code></td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>The input includes lines of a character string representing a binary number. The length of a binary number in each line is between 1 and 100 inclusive. The line containing only zero (0) indicates the end of the input. The last line must not be encoded into decimal digits. The input may contain up to 1,000 lines.</p>

### 출력 

 <p>Print out in each line the decimal digits corresponding to the binary number. There is no space between digits.</p>

