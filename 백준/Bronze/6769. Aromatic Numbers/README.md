# [Bronze II] Aromatic Numbers - 6769 

[문제 링크](https://www.acmicpc.net/problem/6769) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>This question involves calculating the value of aromatic numbers which are a combination of Arabic digits and Roman numerals.</p>

<p>An aromatic number is of the form ARARAR . . . AR, where each A is an Arabic digit, and each R is a Roman numeral. Each pair AR contributes a value described below, and by adding or subtracting these values together we get the value of the entire aromatic number.</p>

<p>An Arabic digit A can be 0, 1, 2, 3, 4, 5, 6, 7, 8 or 9. A Roman numeral R is one of the seven letters I, V, X, L, C, D, or M. Each Roman numeral has a base value:</p>

<table class="table table-bordered" style="width:50%">
	<tbody>
		<tr>
			<td style="text-align:center">Symbol</td>
			<td style="text-align:center">I</td>
			<td style="text-align:center">V</td>
			<td style="text-align:center">X</td>
			<td style="text-align:center">L</td>
			<td style="text-align:center">C</td>
			<td style="text-align:center">D</td>
			<td style="text-align:center">M</td>
		</tr>
		<tr>
			<td style="text-align:center">Base value</td>
			<td style="text-align:center">1</td>
			<td style="text-align:center">5</td>
			<td style="text-align:center">10</td>
			<td style="text-align:center">50</td>
			<td style="text-align:center">100</td>
			<td style="text-align:center">500</td>
			<td style="text-align:center">1000</td>
		</tr>
	</tbody>
</table>

<p>The value of a pair AR is A times the base value of R. Normally, you add up the values of the pairs to get the overall value. However, wherever there are consecutive symbols ARA0R0 with R0 having a strictly bigger base value than R, the value of pair AR must be subtracted from the total, instead of being added.</p>

<p>For example, the number 3M1D2C has the value 3 ∗ 1000 + 1 ∗ 500 + 2 ∗ 100 = 3700 and 3X2I4X has the value 3 ∗ 10 − 2 ∗ 1 + 4 ∗ 10 = 68.</p>

<p>Write a program that computes the values of aromatic numbers.</p>

### 입력 

 <p>The input is a valid aromatic number consisting of between 2 and 20 symbols.</p>

### 출력 

 <p>The output is the decimal value of the given aromatic number.</p>

