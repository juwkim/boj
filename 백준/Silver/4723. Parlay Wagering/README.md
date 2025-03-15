# [Silver II] Parlay Wagering - 4723 

[문제 링크](https://www.acmicpc.net/problem/4723) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

사칙연산, 구현, 수학, 문자열

### 제출 일자

2025년 3월 16일 06:56:42

### 문제 설명

<p>Parlay wagering offers sports bettors the opportunity to win a large sum of money from a small initial wager. A parlay wager is a combination of individual independent wagers that only pays if no individual wager loses. The payout from each wager is applied or “parlayed” to the next wager in turn. If any individual wager loses, the bettor receives nothing. If any individual wager is a tie or “push”, that wager is effectively ignored, reducing the ultimate payout.</p>

<p>The sports book quotes the payout rate for an individual wager as a “money line”, a non-zero integer in the range -2000 to 2000. To compute the payout for a successful wager, the money line is converted to a decimal multiplier as follows: if the money line is positive, it is divided by 100 to obtain the multiplier. If the money line is negative, the absolute value is divided into 100 to obtain the multiplier. The multiplier is always truncated to three digits after the decimal point. The wager is multiplied by this multiplier to determine the amount won. The amount won is truncated to the cent (the sports book keeps the fractional cents).</p>

<p>Consider the following example for a five-way parlay wager:</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td>Money Line</td>
			<td>Wager</td>
			<td>Result</td>
			<td>Multiplier</td>
			<td>Amount Won</td>
		</tr>
		<tr>
			<td>-170</td>
			<td><span>$</span>10.00</td>
			<td>Win</td>
			<td>100/170</td>
			<td><span>$</span>5.88</td>
		</tr>
		<tr>
			<td>-160</td>
			<td><span>$</span>15.88</td>
			<td>Win</td>
			<td>100/160</td>
			<td><span>$</span>9.92</td>
		</tr>
		<tr>
			<td>125</td>
			<td><span>$</span>25.80</td>
			<td>Win</td>
			<td>125/100</td>
			<td><span>$</span>32.25</td>
		</tr>
		<tr>
			<td>-135</td>
			<td><span>$</span>58.05</td>
			<td>Win</td>
			<td>100/135</td>
			<td><span>$</span>42.95</td>
		</tr>
		<tr>
			<td>-140</td>
			<td><span>$</span>101.00</td>
			<td>Win</td>
			<td>100/140</td>
			<td><span>$</span>72.11</td>
		</tr>
		<tr>
			<td colspan="4" rowspan="1" style="text-align:right">Subtotal: </td>
			<td><span>$</span>163.11</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align:right">Original Wager: <span>$</span>10.00</td>
		</tr>
		<tr>
			<td colspan="5" style="text-align:right">Total Returned: <span>$</span>173.11</td>
		</tr>
	</tbody>
</table>

<p>The maximum payout for any parlay wager is <span>$</span>1 million. If the calculated total exceeds that amount, the actual total returned will be <span>$</span>1 million.</p>

<p>Write a program that will calculate the total amount returned for a series of parlay wagers. <br>
For each parlay wager, your program is to print the total amount returned in dollars and cents on a single line starting in the first column without embedded or trailing whitespace. Print the leading dollar sign and insert commas at the millions and thousands positions as needed.</p>

### 입력 

 <p>Input will consist of several wagers. The first line of input to your program will contain the total number of parlay wagers as a single positive integer.</p>

<p>Each wager that follows will be represented by a series of lines.</p>

<p>The first line of each parlay wager contains the initial bet and the count of individual wagers as integers separated from each other by a single space.</p>

<p>The following lines represent the individual wagers, one per line. Each individual wager is given as its money line followed by a single space and the result of the wager (“Win”, “Tie”, or “Loss”).</p>

### 출력 

 <p>For each parlay wager, your program should print one line containing the total amount returned in dollars and cents. Print the leading dollar sign and insert commas at the millions and thousands positions as needed.</p>

<p> </p>

