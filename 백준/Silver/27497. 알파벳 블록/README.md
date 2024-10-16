# [Silver II] 알파벳 블록 - 27497 

[문제 링크](https://www.acmicpc.net/problem/27497) 

### 성능 요약

메모리: 236184 KB, 시간: 616 ms

### 분류

자료 구조, 덱, 스택, 문자열

### 제출 일자

2024년 10월 16일 09:15:50

### 문제 설명

<p>스타는 알파벳 블록을 일렬로 조립하여 문자열을 만드는 게임을 만들었다. 각 블록에는 문자 하나가 적혀 있으며 게임에는 각각 다음 기능을 수행하는 세 개의 버튼이 있다.</p>

<ul>
	<li>문자열 맨 뒤에 블록 추가</li>
	<li>문자열 맨 앞에 블록 추가</li>
	<li>문자열을 구성하는 블록 중 가장 나중에 추가된 블록 제거</li>
</ul>

<p>게임은 처음에 빈 문자열로 시작하며 빈 문자열일 때 문자열을 구성하는 블록 중 가장 나중에 추가된 블록을 제거하는 버튼을 누를 경우 아무런 동작도 하지 않는다. 버튼을 누른 횟수와 누른 버튼이 순서대로 주어질 때 완성된 문자열을 구하여라.</p>

### 입력 

 <p>첫째 줄에 버튼을 누른 횟수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \leq N \leq 1\,000\,000)$</span> </mjx-container></p>

<p>둘째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에는 버튼을 누른 순서대로 누른 버튼에 대한 정보를 주며 아래와 같은 형식으로 주어진다.</p>

<ul>
	<li><code>1 c</code> : 문자열 맨 뒤에 <code>c</code>가 적힌 블록 추가</li>
	<li><code>2 c</code> : 문자열 맨 앞에 <code>c</code>가 적힌 블록 추가</li>
	<li><code>3</code> : 문자열을 구성하는 블록 중 가장 나중에 추가된 블록 제거</li>
</ul>

<p><code>c</code>는 알파벳 대문자 또는 소문자로 주어진다.</p>

### 출력 

 <p>완성된 문자열을 출력한다. 완성된 문자열이 빈 문자열인 경우 0을 출력한다.</p>

