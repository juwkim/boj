# [Bronze III] Good times - 6812 

[문제 링크](https://www.acmicpc.net/problem/6812) 

### 성능 요약

메모리: 30840 KB, 시간: 64 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>A mobile cell service provider in Ottawa broadcasts an automated time standard to its mobile users that reflects the local time at the user’s actual location in Canada. This ensures that text messages have a valid local time attached to them.</p>

<p>For example, when it is 1420 in Ottawa on Tuesday February 24, 2009 (specified using military, 24 hour format), the times across the country are shown in the table below:</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<th>Pacific Time</th>
			<td>Victoria, BC Tuesday 2/24/2009 1120 PST</td>
		</tr>
		<tr>
			<th>Mountain Time</th>
			<td>Edmonton, AB Tuesday 2/24/2009 1220 MST</td>
		</tr>
		<tr>
			<th>Central Time</th>
			<td>Winnipeg, MB Tuesday 2/24/2009 1320 CST</td>
		</tr>
		<tr>
			<th>Eastern Time</th>
			<td>Toronto, ON Tuesday 2/24/2009 1420 EST</td>
		</tr>
		<tr>
			<th>Atlantic Time</th>
			<td>Halifax, NS Tuesday 2/24/2009 1520 AST</td>
		</tr>
		<tr>
			<th>Newfoundland Time</th>
			<td>St. John’s, NL Tuesday 2/24/2009 1550 Newfoundland ST</td>
		</tr>
	</tbody>
</table>

<p>Write a program that accepts the time in Ottawa in 24 hour format and outputs the local time in each of the cities listed above including Ottawa. You should assume that the input time will be valid (i.e., an integer between 0 and 2359 with the last two digits being between 00 and 59).</p>

<p>You should note that 2359 is one minute to midnight, midnight is 0, and 13 minutes after midnight is 13. You do not need to print leading zeros, and input will not contain any extra leading zeros.</p>

### 입력 

 Empty

### 출력 

 Empty

