# [Silver IV] You’ve goat me stumped - 20273 

[문제 링크](https://www.acmicpc.net/problem/20273) 

### 성능 요약

메모리: 114844 KB, 시간: 208 ms

### 분류

기하학, 수학

### 문제 설명

<p>When leaving goats to graze in a field, in order to ensure that they remain in place, it is customary to drive a wooden stake in the middle of the field and tether the goat to it to ensure that it does not run away. This allows the goat to roam within a disk-shaped pasture.</p>

<p>In the far region of Straitmeadows, the fields are long and narrow. This odd geometry has led to an even more peculiar habit of the shepherds. They put a collar on the goat and pass a rope through it (so that the rope can move freely), and they then tie each end of the rope to a stake. This allows the goat to move along the rope but remain sufficiently close to the two stakes.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/343e1a10-5cbe-44ae-a76a-bd33ca89482d/-/preview/" style="width: 333px; height: 138px;"></p>

<p>To ensure the goat doesn't starve, the shepherds need to know (very roughly) which area of grass the goat can graze in this fashion. You will assume that the goat and the stakes are 0-dimensional objects, that the rope is 1-dimensional, and that the field is a plane.</p>

### 입력 

 <p>The input file consists of multiple test cases. The first line of the input file consists of a single integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$c$</span></mjx-container> indicating the number of test cases. Each test case follows and consists of a single line which consists of two integers <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c2113"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ℓ</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\ell$</span></mjx-container> and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$r$</span></mjx-container> separated by a single space. The integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c2113"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>ℓ</mi><mo>≤</mo><mn>30</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \leq \ell \leq 30$</span></mjx-container> indicates the distance between the two stakes in meters. The integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c2113"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ℓ</mi><mo>≤</mo><mi>r</mi><mo>≤</mo><mn>50</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\ell \leq r \leq 50$</span></mjx-container> indicates the length of the rope in meters. </p>

### 출력 

 <p>For each test case in the input, your program should produce one line consisting of a single integer which is the area of pasture that the goat can graze, rounded to the nearest hundred of square meters.</p>

