# [Bronze I] 악질 검거 - 31823 

[문제 링크](https://www.acmicpc.net/problem/31823) 

### 성능 요약

메모리: 110536 KB, 시간: 132 ms

### 분류

구현

### 제출 일자

2024년 5월 16일 11:58:44

### 문제 설명

<p>2034년, 국민대학교의 KPSC 동아리는 그 명성이 대단하여 국민대 자체보다도 KPSC가 더 유명해졌다.</p>

<p>이러한 명성 때문에 많은 사람들이 KPSC에 가입하고자 했으나, 동아리의 명성을 유지하기 위해 한정된 인원만 받고 나머지는 모두 탈락시켜 버렸다.</p>

<p>그러나 동아리에 들어온 후 프로그래밍 공부를 소홀히 하며 잠적하는 회원들이 생겨나기 시작했다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/70f4d3d7-7ac4-461a-95dd-3ab335083580/-/preview/"></p>

<p>이러한 상황을 목격한 부동아리장은 분노하여 '리버스-스트릭을 이용한 강퇴'라는 새로운 규칙을 도입하기로 했다. 여기서 '리버스-스트릭'이란, 문제를 며칠 연속으로 풀지 않았는지 보여주는 지표를 의미한다. 즉, 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 107.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container>일 동안 연속해서 문제를 전혀 풀지 않았다면 '리버스-스트릭' <mjx-container class="MathJax" jax="CHTML" style="font-size: 107.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x$</span></mjx-container>일이라고 한다.</p>

<p>부동아리장을 도와 동아리에 들어온 후 잠적하며 동아리 활동을 소홀히 하는 '악질' 회원들을 식별하는 데 도움을 주자!</p>

### 입력 

 <p>첫 번째 줄에는 KPSC 동아리원의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 107.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>과 일별 활동 기록의 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 107.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 107.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>,</mo><mi>M</mi><mo>≤</mo><mn>200</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \leq N, M \leq 200)$</span></mjx-container> </p>

<p>다음 <mjx-container class="MathJax" jax="CHTML" style="font-size: 107.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에는 각 동아리원의 활동 기록과 이름이 공백을 두고 한 줄에 주어진다.</p>

<p>활동기록은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 107.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>개의 문자가 공백으로 구분되어 주어진다. 이중 <mjx-container class="MathJax" jax="CHTML" style="font-size: 107.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 문자가 <code><span style="color:#c0392b;">*</span></code> 라면 <mjx-container class="MathJax" jax="CHTML" style="font-size: 107.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 날에 문제를 풀었다는 것을, <span style="color:#c0392b;"><code>.</code></span> 이라면 <mjx-container class="MathJax" jax="CHTML" style="font-size: 107.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 날에 문제를 풀지 않았다는 것을 의미한다.</p>

<p>이름은 영어 소문자로만 이루어진 1글자 이상 10글자 이하의 문자열로 주어지며, 이름들 사이에는 중복이 없다.</p>

### 출력 

 <p>첫 번째 줄에는 동아리원들의 최장 리버스-스트릭 중 서로 다른 값들의 개수를 출력한다.</p>

<p>다음 줄부터 각 동아리원의 최장 리버스-스트릭과 이름을 입력받은 순서대로 한 줄에 하나씩 출력한다. 여기서, '최장 리버스-스트릭'이란, 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 107.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>일 기간 내에 달성한 '리버스-스트릭' 중 가장 큰 값을 의미한다.</p>

