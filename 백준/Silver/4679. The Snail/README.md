# [Silver V] The Snail - 4679 

[문제 링크](https://www.acmicpc.net/problem/4679) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>A snail is at the bottom of a 6-foot well and wants to climb to the top. The snail can climb 3 feet while the sun is up, but slides down 1 foot at night while sleeping. The snail has a fatigue factor of 10%, which means that on each successive day the snail climbs 10% × 3 = 0.3 feet less than it did the previous day. (The distance lost to fatigue is always 10% of the first day’s climbing distance.) On what day does the snail leave the well, i.e., what is the first day during which the snail’s height exceeds 6 feet? (A day consists of a period of sunlight followed by a period of darkness.) As you can see from the following table, the snail leaves the well during the third day.</p>

<table class="table table-bordered">
	<thead>
		<tr>
			<th>Day</th>
			<th>Initial Height</th>
			<th>Distance Climbed</th>
			<th>Height After Climbing</th>
			<th>Height After Sliding</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>0′</td>
			<td>3′</td>
			<td>3′</td>
			<td>2′</td>
		</tr>
		<tr>
			<td>2</td>
			<td>2′</td>
			<td>2.7′</td>
			<td>4.7′</td>
			<td>3.7′</td>
		</tr>
		<tr>
			<td>3</td>
			<td>3.7′</td>
			<td>2.4′</td>
			<td>6.1′</td>
			<td>–</td>
		</tr>
	</tbody>
</table>

<p>Your job is to solve this problem in general. Depending on the parameters of the problem, the snail will eventually either leave the well or slide back to the bottom of the well. (In other words, the snail’s height will exceed the height of the well or become negative.) You must find out which happens first and on what day.</p>

### 입력 

 <p>The input file contains one or more test cases, each on a line by itself. Each line contains four integers H, U, D, and F, separated by a single space. If H = 0 it signals the end of the input; otherwise, all four numbers will be between 1 and 100, inclusive. H is the height of the well in feet, U is the distance in feet that the snail can climb during the day, D is the distance in feet that the snail slides down during the night, and F is the fatigue factor expressed as a percentage. The snail never climbs a negative distance. If the fatigue factor drops the snail’s climbing distance below zero, the snail does not climb at all that day. Regardless of how far the snail climbed, it always slides D feet at night.</p>

### 출력 

 <p>For each test case, output a line indicating whether the snail succeeded (left the well) or failed (slid back to the bottom) and on what day. Format the output exactly as shown in the example.</p>

