# [Bronze II] 인경호 울타리 공사 - 33923 

[문제 링크](https://www.acmicpc.net/problem/33923) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 기하학, 많은 조건 분기

### 제출 일자

2025년 5월 20일 10:08:16

### 문제 설명

<p>못된 오리알 도둑이 밤마다 인경호에 몰래 침입해 인덕이들의 알을 훔쳐가기 시작했다! 못된 오리알 도둑을 막기 위해 인덕이들이 힘을 합쳐 인경호에 울타리를 설치하려 한다.</p>

<p>인경호는 세로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개, 가로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>개의 격자점으로 이루어진 직사각형 형태의 호수이며, 상하좌우로 인접한 격자점들 간의 거리는 모두 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>로 동일하다. 인덕이들은 못된 오리알 도둑을 매우 싫어하기에, 인경호의 격자점 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container>개를 각 꼭짓점으로 하는 <strong>가장 큰 정사각형 형태</strong>로 울타리를 설치하려 한다.</p>

<p>울타리 공사 예산이 충분하지 않기 때문에, 울타리는 인경호 바깥으로 이어질 수 없으며 인경호 전체를 감싸는 형태도 될 수 없다. 즉, 다음과 같이 울타리를 설치하는 작업은 울타리가 인경호 전체를 감싸기 때문에 불가능하다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/a3ed51b4-6da5-4528-b1e9-7ad0c56ad668/-/preview/" style="height: 100%; width: 100%; max-width: 400px;"></p>

<p>인덕이들이 인경호에 울타리를 설치할 때, 설치한 울타리를 이용해 만들 수 있는 가장 큰 정사각형의 넓이를 구하시오.</p>

### 입력 

 <p>첫 번째 줄에 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>,</mo><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N, M$</span></mjx-container>이 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>인덕이들이 설치한 울타리를 이용해 만들 수 있는 가장 큰 정사각형의 넓이를 출력한다.</p>

