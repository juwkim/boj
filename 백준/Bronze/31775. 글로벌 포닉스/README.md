# [Bronze IV] 글로벌 포닉스 - 31775 

[문제 링크](https://www.acmicpc.net/problem/31775) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

구현, 문자열

### 제출 일자

2024년 4월 29일 22:33:29

### 문제 설명

<p>모두가 알다시피, 포닉스는 <strong><em>인류의 삶에 기여하는 가치창출대학</em></strong> 포스텍을 대표하는 마스코트이다! 포닉스는 오늘도 <strong>GLOBAL</strong>하고 새로운 가치를 창출하기 위해 노력하고 있다.</p>

<p>컴퓨터 과학 분야에서, <strong>GLOBAL</strong>한 가치란 단언컨대 ICPC World Finals 진출이다. 포닉스는 포스텍의 ICPC World Finals 진출을 위한 응원 문구를 만들려 한다. 응원 문구는 문자열 세 개로 이루어져 있다. 포닉스의 빅데이터 연구 결과, 세 문자열이 순서와 관계없이 각각 <span style="color:#e74c3c;"><code>l</code></span>, <span style="color:#e74c3c;"><code>k</code></span>, <span style="color:#e74c3c;"><code>p</code></span>로 시작할 경우 포스텍은 ICPC World Finals에 진출할 수 있다. 포닉스는 이러한 응원 문구를 <strong>GLOBAL</strong>한 문구로 부르기로 했다.</p>

<p>포닉스가 정한 세 개의 문자열이 주어질 때, 응원 문구가 <strong>GLOBAL</strong>한지 판단하여라.</p>

### 입력 

 <p>첫 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container>개의 줄에 걸쳐 문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.032em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.032em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.032em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>,</mo><msub><mi>S</mi><mn>2</mn></msub><mo>,</mo><msub><mi>S</mi><mn>3</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S_1, S_2, S_3$</span></mjx-container>이 주어진다.</p>

<p>모든 문자열은 알파벳 소문자 또는 숫자로 이루어진 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container> 이하의 문자열이다.</p>

### 출력 

 <p>세 문자열으로 만든 응원 문구가 <strong>GLOBAL</strong>하면 <span style="color:#e74c3c;"><code>GLOBAL</code></span>을, 아니면 <span style="color:#e74c3c;"><code>PONIX</code></span>를 출력한다.</p>

