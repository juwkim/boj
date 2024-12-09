# [Silver II] 가위 가위 가위 - 30506 

[문제 링크](https://www.acmicpc.net/problem/30506) 

### 성능 요약

메모리: 13676 KB, 시간: 80 ms

### 분류

차분 공격

### 제출 일자

2024년 12월 10일 08:02:42

### 문제 설명

<p>세종이는 가위바위보 머신을 개발했다. 머신을 작동시키면 머신 가위바위보 대결을 즐길 수 있다. 한 번의 대결은 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container>번의 가위바위보 게임으로 이루어지며, 각 게임의 결과는 플레이어에게 공개되지 않는다. 대신 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container>번의 가위바위보 게임을 모두 진행한 후 플레이어는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container>번의 게임 중 이긴 게임의 수를 알 수 있다.</p>

<p>가위바위보의 꽃은 무작위성이지만, 난수 생성 알고리즘을 믿지 못하는 세종이는 아예 머신이 낼 손 모양의 순서를 모두 고정해 버렸다. 이를 본 영재는 세종이와 다음과 같은 내기를 하기로 했다.</p>

<ul>
	<li>영재와 머신이 대결한다. 처음에 영재는 반드시 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container>개의 가위를 낸다.</li>
	<li>매 대결이 끝날 때마다, 영재는 자신이 이긴 게임의 수를 확인한다. 그 뒤 영재는 낼 손 모양을 원하는 대로 바꾸고 다음 게임을 진행한다.</li>
	<li>영재는 첫 대결을 포함해 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>101</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$101$</span></mjx-container>번의 대결을 할 수 있다.</li>
	<li>대결 결과를 통해 영재가 머신의 손 모양이 무엇인지 맞히면 영재가, 맞히지 못하면 세종이가 내기에서 이긴다.</li>
</ul>

<p>영재가 내기에서 이길 수 있게 도와주자!</p>

### 입력 

 <p>첫째 줄에 영재가 머신과의 첫 대결에서 이긴 게임의 수를 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>가 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>0</mn><mo>≤</mo><mi>K</mi><mo>≤</mo><mn>100</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(0 \leq K \leq 100)$</span> </mjx-container></p>

### 출력 

 <p>다음을 표준 출력 스트림(<code>stdout</code>)으로 한 줄에 출력해 머신과의 대결을 진행할 수 있다.</p>

<ul>
	<li><code>? hand</code>: 영재의 손 모양을 <code>hand</code>로 바꾸고 다음 대결을 진행한다. <code>hand</code>는 <code>0</code>, <code>2</code>, <code>5</code>로만 이루어진 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container>자 길이의 문자열이어야 한다. <code>hand</code>의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 글자는 영재가 다음 대결의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 게임에서 낼 손 모양을 의미하며, <code>0</code>은 바위, <code>2</code>는 가위, <code>5</code>는 보를 의미한다.</li>
</ul>

<p>출력한 후에는 반드시 표준 출력 버퍼를 비워야 한다. 출력 버퍼를 비우지 않는 경우 예상 밖의 결과를 얻을 수 있음에 유의하라.</p>

<p>대결의 결과는 영재가 이긴 게임의 수를 의미하는 하나의 정수로 주어진다. 만약 머신의 손 모양을 알아낸 경우, <code>! machine_hand</code>를 출력하고 프로그램을 종료할 수 있다. <code>machine_hand</code>는 머신의 손 모양을 뜻하는 문자열로, <code>0</code>, <code>2</code>, <code>5</code>로만 이루어진 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container>자 길이의 문자열이어야 한다. <code>machine_hand</code>의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 글자는 머신이 한 대결의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 게임에서 내는 손 모양을 의미하며, <code>0</code>은 바위, <code>2</code>는 가위, <code>5</code>는 보를 의미한다.</p>

<p>채점 프로그램은 <code>machine_hand</code>와 실제 머신이 내는 손 모양이 모두 일치할 때 이를 정답으로 처리한다. 만약 머신과의 대결 횟수가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>101</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$101$</span></mjx-container>번을 초과하거나, 출력 형식을 지키지 않거나, <code>machine_hand</code>와 실제 머신이 내는 손 모양이 다른 경우 이를 오답으로 처리한다.</p>

<p>그레이더는 비적응적(non-adaptive)으로, 처음에 정한 손 모양을 상황에 따라 바꾸지 않는다.</p>

