# [Silver IV] 선택의 기로 - 30970 

[문제 링크](https://www.acmicpc.net/problem/30970) 

### 성능 요약

메모리: 133724 KB, 시간: 588 ms

### 분류

정렬

### 제출 일자

2023년 12월 24일 03:22:14

### 문제 설명

<figure style="float: right; text-align: center;"><img alt="촉석루 사진" src="https://upload.acmicpc.net/5074acea-f512-48db-8b0a-c5134e706bf4/-/preview/" style="height: 180px; margin-left: 40px;">
<figcaption><strong>[사진]</strong> 촉석루</figcaption>
</figure>

<blockquote>
<p>품질이냐 가격이냐, 그것이 문제로다..</p>
</blockquote>

<p>진주 나들이를 온 보선이는 기념품으로 촉석루 미니어처를 사기로 했다. 촉석루는 진주성에 있는 누각이며 경상남도 유형문화재 중 하나로, 진주성의 남쪽 지휘대로 사용됨과 동시에 논개가 촉석루 앞 의암에서 순국한 것으로 알려져 유명한 곳이다.</p>

<p>촉석루 미니어처를 사기 위해 기념품 가게에 들른 보선이는 놀라움을 금치 못했다. 왜냐하면, 가게에는 각양각색의 촉석루 미니어처가 진열되어 있었기 때문이다. 그리고 모든 촉석루 미니어처는 장인이 한 땀 한 땀 심혈을 기울여서 만들어서 그런지 품질과 가격이 천차만별이었고, <strong>품질과 가격이 전부 동일한 두 촉석루 미니어처는 없었다.</strong> 각양각색의 촉석루 미니어처를 본 보선이는 물욕이 폭발할 뻔했지만 가까스로 마음을 진정시키고, 촉석루 미니어처를 두 개만 사기로 했다. 보선이는 두 가지 방법으로 촉석루 미니어처를 골라보기로 했는데, 이는 다음과 같다.</p>

<ul>
	<li>진열되어 있는 촉석루 미니어처 중에서 품질이 가장 높은 촉석루 미니어처를 골라 가져온다. 만약 그런 미니어처가 여러 개라면 가격이 가장 낮은 것을 골라 가져온다. 이 과정을 두 번 반복하는 것이 첫 번째 방법이다.</li>
	<li>진열되어 있는 촉석루 미니어처 중에서 가격이 가장 낮은 촉석루 미니어처를 골라 가져온다. 만약 그런 미니어처가 여러 개라면 품질이 가장 높은 것을 골라 가져온다. 이 과정을 두 번 반복하는 것이 두 번째 방법이다.</li>
</ul>

<p>보선이가 각 방법에 따라 촉석루 미니어처들을 고르게 될 때 어떤 촉석루 미니어처들을 고르게 되는지 알아보자.</p>

### 입력 

 <p>첫 번째 줄에는 기념품 가게에 진열되어 있는 촉석루 미니어처의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>2</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(2 ≤ N ≤ 100\,000)$</span> </mjx-container></p>

<p>두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에 걸쳐 가게에 진열되어 있는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>번째 촉석루 미니어처 종류의 품질 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D444 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Q</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$Q_i$</span></mjx-container>, 가격 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D443 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.109em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>P</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$P_i$</span></mjx-container>가 공백으로 구분되어 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msub space="4"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D444 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D443 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.109em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><msub><mi>Q</mi><mi>i</mi></msub><mo>,</mo><msub><mi>P</mi><mi>i</mi></msub><mo>≤</mo><mn>10</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 ≤ Q_i, P_i ≤ 10\,000)$</span> </mjx-container></p>

<p>입력으로 주어지는 모든 수는 정수이다.</p>

### 출력 

 <p>첫 번째 줄에는 첫 번째 방법을 선택했을 때의 첫 번째로 고른 촉석루 미니어처의 품질과 가격, 두 번째로 고른 촉석루 미니어처의 품질과 가격을 공백으로 구분하여 순서대로 출력한다.</p>

<p>두 번째 줄에는 두 번째 방법을 선택했을 때의 첫 번째로 고른 촉석루 미니어처의 품질과 가격, 두 번째로 고른 촉석루 미니어처의 품질과 가격을 공백으로 구분하여 순서대로 출력한다.</p>

<p><strong>첫 번째 방법의 결과가 두 번째 방법의 결과에 영향을 미치지 않는다.</strong></p>

