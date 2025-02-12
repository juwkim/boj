# [Silver V] It Is Cold - 9354 

[문제 링크](https://www.acmicpc.net/problem/9354) 

### 성능 요약

메모리: 110736 KB, 시간: 112 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 2월 13일 04:59:40

### 문제 설명

<p>Dr. Ziad Najem is known as the godfather of the ACPC. When the regional contest was held in Alexandria, Egypt, the weather was very cold. What surprised Dr. Ziad was that in the contest hall the fans were turned on! Dr. Ziad immediately needed to know, for each team, the speed in which the air reached that team.</p>

<p>Each team has N fans placed on a straight line to its right. Each fan i has a speed Si and direction Ci. Directions are either towards the team "T" or away from the team "A".</p>

<p>If two fans face the same direction, their speeds add up in the same direction. E.g.</p>

<table border="1" cellpadding="1" cellspacing="1" style="width:500px">
	<tbody>
		<tr>
			<td style="text-align: center;"> </td>
			<td style="text-align: center;">Fan 1</td>
			<td style="text-align: center;">Fan 2</td>
			<td style="text-align: center;">Result</td>
		</tr>
		<tr>
			<td style="text-align: center;">Direction</td>
			<td style="text-align: center;">T</td>
			<td style="text-align: center;">T</td>
			<td style="text-align: center;">T</td>
		</tr>
		<tr>
			<td style="text-align: center;">Speed</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">2+4 = 6</td>
		</tr>
	</tbody>
</table>

<p>If two fans face each other, their speeds cancel out. E.g.</p>

<div>
<table border="1" cellpadding="1" cellspacing="1" style="width:500px">
	<tbody>
		<tr>
			<td style="text-align: center;"> </td>
			<td style="text-align: center;">Fan 1</td>
			<td style="text-align: center;">Fan 2</td>
			<td style="text-align: center;">Result</td>
		</tr>
		<tr>
			<td style="text-align: center;">Direction</td>
			<td style="text-align: center;">A</td>
			<td style="text-align: center;">T</td>
			<td style="text-align: center;">T</td>
		</tr>
		<tr>
			<td style="text-align: center;">Speed</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">4-2 = 2</td>
		</tr>
	</tbody>
</table>
</div>

### 입력 

 <p>The first line of input contains an integer T, the number of teams. For each team, you will be given an integer N, the number of fans. Two lines follow; the first line contains N space separated integers S<sub>i</sub>, the speed of the air produced by fan i (0 ≤ i < N). The second line contains N characters that describe the direction of the fans C<sub>i </sub>(as described above).</p>

<p>T ≤ 100<br>
0 < N ≤ 1000<br>
0 ≤ Si ≤ 1000000000</p>

### 출력 

 <p>There should be T lines, containing a single integer S each that represents the speed in which the air reaches the team. S is zero if no air reaches the team.</p>

