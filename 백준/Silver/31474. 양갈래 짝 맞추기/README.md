# [Silver IV] 양갈래 짝 맞추기 - 31474 

[문제 링크](https://www.acmicpc.net/problem/31474) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

조합론, 수학

### 제출 일자

2024년 3월 6일 03:38:44

### 문제 설명

<p>시현이 카페에 양갈래 손님들이 들어가려고 한다. </p>

<p>양갈래 손님들은 양갈래를 너무 좋아하는 나머지 두 명씩 모여 있어 총 인원은 짝수이다.</p>

<p>시현이 카페에는 두 명씩 앉을 수 있는 테이블이 충분히 많이 있고, 양갈래 손님들은 한 테이블에 두 명씩 앉기로 하였다.</p>

<p>그런 양갈래 손님들을 맞이하게 된 시현이는 갑자기 궁금증이 생겼다.</p>

<p>손님들이 앉는 경우의 수를 세는 조건이 다음과 같을 때, 양갈래 손님들이 모두 앉을 수 있는 방법의 수는 몇 가지가 있을까?</p>

<ol>
	<li>테이블의 좌석을 구분하지 않는다.
	<ul>
		<li>한 테이블에서 손님 A와 손님 B가 앉는 경우, 손님 B와 손님 A가 앉는 경우는 같은 경우이다.</li>
	</ul>
	</li>
	<li>각각의 테이블 또한 구분하지 않는다.
	<ul>
		<li>1번 테이블에 손님 A, B가 앉고, 2번 테이블에 손님 C, D가 앉는 것과, 1번 테이블에 손님 C, D가 앉고, 2번 테이블에 손님 A, B가 앉는 것은 서로 같은 경우이다.</li>
	</ul>
	</li>
</ol>

### 입력 

 <p>첫째 줄에 양갈래 손님의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>28</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \leq N \leq 28$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>은 짝수)</p>

### 출력 

 <p>첫째 줄에 양갈래 손님들이 앉을 수 있는 경우의 수를 출력한다.</p>

<p>연산 중 32비트 정수형 타입의 표현 범위를 초과할 수 있으므로 오버플로우에 주의한다.</p>

