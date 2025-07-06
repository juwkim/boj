# [Silver I] 수라도 - 34043 

[문제 링크](https://www.acmicpc.net/problem/34043) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

애드 혹, 해 구성하기

### 제출 일자

2025년 7월 7일 06:24:19

### 문제 설명

<p>수라도의 호반우들은 무한한 정삼각형 격자에 서로 다른 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 색을 사용하여 각 색마다 정확히 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container>개의 정삼각형을 칠하는 게 가능한지 판단해야 한다. 이때 같은 색으로 색칠된 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container>개의 정삼각형이 반드시 아래의 두 그림 중 하나와 같은 형태를 이루어야 한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/85703242-02a2-4e23-9f04-1118b97fc242/-/preview/" style="width: 100px; height: 88px;"><img alt="" src="https://upload.acmicpc.net/3bcd68cf-2e5f-4f6f-90d7-08d469d272af/-/preview/" style="height: 88px; width: 100px;"></p>

<p>추가로, 임의의 색칠된 정삼각형 칸에서 시작해 인접한 면을 통하여 색칠된 정삼각형 칸으로만 이동해 모든 색칠된 정삼각형 칸에 도달할 수 있어야 한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/744833e8-93f0-4392-9e4f-a5ce84676aa8/-/preview/" style="height: 177px; width: 200px;"><img alt="" src="https://upload.acmicpc.net/cabf9005-8554-46d7-9e57-aaaeae56c25e/-/preview/" style="height: 177px; width: 200px;"></p>

<p style="text-align: center;"><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>=</mo><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N = 2$</span></mjx-container>일 때 왼쪽은 조건을 만족하는 예시, 오른쪽은 만족하지 않는 예시이다.</p>

<p>호반우를 도와 수라도에서 깨달음을 얻어보자.</p>

### 입력 

 <p>첫째 줄에 서로 다른 색의 개수인 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \leq N \leq 100\,000)$</span> </mjx-container></p>

### 출력 

 <p>첫째 줄에 모든 색을 사용하여 조건을 만족하도록 격자 위의 정삼각형들을 칠할 수 있다면 <span style="color:#e74c3c;"><code>YES</code></span>를, 그렇지 않다면 <span style="color:#e74c3c;"><code>NO</code></span>를 출력한다.</p>

