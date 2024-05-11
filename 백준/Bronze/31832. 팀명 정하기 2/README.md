# [Bronze II] 팀명 정하기 2 - 31832 

[문제 링크](https://www.acmicpc.net/problem/31832) 

### 성능 요약

메모리: 109240 KB, 시간: 112 ms

### 분류

구현, 문자열

### 제출 일자

2024년 5월 12일 05:31:02

### 문제 설명

<p>숭실대학교 컴퓨터학부 문제해결 소모임 SCCC 부원들은 매년 SCON, ICPC와 같은 팀 대회에서 사용할 팀명을 정하기 위해 많은 고민을 한다. 특히 여러 개의 후보 중에서 실제로 사용할 팀명 하나를 정하는 것이 어렵기 때문에, 졸업을 두 학기 남겨둔 정휘는 더 이상 부원들이 고통을 받지 않도록 가이드라인을 만들었다.</p>

<p>정휘의 가이드라인에 따르면 아래 조건 중 만족하는 조건의 개수가 많을수록 좋은 팀명이다.</p>

<ul>
	<li>알파벳 대문자보다는 소문자가 귀엽다. 따라서 대문자가 소문자보다 더 많이 등장하면 안 된다.</li>
	<li>팀명이 너무 복잡하면 사회자가 제대로 읽지 못할 수 있다. 따라서 팀명은 10글자 이하로 지어야 한다.</li>
	<li>숫자로만 구성된 팀명은 월드 파이널에 진출하지 못하는 징크스가 있다. 따라서 팀명에는 숫자가 아닌 글자가 하나 이상 포함되어 있어야 한다.</li>
</ul>

<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 팀명 후보가 주어진다. 가이드라인에서 제시한 세 가지 조건을 모두 만족하는 팀명을 출력하는 프로그램을 작성해 보자.</p>

### 입력 

 <p>첫째 줄에 팀명 후보의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>둘째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에 걸쳐 팀명의 후보 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.032em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.032em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c22EF"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.032em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub><mo>,</mo><msub><mi>S</mi><mn>2</mn></msub><mo>,</mo><mo>⋯</mo><mo>,</mo><msub><mi>S</mi><mi>N</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S_1,S_2,\cdots ,S_N$</span></mjx-container>이 한 줄에 하나씩 주어진다.</p>

### 출력 

 <p>세 가지 조건을 모두 만족하는 팀명을 출력한다.</p>

