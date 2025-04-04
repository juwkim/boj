# [Silver I] 버섯 농장 - 27737 

[문제 링크](https://www.acmicpc.net/problem/27737) 

### 성능 요약

메모리: 110852 KB, 시간: 108 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 4일 14:28:36

### 문제 설명

<p>농부 해강이는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>×</mo><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N \times N$</span></mjx-container> 칸으로 이루어진 나무판에서 버섯 농사를 짓는다. 나무판은 버섯이 자랄 수 있는 칸과 없는 칸으로 이루어져 있다.</p>

<p>해강이는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>개의 버섯 포자를 가지고 있다. 버섯 포자는 버섯이 자랄 수 있는 칸에만 심을 수 있다.</p>

<p>각 버섯 포자는 포자가 심어진 칸을 포함해 최대 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>개의 연결된 (버섯이 자랄 수 있는) 칸에 버섯을 자라게 한다. 이때 연결된 칸은 상하좌우로 적어도 한 변을 공유하는 칸들의 집합이라고 정의한다.</p>

<p>또한 한 칸에 버섯 포자를 여러 개 겹쳐서 심을 수 있으며, 만약 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container>개의 버섯 포자를 겹쳐 심으면 포자가 심어진 칸을 포함해 최대 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>×</mo><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x \times K$</span></mjx-container>개의 연결된 (버섯이 자랄 수 있는) 칸에 버섯이 자란다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/d6cf1de2-1a5a-4185-bb45-bc37eb4e4476/-/preview/" style="height: 454px; width: 700px;"></p>

<p style="text-align: center;"><그림 1> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K = 4$</span></mjx-container>일 때 버섯이 자라는 모습이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/239f2d7b-7589-4f72-9088-993428eb234a/-/preview/" style="height: 443px; width: 700px;"></p>

<p style="text-align: center;"><그림 2> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K = 10$</span></mjx-container>일 때 버섯이 자라는 모습이다.</p>

<p>해강이는 버섯 포자를 심을 때 최소 개수로만 심으려고 한다. 해강이가 농사가 가능할지 판단하고, 농사가 가능하다면 남은 버섯 포자의 개수를 출력하시오.</p>

<p><strong>버섯 포자를 하나라도 사용하고</strong> 버섯이 자랄 수 있는 모든 칸에 버섯이 전부 자랐을 때 농사가 가능하다고 정의한다.</p>

### 입력 

 <p>첫 번째 줄에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>가 공백으로 구분되어 주어진다.</p>

<p>두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에 나무판의 각 칸의 상태가 공백으로 구분되어 주어진다.</p>

<p>버섯이 자랄 수 <strong>있는</strong> 칸은 <span style="color:#e74c3c;"><code>0</code></span>, 버섯이 자랄 수 <strong>없는</strong> 칸은 <span style="color:#e74c3c;"><code>1</code></span>로 주어진다. </p>

### 출력 

 <p>만약 버섯 농사가 불가능하면 <span style="color:#e74c3c;"><code>IMPOSSIBLE</code></span>을 출력한다.</p>

<p>버섯 농사가 가능하다면, <span style="color:#e74c3c;"><code>POSSIBLE</code></span>을 출력하고 다음 줄에 남은 버섯 포자의 개수를 출력한다.</p>

