# [Bronze II] Wak Sani Satay - 15838 

[문제 링크](https://www.acmicpc.net/problem/15838) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Wak Sani Satay is a humble stall located in Kajang and has been around since 1969. Many like Wak Sani’s satay because the meat is juicy and tender, served with creamy and sweet kuah kacang, alongside with nasi impit, cucumber and onion slices.</p>

<p>Wak Sani usually calculates his net profit at the end of the week. The net profit is calculated by subtracting the cost from the gross profit. He can get 85 sticks of satay from 1 kg meat. The price for 3 types of satay are shown in Table 1. The price for nasi impit is RM0.80 each while cucumber and onion slices are free of charge.</p>

<p>The cost for making satay for each meat type in shown in Table 2. The cost of spices to marinate satay for every kilogram of meat is RM8.00 and the cost for each nasi impit is RM0.20 each.</p>

<table class="table table-bordered" style="width: 30%;">
	<thead>
		<tr>
			<th>Satay</th>
			<th>Price per stick</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Chicken</td>
			<td>RM0.80</td>
		</tr>
		<tr>
			<td>Beef</td>
			<td>RM1.00</td>
		</tr>
		<tr>
			<td>Lamb</td>
			<td>RM1.20</td>
		</tr>
	</tbody>
</table>

<p>Table 1</p>

<table class="table table-bordered" style="width: 30%;">
	<thead>
		<tr>
			<th>Meat</th>
			<th>Price per kg</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Chicken</td>
			<td>RM7.50</td>
		</tr>
		<tr>
			<td>Beef</td>
			<td>RM24.00</td>
		</tr>
		<tr>
			<td>Lamb</td>
			<td>RM32.00</td>
		</tr>
	</tbody>
</table>

<p>Table 2</p>

<p>Write a program to find the weekly net profit. </p>

### 입력 

 <p>The input consists of a few sets of test cases. The first line for each data case is an integer N (1 ≤ N ≤ 7), which represents the number of days the stall is opened to customers for a week. It is followed by N lines of data, each line represents the sales (in sticks) of chicken satay, beef satay, lamb satay and nasi impit per day. Input is terminated by a test case where N is 0.</p>

### 출력 

 <p>For each test case, output a line in the format "Case #x: RM" where x is the case number (starting from 1), follow by the calculated net profit in Malaysian currency format as shown in the sample output.</p>

