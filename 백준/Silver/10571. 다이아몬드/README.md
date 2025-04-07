# [Silver I] 다이아몬드 - 10571 

[문제 링크](https://www.acmicpc.net/problem/10571) 

### 성능 요약

메모리: 110760 KB, 시간: 104 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 4월 7일 12:03:15

### 문제 설명

<p style="text-align:center"><img alt="" src="https://www.acmicpc.net/upload/images2/diamond.png" style="height:72px; width:210px"></p>

<p>어떠한 다이아몬드의 가치는 그 다이아몬드의 중량인 캐럿과 선명도에 의해서 결정됩니다. 즉, 작지만 선명한 다이아몬드가 크고 선명하지 않은 다이아몬드보다는 가치가 높습니다. 다이아몬드의 선명도는 0.0-10.0의 스캐일로 표현할 수 있는데, 0.0의 선명도는 완벽하게 선명한 다이아몬드를 나타내고 10.0은 가장 결함이 많은 다이아몬드를 나타냅니다.</p>

<p>N개의 다이아몬드의 중량 w<sub>i</sub>와 선명도 c<sub>i</sub>의 정보가 주어졌을때, 이 중에서 다이아몬드의 중량이 높아지고, 선명도 값이 낮아지는 부분열 중 최장의 것의 길이를 구하세요. 예를들어 주어진 정보가 다음과 같다면</p>

<table class="table table-bordered" style="width: 30%;">
	<tbody>
		<tr>
			<td>w<sub>i</sub></td>
			<td>c<sub>i</sub></td>
		</tr>
		<tr>
			<td>1.5</td>
			<td>9.0</td>
		</tr>
		<tr>
			<td>2.0</td>
			<td>2.0</td>
		</tr>
		<tr>
			<td>2.5</td>
			<td>6.0</td>
		</tr>
		<tr>
			<td>3.0</td>
			<td>5.0</td>
		</tr>
		<tr>
			<td>4.0</td>
			<td>2.0</td>
		</tr>
		<tr>
			<td>10.0</td>
			<td>5.5</td>
		</tr>
	</tbody>
</table>

<p>다이아몬드 중량이 높아지고, 선명도 값이 낮아지는 부분열 중 길이가 최장인 것은 다음과 같습니다.</p>

<table class="table table-bordered" style="width: 30%;">
	<tbody>
		<tr>
			<td>1.5</td>
			<td>9.0</td>
		</tr>
		<tr>
			<td>2.5</td>
			<td>6.0</td>
		</tr>
		<tr>
			<td>3.0</td>
			<td>5.0</td>
		</tr>
		<tr>
			<td>4.0</td>
			<td>2.0</td>
		</tr>
	</tbody>
</table>

<p>왜냐하면 표에 나와있는 부분열을 보면, 무게는 증가하고, 선명도의 값은 감소하기 때문입니다.</p>

### 입력 

 <p>테스트 케이스의 개수 T가 주어지고 (1≤T≤100) 각 테스트 케이스마다 다이아몬드의 정보의 개수 N (1≤N≤200)이 주어집니다. 그리고 N개의 줄에 걸쳐서 다이아몬드의 무게와 선명도 w<sub>i, </sub>c<sub>i</sub>가 주어집니다 (0≤w<sub>i,</sub>c<sub>i</sub>≤100).</p>

### 출력 

 <p>각 테스트 케이스마다 다이아몬드의 가치가 높아지는 부분열중 최장의 것의 길이를 구하세요.</p>

