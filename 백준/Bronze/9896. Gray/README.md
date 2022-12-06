# [Bronze II] Gray - 9896 

[문제 링크](https://www.acmicpc.net/problem/9896) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

Empty

### 문제 설명

<p>A binary number is a number in base 2, where the individual digits, or bits, have weights in powers of two. For example, the decimal number 23 is written as 10111 in binary because:</p>

<p>(1 × 2<sup>4</sup>) + (0 × 2<sup>3</sup>) + (1 × 2<sup>2</sup>) + (1 × 2<sup>1</sup>) + (1 × 2<sup>0</sup>) = (1 × 16) + (1 × 4) + (1 × 2) + (1 × 1) = 23.</p>

<p>A Gray code sequence consists of a sequence of binary values, in which each value differs from its immediate predecessor by only a single bit. The following example shows a standard Gray code sequence of 3-bit binary numbers.</p>

<table class="table table-bordered table-center-70">
	<tbody>
		<tr>
			<td>Binary sequence</td>
			<td>000</td>
			<td>001</td>
			<td>010</td>
			<td>011</td>
			<td>100</td>
			<td>101</td>
			<td>110</td>
			<td>111</td>
		</tr>
		<tr>
			<td>Standard Gray code sequence</td>
			<td>000</td>
			<td>001</td>
			<td>011</td>
			<td>010</td>
			<td>110</td>
			<td>111</td>
			<td>101</td>
			<td>100</td>
		</tr>
	</tbody>
</table>

<p>A very simple algorithm is available to convert a binary number into its equicalent standard Gray code value. For example, to convert binary value 011, we start by copying the first bit:</p>

<pre style="text-align: center;">0 1 1
v    
0    
</pre>

<p>To obtain the second bit, we add the first and second bits of the given binary number, to get the sum 0 + 1 = 1:</p>

<pre style="text-align: center;"><strong>0</strong> + <strong>1</strong> 1
    v  
0   1  
</pre>

<p>To obtain the third bit, we add teh second and third bits of the given binary number, to get the sum 1 + 1 = 10 (in binary), but we discard the carry bit so we just take the rightmost bit 0 of the sum:</p>

<pre style="text-align: center;">0 <strong>1</strong> + <strong>1</strong>
      v
0 1   0
</pre>

<p>Hence our answer is 010.</p>

<p>In general, except the first bit, the <i>k</i>-th bit of the standard Gray code is obtained by adding the (<i>k</i>-1)-th bit and the <i>k</i>-th bit of the given binary number and discarding the carry. The discard-carry addition operation can be described completely as:</p>

<pre style="text-align: center;">  0    0    1    1
+ 0  + 1  + 0  + 1
---  ---  ---  ---
   0   1    1    0
---  ---  ---  ---
</pre>

<p>As another example, the 5-bit binary number 10101 is converted to its equivalent standard Gray code value 11111 by applying the above algorithm. The table below shows a few more examples.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td>Binary value</td>
			<td>Equivalent standard Gray code value</td>
		</tr>
		<tr>
			<td align="center">01110</td>
			<td align="center">01001</td>
		</tr>
		<tr>
			<td align="center">111111</td>
			<td align="center">100000</td>
		</tr>
		<tr>
			<td align="center">1001001</td>
			<td align="center">1101101</td>
		</tr>
		<tr>
			<td align="center">000111000</td>
			<td align="center">000100100</td>
		</tr>
	</tbody>
</table>

<p>You are to write a program to convert an <i>n</i>-bit binary value into its equivalent <i>n</i>-bit standard Gray code value, where 1 ≤ <i>n</i> ≤ 20</p>

### 입력 

 <p> </p>

<p>The input consists of two lines, each line containing one integer.</p>

<ol>
	<li>The first line contains the integer <i>n</i>, the number of bits, where 1 ≤ <i>n</i> ≤ 20.</li>
	<li>The second line contains a bit-string of length <i>n</i> representing the <i>n</i>-bit binary number.</li>
</ol>

### 출력 

 <p>The output contains a bit-string of length <i>n</i> representing the standard Gray code equivalent of the given <i>n</i>-bit binary number.</p>

