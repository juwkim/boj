# [Silver III] Binary Encoding - 3496 

[문제 링크](https://www.acmicpc.net/problem/3496) 

### 성능 요약

메모리: 112820 KB, 시간: 152 ms

### 분류

구현

### 제출 일자

2024년 2월 20일 20:15:39

### 문제 설명

<p>Binary encoding represents integer numbers from 0 to 2<sup>n</sup> − 1 inclusive with n bits, each bit is either 0 or 1. In binary encoding most significant digit is written first. Two binary codes are compared from left to right, from the most significant digit to the least significant one. Binary codes are uniquely assigned to numbers from 0 to 2<sup>n</sup> − 1 is a such a way, that corresponding binary codes for numbers in ascending order are themselves in ascending order. For example, binary encoding for numbers from 0 to 7 is:</p>

<table class="table table-bordered" style="width:30%">
	<tbody>
		<tr>
			<th>0</th>
			<td>000</td>
			<th>4</th>
			<td>100</td>
		</tr>
		<tr>
			<th>1</th>
			<td>001</td>
			<th>5</th>
			<td>101</td>
		</tr>
		<tr>
			<th>2</th>
			<td>010</td>
			<th>6</th>
			<td>110</td>
		</tr>
		<tr>
			<th>3</th>
			<td>011</td>
			<th>7</th>
			<td>111</td>
		</tr>
	</tbody>
</table>

<p>Truncated binary encoding generalizes binary encoding to represent integer numbers from 0 to m − 1 inclusive, where m may or may not be equal to 2<sup>n</sup> for some integer number n. Unlike binary encoding, truncated binary encoding uses different number of bits to represent different numbers. If n is the smallest integer number such that m ≤ 2<sup>n</sup>, then truncated binary encoding represents each number from 0 to m −1 with n or with n−1 bits. Some numbers are encoded with n−1 bits only if m < 2<sup>n</sup>; when m = 2<sup>n</sup> truncated binary encoding is the same as binary encoding. Truncated binary codes are compared from left to right, just like binary codes.</p>

<p>Truncated binary encoding also satisfies the following rules:</p>

<ul>
	<li>Smaller integer numbers are represented with smaller or the same number of bits as larger ones.</li>
	<li>Truncated binary codes for numbers in ascending order are themselves in ascending order.</li>
	<li>Truncated binary codes for numbers from 0 to m − 1 are unique.</li>
	<li>No code with n − 1 bits is a prefix of any code with n bits.</li>
	<li>The total number of bits used to represent numbers from 0 to m − 1 is minimal.</li>
</ul>

<p>For example, truncated binary encoding for numbers from 0 to 5 is:</p>

<table class="table table-bordered" style="width:30%">
	<tbody>
		<tr>
			<th>0</th>
			<td>00</td>
			<th>4</th>
			<td>110</td>
		</tr>
		<tr>
			<th>1</th>
			<td>01</td>
			<th>5</th>
			<td>111</td>
		</tr>
		<tr>
			<th>2</th>
			<td>100</td>
			<th> </th>
			<td> </td>
		</tr>
		<tr>
			<th>3</th>
			<td>101</td>
			<th> </th>
			<td> </td>
		</tr>
	</tbody>
</table>

<p>Your task is to encode numbers from 0 to m − 1 with truncated binary encoding.</p>

### 입력 

 <p>The input file contains integer number m (2 ≤ m ≤ 10000).</p>

### 출력 

 <p>Write to the output file m lines. These m lines shall contain truncated binary encoding of numbers from 0 to m − 1 in ascending order.</p>

