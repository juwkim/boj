# [Platinum V] XOR삼형제 2 - 10736 

[문제 링크](https://www.acmicpc.net/problem/10736) 

### 성능 요약

메모리: 109544 KB, 시간: 96 ms

### 분류

애드 혹, 해 구성하기

### 제출 일자

2025년 4월 8일 13:57:36

### 문제 설명

<p><img alt="" src="https://www.acmicpc.net/upload/codershigh2015/statement.png" style="height:674px; width:594px"></p>

<p>(위에서 아래로, 오른쪽에서 왼쪽으로 읽어주세요.)</p>

### 입력 

 <p>첫 줄에 테스트 케이스의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(T\)</span></mjx-container>가 주어진다.</p>

<p>이어서 매 테스트 케이스마다 한 줄에 걸쳐 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(N\)</span></mjx-container> 이 주어진다.</p>

<p>이 문제는 두 개의 부분문제로 이루어져 있다.</p>

<p><a href="https://www.acmicpc.net/problem/10728">1번 문제</a>의 입력은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(1 \leq n \leq 20\)</span></mjx-container>을 만족하며 해결하면 20점을 얻을 수 있다.</p>

<p><a href="https://www.acmicpc.net/problem/10736">2번 문제</a>의 입력은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(1 \leq n \leq 100\)</span></mjx-container>을 만족하며 해결하면 80점을 얻을 수 있다.</p>

### 출력 

 <p>매 테스트 케이스마다 두 줄에 걸쳐서 답을 출력한다.</p>

<ul>
	<li>첫 줄에는 수열의 길이를 출력한다. </li>
	<li>두 번째 줄에는 조건을 만족하는 수열을 공백으로 구분하여 출력한다. 만약 조건을 만족하는 수열이 여러 개라면, 아무 수열이나 하나 출력한다.</li>
</ul>

