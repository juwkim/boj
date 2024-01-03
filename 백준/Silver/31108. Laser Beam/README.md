# [Silver IV] Laser Beam - 31108 

[문제 링크](https://www.acmicpc.net/problem/31108) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

사칙연산, 기하학, 수학

### 제출 일자

2024년 1월 4일 01:53:31

### 문제 설명

<p>There are two infinite flat mirrors located at an angle <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D6FC TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\alpha$</span></mjx-container> relative to each other so that they can be considered as rays on the plane when viewed from the side. Through a tiny hole in one of the mirrors, a laser beam is launched at an angle <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D6FD TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\beta$</span></mjx-container> as shown in the figure below:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/567f4721-c70d-4626-862c-95eb3f248572/-/preview/" style="width: 250px; height: 142px;"></p>

<p>Your task is to count the number of reflections of the laser beam from the mirrors before it goes to infinity. The angle of incidence of the beam on the mirror always coincides with the angle of reflection. The hole through which the beam is launched is extremely small, so we can assume that if the beam suddenly hits the hole, it will still be completely reflected according to the usual rules.</p>

### 입력 

 <p>Given two integers <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D6FC TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>α</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\alpha$</span></mjx-container> and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D6FD TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>β</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\beta$</span></mjx-container> --- angles given in degrees (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D6FC TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c37"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>α</mi><mo>≤</mo><mn>179</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le \alpha \le 179$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D6FD TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c37"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>β</mi><mo>≤</mo><mn>179</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le \beta \le 179$</span></mjx-container>).</p>

### 출력 

 <p>Print one integer --- the number of reflections.</p>

