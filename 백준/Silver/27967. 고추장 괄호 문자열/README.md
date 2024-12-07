# [Silver II] 고추장 괄호 문자열 - 27967 

[문제 링크](https://www.acmicpc.net/problem/27967) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

브루트포스 알고리즘, 그리디 알고리즘

### 제출 일자

2024년 12월 7일 22:01:55

### 문제 설명

<p>키높이 신발을 신고 선반 위에 있던 고추장을 꺼내려던 선생님은 발을 헛디뎌 넘어져 버리고 말았다!</p>

<p>바로 아래엔 선생님이 아끼고 아끼던 완벽한 형태의 올바른 괄호 문자열이 있었는데 여기에 고추장이 묻어버렸다. </p>

<p>올바른 괄호 문자열이란, 두 가지 괄호 <span style="color:#e74c3c;"><code>(</code></span>와 <span style="color:#e74c3c;"><code>)</code></span>만으로 구성된 문자열 중에서 괄호의 짝이 맞는 문자열을 뜻한다. 한 쌍의 괄호 <span style="color:#e74c3c;"><code>()</code></span>를 기본 올바른 괄호 문자열이라 하자. 만약 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container>가 올바른 괄호 문자열이라면, 기본 올바른 괄호 문자열 사이에 이를 넣은 새로운 문자열 <span style="color:#e74c3c;"><code>(</code></span> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container> <span style="color:#e74c3c;"><code>)</code></span>도 올바른 괄호 문자열이 되며, 두 개의 올바른 괄호 문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$y$</span></mjx-container>를 연달아 붙인 문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mi>y</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$xy$</span></mjx-container>도 올바른 괄호 문자열이 된다. 이러한 방식으로 구성할 수 없는 모든 문자열은 올바른 괄호 문자열이 아니다.</p>

<p>예를 들어, <span style="color:#e74c3c;"><code>()(())</code></span>와 <span style="color:#e74c3c;"><code>((()))</code></span>는 올바른 괄호 문자열이지만, <span style="color:#e74c3c;"><code>(((</code></span>, <span style="color:#e74c3c;"><code>())</code></span>, <span style="color:#e74c3c;"><code>(()</code></span>, <span style="color:#e74c3c;"><code>)(()</code></span> 는 올바른 괄호 문자열이 아니다.</p>

<p>입력으로 고추장이 묻은 괄호 문자열이 주어진다. 고추장이 묻은 자리에 적당한 괄호를 넣어 선생님의 올바른 괄호 문자열을 복구할 수 있도록 도와주자!</p>

### 입력 

 <p>첫 번째 줄에 괄호 문자열의 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>2</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>20</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(2 \le N \le 20)$</span> </mjx-container></p>

<p>두 번째 줄에 괄호 문자열이 주어진다. 이 괄호 문자열은 <span style="color:#e74c3c;"><code>(</code></span>와 <span style="color:#e74c3c;"><code>)</code></span>, 그리고 고추장이 묻은 자리인 <span style="color:#e74c3c;"><code>G</code></span>로 이루어져 있다.</p>

<p>복구했을 때 올바른 괄호 문자열이 하나라도 존재하는 경우만 입력으로 주어진다.</p>

<p>또한, 운이 좋게도 고추장이 옆으로 떨어져 고추장이 묻지 않은 경우도 주어질 수 있다.</p>

### 출력 

 <p>가능한 문자열을 출력한다. 가능한 문자열이 여러 개 존재할 경우, 그 중 하나만 출력한다.</p>

