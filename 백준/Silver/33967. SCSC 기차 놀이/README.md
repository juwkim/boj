# [Silver V] SCSC 기차 놀이 - 33967 

[문제 링크](https://www.acmicpc.net/problem/33967) 

### 성능 요약

메모리: 111092 KB, 시간: 124 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 5월 21일 10:53:31

### 문제 설명

<p>기차를 좋아하는 SCSC 부원 연호는 S와 C 모양을 한 줄로 이어 기차를 만들어 보고자 한다. 연호가 기차를 만드는 데에 사용할 S와 C 모양 차량들은 다음 그림과 같다.</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/7baf692e-0143-4932-8a0e-429d2ee87902/-/preview/"></td>
			<td style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/88010666-2324-4546-a197-dc52812b341c/-/preview/"></td>
			<td style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/4270bd15-822d-4e55-8139-d113542138d4/-/preview/"></td>
			<td style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/55c222a0-eeb3-4ecb-989a-9e70f953a1f6/-/preview/"></td>
		</tr>
		<tr>
			<td style="text-align: center;">그림1. S-5 모양 차량</td>
			<td style="text-align: center;">그림2. C-[ 모양 차량</td>
			<td style="text-align: center;">그림3. S-2 모양 차량</td>
			<td style="text-align: center;">그림4. C-] 모양 차량</td>
		</tr>
	</tbody>
</table>

<p>연호가 차량을 일렬로 빈틈없이 연결할 때 차량의 벽으로 구분되는 각각의 공간을 기차간(汽車間)이라고 한다. 이때 연호는 자기가 만든 SCSC 기차가 총 몇 개의 기차간을 가지게 될지 궁금해졌다. 연호의 SCSC 기차 설계도가 주어질 때, SCSC 기차가 총 몇 개의 기차간을 가지게 될지 구해보자!</p>

### 입력 

 <p>첫째 줄에 SCSC 기차 설계도에 포함된 차량의 수를 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>2</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>200</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(2 \le N \le 200\,000)$</span> </mjx-container></p>

<p>둘째 줄에 문자열 <span style="color:#e74c3c;"><code>2</code></span>,<span style="color:#e74c3c;"> <code>5</code></span>, <span style="color:#e74c3c;"><code>[</code></span>, <span style="color:#e74c3c;"><code>]</code></span>로 이루어진 연호의 SCSC 기차 설계도가 주어진다.</p>

<p>설계도의 처음은 반드시 <span style="color:#e74c3c;"><code>[</code></span>로 시작하고, 끝은 반드시 <span style="color:#e74c3c;"><code>]</code></span>로 끝난다.</p>

### 출력 

 <p>첫째 줄에 연호의 설계도에 따라 만들어질 SCSC 기차의 기차간 총 개수를 출력한다.</p>

