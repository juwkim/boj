# [Silver I] 동전 퍼즐 - 27921 

[문제 링크](https://www.acmicpc.net/problem/27921) 

### 성능 요약

메모리: 110964 KB, 시간: 124 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2025년 4월 8일 17:02:45

### 문제 설명

<p>동전 퍼즐을 풀어 보자! 처음에 무한 격자 평면에 동전 몇 개가 놓여 있다. 모든 동전은 격자점 위에 있다.</p>

<p>퍼즐의 목표는 최소 개수의 동전을 옮겨서 새로운 모양을 만드는 것이다. 동전을 옮길 때는 한 번에 한 개씩, 동전을 들어서 빈 격자점에 놓으면 된다. 새로운 모양이 만들어지는 위치는 어디든 상관없지만, 회전된 모양이나 대칭된 모양을 만드는 것은 인정되지 않는다.</p>

<p>예를 들어, 다음과 같은 두 가지 동전의 배치를 생각하자.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/ff7e9006-2a35-4a6e-8982-e9896295eb5a/-/preview/" style="width: 700px; height: 350px;"></p>

<p>첫 번째 배치에서 두 번째 배치로 만들기 위해서는 아래와 같이 최소 네 개의 동전을 옮겨야 한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/5565b710-b0a8-438d-9f25-ab650af440bd/-/preview/" style="width: 455px; height: 350px;"></p>

<p>현재 동전의 배치와 만들어야 하는 동전의 배치가 주어질 때, 옮겨야 하는 동전의 개수는 최소 몇 개인지 구하시오.</p>

### 입력 

 <p>첫 번째 줄에 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.057em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mn>1</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H_1$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44A TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.104em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>W</mi><mn>1</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$W_1$</span></mjx-container>이 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msub space="4"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.057em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44A TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.104em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><msub><mi>H</mi><mn>1</mn></msub><mo>,</mo><msub><mi>W</mi><mn>1</mn></msub><mo>≤</mo><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\le H_1,W_1\le 10$</span></mjx-container>)</p>

<p>그다음 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.057em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mn>1</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H_1$</span></mjx-container>개의 줄에 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44A TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.104em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>W</mi><mn>1</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$W_1$</span></mjx-container>의 문자열이 주어진다. ‘<span style="color:#e74c3c;"><code>.</code></span>’은 빈칸, ‘<span style="color:#e74c3c;"><code>O</code></span>’는 동전이 있는 칸이다. 현재 동전의 배치를 나타낸다.</p>

<p>그다음 줄에 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.057em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mn>2</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H_2$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44A TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.104em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>W</mi><mn>2</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$W_2$</span></mjx-container>가 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msub space="4"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.057em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44A TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.104em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><msub><mi>H</mi><mn>2</mn></msub><mo>,</mo><msub><mi>W</mi><mn>2</mn></msub><mo>≤</mo><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\le H_2,W_2\le 10$</span></mjx-container>)</p>

<p>그다음 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.057em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>H</mi><mn>2</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H_2$</span></mjx-container>개의 줄에 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44A TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.104em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>W</mi><mn>2</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$W_2$</span></mjx-container>의 문자열이 주어진다. ‘<span style="color:#e74c3c;"><code>.</code></span>’은 빈칸, ‘<span style="color:#e74c3c;"><code>O</code></span>’는 동전이 있는 칸이다. 만들어야 하는 동전의 배치를 나타낸다.</p>

<p>두 배치의 동전의 개수는 동일함이 보장된다.</p>

### 출력 

 <p>옮겨야 하는 동전의 최소 개수를 출력한다.</p>

