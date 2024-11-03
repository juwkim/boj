# [Bronze III] BB84 - 32515 

[문제 링크](https://www.acmicpc.net/problem/32515) 

### 성능 요약

메모리: 122664 KB, 시간: 140 ms

### 분류

구현, 문자열

### 제출 일자

2024년 11월 3일 23:19:01

### 문제 설명

<p>BB84 프로토콜은 1984년 찰스 베넷(Charles Bennett)과 질 브라사드(Gilles Brassard)가 제안한 양자 키 분배 방식이다.</p>

<p>정훈이가 BB84 프로토콜로 이안이에게 키를 보내려고 한다. 키는 <code>0</code>과 <code>1</code>로 이루어진 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>인 문자열이다. 그런데 태균이가 통신망을 도청할 위험이 있어서, 도청이 감지되면 작업을 중단해야 한다.</p>

<p>정훈이는 키의 각 자리를 양자 상태인 '큐비트'로 구현한다. 각 큐비트는 기저 <code>V</code> 또는 기저 <code>H</code>의 두 가지 상태 중 하나로 생성된다. 큐비트를 만들 때 사용한 기저와 동일한 기저로 측정하면, 해당 큐비트가 나타내는 키의 값을 정확히 얻을 수 있다. 하지만 다른 기저로 측정하면 <code>0</code> 또는 <code>1</code>이 무작위로 나온다. 예를 들어, 키의 첫 번째 자리가 <code>0</code>이고, 정훈이가 첫 번째 큐비트를 기저 <code>V</code>로 만들었다면, 이안이가 기저<code>V</code>로 첫 번째 큐비트를 측정할 때는 반드시 <code>0</code>이 나오지만, 기저 <code>H</code>로 측정하면 <code>0</code>이나 <code>1</code>이 무작위로 나온다.</p>

<p>정훈이는 키의 각 자리에 해당하는 큐비트를 만들 때, 기저를 임의로 선택해서 전송한다. 이안이도 임의로 기저를 선택해 큐비트를 측정한다. 그런 다음 두 사람은 서로 같은 기저를 선택한 자리들을 확인한 후, 정훈이는 그 자리에 해당하는 키 값을, 이안이는 그 자리에 해당하는 측정값을 모아 각각 '새로운 키'를 만든다.</p>

<p>정상적으로 통신이 이루어졌다면 두 사람의 '새로운 키'는 완전히 일치해야 한다. 하지만 태균이가 임의의 기저로 큐비트를 측정한 후, 다시 임의의 기저로 큐비트를 재생성해 이안이에게 보내는 식으로 도청할 수 있다. 이 경우, 높은 확률로 두 사람의 '새로운 키'는 일치하지 않게 된다.</p>

<p>정훈이의 기저 선택과 전송한 키, 이안이의 기저 선택과 측정값이 주어졌을 때, 태균이가 도청한 것이 확실한지 여부를 판단하고, 태균이가 도청하지 않았거나 도청 여부를 알 수 없다면 두 사람이 만든 '새로운 키'를 구하여라.</p>

### 입력 

 <p>첫 번째 줄에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>두 번째 줄에 문자 <code>V</code>와 <code>H</code>로 이루어진 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 문자열이 주어지고, 이는 정훈이의 기저 선택을 나타낸다.</p>

<p>세 번째 줄에 문자 <code>0</code>과 <code>1</code>로 이루어진 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 문자열이 주어지고, 이는 정훈이가 전송한 키를 나타낸다.</p>

<p>네 번째 줄에 문자 <code>V</code>와 <code>H</code>로 이루어진 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 문자열이 주어지고, 이는 이안이의 기저 선택을 나타낸다.</p>

<p>다섯 번째 줄에 문자 <code>0</code>과 <code>1</code>로 이루어진 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 문자열이 주어지고, 이는 이안이의 큐비트 측정값을 나타낸다.</p>

### 출력 

 <p>태균이가 도청하지 않았거나 도청 여부를 알 수 없다면 첫 번째 줄에 정훈이와 이안이가 만든 '새로운 키'를 출력하고, 태균이가 도청한 것이 확실하다면 첫 번째 줄에 <code>htg!</code>를 출력한다.</p>

