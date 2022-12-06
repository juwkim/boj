# [Bronze II] Elevators - 20571 

[문제 링크](https://www.acmicpc.net/problem/20571) 

### 성능 요약

메모리: 30888 KB, 시간: 68 ms

### 분류

많은 조건 분기(case_work)

### 문제 설명

<p>Whenever a new building is built, it must comply with all the relevant building regulations. In particular, there are rules governing the number of elevators a building must have depending on its number of floors and zoning district.</p>

<p>If a building has only one floor, it doesn't need any elevators; otherwise, it needs more elevators the more floors it has, and the exact number depends on its zoning district. The following tables describe the number of elevators necessary for a building in each of the residential, commercial, and industrial zoning districts.</p>

<table class="table table-bordered table-center-60 th-center td-center">
	<thead>
		<tr>
			<th colspan="2">Residential</th>
			<th colspan="2">Commercial</th>
			<th colspan="2">Industrial</th>
		</tr>
		<tr>
			<th>Floors</th>
			<th>Elevators</th>
			<th>Floors</th>
			<th>Elevators</th>
			<th>Floors</th>
			<th>Elevators</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>$1$</td>
			<td>$0$</td>
			<td>$1$</td>
			<td>$0$</td>
			<td>$1$</td>
			<td>$0$</td>
		</tr>
		<tr>
			<td>$2-5$</td>
			<td>$1$</td>
			<td>$2-7$</td>
			<td>$1$</td>
			<td>$2-4$</td>
			<td>$1$</td>
		</tr>
		<tr>
			<td>$6-10$</td>
			<td>$2$</td>
			<td>$8-14$</td>
			<td>$2$</td>
			<td>$5-8$</td>
			<td>$2$</td>
		</tr>
		<tr>
			<td>$11-15$</td>
			<td>$3$</td>
			<td>$15-20$</td>
			<td>$3$</td>
			<td>$9-12$</td>
			<td>$3$</td>
		</tr>
		<tr>
			<td>$16-20$</td>
			<td>$4$</td>
			<td> </td>
			<td> </td>
			<td>$13-16$</td>
			<td>$4$</td>
		</tr>
		<tr>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td>$17-20$</td>
			<td>$5$</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;">Table 1: Elevator requirements by zone</p>

<p>You are given the zoning district of a new building and how many floors it has. How many elevators does it need?</p>

### 입력 

 <p>The only line of input contains a string representing the zoning district of the building ("residential", "commercial", or "industrial"), followed by a space and an integer $N$ ($1 \leq N \leq 20$), the number of floors the building has.</p>

### 출력 

 <p>Output a single integer: the number of elevators the building must have.</p>

