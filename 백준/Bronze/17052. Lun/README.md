# [Bronze I] Lun - 17052 

[문제 링크](https://www.acmicpc.net/problem/17052) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Mom Tihana wanted to buy her daughter Leda a plush toy via an online store. During the purchase process, the system asked for a credit card number to be entered. However, the purchase failed because Tihana mistakenly wrote one of the digits from that number. Internet research has revealed that such systems recognize the wrong number based on Luhn's algorithm.</p>

<p>This algorithm confirms the correctness of the number using a control digit which is always the last digit in the number. Steps to determine the validity of a number are:</p>

<ul>
	<li>Starting from the second digit from the right in the number (tens of the number), double the value of every second digit to the left. If this product is greater than nine, then the digits of that product should be summed up.</li>
	<li>Calculate the sum of all values obtained in the previous step.</li>
	<li>The sum thus obtained should be multiplied by nine and it should be determined the remainder of division by ten.</li>
	<li>If the resulting remainder is equal to the last digit of the number (unit), the number is considered valid.</li>
</ul>

<p>E.g. account number 79927398713 is considered valid because the end right digit 3 can be obtained from the remaining digits in the way described.</p>

<table class="table table-bordered table-striped">
	<tbody>
		<tr>
			<th style="text-align: center;">Account number</th>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;">8</td>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;"><strong>3</strong></td>
		</tr>
		<tr>
			<th style="text-align: center;">Double every other</th>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;"><strong>18</strong></td>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;"><strong>4</strong></td>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;"><strong>6</strong></td>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;"><strong>16</strong></td>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;"><strong>2</strong></td>
			<td style="text-align: center;">-</td>
		</tr>
		<tr>
			<th style="text-align: center;">Sum</th>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;"><strong>9</strong> (1+8)</td>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">6</td>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;"><strong>7</strong> (1+6)</td>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">= <strong>67</strong></td>
		</tr>
	</tbody>
	<tfoot>
		<tr>
			<td colspan="12" style="text-align: center;">(Sum after intermediate step · 9) mod 10 = (67 · 9) mod 10 = 603 mod 10 = 3</td>
		</tr>
	</tfoot>
</table>

<p>Write a program that loads the card number as a N-string that consists only of digits and exactly one sign "x", and prints the smallest one-digit number which we can replace the sign "x" with so that the account number is valid.</p>

### 입력 

 <p>In the first line there is an integer number N (1 ≤ N ≤ 100), the length of string from the task's test. In the second line there is a string of length N consisting of just signs “0”, “1”, “2”, “3”, “4”, “5”, “6”, “7” , “8”, “9” and exactly one sign "x".</p>

### 출력 

 <p>In the only line of the output it should be printed the required one-digit number.</p>

