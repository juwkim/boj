# [Bronze I] 치매예방수칙 3.3.3 - 33709 

[문제 링크](https://www.acmicpc.net/problem/33709) 

### 성능 요약

메모리: 108384 KB, 시간: 96 ms

### 분류

사칙연산, 수학, 파싱, 문자열

### 제출 일자

2025년 4월 1일 13:29:24

### 문제 설명

<p>윤수는 산책하던 중 치매 예방 수칙을 홍보하는 포스터를 보게 되었다. 포스터에 적힌 치매 예방 슬로건 "치매 예방 수칙 3.3.3"을 보고, 치매를 예방하는 데 지켜야 할 총 수칙의 개수가 각 수칙을 구분자를 기준으로 분리한 후 모두 더해 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mtext class="mjx-n"><mjx-c class="mjx-c2B"></mjx-c></mjx-mtext><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mtext class="mjx-n"><mjx-c class="mjx-c2B"></mjx-c></mjx-mtext><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mtext>+</mtext><mn>3</mn><mtext>+</mtext><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3 \text{+} 3 \text{+} 3$</span></mjx-container>, 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$9$</span></mjx-container>개임을 알았다. 산책길에 본 다른 포스터들에서는 이 슬로건의 치매 예방 수칙의 개수를 <span style="color:#e74c3c;"><code>.</code></span> 뿐 아니라 <span style="color:#e74c3c;"><code>|</code></span>, <span style="color:#e74c3c;"><code>:</code></span>, <span style="color:#e74c3c;"><code>#</code></span>과 같이 다양한 문자를 사용해 구분하였다. 다양한 치매 예방 수칙 홍보 포스터를 관찰하던 윤수는 포스터의 슬로건이 다음 규칙을 따른다는 사실을 발견하였다.</p>

<ul>
	<li>슬로건의 길이는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1000$</span></mjx-container>자를 넘지 않고, 각 치매 예방 수칙의 개수는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1000$</span></mjx-container>이하이다. 각 치매 예방 수칙은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>으로 시작하지 않는다.</li>
	<li>각 치매 예방 수칙의 개수는 특수문자 한 자로 구분한다. 또한, 슬로건의 시작과 끝은 특수문자가 아니다.</li>
	<li>구분자는 특수문자로 <span style="color:#e74c3c;"><code>.</code></span>, <span style="color:#e74c3c;"><code>|</code></span>, <span style="color:#e74c3c;"><code>:</code></span>, <span style="color:#e74c3c;"><code>#</code></span> 네 가지 중 하나이다.</li>
</ul>

<p>치매 예방 슬로건이 주어졌을 때 치매를 막기 위해 지켜야 할 수칙의 총 개수를 구하시오.</p>

### 입력 

 <p>첫 번째 줄에 치매 예방 슬로건의 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>두 번째 줄에 본문에 주어진 규칙을 따르는 슬로건이 문자열로 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 치매를 막기 위해 지켜야 할 수칙의 총 개수를 출력한다.</p>

