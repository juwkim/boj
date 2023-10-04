# [Silver IV] Avoiding Financial Nightmare - 7801 

[문제 링크](https://www.acmicpc.net/problem/7801) 

### 성능 요약

메모리: 114328 KB, 시간: 116 ms

### 분류

이분 탐색

### 문제 설명

<p>Nowadays, getting a loan from a bank or financial company has become very popular, either it’s for commercial or personal purposes. If you are a well-managed on your expenses, having a loan from a bank or using credit cards for your expenses could be a good help, otherwise it could be your worst financial nightmare. By considering the risks of paying bills, our professor has decided to get a loan to buy a new house on a pleasant city in Indonesia.</p>

<p>Our professor has considered 3 main variables that will affect his monthly bills:</p>

<ul>
	<li>Principal, the remaining amount of the loan</li>
	<li>Period, the number of months to pay off the loan</li>
	<li>Rate, the monthly interest rate</li>
</ul>

<p>To help their customer, bank or financial company normally offers a fixed amount payment system. Every month the customer should pay a fixed amount of money which consists of two kinds of payment:</p>

<ol>
	<li>
	<p>Interest Payment.</p>

	<pre>Interest Payment = Rate x Remaining Principal.</pre>

	<p>The amount of interest payment should be rounded up to the higher nearest integer.</p>
	</li>
	<li>
	<p>Principal Payment.</p>

	<pre>Principal Payment = Total Payment - Interest Payment.</pre>

	<p>The previous Principal is to be subtracted with the current Principal Payment to get the current Principal.</p>
	</li>
</ol>

<p>The total monthly payment should be calculated in some way so that the total monthly payment to be paid spread evenly each month, and at the end of the period the remaining Principal is zero or a negative amount nearest to zero (if it’s not possible to reach zero).</p>

<p>For example, let the professor get a loan in the amount of <span>$</span>42,000 with 5% interest rate per month that should be paid in 5 months.</p>

<table class="table table-bordered" style="width:60%">
	<thead>
		<tr>
			<th rowspan="2">Term</th>
			<th colspan="3">Payment</th>
			<th rowspan="2">Principal</th>
		</tr>
		<tr>
			<th>Total</th>
			<th>Interest Payment</th>
			<th>Principal Payment</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>-</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
			<td><span>$</span>42,000</td>
		</tr>
		<tr>
			<td>1</td>
			<td><span>$</span>9,701</td>
			<td><span>$</span>2,100</td>
			<td><span>$</span>7,601</td>
			<td><span>$</span>34,399</td>
		</tr>
		<tr>
			<td>2</td>
			<td><span>$</span>9,701</td>
			<td><span>$</span>1,720</td>
			<td><span>$</span>7,981</td>
			<td><span>$</span>26,418</td>
		</tr>
		<tr>
			<td>3</td>
			<td><span>$</span>9,701</td>
			<td><span>$</span>1,321</td>
			<td><span>$</span>8,380</td>
			<td><span>$</span>18,038</td>
		</tr>
		<tr>
			<td>4</td>
			<td><span>$</span>9,701</td>
			<td><span>$</span>902</td>
			<td><span>$</span>8,799</td>
			<td><span>$</span>9,239</td>
		</tr>
		<tr>
			<td>5</td>
			<td><span>$</span>9,701</td>
			<td><span>$</span>462</td>
			<td><span>$</span>9,239</td>
			<td><span>$</span>0</td>
		</tr>
	</tbody>
</table>

<p>1st term: He should pay <span>$</span>9,701 (<span>$</span>2,100 for interest payment, and <span>$</span>7,601 for principal payment)</p>

<ul>
	<li>Interest Payment    : 5% x <span>$</span>42,000    = <span>$</span>2,100</li>
	<li>Principal Payment    : <span>$</span>9,701 - <span>$</span>2,100    = <span>$</span>7,601</li>
	<li>Current Principal    : <span>$</span>42,000 - <span>$</span>7,601    = <span>$</span>34,399</li>
</ul>

<p>2nd term: He pays <span>$</span>9,701 (<span>$</span>1,702 for interest payment, and <span>$</span>7,981 for principal payment)</p>

<ul>
	<li>Interest Payment    : 5% x <span>$</span>34,399    = <span>$</span>1,720</li>
	<li>Principal Payment    : <span>$</span>9,701 - <span>$</span>1,720    = <span>$</span>6,902</li>
	<li>Current Principal    : <span>$</span>34,399 - <span>$</span>6,902    = <span>$</span>26,418,      and so on.</li>
</ul>

<p>Unfortunately, the professor is terrible with financial stuffs. We don’t want him to end up broke, do we? So, let us help him with the calculation on how much money he should spend to pay his monthly bills on the loan. In that way, the professor will be able to buy his new house and who knows that someday we might be invited to visit his house in return to our help.</p>

### 입력 

 <p>The input contains multiple cases. Each case consists of three integers respectively, N (1 ≤ N ≤ 100,000,000) the initial principal, M (1 ≤ M ≤ 100) the period, and R (0 ≤ R ≤ 100) the percent rate.</p>

### 출력 

 <p>For each case, you should output in a single line the total monthly payment should be made to satisfy the condition.</p>

