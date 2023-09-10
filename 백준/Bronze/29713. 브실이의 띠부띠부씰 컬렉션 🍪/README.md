# [Bronze II] 브실이의 띠부띠부씰 컬렉션 🍪 - 29713 

[문제 링크](https://www.acmicpc.net/problem/29713) 

### 성능 요약

메모리: 114436 KB, 시간: 140 ms

### 분류

구현, 문자열

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/8dd922e4-0fc1-420e-b802-42dd6ed3d1e3/-/preview/" style="max-width: 100%; height: 229px; width: 400px;"></p>

<p>이 세상에서 두 번째로 맛있는 과자 브실칩이 있다.</p>

<p>하나의 브실칩에는 <code><span data-darkreader-inline-color="" style="color: rgb(231, 76, 60); --darkreader-inline-color: #e95849;">A</span></code>부터 <code><span data-darkreader-inline-color="" style="color: rgb(231, 76, 60); --darkreader-inline-color: #e95849;">Z</span></code> 중 하나의 알파벳 띠부띠부씰이 들어있다.</p>

<p>모은 띠부띠부씰들로 <code><span data-darkreader-inline-color="" style="color: rgb(231, 76, 60); --darkreader-inline-color: #e95849;">BRONZESILVER</span></code> 글자를 만들어 우편으로 보내면 이 세상에서 제일 맛있는 골드칩 한 봉지를 배송해 준다고 한다.</p>

<p>지금까지 모은 띠부띠부씰들로 골드칩을 최대 몇 봉지 배송받을 수 있을지 계산해 보자.</p>

### 입력 

 <p>첫 번째 줄에는 모은 알파벳 띠부띠부씰 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> 이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \le N \le 1\,000)$</span> </mjx-container></p>

<p>두 번째 줄에는 알파벳 대문자로 이루어진 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 알파벳 띠부띠부씰이 나열된다.</p>

### 출력 

 <p>배송받을 수 있는 최대 골드칩 봉지 수를 출력한다.</p>

