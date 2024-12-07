# [Silver II] 어깨동무 - 27932 

[문제 링크](https://www.acmicpc.net/problem/27932) 

### 성능 요약

메모리: 265860 KB, 시간: 1452 ms

### 분류

이분 탐색, 매개 변수 탐색, 정렬

### 제출 일자

2024년 12월 7일 22:51:17

### 문제 설명

<p>고연전 때 응원을 해 본 양교의 학생들이라면 양 옆 사람들과 어깨동무를 해 본 경험이 있을 것이다! 어깨동무를 할 때 제일 불편할 때가 옆 사람과 키 차이가 많이 날 때이다. 옆 사람들과 키 차이가 나게 되면 응원 동작을 할 때 어깨동무를 하기가 힘들어지고 쉽게 지치게 된다. </p>

<p>그런데 윤헌이는 응원하던 도중, 모든 사람들은 이웃한 사람 중 하나 이상과 키 차이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H$</span></mjx-container>보다 커지면 지친다는 사실을 깨달았다. 그리고 현재 경기 점수 차에 따라서 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H$</span></mjx-container>의 값이 달라진다는 것도 발견했다! 구체적으로, 고려대가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H$</span></mjx-container>점차로 연세대를 이기고 있을 때 고려대 학생들은 자신과 이웃한 사람들과 키 차이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H$</span></mjx-container>가 될 때까지는 지치지 않는다. 고려대와 연세대가 비기고 있다면 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi><mo>=</mo><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H=0$</span></mjx-container>이 된다. 고려대가 지고 있는 경우는 고려하지 않는다.</p>

<p>윤헌이는 일렬로 선 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>명의 고려대생들 중 지친 사람이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>명 이하가 되기 위해서는 고려대가 경기를 최소 몇 점 차로 이기고 있어야 하는지가 궁금해졌다. 윤헌이를 위해 이를 구해 주자!</p>

### 입력 

 <p>첫 줄에 고려대를 응원하는 학생의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>과 지친 사람 수의 최댓값 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>가 공백으로 구분되어 주어진다.</p>

<p>두 번째 줄에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>명의 학생의 키가 순서대로 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>지친 사람이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container>명 이하가 되기 위한 최소 점수 차이를 출력한다. 점수 차가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H$</span></mjx-container>라고 할 때, 사람들은 옆에 있는 사람들과 키 차이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H$</span></mjx-container> 이하이면 지치지 않는다.</p>

