# [Bronze III] 팀명 정하기 - 28114 

[문제 링크](https://www.acmicpc.net/problem/28114) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현

### 문제 설명

<blockquote>
<p>현대 모비스는 모빌리티 SW 해커톤, 알고리즘 경진대회, 채용 연계형 SW 아카데미 등 다양한 SW 인재 발굴 프로그램을 진행하고 있다. 지난 2월에 개최된 모빌리티 SW 해커톤은 국내 14개 대학의 소프트웨어 동아리 20개 팀, 70여 명이 참여해 모빌리티 소프트웨어 개발 실력을 겨뤘다.</p>
</blockquote>

<p>숭실대학교 컴퓨터학부 문제해결 소모임 SCCC 부원들은 매년 모빌리티 SW 해커톤, SCON, ICPC와 같은 팀 대회에서 사용할 팀명을 정하기 위해 많은 고민을 한다. 졸업을 한 학기 남겨둔 성서는 더 이상 부원들이 팀명으로 고통을 받지 않도록 가이드라인을 만들었다.</p>

<p>성서의 가이드라인에 따르면 팀 이름을 짓는 방법은 두 가지가 있다.</p>

<ol>
	<li>세 참가자의 입학 연도를 100으로 나눈 나머지를 오름차순으로 정렬해서 이어 붙인 문자열</li>
	<li>세 참가자 중 성씨를 영문으로 표기했을 때의 첫 글자를 백준 온라인 저지에서 해결한 문제가 많은 사람부터 차례대로 나열한 문자열</li>
</ol>

<p>예를 들어 600문제를 해결한 18학번 안(AHN)씨, 2000문제를 해결한 19학번 이(LEE)씨, 6000문제를 해결한 20학번 오(OH)씨로 구성된 팀을 생각해 보자. 첫 번째 방법으로 팀명을 만들면 181920이 되고, 두 번째 방법으로 팀명을 만들면 OLA가 된다.</p>

<p>2000문제를 해결한 19학번 이(LEE)씨, 9000문제를 21학번 나(NAH)씨, 1000문제를 해결한 22학번 박(PARK)씨로 구성된 팀은 첫 번째 방법으로 팀명을 만들면 192122가 되고, 두 번째 방법으로 팀명을 만들면 NLP가 된다.</p>

<p>세 팀원의 백준 온라인 저지에서 해결한 문제의 개수, 입학 연도, 그리고 성씨가 주어지면 첫 번째 방법과 두 번째 방법으로 만들어지는 팀명을 차례대로 출력하는 프로그램을 작성하라.</p>

### 입력 

 <p>첫째 줄에 첫 번째 팀원이 백준 온라인 저지에서 해결한 문제의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D443 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.109em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>1</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$P_1$</span></mjx-container>, 입학 연도 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44C TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.182em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Y</mi><mn>1</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$Y_1$</span></mjx-container>, 성씨 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.032em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>S</mi><mn>1</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S_1$</span></mjx-container>이 공백으로 구분되어 주어진다.</p>

<p>둘째 줄과 셋째 줄에는 두 번째 팀원의 정보 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D443 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.109em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44C TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.182em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.032em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>2</mn></msub><mo>,</mo><msub><mi>Y</mi><mn>2</mn></msub><mo>,</mo><msub><mi>S</mi><mn>2</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$P_2,Y_2,S_2$</span></mjx-container>와 세 번째 팀원의 정보 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D443 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.109em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44C TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.182em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.032em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mn>3</mn></msub><mo>,</mo><msub><mi>Y</mi><mn>3</mn></msub><mo>,</mo><msub><mi>S</mi><mn>3</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$P_3,Y_3,S_3$</span></mjx-container>이 첫째 줄과 같은 형식으로 주어진다.</p>

### 출력 

 <p>첫째 줄에 첫 번째 방법으로 만든 팀명을 출력한다.</p>

<p>둘째 줄에 두 번째 방법으로 만든 팀명을 출력한다.</p>

