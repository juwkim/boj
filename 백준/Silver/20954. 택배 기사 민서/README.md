# [Silver II] 택배 기사 민서 - 20954 

[문제 링크](https://www.acmicpc.net/problem/20954) 

### 성능 요약

메모리: 118932 KB, 시간: 152 ms

### 분류

구현, 수학

### 제출 일자

2024년 12월 11일 05:22:16

### 문제 설명

<p>민서는 택배 기사이다. 활기차게 월요일을 맞은 민서는 놀라 자빠질 수밖에 없었다. 코로나19 사태로 인하여 비대면 활동이 확산되면서 택배 물량이 급증하였기 때문이다. 민서에게 배정된 택배는 거의 무한개에 가까웠고 이대로라면 과로사를 피할 수 없을 것이다. 민서는 건강을 위하여 오늘까지만 열심히 일하고 내일부터는 택배 기사 대신 교수를 하기로 결심하였다.</p>

<p>민서가 사는 동네는 수직선으로 표현할 수 있으며, 민서는 수직선의 원점, 즉 수직선의 좌표 0에서 배달을 준비하고 있다. 각 택배에는 0번부터 차례대로 번호가 매겨져 있으며, 택배의 목적지는 수직선 위의 좌표로 표현할 수 있다. i번 택배의 목적지 D<sub>i</sub>는 다음과 같다.</p>

<p><mjx-container class="MathJax" jax="CHTML" display="true" style="font-size: 109%; position: relative;"> <mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D437 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-msup><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-script style="vertical-align: 0.413em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msup><mjx-mi class="mjx-i"><mjx-c class="mjx-cD7"></mjx-c></mjx-mi><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.413em;"><mjx-texatom size="s" texclass="ORD"><mjx-mrow><mjx-mo class="mjx-sop"><mjx-c class="mjx-c230A TEX-S1"></mjx-c></mjx-mo><mjx-mfrac><mjx-frac><mjx-num><mjx-nstrut></mjx-nstrut><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-num><mjx-dbox><mjx-dtable><mjx-line></mjx-line><mjx-row><mjx-den><mjx-dstrut></mjx-dstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mo class="mjx-sop"><mjx-c class="mjx-c230B TEX-S1"></mjx-c></mjx-mo></mjx-mrow></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mi>D</mi><mi>i</mi></msub><mo>=</mo><mo stretchy="false">(</mo><mo>−</mo><mn>1</mn><msup><mo stretchy="false">)</mo><mi>i</mi></msup><mi>×</mi><msup><mn>2</mn><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="INNER"><mo data-mjx-texclass="OPEN">⌊</mo><mfrac><mi>i</mi><mn>2</mn></mfrac><mo data-mjx-texclass="CLOSE">⌋</mo></mrow></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$$D_i=(-1)^i×2^{\left\lfloor\frac{i}{2}\right\rfloor}$$</span> </mjx-container></p>

<p>여기서 ⌊x⌋는 바닥 함수로, x보다 크지 않은, 즉 x 이하의 정수 중 가장 큰 정수를 의미한다. 예를 들어, 3번 택배의 목적지 D<sub>3</sub>은 다음과 같이 계산할 수 있다.</p>

<p><mjx-container class="MathJax" jax="CHTML" display="true" style="font-size: 109%; position: relative;"> <mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D437 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-msup><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-script style="vertical-align: 0.413em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-script></mjx-msup><mjx-mi class="mjx-i"><mjx-c class="mjx-cD7"></mjx-c></mjx-mi><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.413em;"><mjx-texatom size="s" texclass="ORD"><mjx-mrow><mjx-mo class="mjx-sop"><mjx-c class="mjx-c230A TEX-S1"></mjx-c></mjx-mo><mjx-mfrac><mjx-frac><mjx-num><mjx-nstrut></mjx-nstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-num><mjx-dbox><mjx-dtable><mjx-line></mjx-line><mjx-row><mjx-den><mjx-dstrut></mjx-dstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mo class="mjx-sop"><mjx-c class="mjx-c230B TEX-S1"></mjx-c></mjx-mo></mjx-mrow></mjx-texatom></mjx-script></mjx-msup><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mi>D</mi><mn>3</mn></msub><mo>=</mo><mo stretchy="false">(</mo><mo>−</mo><mn>1</mn><msup><mo stretchy="false">)</mo><mn>3</mn></msup><mi>×</mi><msup><mn>2</mn><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="INNER"><mo data-mjx-texclass="OPEN">⌊</mo><mfrac><mn>3</mn><mn>2</mn></mfrac><mo data-mjx-texclass="CLOSE">⌋</mo></mrow></mrow></msup><mo>=</mo><mo>−</mo><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$$D_3=(-1)^3×2^{\left\lfloor\frac{3}{2}\right\rfloor}=-2$$</span> </mjx-container></p>

<p>민서는 수직선의 원점에서 출발하여 0번 택배부터 차례대로 배달을 시작한다. 택배를 배달하기 위해서는 현재 위치로부터 택배의 목적지까지 이동해야 한다. 민서는 현재 좌표에서 인접한 좌표로, 즉 현재 좌표에서 1만큼 차이 나는 좌표로 이동할 수 있으며, 이때 1초의 시간이 소요된다. 또한 민서는 항상 최단 경로로 이동한다.</p>

<p>민서는 온종일 쉬지도 않고 열심히 택배를 배달하고 있다. 문득 민서는 수직선 위의 특정 좌표 x에 처음으로 도달하는 시점이 언제인지 궁금해졌다.</p>

<p>좌표 x가 주어졌을 때, 해당 좌표에 처음으로 도달하는 시점을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 번째 줄에 테스트 케이스의 수 T가 주어진다.</p>

<p>이후 T개의 줄에 걸쳐 정수 좌표 x가 한 줄에 하나씩 주어진다.</p>

### 출력 

 <p>각 테스트 케이스에 대한 답을 한 줄에 하나씩 출력한다.</p>

