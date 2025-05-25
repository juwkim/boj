# [Bronze III] 어게인 포닉스 - 33950 

[문제 링크](https://www.acmicpc.net/problem/33950) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

구현, 문자열

### 제출 일자

2025년 5월 26일 00:55:24

### 문제 설명

<p>모두가 알다시피, 포닉스는 또 다시 꿈을 이룬 행복한 불사조이다!</p>

<p>작년에 응원 문구를 성공적으로 만들어 포스텍의 ICPC World Finals 진출을 도운 포닉스는 올해 역시 포스텍의 <strong>GLOBAL</strong>한 가치 창출을 위한 응원단장을 맡게 되었다.</p>

<p>포닉스의 역할은 학생들이 만든 응원 문구를 수정하는 것이다. 이 응원 문구가 충분히 <strong>GLOBAL</strong>하지 않다고 생각한 포닉스는, 응원 문구에 등장하는 연속하는 부분 문자열 <span style="color:#e74c3c;"><code>PO</code></span> 를 모두 자신이 가장 좋아하는 음식인 쌀국수(<span style="color:#e74c3c;"><code>PHO</code></span>)로 몰래 바꿔두려 한다.</p>

<p>학생들이 만든 응원 문구 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T$</span></mjx-container>개가 주어질 때 포닉스의 수정을 거친 응원 문구를 구하여라.</p>

### 입력 

 <p>첫 번째 줄에 응원 문구의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T$</span></mjx-container>가 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>T</mi><mo>≤</mo><mn>100</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1\le T\le 100)$</span> </mjx-container></p>

<p>두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T$</span></mjx-container>개의 줄에 걸쳐 학생들이 만든 응원 문구를 나타내는 문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>가 주어진다.</p>

<p>주어지는 모든 문자열은 알파벳 대문자로 이루어진 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container> 이하의 문자열이다.</p>

### 출력 

 <p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T$</span></mjx-container>개의 줄에 걸쳐 포닉스의 수정을 거친 응원 문구를 한 줄에 하나씩 순서대로 출력한다.</p>

