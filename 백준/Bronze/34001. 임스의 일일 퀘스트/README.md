# [Bronze III] 임스의 일일 퀘스트 - 34001 

[문제 링크](https://www.acmicpc.net/problem/34001) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

구현, 많은 조건 분기

### 제출 일자

2025년 5월 26일 00:32:00

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/ab071a9e-3505-4951-ab0b-b71263bf46d5/-/preview/"></p>

<p>메이플스토리의 스토리를 즐기는 임스는 스토리를 모두 클리어한 이후 심볼을 지급하는 일일 퀘스트만 골라서 클리어하기 시작했습니다.</p>

<p>임스가 해당 지역의 스토리 퀘스트를 완료하면 몬스터를 잡을 수 있습니다.</p>

<p>심볼을 지급하는 일일 퀘스트의 경우, 아케인리버는 200, 210, 220, 225, 230, 235 레벨에 추가되고, 그란디스의 경우, 260, 265, 270, 275, 280, 285, 290 레벨에 추가됩니다.</p>

<p>일일 퀘스트는 기본적으로 500마리를 잡아야하고, 감소 레벨에 도달하면 해당 지역의 일일 퀘스트를 클리어하기 위하여 잡아야 하는 몬스터의 마릿수가 200 감소합니다.</p>

<p>임스의 레벨 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$L$</span></mjx-container>이 주어질 때, 아케인 리버, 그란디스 일일 퀘스트에서 임스가 잡아야 하는 퀘스트별 몬스터 수를 출력하세요.</p>

<p>일일 퀘스트를 모두 클리어해도 임스의 레벨은 오르지 않습니다.</p>

<table class="table table-bordered td-center table-center-50">
	<tbody>
		<tr>
			<td>지역명</td>
			<td>퀘스트 레벨</td>
			<td>1차 감소 레벨</td>
			<td>2차 감소 레벨</td>
		</tr>
		<tr>
			<td>소멸의 여로</td>
			<td>200</td>
			<td>210</td>
			<td>220</td>
		</tr>
		<tr>
			<td>츄츄 아일랜드</td>
			<td>210</td>
			<td>220</td>
			<td>225</td>
		</tr>
		<tr>
			<td>꿈의 도시 레헬른</td>
			<td>220</td>
			<td>225</td>
			<td>230</td>
		</tr>
		<tr>
			<td>신비의 숲 아르카나</td>
			<td>225</td>
			<td>230</td>
			<td>235</td>
		</tr>
		<tr>
			<td>기억의 늪 모라스</td>
			<td>230</td>
			<td>235</td>
			<td>245</td>
		</tr>
		<tr>
			<td>태초의 바다 에스페라</td>
			<td>235</td>
			<td>245</td>
			<td>250</td>
		</tr>
	</tbody>
</table>

<table class="table table-bordered td-center table-center-50">
	<tbody>
		<tr>
			<td>지역명</td>
			<td>퀘스트 레벨</td>
			<td>1차 감소 레벨</td>
			<td>2차 감소 레벨</td>
		</tr>
		<tr>
			<td>세르니움</td>
			<td>260</td>
			<td>265</td>
			<td>270</td>
		</tr>
		<tr>
			<td>호텔 아르크스</td>
			<td>265</td>
			<td>270</td>
			<td>275</td>
		</tr>
		<tr>
			<td>오디움</td>
			<td>270</td>
			<td>275</td>
			<td>280</td>
		</tr>
		<tr>
			<td>도원경</td>
			<td>275</td>
			<td>280</td>
			<td>285</td>
		</tr>
		<tr>
			<td>아르테리아</td>
			<td>280</td>
			<td>285</td>
			<td>290</td>
		</tr>
		<tr>
			<td>카르시온</td>
			<td>285</td>
			<td>290</td>
			<td>295</td>
		</tr>
		<tr>
			<td>탈라하트</td>
			<td>290</td>
			<td>295</td>
			<td>300</td>
		</tr>
	</tbody>
</table>

<p>해당 표는 아케인 리버와 그란디스 지역의 일일 퀘스트에 대한 정보를 나타내는 표입니다.</p>

### 입력 

 <p>임스의 레벨 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$L$</span></mjx-container>이 주어집니다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D43F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>200</mn><mo>≤</mo><mi>L</mi><mo>≤</mo><mn>300</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(200 \le L \le 300)$</span> </mjx-container></p>

### 출력 

 <p>첫 번째 줄에는 아케인 리버 일일 퀘스트를 클리어하는데 필요한 몬스터 수를 공백을 기준으로 구분하여 퀘스트 레벨 오름차순으로 출력하세요.</p>

<p>두 번째 줄에는 그란디스 일일 퀘스트를 클리어하는데 필요한 몬스터 수를 공백을 기준으로 구분하여 퀘스트 레벨 오름차순으로 출력하세요.</p>

<p>임스의 레벨이 부족한 경우, 잡을 수 없으므로 0을 출력합니다.</p>

