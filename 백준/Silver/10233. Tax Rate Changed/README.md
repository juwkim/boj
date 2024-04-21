# [Silver III] Tax Rate Changed - 10233 

[문제 링크](https://www.acmicpc.net/problem/10233) 

### 성능 요약

메모리: 110608 KB, 시간: 300 ms

### 분류

사칙연산, 브루트포스 알고리즘, 구현, 수학

### 제출 일자

2024년 4월 21일 12:38:17

### 문제 설명

<p>VAT (value-added tax) is a tax imposed at a certain rate proportional to the sale price.</p>

<p>Our store uses the following rules to calculate the after-tax prices.</p>

<ul>
	<li>When the VAT rate is <i>x</i>%, for an item with the before-tax price of <i>p</i> yen, its after-tax price of the item is <i>p</i> (100+<i>x</i>) / 100 yen, fractions rounded off.</li>
	<li>The total after-tax price of multiple items paid at once is the sum of after-tax prices of the items.</li>
</ul>

<p>The VAT rate is changed quite often. Our accountant has become aware that "different pairs of items that had the same total after-tax price may have different total after-tax prices after VAT rate changes." For example, when the VAT rate rises from 5% to 8%, a pair of items that had the total after-tax prices of 105 yen before can now have after-tax prices either of 107, 108, or 109 yen, as shown in the table below.</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<th>Before-tax prices of two items</th>
			<th>After-tax price with 5% VAT</th>
			<th>After-tax price with 8% VAT</th>
		</tr>
		<tr>
			<td>20, 80</td>
			<td>21 + 84 = 105</td>
			<td>21 + 86 = 107</td>
		</tr>
		<tr>
			<td>2, 99</td>
			<td>2 + 103 = 105</td>
			<td>2 + 106 = 108</td>
		</tr>
		<tr>
			<td>13, 88</td>
			<td>13 + 92 = 105</td>
			<td>14 + 95 = 109</td>
		</tr>
	</tbody>
</table>

<p>Our accountant is examining effects of VAT-rate changes on after-tax prices. You are asked to write a program that calculates the possible maximum total after-tax price of two items with the new VAT rate, knowing their total after-tax price before the VAT rate change.</p>

### 입력 

 <p>The input consists of multiple datasets. Each dataset is in one line, which consists of three integers <i>x</i>, <i>y</i>, and <i>s</i> separated by a space. <i>x</i> is the VAT rate in percent <i>before</i> the VAT-rate change, <i>y</i> is the VAT rate in percent <i>after</i> the VAT-rate change, and <i>s</i> is the sum of after-tax prices of two items <i>before</i> the VAT-rate change. For these integers, 0 < <i>x</i> < 100, 0 < <i>y</i> < 100, 10 < <i>s</i> < 1000, and <i>x</i> ≠ <i>y</i> hold. For before-tax prices of items, all possibilities of 1 yen through <i>s</i>-1 yen should be considered.</p>

<p>The end of the input is specified by three zeros separated by a space.</p>

### 출력 

 <p>For each dataset, output in a line the possible maximum total after-tax price when the VAT rate is changed to <i>y</i>%.</p>

