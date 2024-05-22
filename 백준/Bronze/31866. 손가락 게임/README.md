# [Bronze II] 손가락 게임 - 31866 

[문제 링크](https://www.acmicpc.net/problem/31866) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

많은 조건 분기, 구현

### 제출 일자

2024년 5월 22일 11:07:55

### 문제 설명

<p>손가락 게임은 두 플레이어가 동시에 손가락을 일정 개수 펴서 특정 표식을 만들어 상성을 겨루는 게임이다. 플레이어는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>개의 손가락을 펴서 '바위' 표식(즉, 손가락을 피지 않은 상태), <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2$</span></mjx-container>개의 손가락을 펴서 '가위' 표식, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container>개의 손가락을 펴서 '보' 표식을 만들 수 있다. 이 외의 개수의 손가락을 피면 '무효' 표식을 만든 것으로 간주한다.</p>

<p>두 플레이어 모두 같은 표식을 낼 경우 승패를 가릴 수 없으며, 표식에 따른 상성은 아래와 같다.</p>

<ol>
	<li>'무효' 외의 다른 표식을 낸 플레이어는 '무효'를 낸 플레이어를 상대로 승리한다.</li>
	<li>'바위'를 낸 플레이어는 '가위'를 낸 플레이어를, '가위'를 낸 플레이어는 '보'를 낸 플레이어를, '보'를 낸 플레이어는 '바위'를 낸 플레이어를 상대로 승리한다.</li>
</ol>

<p>준성과 익준은 손가락 게임을 진행하려고 한다. 두 사람이 핀 손가락의 개수를 보고 승패를 판별해 주도록 하자.</p>

### 입력 

 <p>첫 번째 줄에 준성이 핀 손가락의 개수와 익준이 핀 손가락의 개수가 공백을 사이에 두고 주어진다.</p>

<p>두 사람이 핀 손가락의 개수는 각각 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container> 이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container> 이하의 정수다.</p>

### 출력 

 <p>첫 번째 줄에 준성이 이겼다면 <span style="color:#e74c3c;"><code>></code></span>, 익준이 이겼다면 <span style="color:#e74c3c;"><code><</code></span>, 승패를 가릴 수 없었다면 <span style="color:#e74c3c;"><code>=</code></span>을 출력한다.</p>

