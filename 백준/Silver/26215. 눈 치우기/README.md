# [Silver III] 눈 치우기 - 26215 

[문제 링크](https://www.acmicpc.net/problem/26215) 

### 성능 요약

메모리: 108080 KB, 시간: 120 ms

### 분류

그리디 알고리즘, 구현, 시뮬레이션, 정렬

### 제출 일자

2023년 12월 30일 03:55:19

### 문제 설명

<p>지난 밤 겨울 숲에는 눈이 많이 내렸다. 당신은 숲의 주민들을 위해 눈이 오지 않는 동안 모든 집 앞의 눈을 치우고자 한다.</p>

<p>당신은 1분에 한 번씩 두 집을 선택해서 두 집 앞의 눈을 각각 1만큼 치우거나, 한 집을 선택해서 그 집 앞의 눈을 1만큼 치울 수 있다.</p>

<p>모든 집 앞의 눈을 전부 치울 때까지 걸리는 최소 시간은 얼마일까?</p>

### 입력 

 <p>첫 줄에 집의 수를 의미하는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq N \leq 100$</span></mjx-container>)이 주어진다.</p>

<p>다음 줄에는 각각의 집 앞에 쌓여 있는 눈의 양을 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-texatom></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mrow data-mjx-texclass="ORD"><mi>i</mi></mrow></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a_{i}$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msub space="4"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-texatom></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><msub><mi>a</mi><mrow data-mjx-texclass="ORD"><mi>i</mi></mrow></msub><mo>≤</mo><mn>2000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq a_{i} \leq 2000$</span></mjx-container>)이 주어진다.</p>

### 출력 

 <p>모든 집 앞의 눈을 치우는 데 최소 몇 분이 걸리는지를 출력한다. 24시간(1440분)이 넘게 걸릴 경우 -1을 출력한다.</p>

