# [Silver V] 🐜 기적의 매매법 🐜 - 20546 

[문제 링크](https://www.acmicpc.net/problem/20546) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation)

### 문제 설명

<p>"오늘도 호재만 있게 해주세요. 버핏-"</p>

<p>2년차 개미 준현이는 오늘도 버핏신에게 기도를 올린다. 장기 투자를 지향하는 준현이는 한 번 산 주식은 절대 팔지 않는다. 2099년이 되어도 주식을 팔지 않을 것이다. 주식 매수 후 오로지 기도만 하기 때문에 이를 BNP 전략이라고 한다. BNP는 Buy and Pray의 약자이다. 준현이는 주식을 살 수 있다면 무조건 최대한 많이 산다. 준현이는 욕심쟁이이기 때문에, 주식을 살 수 있다면 가능한 만큼 즉시 매수한다. 다음은 준현이가 현금 100원으로 A기업의 주식을 사는 경우이다.</p>

<table border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 500px;">
	<thead>
		<tr>
			<th scope="row"> </th>
			<th scope="col">1일</th>
			<th scope="col">2일</th>
			<th scope="col">3일</th>
			<th scope="col">4일</th>
			<th scope="col">5일</th>
			<th scope="col">6일</th>
			<th scope="col">7일</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row">현금</th>
			<td style="text-align: center;">100</td>
			<td style="text-align: center;">20</td>
			<td style="text-align: center;">20</td>
			<td style="text-align: center;">6</td>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">0</td>
		</tr>
		<tr>
			<th scope="row">주가</th>
			<td style="text-align: center;">40</td>
			<td style="text-align: center;">33</td>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">12</td>
			<td style="text-align: center;">50</td>
		</tr>
		<tr>
			<th scope="row">매수 가능 주식 수</th>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">0</td>
		</tr>
		<tr>
			<th scope="row">매수여부</th>
			<td style="text-align: center;">O</td>
			<td style="text-align: center;">X</td>
			<td style="text-align: center;">O</td>
			<td style="text-align: center;">O</td>
			<td style="text-align: center;">X</td>
			<td style="text-align: center;">X</td>
			<td style="text-align: center;">X</td>
		</tr>
		<tr>
			<th scope="row">남은 현금</th>
			<td style="text-align: center;">20</td>
			<td style="text-align: center;">20</td>
			<td style="text-align: center;">6</td>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">0</td>
		</tr>
		<tr>
			<th scope="row">보유 주식 수</th>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">7</td>
		</tr>
	</tbody>
</table>

<p>"주식은 타이밍이지!"</p>

<p>반면, 성민이는 오늘도 주식 거래 프로그램을 실행한다. 모니터 8개에서 뿜어져 나오는 화려한 주식 차트가 성민이를 감싼다. 성민이는 주식이 타이밍 싸움이라 생각한다. 전형적인 단기 투자자로 생각하면 오산이다. 성민이만의 전략이 있기 때문이다. 이른바 33 매매법으로, 그 방법은 다음의 세 가지 룰로 이루어져있다.</p>

<ul>
	<li>모든 거래는 전량 매수와 전량 매도로 이루어진다. 현재 가지고 있는 현금이 100원이고 주가가 11원이라면 99원어치의 주식을 매수하는 것이다. 단, 현금이 100원 있고 주가가 101원이라면 주식을 살 수 없다. 성민이는 빚을 내서 주식을 하지는 않는다.</li>
	<li>3일 연속 가격이 전일 대비 상승하는 주식은 다음날 무조건 가격이 하락한다고 가정한다. 따라서 현재 소유한 주식의 가격이 3일째 상승한다면, 전량 매도한다. 전일과 오늘의 주가가 동일하다면 가격이 상승한 것이 아니다.</li>
	<li>3일 연속 가격이 전일 대비 하락하는 주식은 다음날 무조건 가격이 상승한다고 가정한다. 따라서 이러한 경향이 나타나면 즉시 주식을 전량 매수한다. 전일과 오늘의 주가가 동일하다면 가격이 하락한 것이 아니다.</li>
</ul>

<p>준현이와 성민이는 각자의 매매법 중 어떤 방법이 더 수익률이 높은지 겨뤄보기로 했다. 오로지 MachineDuck이라는 기업의 주식만 거래가 가능하며, 내기 기간은 2021년 1월 1일부터 2021년 1월 14일까지이다. 준현이와 성민이에게 주어진 현금은 동일하다. 세기의 대결이기 때문에 이 기간에는 매일 주식 거래가 가능하다. 2021년 1월 14일에 더 많은 자산을 보유한 사람이 승리한다. 1월 14일의 자산은 (현금 + 1월 14일의 주가 × 주식 수)로 계산한다.</p>

<p>우리는 2021년 1월 1일부터 2021년 1월 14일까지의 주식 가격을 미리 알고 있다. 준현이와 성민이 중 누가 더 높은 수익률을 낼지 맞혀보자!</p>

### 입력 

 <p>첫 번째 줄에 준현이와 성민이에게 주어진 현금이 주어진다.</p>

<p>두 번째 줄에 2021년 1월 1일부터 2021년 1월 14일까지의 MachineDuck 주가가 공백을 두고 차례대로 주어진다. 모든 입력은 1000 이하의 양의 정수이다.</p>

### 출력 

 <p>1월 14일 기준 준현이의 자산이 더 크다면 "BNP"를, 성민이의 자산이 더 크다면 "TIMING"을 출력한다.</p>

<p>둘의 자산이 같다면 "SAMESAME"을 출력한다. 모든 결과 따옴표를 제외하고 출력한다.</p>

