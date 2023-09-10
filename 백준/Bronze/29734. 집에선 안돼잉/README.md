# [Bronze II] 집에선 안돼잉 - 29734 

[문제 링크](https://www.acmicpc.net/problem/29734) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현, 수학

### 문제 설명

<p>브실이는 해야 할 과제가 있다. 그렇지만 이 외에도 할 일이 너무 많은 브실이는 최대한 빨리 과제를 제출하고 다른 일을 하려고 한다.</p>

<p>집에서 과제를 하면 효율이 너무 떨어진다는 사실은 여러분들도 알고 있을 것이다. 집에는 얼른 드러누워 잠이나 자고 싶은 아늑한 침대, 할 일만 있으면 안 보던 뉴스도 재미있어진다는 텔레비전 등 방해 요소가 너무 많기 때문이다. 하지만 독서실에 가서 과제를 하면 이런 방해 요소가 없기 때문에, 온전히 집중해서 일을 빨리 끝낼 수 있다.</p>

<p>하지만 가끔은 집에서 과제를 하는 것이 더 효율이 좋을 때도 있다. 과제를 끝내는 즉시 바로 뒤에 있는 침대에 눕거나, 유튜브를 켤 수 있기 때문일까? 이상한 일이지만 그런 일도 있는 법이다.</p>

<p>일이 무엇이든, 일을 하다 보면 어느 순간 피곤함이 몰려온다. 졸음을 참으며 일하는 것은 효율이 떨어지기에, 브실이는 일을 8시간 한 뒤에는 잠을 일정 시간 자야 한다. 이는 과제를 할 때도 마찬가지이다. 그러나 독서실에서는 잠을 잘 수 없기에 브실이는 집에 돌아가서 잠을 청하고, 다시 독서실에 출근해 과제를 이어서 해야 한다.</p>

<p>브실이의 생활 패턴을 알고 있는 우리가, 브실이의 워라밸(Work-Life Balance)을 위해 어디서 과제를 하면 좋을지 정해주자!</p>

<p>브실이는 처음에 집에 있다. 또한 과제를 한번 시작하면 다른 장소에서는 과제를 이어서 할 수 없으며, 과제는 마치는 즉시 어디에서나 인터넷을 통해 제출할 수 있다.</p>

### 입력 

 <p>첫 번째 줄에 집에서 과제를 하는 데에 필요한 시간 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, 독서실에서 과제를 하는 데에 필요한 시간 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 공백으로 구분되어 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>,</mo><mi>M</mi><mo>≤</mo><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mn>12</mn></mrow></msup><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \le N, M \le 10^{12})$</span> </mjx-container></p>

<p>두 번째 줄에 브실이가 집에서 독서실로, 또는 독서실에서 집으로 이동하는 데 걸리는 시간 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T$</span></mjx-container>와, 브실이의 수면시간 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>가 공백으로 구분되어 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>T</mi><mo>,</mo><mi>S</mi><mo>≤</mo><mn>10</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \le T, S \le 10\,000)$</span> </mjx-container></p>

### 출력 

 <p>브실이가 집에서 과제를 하는 것이 과제를 더 빠르게 제출할 수 있다면 첫째 줄에 <span style="color:#e74c3c;"><code>Zip</code></span>을, 독서실에서 과제를 하는 것이 과제를 더 빠르게 제출할 수 있다면 첫째 줄에 <span style="color:#e74c3c;"><code>Dok</code></span>을 출력한다.</p>

<p>둘째 줄에는 브실이가 과제를 제출하는 데 걸리는 최소 시간을 출력한다.</p>

<p>집과 독서실 어디에서 공부하든, 과제를 제출하는 데 걸리는 최소 시간이 같은 경우는 주어지지 않는다.</p>

