# [Bronze I] 옷걸이 - 27951 

[문제 링크](https://www.acmicpc.net/problem/27951) 

### 성능 요약

메모리: 218032 KB, 시간: 536 ms

### 분류

그리디 알고리즘, 구성적

### 문제 설명

<p>경기과학고등학교에는 아주 무시무시한 부서 하나가 있다. 그 부서의 이름은 바로 '자치부'이다. '자치부'가 하는 주된 역할 중 하나는 아침에 지정된 기숙사에 들어가서 방의 정리 정돈 상태를 확인하고 검사하는 일이다. 은호는 자치부의 일원으로서 기숙사 호실들을 모두 점검하게 되었다. 근데, 은호가 점검하는 호실마다 옷들이 너저분하게 깔려있었고 심각하게 어질러져 있었다. 이에 은호는 기숙사 대청소 날을 만들어 기숙사 옷들을 모두 정리하려고 한다.</p>

<p>은호가 경곽의 옷걸이 조사해 보았더니 총 세 가지 종류가 있었다. 하나는 상의만 걸 수 있는 옷걸이, 또 다른 하나는 하의만 걸 수 있는 옷걸이, 마지막 하나는 상의와 하의 모두 걸 수 있는 옷걸이다. 하나의 옷걸이에는 하나의 상의 또는 하의만 걸 수 있음을 유의하자.</p>

<p>은호는 기숙사 옷들을 정리하기 전에 옷걸이가 모든 옷을 걸기에 부족하지는 않은지 조사하고자 한다. 은호는 경곽 기숙사에 있는 상의와 하의의 개수, 그리고 옷걸이의 개수와 그 종류를 모두 조사했다. <strong>놀랍게도 옷걸이의 개수와 옷의 개수는 같았다.</strong> 다만, 옷이 너무 많았기 때문에 은호는 프로그램을 이용해 모든 옷을 정리할 수 있는지 없는지 구하고자 한다. 또 만약 정리할 수 있으면, 어떻게 걸면 옷을 모두 정리할 수 있는지 알고 싶어 한다.</p>

<p>은호는 건표와 급한 약속이 있어서 이 프로그램 구현을 여러분에게 맡기고 갔다. 은호를 대신해서 프로그램을 짜주자.</p>

### 입력 

 <p>첫째 줄에는 옷걸이의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>둘째 줄에는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 정수가 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$A_i$</span></mjx-container>는 옷걸이의 종류를 나타낸다.</p>

<p>1은 상의 걸이를, 2는 하의 걸이를, 3은 모두 걸 수 있는 옷걸이를 나타낸다.</p>

<p>마지막 줄에는 두 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D448 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>U</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$U$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D437 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$D$</span></mjx-container>가 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D448 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>U</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$U$</span></mjx-container>는 상의의 개수, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D437 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>D</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$D$</span></mjx-container>는 하의의 개수이다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D448 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D437 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>U</mi><mo>+</mo><mi>D</mi><mo>=</mo><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$U+D=N$</span></mjx-container> 임이 보장된다.</p>

### 출력 

 <p>첫째 줄에 주어진 상의와 하의를 옷걸이에 모두 걸 수 있으면 '<code>YES</code>'를, 아니면 '<code>NO</code>'를 출력한다.</p>

<p>만약 모두 걸 수 있다면 둘째 줄에 각 옷걸이에 어떻게 걸었는지를 길이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>인 문자열 형태로 출력한다.</p>

<p>문자열에서 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 문자는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 옷걸이에 건 의상의 종류를 나타내며, '<code>U</code>'인 경우 상의를, '<code>D</code>'인 경우 하의를 걸었음을 나타낸다. (작은따옴표는 출력하지 않는다.)</p>

<p>문자는 모두 대문자로 출력해야 한다.</p>

