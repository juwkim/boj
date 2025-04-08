# [Silver I] 이변마작 9 - 33043 

[문제 링크](https://www.acmicpc.net/problem/33043) 

### 성능 요약

메모리: 122044 KB, 시간: 140 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 매개 변수 탐색, 슬라이딩 윈도우

### 제출 일자

2025년 4월 8일 12:39:49

### 문제 설명

<p>마작의 <strong>패</strong><sup>牌</sup>는 $34$종류의 패가 각각 $4$장씩, 총 $136$장으로 이루어져 있습니다. 패의 종류는 다음과 같습니다.</p>

<table class="table table-bordered">
	<thead>
		<tr>
			<th scope="col">모양</th>
			<th scope="col">이름</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/8b398835-395f-42b9-b41e-d987003f58c5/-/preview/" style="vertical-align: middle; height: 3em; display: inline-block;" class="no-responsive"></td>
			<td>만수패<sup>萬數牌</sup></td>
		</tr>
		<tr>
			<td colspan="2">패에 쓰여 있는 한자에 따라 <code><span style="color:#e74c3c;">1m</span></code>, <code><span style="color:#e74c3c;">2m</span></code>, <code><span style="color:#e74c3c;">3m</span></code>, <code><span style="color:#e74c3c;">4m</span></code>, <code><span style="color:#e74c3c;">5m</span></code>, <code><span style="color:#e74c3c;">6m</span></code>, <code><span style="color:#e74c3c;">7m</span></code>, <code><span style="color:#e74c3c;">8m</span></code>, <code><span style="color:#e74c3c;">9m</span></code>으로 총 $9$개의 종류가 있습니다.</td>
		</tr>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/2c88822d-aa08-4291-bd78-66d5249a6ad2/-/preview/" style="vertical-align: middle; height: 3em; display: inline-block;" class="no-responsive"></td>
			<td>통수패<sup>筒數牌</sup></td>
		</tr>
		<tr>
			<td colspan="2">패에 그려져 있는 바퀴의 개수에 따라 <code><span style="color:#e74c3c;">1p</span></code>, <code><span style="color:#e74c3c;">2p</span></code>, <code><span style="color:#e74c3c;">3p</span></code>, <code><span style="color:#e74c3c;">4p</span></code>, <code><span style="color:#e74c3c;">5p</span></code>, <code><span style="color:#e74c3c;">6p</span></code>, <code><span style="color:#e74c3c;">7p</span></code>, <code><span style="color:#e74c3c;">8p</span></code>, <code><span style="color:#e74c3c;">9p</span></code>로 총 $9$개의 종류가 있습니다.</td>
		</tr>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/4639715a-cda5-43ec-8468-1b3b935fe1b0/-/preview/" style="vertical-align: middle; height: 3em; display: inline-block;" class="no-responsive"></td>
			<td>삭수패<sup>索數牌</sup></td>
		</tr>
		<tr>
			<td colspan="2">패에 그려져 있는 대나무의 개수에 따라 <code><span style="color:#e74c3c;">1s</span></code>, <code><span style="color:#e74c3c;">2s</span></code>, <code><span style="color:#e74c3c;">3s</span></code>, <code><span style="color:#e74c3c;">4s</span></code>, <code><span style="color:#e74c3c;">5s</span></code>, <code><span style="color:#e74c3c;">6s</span></code>, <code><span style="color:#e74c3c;">7s</span></code>, <code><span style="color:#e74c3c;">8s</span></code>, <code><span style="color:#e74c3c;">9s</span></code>로 총 $9$개의 종류가 있습니다.</td>
		</tr>
		<tr>
			<td><img alt="" src="" style="vertical-align: middle; height: 3em; display: inline-block;" class="no-responsive"></td>
			<td>자패<sup>字牌</sup></td>
		</tr>
		<tr>
			<td colspan="2">패에 쓰여 있는 글자의 종류에 따라 <code><span style="color:#e74c3c;">1z</span></code>, <code><span style="color:#e74c3c;">2z</span></code>, <code><span style="color:#e74c3c;">3z</span></code>, <code><span style="color:#e74c3c;">4z</span></code>, <code><span style="color:#e74c3c;">5z</span></code>, <code><span style="color:#e74c3c;">6z</span></code>, <code><span style="color:#e74c3c;">7z</span></code>로 총 $7$개의 종류가 있습니다.</td>
		</tr>
	</tbody>
</table>

<p>여러분은 마작패의 모양을 익히기 위해 마작패를 섞어 하나씩 놓아보고 있었습니다. 그러던 도중 마작패의 종류가 바뀌는 <strong>이변</strong>이 일어났지만, 같은 종류의 패가 $4$장씩 존재한다는 사실을 익힌 여러분은 이변을 성공적으로 해결하였습니다.</p>

<p>이번에는 더 큰 이변이 일어나고 있습니다! 마작패의 종류가 바뀌는 이변에 더해서, 마작패가 늘어나 최대 $100\,000$장의 마작패가 쌓이게 되었습니다.</p>

<p>하지만 안타깝게도 여러분은 늘어난 마작패의 개수에서 이상함을 눈치채지 못했습니다. 그래서 이전처럼 같은 종류의 패가 $5$장 이상 나오는지 확인하여 이변을 해결해야 하는데, 여러분의 <strong>기억력</strong> $X$는 유한하기 때문에 가장 최근에 놓은 $X$장의 패만을 기억할 수 있습니다. 다시 말해, 여러분이 이변을 눈치채려면 어떤 패를 놓은 직후에 여러분의 기억 속에 있는 $X$장의 패 중에서 같은 종류의 패가 $5$장 이상 있어야 합니다.</p>

<p>이변을 눈치채기 위해 필요한 최소 기억력을 구해 주세요.</p>

### 입력 

 <p>첫 번째 줄에 늘어놓을 마작패의 개수 $N$이 주어집니다. $(1 \le N \le 100\,000)$</p>

<p>두 번째 줄에 $N$장의 마작패의 종류가 놓아볼 순서대로 공백으로 구분되어 주어집니다. 입력으로 주어지는 모든 마작패는 위에서 설명한 $34$종 중 하나입니다.</p>

### 출력 

 <p>이변을 눈치채기 위해 필요한 최소 기억력을 출력합니다. 아무리 기억력이 좋아도 이변을 눈치챌 수 없다면, 대신 <code><span style="color:#e74c3c;">-1</span></code>을 출력합니다.</p>

