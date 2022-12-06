# [Bronze II] Congestion Charging Zone - 16735 

[문제 링크](https://www.acmicpc.net/problem/16735) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>Tehran municipality has set up a new charging method for the Congestion Charging Zone (CCZ) which controls the passage of vehicles in Tehran’s high-congestion areas in the congestion period (CP) from 6:30 to 19:00. There are plate detection cameras inside or at the entrances of the CCZ recording vehicles seen at the CCZ. The table below summarizes the new charging method.</p>

<table class="table table-bordered" style="width: 60%;">
	<thead>
		<tr>
			<th style="text-align: center;">The first time seen in the CP</th>
			<th style="text-align: center;">The last time seen in the CP</th>
			<th style="text-align: center;">Charge</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align: center;">6:30 to 10:00</td>
			<td style="text-align: center;">6:30 to 16:00</td>
			<td style="text-align: center;">24000</td>
		</tr>
		<tr>
			<td style="text-align: center;">6:30 to 10:00</td>
			<td style="text-align: center;">16:01 to 19:00</td>
			<td style="text-align: center;">36000</td>
		</tr>
		<tr>
			<td style="text-align: center;">10:01 to 16:00</td>
			<td style="text-align: center;">10:01 to 16:00</td>
			<td style="text-align: center;">16800</td>
		</tr>
		<tr>
			<td style="text-align: center;">10:01 to 19:00</td>
			<td style="text-align: center;">16:01 to 19:00</td>
			<td style="text-align: center;">24000</td>
		</tr>
	</tbody>
</table>

<p>Note that the first time and the last time that a vehicle is seen in the CP may be the same. Write a program to compute the amount of charge of a given vehicle in a specific day.</p>

### 입력 

 <p>The first line of the input contains a positive integer n (1 ≤ n ≤ 100) where n is the number of records for a vehicle. Each of the next n lines contains a time at which the vehicle is seen. Each time is of form <hour>:<minute>, where <hour> is an integer number between 0 and 23 (inclusive) and <minute> is formatted as an exactly two-digit number between 00 and 59 (inclusive).</p>

### 출력 

 <p>Print the charge to be paid by the owner of the vehicle in the output.</p>

