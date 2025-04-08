# [Silver I] K 물류창고 - 23350 

[문제 링크](https://www.acmicpc.net/problem/23350) 

### 성능 요약

메모리: 112304 KB, 시간: 112 ms

### 분류

자료 구조, 구현, 큐, 시뮬레이션

### 제출 일자

2025년 4월 8일 11:41:18

### 문제 설명

<p>K사의 물류창고를 운영하는 도커 씨는 오늘 발주를 처리하기 위해 N 개의 컨테이너들을 적재해야 한다. 도커씨는 이 일을 하나의 로봇을 이용해 처리하려 한다. 로봇은 컨테이너를 옮길 때마다 컨테이너의 무게만큼 비용을 발생시킨다.</p>

<p>컨테이너마다 우선순위가 있는데 우선순위는 1 이상 M 이하의 정수로 표현된다. 우선순위가 1에 가까울 수록 높은 우선순위를 가지고, M에 가까울 수록 낮은 우선순위를 가진다. M개의 각 우선순위에 대하여 해당 우선순위를 갖는 컨테이너가 적어도 하나 존재한다.</p>

<p>컨테이너는 레일을 통해 하나씩 오고, 우선순위가 낮은 컨테이너를 먼저 적재한다. 낮은 우선순위의 컨테이너들이 모두 적재되지 않은 상태에서 높은 우선순위의 컨테이너가 온다면 레일의 처음으로 보낸다. 레일의 처음으로 보낼 때, 컨테이너의 무게만큼 비용이 발생한다. 낮은 우선순위의 컨테이너가 온다면, 무조건 적재한다.</p>

<p>컨테이너의 우선순위가 같을 땐, 무게가 무거운 컨테이너를 아래에 위치시킨다.</p>

<p>컨테이너의 우선순위가 같으면서 무게도 같은 경우는 어느 것이 위에 있어도 상관없다.</p>

<p>우선순위는 같으나, 무게가 가벼운 컨테이너가 먼저 적재돼 있을 경우, 가벼운 컨테이너가 무거운 컨테이너 위로 갈 수 있도록 컨테이너를 빼내고 다시 적재한다. 이 과정을, 가벼운 컨테이너가 모두 빠질 때까지 반복한다. 이 과정에서 컨테이너를 뺄 때와 적재될 때 컨테이너의 무게만큼 비용이 발생한다.</p>

<p>작업이 모두 끝난 후 도커 씨가 부담해야 할 비용을 출력하자.</p>

### 입력 

 <p>첫째 줄엔 컨테이너의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>과 우선순위의 종류 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>M</mi><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le M \le N \le 100$</span></mjx-container>)</p>

<p>2번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>+</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N + 1$</span></mjx-container>번째 줄까지는 컨테이너들의 우선순위 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D443 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$P$</span></mjx-container>(<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D443 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>P</mi><mo>≤</mo><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le P \le M$</span></mjx-container>), 무게 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>W</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$W$</span></mjx-container>(<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44A TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>W</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le W \le 100$</span></mjx-container>)가 순서대로 주어진다.</p>

<p>레일에 배치되는 순서는 입력으로 주어지는 컨테이너의 순서와 동일하다.</p>

<p>모든 입력은 1 이상의 정수이다.</p>

### 출력 

 <p>로봇이 들어올린 무게들의 합을 출력한다.</p>

