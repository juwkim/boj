# [Silver II] Weird Numbers - 3441 

[문제 링크](https://www.acmicpc.net/problem/3441) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 정수론

### 제출 일자

2025년 2월 16일 16:46:58

### 문제 설명

<p>Binary numbers form the principal basis of computer science. Most of you have heard of other systems, such as ternary, octal, or hexadecimal. You probably know how to use these systems and how to convert numbers between them. But did you know that the system base (radix) could also be negative? One assistant professor at the Czech Technical University has recently met negabinary numbers and other systems with a negative base. Will you help him to convert numbers to and from these systems?</p>

<p>A number N written in the system with a positive base R will always appear as a string of digits between 0 and R − 1, inclusive. A digit at the position P (positions are counted from right to left and starting with zero) represents a value of R<sup>P</sup>. This means the value of the digit is multiplied by R<sup>P</sup> and values of all positions are summed together. For example, if we use the octal system (radix R = 8), a number written as 17024 has the following value:</p>

<p style="text-align:center">1×8<sup>4</sup> + 7×8<sup>3</sup> + 0×8<sup>2</sup> + 2×8<sup>1</sup> + 4×8<sup>0</sup> = 1×4096 + 7×512 + 2×8 + 4×1 = 7700</p>

<p>With a negative radix −R, the principle remains the same: each digit will have a value of (−R)<sup>P</sup>. For example, a negaoctal (radix R = −8) number 17024 counts as:</p>

<p style="text-align:center">1×(−8)<sup>4</sup> + 7×(−8)<sup>3</sup> + 0×(−8)<sup>2</sup> + 2×(−8)<sup>1</sup> + 4×(−8)<sup>0</sup> = 1×4096 − 7×512 − 2×8 + 4×1 = 500</p>

<p>One big advantage of systems with a negative base is that we do not need a minus sign to express negative numbers. A couple of examples for the negabinary system (R = −2):</p>

<table class="table table-bordered" style="width:50%">
	<thead>
		<tr>
			<th>decimal</th>
			<th>negabinary</th>
			<th>decimal</th>
			<th>negabinary</th>
			<th>decimal</th>
			<th>negabinary</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>-10</td>
			<td>1010</td>
			<td>-3</td>
			<td>1101</td>
			<td>4</td>
			<td>100</td>
		</tr>
		<tr>
			<td>-9</td>
			<td>1011</td>
			<td>-2</td>
			<td>10</td>
			<td>5</td>
			<td>101</td>
		</tr>
		<tr>
			<td>-8</td>
			<td>1000</td>
			<td>-1</td>
			<td>11</td>
			<td>6</td>
			<td>11010</td>
		</tr>
		<tr>
			<td>-7</td>
			<td>1001</td>
			<td>0</td>
			<td>0</td>
			<td>7</td>
			<td>11011</td>
		</tr>
		<tr>
			<td>-6</td>
			<td>1110</td>
			<td>1</td>
			<td>1</td>
			<td>8</td>
			<td>11000</td>
		</tr>
		<tr>
			<td>-5</td>
			<td>1111</td>
			<td>2</td>
			<td>110</td>
			<td>9</td>
			<td>11001</td>
		</tr>
		<tr>
			<td>-4</td>
			<td>1100</td>
			<td>3</td>
			<td>111</td>
			<td>10</td>
			<td>11110</td>
		</tr>
	</tbody>
</table>

<p>You may notice that the negabinary representation of any integer number is unique, if no “leading zeros” are allowed. The only number that can start with the digit “0”, is the zero itself.</p>

### 입력 

 <p>The input will contain several conversions, each of them specified on one line. A conversion from the decimal system to some negative-base system will start with a lowercase word “to” followed by a minus sign (with no space before it), the requested base (radix) R, one space, and a decimal number N.</p>

<p>A conversion to the decimal system will start with a lowercase word “from”, followed by a minus sign, radix R, one space, and a number written in the system with a base of −R.</p>

<p>The input will be terminated by a line containing a lowercase word “end”. All numbers will satisfy the following conditions: 2 ≤ R ≤ 10, −1 000 000 ≤ N ≤ 1 000 000 (decimal).</p>

### 출력 

 <p>For each conversion, print one number on a separate line. If the input used a decimal format, output the same number written in the system with a base −R. If the input contained such a number, output its decimal value.</p>

<p>Both input and output numbers must not contain any leading zeros. The minus sign “-” may only be present with negative numbers written in the decimal system. Any non-negative number or a number written in a negative-base system must not start with it.</p>

