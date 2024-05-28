# [Silver V] 현대모비스 특별상의 주인공은? 2 - 31924 

[문제 링크](https://www.acmicpc.net/problem/31924) 

### 성능 요약

메모리: 111688 KB, 시간: 180 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2024년 5월 29일 04:41:25

### 문제 설명

<p style="text-align: center;"><img data-image="2bac06c4-3e43-4a4e-a817-0115df85cc78" src="https://upload.acmicpc.net/2bac06c4-3e43-4a4e-a817-0115df85cc78/-/preview/" style="width: 300px; height: 105px;"></p>

<p>올해도 어김없이 현대모비스는 실력 있는 소프트웨어 인재를 양성하고 독려하기 위해 APC의 주최 동아리인 A.N.S.I.를 후원하고 있다. 올해 현대모비스는 2024 APC에 참가한 여러분들을 위해 특별상을 준비하였다.</p>

<p>현대모비스는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>×</mo><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N \times N$</span></mjx-container> 크기의 격자판을 준비하였다. 격자판의 각 칸에는 알파벳 대문자가 한 글자씩 적혀있다. 특별상은 이 격자판에서 가장 많은 <span style="color:#e74c3c;"><code>MOBIS</code></span>를 찾은 사람에게 주어지는데, <code><span style="color:#e74c3c;">MOBIS</span></code>를 찾는 것은 다음의 규칙을 따른다.</p>

<ul>
	<li>격자 위의 임의 위치에서 시작하여 상, 하, 좌, 우, 대각선의 8방향 중 한 방향으로 격자에 적힌 글자들을 차례로 5개 이어 붙였을 때, 이어 붙인 글자가 <span style="color:#e74c3c;"><code>MOBIS</code></span>여야 한다.</li>
</ul>

<p>현빈이는 어떻게든 특별상의 주인공이 되고 싶다. 현빈이를 도와 주어진 격자판에서 <span style="color:#e74c3c;"><code>MOBIS</code></span>를 최대 몇 번 찾을 수 있는지 구해보자.</p>

### 입력 

 <p>첫 번째 줄에 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \leq N \leq 100)$</span> </mjx-container></p>

<p>두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>+</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N+1$</span></mjx-container>번째 줄까지, 현대모비스가 준비한 격자판의 정보가 주어진다. 각 줄은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 알파벳 대문자로 이루어져 있다.</p>

### 출력 

 <p>주어진 격자판에서 찾을 수 있는 <span style="color:#e74c3c;"><code>MOBIS</code></span>의 개수를 출력한다.</p>

