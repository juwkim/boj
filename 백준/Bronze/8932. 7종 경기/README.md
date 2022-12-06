# [Bronze III] 7종 경기 - 8932 

[문제 링크](https://www.acmicpc.net/problem/8932) 

### 성능 요약

메모리: 28776 KB, 시간: 1028 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>민혁이는 한국에서 열리는 7종 경기 대회에 참가한다. 7종 경기는 육상의 필드 경기와 트랙 경기 7 종목으로 이루어져 있다. (100미터 허들, 높이뛰기, 포환던지기, 200미터 달리기, 멀리뛰기, 창던지기, 800미터 달리기) 민혁이의 각 종목의 기록이 주어졌을 때, 기록을 점수로 환산해서 총점을 구하는 프로그램을 작성하시오.</p>

<p>7종 경기의 총점은 각 종목의 점수의 합이다. 각 종목의 점수는 다음과 같은 식을 이용해서 구할 수 있다.</p>

<ul>
	<li>트랙 경기: \(Score=\left\lfloor A \times (B-P)^{C} \right\rfloor\)</li>
	<li>필드 경기: \(Score=\left\lfloor A \times (P-B)^{C} \right\rfloor\)</li>
</ul>

<p>A, B, C는 아래 표에 적혀져 있는 상수이다. P는 선수의 성적으로 단위는 아래에 나와있다.</p>

<p>모든 종목의 점수는 정수이다.</p>

<table class="table table-bordered" style="width:65%">
	<thead>
		<tr>
			<th style="width:15%">종목</th>
			<th style="width:10%">A</th>
			<th style="width:10%">B</th>
			<th style="width:10%">C</th>
			<th style="width:10%">P</th>
			<th style="width:10%">종류</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>100미터 허들</td>
			<td>9.23076</td>
			<td>26.7</td>
			<td>1.835</td>
			<td>sec</td>
			<td>트랙</td>
		</tr>
		<tr>
			<td>높이뛰기</td>
			<td>1.84523</td>
			<td>75</td>
			<td>1.348</td>
			<td>cm</td>
			<td>필드</td>
		</tr>
		<tr>
			<td>포환던지기</td>
			<td>56.0211</td>
			<td>1.5</td>
			<td>1.05</td>
			<td>m</td>
			<td>필드</td>
		</tr>
		<tr>
			<td>200미터 달리기</td>
			<td>4.99087</td>
			<td>42.5</td>
			<td>1.81</td>
			<td>sec</td>
			<td>트랙</td>
		</tr>
		<tr>
			<td>멀리뛰기</td>
			<td>0.188807</td>
			<td>210</td>
			<td>1.41</td>
			<td>cm</td>
			<td>필드</td>
		</tr>
		<tr>
			<td>창던지기</td>
			<td>15.9803</td>
			<td>3.8</td>
			<td>1.04</td>
			<td>m</td>
			<td>필드</td>
		</tr>
		<tr>
			<td>800미터 달리기</td>
			<td>0.11193</td>
			<td>254</td>
			<td>1.88</td>
			<td>sec</td>
			<td>트랙</td>
		</tr>
	</tbody>
</table>

<p>모든 필드 경기는 B ≤ P, 트랙 경기는 P ≤ B를 만족한다.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다. (1 ≤ T ≤ 1000) 각 테스트 케이스는 일곱 개의 정수로 이루어져 있다. 이 정수는 민혁이의 종목별 기록이다. 순서는 100미터 허들, 높이뛰기, 포환던지기, 200미터 달리기, 멀리뛰기, 창던지기, 800미터 달리기이다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서, 민혁이의 총점을 출력한다.</p>

