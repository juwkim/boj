# [Silver IV] PSU Campuses - 9609 

[문제 링크](https://www.acmicpc.net/problem/9609) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

Empty

### 문제 설명

<p>Prince of Songkla University or PSU has 5 campuses in the South of Thailand. These campuses are Hatyai(H), Pattani(P), Suratthani(S), Phuket(K) and Trang(T). The distances between these campuses are shown in the table below. </p>

<table class="table table-bordered" style="width:60%">
	<thead>
		<tr>
			<th>Campuses</th>
			<th>Distance (km)</th>
			<th>Campuses</th>
			<th>Distance (km)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Hatyai – Pattani</td>
			<td>103</td>
			<td>Pattani - Phuket</td>
			<td>577</td>
		</tr>
		<tr>
			<td>Hatyai – Suratthani</td>
			<td>329</td>
			<td>Pattani - Trang</td>
			<td>260</td>
		</tr>
		<tr>
			<td>Hatyai – Phuket</td>
			<td>466</td>
			<td>Suratthani - Phuket</td>
			<td>287</td>
		</tr>
		<tr>
			<td>Hatyai – Trang</td>
			<td>148</td>
			<td>Suratthani - Trang</td>
			<td>226</td>
		</tr>
		<tr>
			<td>Pattani – Suratthani</td>
			<td>408</td>
			<td>Phuket - Trang</td>
			<td>312</td>
		</tr>
	</tbody>
</table>

<p>When the President of PSU goes on mission in different campuses, he or she may want to know the total distance of the mission. The mission always starts from Hatyai campus and when the mission ends the president will always go back directly to Hatyai campus. </p>

<p>Given a list of campuses of a mission, your task is to write a program to calculate the total distance of the mission. </p>

### 입력 

 <p>The first line contains an integer n (1 ≤ n ≤ 100) which determines the number of missions. The following n lines contain a description of each mission. A mission is described by a string comprising only characters H, P, S, K and T which refer to PSU campuses. The president visits the campuses in the order indicated in that string. Since Hatyai campus is always the starting point and also the end point of a mission, we will not mention H at the beginning or the end of the string. However, H can be an intermediate campus in a mission. A mission string may contain at most 10 characters. </p>

### 출력 

 <p>For each mission (mission<sub>i</sub>), print out in a line, “Case i: ” followed by the total distance (km), exactly as shown in the sample output. </p>

