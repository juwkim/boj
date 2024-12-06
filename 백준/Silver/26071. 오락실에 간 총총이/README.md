# [Silver II] 오락실에 간 총총이 - 26071 

[문제 링크](https://www.acmicpc.net/problem/26071) 

### 성능 요약

메모리: 110736 KB, 시간: 164 ms

### 분류

애드 혹, 많은 조건 분기

### 제출 일자

2024년 12월 7일 04:29:46

### 문제 설명

<p style="text-align: center;"><img alt="곰곰 피규어를 생각하며 신나있는 총총이" src="https://upload.acmicpc.net/ccc56785-97d2-4857-b92e-cb8c96b035b8/-/preview/" style="max-height: 200px; object-fit:contain; display:inline-block;"></p>

<p>우연히 들리게 된 오락실에서, 총총이는 귀여운 곰곰이가 잔뜩 등장하는 게임을 발견했다.</p>

<p>게임의 화면은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>×</mo><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N \times N$</span></mjx-container> 크기의 칸으로 나누어져 있고, 각 칸에는 곰곰이가 있거나 또는 비어있다. 화면에는 최소 한 마리의 곰곰이가 존재한다.</p>

<p>게임은 상하좌우 네 개의 버튼을 눌러서 진행할 수 있다. 각 버튼을 누르게 되면, 화면에 있는 모든 곰곰이들이 그 버튼에 해당하는 방향으로 한 칸 움직이게 된다. 만약 이미 화면의 끝에 있어서 그 방향으로 이동하지 못하는 곰곰이들은 가만히 있는다. 버튼을 잘 눌러서 모든 곰곰이들을 하나의 칸에 모으게 되면, 화면에 <em><strong>GOMGOM</strong> </em>이라는 글자가 뜨면서 승리하게 된다.</p>

<p>현재 오락실에서는 이 게임을 가장 적은 횟수의 버튼을 눌러서 승리한 플레이어에게 곰곰 피규어를 주는 이벤트를 진행하고 있다. 귀여운 곰곰 피규어를 노리는 총총이를 위해, 최소 몇 번의 버튼을 눌러야 게임을 클리어할 수 있는지를 구해보자.</p>

### 입력 

 <p>첫째 줄에 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>500</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \le N \le 1\,500)$</span></mjx-container>  </p>

<p>둘째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에 걸쳐 게임 화면의 상태가 주어진다. 각 줄에는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 문자가 공백없이 주어지고, 모든 문자는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$G$</span></mjx-container> 또는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2E"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$.$</span></mjx-container> 중 하나이다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$G$</span></mjx-container> 는 그 칸에 곰곰이가 있다는 뜻이고, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2E"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>.</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$.$</span></mjx-container> 는 그 칸이 비어있음을 의미한다.  </p>

<p><strong>최소 하나 이상의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>G</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$G$</span></mjx-container> 문자가 주어짐이 보장된다.</strong></p>

### 출력 

 <p>모든 곰곰이를 하나의 칸에 모으기 위해, 총총이가 최소 몇 번 버튼을 눌러야 하는지 구하시오.</p>

