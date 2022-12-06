# [Silver IV] blobnom - 24498 

[문제 링크](https://www.acmicpc.net/problem/24498) 

### 성능 요약

메모리: 261704 KB, 시간: 432 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>블롭들은 심심해서 서로를 이용해 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml></mjx-container>개의 탑을 만들었다. 각 탑의 높이는 그 탑에 있는 블롭의 수와 같다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e2a1544d-acfb-4160-a6a9-f58e7b73f7ae/-/preview/" style="display: inline-block; width: 50%; max-width: 256px;"></p>

<p>여러분은 다음 행동을 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml></mjx-container>회 이상 할 수 있다.</p>

<ol>
	<li>처음과 마지막이 아닌 탑 중 하나를 선택한다. 단, 선택한 탑과 인접한 두 탑의 높이가 모두 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml></mjx-container> 이상이어야 한다.</li>
	<li>선택한 탑과 인접한 두 탑에 있는 블롭을 한 마리씩 각각 땅에 내려놓는다. 즉, 인접한 두 탑의 높이가 모두 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml></mjx-container>만큼 감소한다.</li>
	<li>땅에 내려놓은 두 마리의 블롭 중 하나의 블롭만 1.에서 선택한 탑에 쌓는다. 즉, 선택한 탑의 높이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml></mjx-container>만큼 증가한다.</li>
</ol>

<p>이 과정에서 이전에 인접하지 않았던 두 탑이 새롭게 인접하게 되지는 않는다. 채완이를 위해 만들 수 있는 가장 높은 탑의 높이를 구해 주자.</p>

### 입력 

 <p>첫째 줄에 탑의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml></mjx-container>이 주어진다.</p>

<p>둘째 줄에 각 탑의 높이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><span aria-hidden="true" class="no-mathjax mjx-copytext">$A_1, A_2, \cdots, A_N$</span></mjx-container>이 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>문제의 정답을 출력한다.</p>

