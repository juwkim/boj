# [Silver I] 숫자 할리갈리 게임 - 20923 

[문제 링크](https://www.acmicpc.net/problem/20923) 

### 성능 요약

메모리: 152320 KB, 시간: 384 ms

### 분류

자료 구조, 덱, 구현, 시뮬레이션

### 제출 일자

2024년 10월 27일 23:23:57

### 문제 설명

<p>인간이 가장 심심함을 느낀다는 오후 1시 22분, 도도와 수연이는 숫자 할리 갈리 게임을 하려 한다. 숫자 할리 갈리 게임의 규칙은 다음과 같다.</p>

<p style="text-align: center;"><strong>[숫자 할리 갈리 게임의 규칙]</strong></p>

<ol>
	<li>도도와 수연이는 각각 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>장의 카드로 이루어진 덱을 배분받는다. 게임 시작 시 그라운드는 비어있는 상태이다.
	<ul>
		<li>덱은 숫자가 보이지 않게 카드를 뒤집어 쌓아 놓은 카드 더미를 의미한다. 도도와 수연이는 자신의 덱을 가지고 게임을 진행하게 된다.</li>
		<li>그라운드는 카드를 내려놓게 되는 땅을 의미한다. 그라운드에 카드를 내려놓을 때는 자신의 그라운드에 카드를 내려놓으며, 그라운드에 카드 더미가 존재할 경우 카드 더미 위에 카드를 내려놓는 방식으로 게임을 진행한다.</li>
	</ul>
	</li>
	<li>도도를 시작으로 도도와 수연이가 차례대로 자신이 가진 덱에서 가장 위에 위치한 카드를 그라운드에 숫자가 보이도록 내려놓는다.</li>
	<li>종을 치는 사람이 그라운드에 나와 있는 카드 더미를 모두 가져간다. 종을 치는 조건은 다음과 같다.
	<ul>
		<li>그라운드에 나와 있는 각각의 카드 더미에서 가장 위에 위치한 카드의 숫자 합이 5가 되는 순간 수연이가 종을 친다. 단, 어느 쪽의 그라운드도 비어있으면 안된다.</li>
		<li>그라운드에 나와 있는 각각의 카드 더미 중 가장 위에 위치한 카드의 숫자가 5가 나오는 순간 도도가 종을 친다.</li>
	</ul>
	</li>
	<li>종을 쳤다면, 상대방의 그라운드에 있는 카드 더미를 뒤집어 자신의 덱 아래로 그대로 합친 후 자신의 그라운드에 있는 카드 더미 역시 뒤집어 자신의 덱 아래로 그대로 가져와 합친다.
	<ul>
		<li>종을 쳐서 그라운드에 있는 카드 더미를 가져가는 행위는 게임의 진행 순서에 영향을 미치지 않는다.</li>
	</ul>
	</li>
</ol>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/22dc1ff3-6e90-4441-b84f-6544eb329eeb/-/preview/" style="height: 238px; width: 500px;"></p>

<ol start="5">
	<li>한 명이 2-4번까지의 과정을 진행하는 것을 1번 진행한 것으로 보며 다음과 같은 방법으로 게임의 승패가 결정된다.
	<ol>
		<li>게임 진행 도중 자신의 덱에 있는 카드의 수가 0개가 되면 상대방이 승리한 것으로 본다.</li>
		<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>번 진행한 후 자신의 덱에 더 많은 카드를 지닌 사람이 승리한다.</li>
		<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>번 진행 후 각자의 덱에 있는 카드의 개수가 같다면 비긴 것으로 본다.</li>
	</ol>
	</li>
</ol>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/3e2fe162-2931-457c-808f-1f84551e7061/-/preview/" style="height: 172px; width: 500px;"></p>

<p>게임을 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>번 진행한 후 승리한 사람은 누구일까?</p>

### 입력 

 <p>첫째 줄에는 도도와 수연이가 가지는 카드의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>(<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>30</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$ 1 \leq N \leq 30\,000$</span></mjx-container>)과 게임 진행 횟수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>(<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>M</mi><mo>≤</mo><mn>2</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>500</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$ 1 \leq M \leq 2\,500\,000$</span></mjx-container>)이 주어진다.</p>

<p>둘째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에는 띄어쓰기로 구분하여 도도와 수연이가 가진 덱의 맨 아래에 위치한 카드에 적혀 있는 수부터 맨 위에 위치한 카드에 적힌 수까지 차례대로 주어진다. (각각의 카드는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> 이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container> 이하의 자연수가 적혀있다.)</p>

### 출력 

 <p>게임을 이긴 사람이 도도라면 <span style="color:#e74c3c;"><code>do</code></span>를 출력하고 게임을 이긴 사람이 수연이라면 <code><span style="color:#e74c3c;">su</span></code>를 출력한다. 비겼을 경우, <span style="color:#e74c3c;"><code>dosu</code></span>를 출력한다.</p>

