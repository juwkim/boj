# [Bronze I] Külmkapimagnetid - 29966 

[문제 링크](https://www.acmicpc.net/problem/29966) 

### 성능 요약

메모리: 114328 KB, 시간: 120 ms

### 분류

임의 정밀도 / 큰 수 연산, 그리디 알고리즘

### 제출 일자

2023년 9월 16일 07:18:00

### 문제 설명

<p>Jukul on hulk numbritega külmkapimagneteid. Lisaks on tal üks plussmärgiga magnet.</p>

<p>Ta tahab panna kõik oma magnetid ritta nii, et tulemusena saadud avaldise väärtus oleks võimalikult väike. Arvud avaldises võivad alata ka nullidega (näiteks <code>00042</code>).</p>

### 입력 

 <p>Tekstifaili esimesel real on numbrimagnetite arv <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>10</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \le N \le 10\,000$</span></mjx-container>) ja teisel real sõne pikkusega <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, mis koosneb ainult numbritest <code>0</code><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2026"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>…</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\ldots$</span> </mjx-container><code>9</code> --- need on kõik Juku numbrimagnetid suvalises järjekorras.</p>

### 출력 

 <p>Tekstifaili ainsale reale väljastada üks mittenegatiivne täisarv: avaldise minimaalne võimalik väärtus.</p>

