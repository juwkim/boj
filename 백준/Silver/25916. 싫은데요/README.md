# [Silver I] 싫은데요 - 25916 

[문제 링크](https://www.acmicpc.net/problem/25916) 

### 성능 요약

메모리: 191888 KB, 시간: 192 ms

### 분류

두 포인터

### 제출 일자

2024년 10월 20일 01:57:04

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/7047e2fb-861b-43df-9d5e-23b23001c102/-/preview/" style="width: 120px; height: 104px;"></p>

<p>싫은데요 햄스터는 콩쥐를 위해서 깨진 독을 자기 몸으로 막으려고 한다.</p>

<p>햄스터는 유체라 자기 몸을 그림처럼 늘릴 수 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/fc7b80e6-a1fb-4e6f-a5bd-9fbbef6e349d/-/preview/" style="width: 591px; height: 186px;"></p>

<p>또, 햄스터는 유체라 자기 몸을 아래 그림처럼 늘릴 수도 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/4f612b6a-fb6f-4315-ba9b-3682db7b5741/-/preview/" style="width: 591px; height: 180px;"></p>

<p>하지만 햄스터의 부피는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>으로 정해져 있기 때문에, 늘릴 수 있는 크기에는 한계가 있다.</p>

<p>독에 왼쪽부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 구멍이 일렬로 뚫려 있고, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 구멍의 크기 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A_i$</span></mjx-container>가 주어진다. 햄스터는 구멍을 막기 위해 정확히 그 크기만큼의 부피를 소모해야 한다.</p>

<p>싫은데요 햄스터는 콩쥐에게 최대한 도움이 되길 원하기 때문에 자기 부피를 가능한 한 많이 활용하길 원한다.</p>

<p>어떻게 막으면 햄스터가 원하는 방식으로 독을 막는지 구해서 알려주자.</p>

<p>아무리 햄스터가 유체라고 하지만 몸을 둘로 나눌 수는 없기 때문에 막는 모든 구멍은 연속되어야 한다.</p>

### 입력 

 <p>입력은 아래와 같이 주어진다.</p>

<div style="background:#eeeeee;border:1px solid #cccccc;padding:5px 10px;">
<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span> </mjx-container></p>

<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A_1$</span></mjx-container> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A_2$</span></mjx-container> ... <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>N</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A_N$</span> </mjx-container></p>
</div>

### 출력 

 <p>구멍을 막는 데에 활용할 수 있는 최대 부피를 출력한다.</p>

