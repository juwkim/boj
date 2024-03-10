# [Bronze IV] 시계탑 - 31561 

[문제 링크](https://www.acmicpc.net/problem/31561) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

사칙연산, 수학

### 제출 일자

2024년 3월 11일 07:50:02

### 문제 설명

<p>근성은 공대 7호관 옆 카페에서 자바칩 프라푸치노를 주문하려다 문득 생각이 나 카페 직원에게 물어보았다.</p>

<blockquote>
<p><strong>c++칩 프라푸치노는 없나요?</strong></p>
</blockquote>

<p>근성의 황당한 질문을 들은 카페 직원은 화가 나서 근성을 바로 앞에 있는 시계탑 분침에 묶어버렸다.</p>

<p>그러자 시계탑의 분침이 근성의 무게로 인해 이상하게 돌아가기 시작했다. 분침은 정확히 다음 순서를 매시간 반복한다.</p>

<ol>
	<li>매시간 정각에 분침은 12시 방향을 가리킨다.</li>
	<li>매시간 정각부터 15분까지 분침은 시계 방향으로 정상적인 분침의 회전 속도의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2$</span></mjx-container>배로 움직인다. 즉, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>15</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$15$</span></mjx-container>분 간 분침은 12시 방향에서 시계 방향으로 6시 방향까지 움직인다.</li>
	<li>매시간 15분에 분침은 6시 방향을 가리킨다.</li>
	<li>매시간 15분부터 다음 시간 정각까지 분침은 시계 방향으로 정상적인 분침의 회전 속도의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mfrac><mjx-frac><mjx-num><mjx-nstrut></mjx-nstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-num><mjx-dbox><mjx-dtable><mjx-line></mjx-line><mjx-row><mjx-den><mjx-dstrut></mjx-dstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>2</mn><mn>3</mn></mfrac></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\frac{2}{3}$</span></mjx-container>배로 움직인다. 즉, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>45</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$45$</span></mjx-container>분 간 분침은 6시 방향에서 시계 방향으로 12시 방향까지 움직인다.</li>
</ol>

<p style="display:flex;flex-direction:row;justify-content:center;"><img alt="" src="https://upload.acmicpc.net/c10b5fde-7fdc-43d5-a54a-830de09a329b/-/preview/" style="max-height:200px;max-width:200%"></p>

<p>정상적인 시계탑의 분침은 매시간 정각에 정확히 12시 방향을 가리키며, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>시간에 한 바퀴를 시계 방향으로 일정한 회전 속도로 움직인다.</p>

<p>바뀐 시계탑의 시침은 정상적인 시계탑과 똑같이 돌아가기 때문에 문제가 없었으나, 사람들은 지금이 몇 분인지 헷갈리기 시작했다.</p>

<p>바뀐 시계탑을 보고 올바른 시각을 구해 사람들에게 알려주자.</p>

### 입력 

 <p>바뀐 시계탑의 분침이 가리키는 분을 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 주어진다.</p>

### 출력 

 <p>올바른 시각의 분을 나타내는 실수를 정확하게 출력한다. 이때 값은 소수점 첫째 자리까지 출력해야 하며, 항상 답을 정확하게 출력할 수 있음을 증명할 수 있다.</p>

