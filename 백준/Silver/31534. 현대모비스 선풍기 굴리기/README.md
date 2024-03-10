# [Silver IV] 현대모비스 선풍기 굴리기 - 31534 

[문제 링크](https://www.acmicpc.net/problem/31534) 

### 성능 요약

메모리: 108080 KB, 시간: 136 ms

### 분류

기하학, 3차원 기하학, 수학, 피타고라스 정리

### 제출 일자

2024년 3월 11일 08:32:15

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://u.acmicpc.net/246d332b-f9c8-4d92-85ce-3ebf53955840/hyundaimobis_CI.png" style="height: 138px; width: 400px;"></p>

<blockquote>
<p>현대모비스는 자율주행, 전동화, 커넥티비티 등 미래 모빌리티 기술의 핵심인 소프트웨어에 집중하고 있다. 대표적으로 CAN(Controller Area Network) 프로토콜로 대표되는 차량 네트워크 분야, 센서 등 여러 ECU(Electronic Contorl Unit) 및 MCU(Micro Controller Unit) 기반의 임베디드 분야, 자율주행 등의 AI 분야, OS와 분리된 보안 영역인 TEE(Trusted Execution Environment) 등 자동차에서 사용되는 보안 분야까지 다양한 소프트웨어 분야에 초점을 두고 있다.</p>

<p>현대모비스는 이러한 소프트웨어 인재를 양성하고 기회를 주기 위해 소프트웨어와 관련한 다양한 대회를 개최하고 프로그램을 진행했다. 특히, 매년 대학(원)생 및 일반인을 대상으로 ”현대모비스 알고리즘 경진대회”와 ”현대모비스 모빌리티 SW 해커톤” 등 다양한 대회를 개최하고 있으며, 우수한 소프트웨어 인재들에게 여러 기회와 혜택을 통해 지원하고 있다.</p>
</blockquote>

<p>지난해 현대모비스 알고리즘 경진대회에 참가한 재우는 기념품 중 하나로 다음과 같이 생긴 휴대용 선풍기를 받았다. 선풍기는 바람이 나오는 부분과 선풍기를 받치는 부분으로 이루어져 있다. 재우는 심심할 때 선풍기 받침대를 바닥에 굴리며 놀다가 문득 새삼 선풍기 받침이 굴러갈 때 자취의 넓이가 궁금해져서 다음과 같은 문제를 만들었다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/ada20997-b623-4e9e-ab82-100032948235/-/preview/" style="height: 302px; width: 400px;"></p>

<p>두 밑변의 길이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b$</span></mjx-container>이며 다른 변 중 하나가 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c210E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$h$</span></mjx-container>로 두 밑변과 수직을 이루는 사다리꼴을 생각하자. 이때, 이 변을 <strong>높이변</strong>이라고 하자. 만약 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>=</mo><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a=0$</span></mjx-container>이라면, 사다리꼴이 아닌 삼각형이라고 생각할 수 있다.</p>

<p>이 사다리꼴을 <strong>높이변</strong>을 축으로 하여 회전시키면 오른쪽과 같은 입체 도형 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>가 하나 나온다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/af16b27d-48b5-4848-a19f-d4ff59ad8bc1/-/preview/" style="height: 258px; width: 400px;"></p>

<p>이제 이 도형의 옆면을 바닥에 놓고 아래와 같이 무한히 굴린다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/115bee84-d302-4686-8279-ed12f8808286/-/crop/892x827/2773,1278/-/preview/" style="height: 371px; width: 400px;"></p>

<p>도형의 옆면이 만드는 자취가 남게 될 것이다. 이 자취의 넓이를 구해보자.</p>

<p>이 도형을 굴리는 동안 넘어지지 않으며, 미끄러지지 않는다고 가정한다.</p>

### 입력 

 <p>첫 번째 줄에 문제에서 주어진 세 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c210E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$h$</span></mjx-container>가 공백으로 구분되어 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c3B"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>0</mn><mo>≤</mo><mi>a</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo>;</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(0\le a\le 1\,000;$</span></mjx-container> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c210E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>b</mi><mo>,</mo><mi>h</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\le b,h\le 1\,000)$</span> </mjx-container></p>

### 출력 

 <p>주어진 사다리꼴로 만든 회전체 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>를 굴렸을 때 자취의 넓이를 출력한다.</p>

<p>단, 정답과의 절대오차 또는 상대오차가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mo>−</mo><mn>6</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^{-6}$</span></mjx-container> 이하이면 정답으로 인정되며, 자취가 유한하지 않다면 <span style="color:#e74c3c;"><code>-1</code></span>을 출력한다.</p>

