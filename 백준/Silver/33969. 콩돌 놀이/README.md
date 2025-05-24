# [Silver II] 콩돌 놀이 - 33969 

[문제 링크](https://www.acmicpc.net/problem/33969) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

수학, 애드 혹, 백트래킹

### 제출 일자

2025년 5월 25일 00:25:31

### 문제 설명

<p>스누와 크누스는 콩돌해안에 놀러 갔다. 그곳에는 흰색 콩돌과 검은색 콩돌이 아주 많았는데, 이를 본 스누는 재미있는 생각이 나서 흰색 콩돌을 잔뜩 주워 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>×</mo><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N \times M$</span></mjx-container> 크기의 격자 모양으로 배치하여 콩돌 놀이를 시작하였다. 콩돌 놀이는 다음과 같다.</p>

<ul>
	<li>격자에 존재하는 임의의 <strong>S</strong> 모양에 모두 흰색 콩돌이 있다면, 해당 위치의 흰색 콩돌을 모두 검은색 콩돌로 바꾼다.</li>
	<li>격자에 존재하는 임의의 <strong>C</strong> 모양에 모두 흰색 콩돌이 있다면, 해당 위치의 흰색 콩돌을 모두 검은색 콩돌로 바꾼다.</li>
	<li>스누는 흰색 콩돌을 검은색 콩돌로 바꾸는 작업을 모양에 관계없이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>회 이상 원하는 순서대로 실행할 수 있다.</li>
</ul>

<p><strong>S</strong>와 <strong>C</strong>의 모양은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>×</mo><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5 \times 3$</span></mjx-container> 또는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>×</mo><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3 \times 5$</span></mjx-container> 격자에 돌이 놓인 모양이다. 주어진 모양을 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2218"></mjx-c></mjx-mo></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>90</mn><mrow data-mjx-texclass="ORD"><mo>∘</mo></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$90^{\circ}$</span></mjx-container> 간격으로 회전시킬 수는 있지만 뒤집는 것은 불가능하다. 다음 그림을 참고하자.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e66dda04-ea2f-4ef2-b254-b97274adaf8f/-/preview/" style="height: 350px; width: 600px;"></p>

<p>스누가 노는 모습을 본 크누스가 신기해하며 무엇을 한 건지 물어보자 스누는 <strong>S</strong>와 <strong>C</strong> 모양을 검은색 콩돌로 만들며 놀고 있었다고 답했다. 알고리즘 고수 크누스는 이를 보고 스누가 만든 무늬에 검은색 콩돌로 만들어진 <strong>S</strong>와 <strong>C</strong>가 각각 몇 개 포함되어 있는지 단번에 알아챘다. 우리도 알고리즘 고수이기 때문에 그가 내놓을 수 있는 답을 예측해 보자!</p>

### 입력 

 <p>첫째 줄에 격자의 크기를 나타내는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>과 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 공백으로 구분되어 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>,</mo><mi>M</mi><mo>≤</mo><mn>10</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \leq N, M \leq 10)$</span> </mjx-container></p>

<p>둘째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에 걸쳐 스누가 만든 콩돌 무늬가 주어진다. <code><font color="#e74c3c">x</font></code>는 검은색 콩돌을, <code><font color="#e74c3c">.</font></code>은 흰색 콩돌을 의미한다.</p>

<p>입력으로 주어지는 모든 수는 정수이다.</p>

### 출력 

 <p>첫째 줄에 콩돌 무늬에 포함된 <strong>S</strong>와 <strong>C</strong>의 개수를 공백으로 구분하여 출력한다. 가능한 답이 여러 가지라면 아무거나 하나 출력한다.</p>

