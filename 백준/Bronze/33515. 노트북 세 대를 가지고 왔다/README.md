# [Bronze V] 노트북 세 대를 가지고 왔다 - 33515 

[문제 링크](https://www.acmicpc.net/problem/33515) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

구현, 수학

### 제출 일자

2025년 2월 27일 00:20:29

### 문제 설명

<p>형진이와 다른 두 팀원은 실수로 세 대의 노트북을 대회장에 가져오고 말았다. 하지만 대회장에선 한 대의 노트북만 사용할 수 있다. 세 사람 모두 자신의 노트북을 대회에서 사용하고 싶어 했고, 이에 “백준 온라인 저지(BOJ) 1001번 문제를 가장 먼저 푸는 사람”의 노트북을 사용하기로 내기를 걸었다.</p>

<ul>
	<li>세 명 중 백준 1001번 문제를 가장 먼저 푼 사람의 노트북을 사용한다.</li>
	<li>풀이 시간이 가장 짧은 사람이 여러 명인 경우, 그들 중 형진이가 포함된다면 형진이의 노트북을 사용한다.</li>
</ul>

<p>다른 두 팀원이 백준 1001번 문제를 푸는 데 걸린 시간(초 단위)이 주어질 때, 형진이 자신의 노트북으로 대회에 참가하기 위해서는 다른 팀원들보다 같거나 더 빠른 시간 안에 문제를 풀어야 한다. 형진이의 노트북으로 대회에 참가하기 위해 형진이가 백준 1001번 문제를 푸는 데까지 필요한 최대 시간(초 단위)을 출력하시오.</p>

### 입력 

 <p>첫 번째 줄에 두 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.12em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.12em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mn>1</mn></msub><mo>,</mo><msub><mi>T</mi><mn>2</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T_1, T_2$</span></mjx-container>가 공백으로 구분되어 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msub space="4"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.12em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.12em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><msub><mi>T</mi><mn>1</mn></msub><mo>,</mo><msub><mi>T</mi><mn>2</mn></msub><mo>≤</mo><mn>10</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \le T_1, T_2 \le 10\,000)$</span> </mjx-container></p>

<p>이는 형진이를 제외한 두 팀원이 백준 1001번 문제를 푸는 데 걸린 시간을 초 단위로 나타낸 것이다.</p>

### 출력 

 <p>형진이의 노트북으로 대회에 참가하기 위해 형진이가 백준 1001번 문제를 푸는 데까지 필요한 최대 시간을 초 단위로 출력한다.</p>

