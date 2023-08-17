# [Bronze I] 재우야 임관하자 - 28682 

[문제 링크](https://www.acmicpc.net/problem/28682) 

### 성능 요약

메모리: 13840 KB, 시간: 96 ms

### 분류

애드 혹, 구현, 수학, 확률론

### 문제 설명

<p><u><strong>이 문제는 인터랙티브 문제이다. 아래 노트에 나와 있는 방식으로 입출력을 진행해야 한다.</strong></u></p>

<p>2023년 2학기, 드디어 고려대학교에 드랍(수강포기제)이 부활한다! 이번 학기를 마치고 졸업하는 사이버국방학과 재우는 원래도 DP 문제를 좋아했는데, 최근에 시즌 2가 나온 드라마 <D.P.> 시리즈를 보고 졸업 후 장교로 임관하기로 마음먹었다. 재우는 임관을 위해 최대 3개까지 수강할 수 있는 운동 과목을 수강하기로 했다. <a href="https://www.acmicpc.net/problem/27309">작년에 F를 받은 “수영” 과목</a>의 재수강은 물론, “축구”와 “볼링” 과목까지 최대로 수강하게 되었다.</p>

<p>드랍을 할 수 있는 날이 다가오자, 재우는 갑자기 <a href="https://www.acmicpc.net/problem/27309">작년에 수영을 F 받은 기억</a>이 떠올라 PTSD가 왔다. 이에 재우는 지도 교수님께 면담을 요청했고, 재우의 정보를 보던 교수님께서는 재우가 세 과목 중 두 과목을 F를 받고 한 과목만 <code>Pass</code>를 받을 수 있다는 사실을 알게 되었다. 원래는 이를 알려주면 안되지만, 재우를 딱하게 생각한 교수님은 한 가지 생각을 한다. 바로 재우가 좋아하는 <D.P. 시즌 1>에서 나온 몬티홀 문제로 주기로 한 것이다!</p>

<p>이제 재우는 다음과 같은 과정을 통해 정보를 얻을 수 있다.</p>

<ol>
	<li>먼저, 재우가 <code>Pass</code>로 예상되는 과목 하나를 교수님께 말씀드린다.</li>
	<li>그러면 교수님께서 재우에게 그 과목을 제외한 다른 두 과목 중 F를 받는 과목 하나를 알려주신다.</li>
</ol>

<p>재우는 이 정보를 통해 두 과목을 드랍하고, 남은 한 과목을 수강하기로 하였다. 재우는 남은 한 과목이 <code>Pass</code> 받기를 원한다. 재우가 되어 그 과목을 찾아보자.</p>

<p>총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>500</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\,500$</span></mjx-container>개의 독립적인 평행 세계가 존재해 각 평행 세계의 재우는 위의 결정을 해야 한다. 각각의 평행 세계에 대해 프로그램 시작 시 재우가 <code>Pass</code>를 받을 과목 하나가 독립적으로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mfrac><mjx-frac><mjx-num><mjx-nstrut></mjx-nstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-num><mjx-dbox><mjx-dtable><mjx-line></mjx-line><mjx-row><mjx-den><mjx-dstrut></mjx-dstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>1</mn><mn>3</mn></mfrac></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\frac{1}{3}$</span></mjx-container>의 확률로 결정된다.</p>

<p>각 평행 세계에 대해 위의 1번과 2번 과정은 모두 다른 세계와 독립적으로 진행된다.</p>

<p>아래 인터랙티브 과정을 거쳐 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>500</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\,500$</span></mjx-container>개의 독립적인 평행 세계에 존재하는 재우 중 총 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>900</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$900$</span></mjx-container>명 이상의 최종적으로 예상한 과목이 프로그램이 정한 과목과 같아 재우가 <code>Pass</code>를 받았다면 정답이다. 모든 평행 세계의 행동은 독립적으로 시행된다. 만약 해당 문제의 해답을 모르겠다면, 아래 <strong>노트</strong>를 읽어보자.</p>

### 입력 

 <p>프로그램이 시작되면 먼저 평행 세계의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>500</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n = 1\,500$</span></mjx-container>을 입력받는다.</p>

<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>개의 평행 세계에 대해 <code>Pass</code>로 예상되는 과목을 <span style="color:#e74c3c;"><code>swimming</code></span>, <span style="color:#e74c3c;"><code>bowling</code></span>, <span style="color:#e74c3c;"><code>soccer</code></span> 중 각각 하나씩 골라 한 줄에 공백으로 구분된 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>개의 과목 이름을 출력한다. (이 과정 직후 flush한다)</p>

<p>그럼 프로그램은 각 평행 세계에 대해 고른 과목을 제외한 과목 두 개 중 F인 과목 이름을 하나씩 공백으로 구분하여 준다.</p>

<p>이 정보를 토대로 최종적으로 각 평행 세계에 대해 <code>Pass</code>로 예상되는 과목의 이름을 한 줄에 공백으로 구분하여 출력한다. (이 과정 직후 flush한다)</p>

<p>예제는 평행 세계가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n=4$</span></mjx-container>개 존재할 때의 예시이며 예제는 채점하지 않는다. 실제로 프로그램은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>=</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>500</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n=1\,500$</span></mjx-container>개인 입력에 대해서 정확히 한 번 실행된다.</p>

### 출력 

 Empty

