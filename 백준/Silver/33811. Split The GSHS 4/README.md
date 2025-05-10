# [Silver II] Split The GSHS 4 - 33811 

[문제 링크](https://www.acmicpc.net/problem/33811) 

### 성능 요약

메모리: 111784 KB, 시간: 112 ms

### 분류

다이나믹 프로그래밍, 문자열, 최대 부분 배열 문제

### 제출 일자

2025년 5월 11일 03:14:20

### 문제 설명

<p>경기도의 명소 경기과학고등학교에는 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 역사 깊은 문자열이 있습니다. 이 문자열은 <code>G, S, H</code>로만 이루어져 있어 문자열의 중간에 <code>GSHS</code>가 부분 문자열로 포함되어 있습니다.</p>

<p>하지만, 설곽이는 이 문자열의 중간에 <code>SSHS</code>라는 문자열도 부분 문자열로 포함되어 있음을 깨달았습니다. 그래서 설곽이는 이 역사 깊은 문자열을 쪼개서 부분 문자열을 얻어 서울과학고등학교의 역사 깊은 문자열로 만들려고 합니다. 문자열의 앞과 뒤에서 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>개 이상의 글자를 지워 얻을 수 있는 문자열을 부분 문자열이라 합니다.</p>

<p>설곽이는 이 부분 문자열이 서울과학고등학교를 대표해야 하므로, 문자열 내부에서 (<code>SSHS의 개수</code>) <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$-$</span></mjx-container> (<code>GSHS의 개수</code>)를 최대화하려고 합니다. 가능한 개수 차의 최댓값을 구하는 코드를 작성하세요.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/368d57e2-c8b4-4d00-86be-fc68592bd918/-/preview/" style="width: 280px; height: 200px;"></p>

### 입력 

 <p>첫째 줄에 문자열의 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어집니다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>500</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 500\,000$</span></mjx-container>) 둘째 줄에 <code>G, S, H</code>로 구성된 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 문자열이 주어집니다.</p>

### 출력 

 <p>첫째 줄에 모든 부분 문자열 중 (<code>SSHS의 개수</code>) <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$-$</span></mjx-container> (<code>GSHS의 개수</code>)의 최댓값을 출력합니다.</p>

