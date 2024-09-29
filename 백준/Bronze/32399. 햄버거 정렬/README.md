# [Bronze III] 햄버거 정렬 - 32399 

[문제 링크](https://www.acmicpc.net/problem/32399) 

### 성능 요약

메모리: 108080 KB, 시간: 84 ms

### 분류

구현

### 제출 일자

2024년 9월 29일 18:05:17

### 문제 설명

<p><strong>햄버거 문자열</strong>은 세 개의 문자 <span style="color:#e74c3c;"><code>(</code></span>, <span style="color:#e74c3c;"><code>1</code></span>, <span style="color:#e74c3c;"><code>)</code></span>가 순서대로 나열된 문자열이다.</p>

<p>준휘는 세 개의 문자 <span style="color:#e74c3c;"><code>(</code></span>, <span style="color:#e74c3c;"><code>1</code></span>, <span style="color:#e74c3c;"><code>)</code></span>를 아무렇게나 나열해서 문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>를 만들었다. 준휘는 이 문자열에서 원하는 문자 하나를 떼서 다른 문자의 앞이나 뒤에 놓는 과정을 반복할 수 있다. 문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>를 <strong>햄버거 문자열</strong>로 만들기 위해서 이 과정을 최소 몇 번 반복해야 하는지 구해보자.</p>

### 입력 

 <p>문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>가 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>의 길이는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container>이고, <span style="color:#e74c3c;"><code>(</code></span>, <span style="color:#e74c3c;"><code>1</code></span>, <span style="color:#e74c3c;"><code>)</code></span>가 한 글자씩 포함되어 있다.</p>

### 출력 

 <p>문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>를 햄버거 문자열로 만들기 위해서 위 과정을 최소 몇 번 반복해야 하는지 출력한다.</p>

