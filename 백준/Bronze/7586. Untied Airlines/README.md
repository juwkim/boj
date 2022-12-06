# [Bronze I] Untied Airlines - 7586 

[문제 링크](https://www.acmicpc.net/problem/7586) 

### 성능 요약

메모리: 28776 KB, 시간: 180 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set)

### 문제 설명

<p>An airline called Untied, has had a series of bad press articles. The flying public are not impressed. So Untied has decided to award upgrades on future flights if a passenger suffers certain elements of poor service.</p>

<p>The poor service includes things like lost luggage, the stewardess swiping a passenger in the face as she reaches past them, or cancelling flights at short notice and not offering alternative flights in time for connections.</p>

<p>These elements of poor service are encoded and each is awarded points. If a passenger collects 200 such points on one flight, then their next flight is automatically upgraded. The poor service codes and associated points are shown in the table below.</p>

<p>Your job is to tell Untied for each flight, how many upgrades are awarded.</p>

### 입력 

 <p>Input consists of a series of flights, each beginning with a flight number. Input is terminated by a flight number which is just a single # - do not process this flight.</p>

<p>The flight number starts with UT, in upper case, followed by a sequence of up to 4 digits (eg: UT525). Each line after the flight number begins with a seat number (a 2 digit number followed by a single letter eg: 25H means seat H in row 25). The seat number is followed by a space and then one of the letter codes, always upper case. The seat letter will be in the range A to J.</p>

<p>The last seat number for a flight is 00A, which does not correspond to a valid seat. Do not process this seat.</p>

<p>Table of codes and points awarded</p>

<table class="table table-bordered" style="width:50%">
	<thead>
		<tr>
			<th>Service Problem</th>
			<th>Code</th>
			<th>Points</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Lost Luggage</td>
			<td>L</td>
			<td>120</td>
		</tr>
		<tr>
			<td>Struck by Stewardess</td>
			<td>S</td>
			<td>150</td>
		</tr>
		<tr>
			<td>Overbooked and bumped off flight after checking in</td>
			<td>B</td>
			<td>150</td>
		</tr>
		<tr>
			<td>Not greeted by name</td>
			<td>N</td>
			<td>40</td>
		</tr>
		<tr>
			<td>Not given seat in class paid for</td>
			<td>C</td>
			<td>160</td>
		</tr>
		<tr>
			<td>Drinks trolley ran into passenger</td>
			<td>D</td>
			<td>100</td>
		</tr>
		<tr>
			<td>Stewardess rude</td>
			<td>R</td>
			<td>100</td>
		</tr>
		<tr>
			<td>No space in overhead locker</td>
			<td>O</td>
			<td>100</td>
		</tr>
	</tbody>
</table>

### 출력 

 <p>Output consists of a single line for each flight in the input. It consists of the flight number, followed by a space, followed by the number of flight upgrades that have to be awarded. If the flight has no upgrades awarded, still display the flight number with a zero as the number of upgrades. </p>

