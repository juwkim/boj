# [Bronze III] Lodê - 10312 

[문제 링크](https://www.acmicpc.net/problem/10312) 

### 성능 요약

메모리: 30840 KB, 시간: 156 ms

### 분류

수학(math), 정수론(number_theory)

### 문제 설명

<p>In 1999, there were another three contests at the Czech Technical University: faculty round (FEL++), CTU Open, and Central Europe Regional Contest. The enthusiasm of the “founding fathers” had decreased a little bit and there was no wonder. They had been organizing two or three competitions a year for a period of five years. What had once been fun turned into hard work. Fortunately, many new organizers arose from the former contestants, so the tradition could go on.</p>

<p>The problem Lodē was added to the 1999 contest at the very last moment and it was intended to be an easy one. Now you may find out yourselves how difficult or easy it was.</p>

<hr>
<p>Juliet reads an interesting sci-fi book. In one chapter, the main character needs to solve a problem of maximizing the utilization of cargo spaceships. The ships transport valuable items that have the form of D-dimensional mesh with the size of 3 nodes in each dimension. The nodes are formed by balls of the same weight. The connections between balls are so light that their weight is negligible compared to the weight of balls. This means that the weight of any item is determined solely by the number of its nodes. On the other hand, the value of such an item is equal to the number of nodes plus the number of connections.</p>

<table class="table" style="width:100%">
	<tbody>
		<tr>
			<td style="width: 33%; text-align: center;"><img alt="" src="" style="height:112px; width:120px"></td>
			<td style="width: 33%; text-align: center;"><img alt="" src="" style="height:112px; width:151px"></td>
			<td style="width: 34%; text-align: center;"><img alt="" src="" style="height:112px; width:125px"></td>
		</tr>
		<tr>
			<td style="text-align: center;">zero dimension</td>
			<td style="text-align: center;">first dimension</td>
			<td style="text-align: center;">second dimension</td>
		</tr>
		<tr>
			<td style="text-align: center;">weight = 1</td>
			<td style="text-align: center;">weight = 3</td>
			<td style="text-align: center;">weight = 9</td>
		</tr>
		<tr>
			<td style="text-align: center;">price = 1</td>
			<td style="text-align: center;">price = 5</td>
			<td style="text-align: center;">price = 21</td>
		</tr>
	</tbody>
</table>

<p>Each spaceships has a limited tonnage and we want to maximize the total value of items that may be stored in the ship without exceeding the tonnage. Your task is to decide what items of what dimension should be loaded to maximize their total value, providing that we have an unlimited supply of items of all dimensions.</p>

### 입력 

 <p>The first line of the input contains the number of test cases N. Each test case then consists of a single line containing one positive integer number K < 10 000 000 giving the ship cargo capacity.</p>

### 출력 

 <p>For each test case, print one line containing space-separated non-negative numbers X<sub>m</sub> X<sub>m−1</sub> ... X<sub>1</sub> X<sub>0</sub>, where X<sub>m</sub> > 0 and X<sub>i</sub> (0 ≤ i ≤ m) is the number of items of the i-th dimension that we need to store to maximize their total value.</p>

