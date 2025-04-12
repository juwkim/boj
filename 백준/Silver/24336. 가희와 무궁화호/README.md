# [Silver I] 가희와 무궁화호 - 24336 

[문제 링크](https://www.acmicpc.net/problem/24336) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 수학, 문자열

### 제출 일자

2025년 4월 13일 01:57:42

### 문제 설명

<p>아래 [표 1]은 경부선에서 무궁화호가 정차하는 역을 나타냅니다.</p>

<table class="table table-bordered table-center-70" style="width: 800px;">
	<tbody>
		<tr>
			<td style="text-align: center;">역 번호</td>
			<td style="text-align: center;">역 이름</td>
			<td style="text-align: center;">거리(km)</td>
			<td style="text-align: center;">필수 정차 여부</td>
			<td style="text-align: center;">역 번호</td>
			<td style="text-align: center;">역 이름</td>
			<td style="text-align: center;">거리(km)</td>
			<td style="text-align: center;">필수 정차 여부</td>
		</tr>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: right;">Seoul</td>
			<td style="text-align: right;">0.0</td>
			<td style="text-align: right;">Y</td>
			<td style="text-align: center;">23</td>
			<td style="text-align: right;">Chupungnyeong</td>
			<td style="text-align: right;">234.7</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">2</td>
			<td style="text-align: right;">Yeongdeungpo</td>
			<td style="text-align: right;">9.1</td>
			<td style="text-align: right;">Y</td>
			<td style="text-align: center;">24</td>
			<td style="text-align: right;">Gimcheon</td>
			<td style="text-align: right;">253.8</td>
			<td style="text-align: right;">Y</td>
		</tr>
		<tr>
			<td style="text-align: center;">3</td>
			<td style="text-align: right;">Anyang</td>
			<td style="text-align: right;">23.9</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">25</td>
			<td style="text-align: right;">Gumi</td>
			<td style="text-align: right;">276.7</td>
			<td style="text-align: right;">Y</td>
		</tr>
		<tr>
			<td style="text-align: center;">4</td>
			<td style="text-align: right;">Suwon</td>
			<td style="text-align: right;">41.5</td>
			<td style="text-align: right;">Y</td>
			<td style="text-align: center;">26</td>
			<td style="text-align: right;">Sagok</td>
			<td style="text-align: right;">281.3</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">5</td>
			<td style="text-align: right;">Osan</td>
			<td style="text-align: right;">56.5</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">27</td>
			<td style="text-align: right;">Yangmok</td>
			<td style="text-align: right;">289.5</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">6</td>
			<td style="text-align: right;">Seojeongri</td>
			<td style="text-align: right;">66.5</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">28</td>
			<td style="text-align: right;">Waegwan</td>
			<td style="text-align: right;">296.0</td>
			<td style="text-align: right;">Y</td>
		</tr>
		<tr>
			<td style="text-align: center;">7</td>
			<td style="text-align: right;">Pyeongtaek</td>
			<td style="text-align: right;">75.0</td>
			<td style="text-align: right;">Y</td>
			<td style="text-align: center;">29</td>
			<td style="text-align: right;">Sindong</td>
			<td style="text-align: right;">305.9</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">8</td>
			<td style="text-align: right;">Seonghwan</td>
			<td style="text-align: right;">84.4</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">30</td>
			<td style="text-align: right;">Daegu</td>
			<td style="text-align: right;">323.1</td>
			<td style="text-align: right;">Y</td>
		</tr>
		<tr>
			<td style="text-align: center;">9</td>
			<td style="text-align: right;">Cheonan</td>
			<td style="text-align: right;">96.6</td>
			<td style="text-align: right;">Y</td>
			<td style="text-align: center;">31</td>
			<td style="text-align: right;">Dongdaegu</td>
			<td style="text-align: right;">326.3</td>
			<td style="text-align: right;">Y</td>
		</tr>
		<tr>
			<td style="text-align: center;">10</td>
			<td style="text-align: right;">Sojeongni</td>
			<td style="text-align: right;">107.4</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">32</td>
			<td style="text-align: right;">Gyeongsan</td>
			<td style="text-align: right;">338.6</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">11</td>
			<td style="text-align: right;">Jeonui</td>
			<td style="text-align: right;">114.9</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">33</td>
			<td style="text-align: right;">Namseonghyeon</td>
			<td style="text-align: right;">353.1</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">12</td>
			<td style="text-align: right;">Jochiwon</td>
			<td style="text-align: right;">129.3</td>
			<td style="text-align: right;">Y</td>
			<td style="text-align: center;">34</td>
			<td style="text-align: right;">Cheongdo</td>
			<td style="text-align: right;">361.8</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">13</td>
			<td style="text-align: right;">Bugang</td>
			<td style="text-align: right;">139.8</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">35</td>
			<td style="text-align: right;">Sangdong</td>
			<td style="text-align: right;">372.2</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">14</td>
			<td style="text-align: right;">Sintanjin</td>
			<td style="text-align: right;">151.9</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">36</td>
			<td style="text-align: right;">Miryang</td>
			<td style="text-align: right;">381.6</td>
			<td style="text-align: right;">Y</td>
		</tr>
		<tr>
			<td style="text-align: center;">15</td>
			<td style="text-align: right;">Daejeon</td>
			<td style="text-align: right;">166.3</td>
			<td style="text-align: right;">Y</td>
			<td style="text-align: center;">37</td>
			<td style="text-align: right;">Samnangjin</td>
			<td style="text-align: right;">394.1</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">16</td>
			<td style="text-align: right;">Okcheon</td>
			<td style="text-align: right;">182.5</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">38</td>
			<td style="text-align: right;">Wondong</td>
			<td style="text-align: right;">403.2</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">17</td>
			<td style="text-align: right;">Iwon</td>
			<td style="text-align: right;">190.8</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">39</td>
			<td style="text-align: right;">Mulgeum</td>
			<td style="text-align: right;">412.4</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">18</td>
			<td style="text-align: right;">Jitan</td>
			<td style="text-align: right;">196.4</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">40</td>
			<td style="text-align: right;">Hwamyeong</td>
			<td style="text-align: right;">421.8</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">19</td>
			<td style="text-align: right;">Simcheon</td>
			<td style="text-align: right;">200.8</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">41</td>
			<td style="text-align: right;">Gupo</td>
			<td style="text-align: right;">425.2</td>
			<td style="text-align: right;">Y</td>
		</tr>
		<tr>
			<td style="text-align: center;">20</td>
			<td style="text-align: right;">Gakgye</td>
			<td style="text-align: right;">204.6</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;">42</td>
			<td style="text-align: right;">Sasang</td>
			<td style="text-align: right;">430.3</td>
			<td style="text-align: right;">N</td>
		</tr>
		<tr>
			<td style="text-align: center;">21</td>
			<td style="text-align: right;">Yeongdong</td>
			<td style="text-align: right;">211.6</td>
			<td style="text-align: right;">Y</td>
			<td style="text-align: center;">43</td>
			<td style="text-align: right;">Busan</td>
			<td style="text-align: right;">441.7</td>
			<td style="text-align: right;">Y</td>
		</tr>
		<tr>
			<td style="text-align: center;">22</td>
			<td style="text-align: right;">Hwanggan</td>
			<td style="text-align: right;">226.2</td>
			<td style="text-align: right;">N</td>
			<td style="text-align: center;"> </td>
			<td style="text-align: right;"> </td>
			<td style="text-align: right;"> </td>
			<td style="text-align: right;"> </td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 1] 경부선에서 무궁화호가 정차하는 역들</strong></p>

<p>[표 1]에서 역 이름과 각각의 역에 대응되는 역 번호가 있습니다. Seoul 역은 1번, Busan역은 43번입니다. 역 번호가 증가하는 방향은 하행이고, 역 번호가 감소하는 방향은 상행입니다. 예를 들어 1번 Seoul 역에서 31번 Dongdaegu 역으로 가는 경우, 역 번호가 증가하는 방향이므로 하행이고, 43번 Busan 역에서 15번 Daejeon 역으로 가는 방향은 역 번호가 감소하는 방향이므로 상행입니다.</p>

<p>[표 1]에서 거리란 <strong>Seoul<em> </em>역으로부터의 거리</strong>를 의미합니다. 예를 들어 22번 Hwanggan<em> </em>역은 1번 Seoul<em> </em>역으로부터 226.2km 떨어져 있습니다.</p>

<p>가희가 타고 있는 무궁화호가 <em>k</em>개의 역, <em>S<sub>1</sub></em>, <em>S<sub>2</sub></em>, ... , <em>S<sub>k </sub></em>순서대로 정차한다고 해 보겠습니다. 즉, x번째로 정차하는 역은 <em>S<sub>x</sub></em>입니다. 이때, 무궁화호는 <em>S<sub>1 </sub></em>역을 출발, <em>S<sub>2 </sub></em>역 도착, <em>S<sub>2 </sub></em>역 출발, ... , <em>S<sub>k </sub></em>역 도착순으로 수행하게 됩니다.</p>

<p>무궁화호가 시각 hh:mm에 역에 도착하거나 출발하는 것을 이벤트라고 정의하겠습니다. 가희가 타고 있는 무궁화호의 <em>x</em>번째 이벤트는 아래와 같이 정의됩니다.</p>

<ul>
	<li>x가 홀수일 때, 무궁화호가 <em>S<sub>⌊x/2⌋+1 </sub></em>번째 역을 출발</li>
	<li>x가 짝수일 때, 무궁화호가 <em>S<sub>⌊x/2⌋+1 </sub></em>번째 역에 도착</li>
	<li>⌊x⌋는 내림을 의미합니다.</li>
</ul>

<p>예를 들어, 가희가 탄 무궁화호가 아래 [표 2]와 같이 18개 역을 순서대로 정차한다고 하겠습니다.</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 600px;">
	<tbody>
		<tr>
			<td style="text-align: center;">순번</td>
			<td style="text-align: center;">역 이름</td>
			<td style="text-align: center;">순번</td>
			<td style="text-align: center;">역 이름</td>
		</tr>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: right;">Seoul</td>
			<td style="text-align: center;">10</td>
			<td style="text-align: right;">Gumi</td>
		</tr>
		<tr>
			<td style="text-align: center;">2</td>
			<td style="text-align: right;">Yeongdeungpo</td>
			<td style="text-align: center;">11</td>
			<td style="text-align: right;">Waegwan</td>
		</tr>
		<tr>
			<td style="text-align: center;">3</td>
			<td style="text-align: right;">Suwon</td>
			<td style="text-align: center;">12</td>
			<td style="text-align: right;">Daegu</td>
		</tr>
		<tr>
			<td style="text-align: center;">4</td>
			<td style="text-align: right;">Pyeongtaek</td>
			<td style="text-align: center;">13</td>
			<td style="text-align: right;">Dongdaegu</td>
		</tr>
		<tr>
			<td style="text-align: center;">5</td>
			<td style="text-align: right;">Cheonan</td>
			<td style="text-align: center;">14</td>
			<td style="text-align: right;">Gyeongsan</td>
		</tr>
		<tr>
			<td style="text-align: center;">6</td>
			<td style="text-align: right;">Jochiwon</td>
			<td style="text-align: center;">15</td>
			<td style="text-align: right;">Cheongdo</td>
		</tr>
		<tr>
			<td style="text-align: center;">7</td>
			<td style="text-align: right;">Daejeon</td>
			<td style="text-align: center;">16</td>
			<td style="text-align: right;">Miryang</td>
		</tr>
		<tr>
			<td style="text-align: center;">8</td>
			<td style="text-align: right;">Yeongdong</td>
			<td style="text-align: center;">17</td>
			<td style="text-align: right;">Gupo</td>
		</tr>
		<tr>
			<td style="text-align: center;">9</td>
			<td style="text-align: right;">Gimcheon</td>
			<td style="text-align: center;">18</td>
			<td style="text-align: right;">Busan</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 2] 가희가 탄 무궁화호가 Seoul 역에서 Busan 역까지 가는 동안 정차하는 역의 예</strong></p>

<p>가희가 탄 무궁화호는 18개 역에 정차하고, 이 중 3번째로 정차하는 역은 Suwon<em> </em>역입니다. 또한, 3번째로 발생하는 이벤트는 Yeongdeungpo<em> </em>역을 출발하는 것입니다.</p>

<p>가희가 타고 있는 무궁화호의 <em>x</em>번째 이벤트가 hh<sub>x</sub>:mm<sub>x</sub>에 발생했고, <em>x+1</em>번째 이벤트가 hh<sub>x+1</sub>:mm<sub>x+1</sub>에 발생했다고 해 보겠습니다.</p>

<ul>
	<li>시각<i> </i>hh<sub>x</sub>:mm<sub>x</sub>이 시각 hh<sub>x+1</sub>:mm<sub>x+1</sub>보다 앞선다면, <em>x</em>번째 이벤트와 <em>x+1</em>번째 이벤트는 같은 날에 발생합니다.</li>
	<li>그렇지 않으면 <strong><em>x</em>번째 이벤트가 발생한 날 다음날에 <em>x+1</em>번째 이벤트가 발생</strong>합니다.</li>
</ul>

<p>가희는 가희가 타고 있는 열차의 시간표를 보고, 특정 구간의 표정속도를 구하고 싶습니다. 가희를 도와주세요.</p>

<p>표정속도란, 일정 거리를 주행했을 경우 그 거리를 소요된 총 시간(주행 시간 + 정차 시간)으로 나누어 구한 속도를 의미합니다.</p>

### 입력 

 <p>첫 번째 줄에 가희가 타고 있는 열차의 정차역 개수 <em>N</em>과 가희의 질문 개수 <em>Q</em>가 주어집니다.</p>

<p>두 번째 줄부터 <em>N</em>개의 줄에 걸쳐서 정차역 이름과 도착 정보, 출발 정보가 공백을 구분으로 해서 주어집니다. <strong>열차가 정차하는 순서대로</strong> 주어지며, 첫 번째로 주어지는 역은 시발역, 마지막으로 주어지는 역은 종착역입니다.</p>

<p>도착 정보와 출발 정보는 아래와 같이 주어집니다.</p>

<ul>
	<li>시발역 (열차가 운행을 시작하는 역)에 대한 도착 정보는 -:-로 주어집니다.</li>
	<li>종착역 (열차가 운행을 종료하는 역)에 대한 출발 정보는 -:-로 주어집니다.</li>
	<li>그 외에는 출발 정보와 도착 정보는 <em>hh:mm</em> 형식으로 주어집니다. <em>hh:mm </em>형식은
	<ul>
		<li><em>hh</em>는 0 이상 23 이하의 정수, <em>mm</em>은 0 이상 59 이하의 정수로 주어집니다. 만약, 한 자리 숫자면 앞에 0을 붙입니다.</li>
	</ul>
	</li>
</ul>

<p><em>N+2</em>번째 줄부터 <em>Q</em>개의 줄에 걸쳐서 <em>station<sub>1</sub></em>과 <em>station<sub>2</sub></em>가 공백을 구분으로 해서 주어집니다.</p>

<p>이는 가희가 타고 간 열차의 운행 구간 <em>station<sub>1</sub></em> ~ <em>station<sub>2</sub></em>의 표정속도(km/h)를 구하라는 의미입니다.</p>

### 출력 

 <p><em>Q</em>개의 질문에 대한 답을 한 줄에 하나씩 출력해 주세요. <b>모범 답안과의 절대/상대 오차가 10<sup>-6</sup> 이하인 경우 정답으로 인정됩니다.</b></p>

