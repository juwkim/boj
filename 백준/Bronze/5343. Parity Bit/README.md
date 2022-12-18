# [Bronze III] Parity Bit - 5343 

[문제 링크](https://www.acmicpc.net/problem/5343) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

비트마스킹(bitmask), 구현(implementation)

### 문제 설명

<p>A parity bit, or check bit, is a bit that is added to the end of a sequence of bits for error detection. In telecommunications and computing all data is transformed into a sequence of zeros and ones. For this problem you may assume that all information is coded using 8 bits, with the first 7 bits used for data and the last bit used as the parity bit. The parity bit is set to one if the number of ones in the preceding 7 bits is odd, and the parity bit is set to zero if the number of ones in the preceding 7 bits is even.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<th>7 bits of data (count of 1 bits)</th>
			<th>8 bits including parity bit</th>
		</tr>
		<tr>
			<td>0000000 (0)</td>
			<td>00000000</td>
		</tr>
		<tr>
			<td>0101001 (3)</td>
			<td>01010011</td>
		</tr>
		<tr>
			<td>0111001 (4)</td>
			<td>01110010</td>
		</tr>
		<tr>
			<td>0110111 (5)</td>
			<td>01101111</td>
		</tr>
		<tr>
			<td>1001100 (2)</td>
			<td>10011000</td>
		</tr>
	</tbody>
</table>

<p>The parity bit can be used to determine if the data was transmitted incorrectly. If the parity bit is incorrect (does not match the parity of the previous 7 bits), then a parity error occurred. Your job is to read lines of data and determine the number of parity errors on each line.</p>

### 입력 

 <p>The first line will be a positive integer indicating the number of lines of data transmitted. Each line of data will be a sequence of zeros and ones and the length of the line will be a multiple of 8 and no longer than 64.</p>

### 출력 

 <p>For each data transmission line print the number of parity errors found in the data transmission.</p>

