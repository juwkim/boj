# [Silver II] Bierki - 8637 

[문제 링크](https://www.acmicpc.net/problem/8637) 

### 성능 요약

메모리: 112592 KB, 시간: 100 ms

### 분류

이분 탐색, 기하학, 두 포인터

### 제출 일자

2025년 3월 13일 01:38:24

### 문제 설명

<p>Jaś lubi budować trójkąty z bierek. W tym celu trzyma je w worku, z którego wybiera trzy bierki na chybił-trafił. Bierki mogą mieć różne długości i nie zawsze Jaś może zbudować trójkąt, a wtedy wpada w histerię. Mama Jasia ma dość histerycznych napadów synka i dlatego poprosiła Ciebie o pomoc. Należy odrzucić niektóre bierki w taki sposób, aby z pozostałych zawsze dało się ułożyć trójkąt, jednocześnie zostawiając jak najwięcej bierek w worku.</p>

<p>Opracuj program, który:</p>

<ul>
	<li>wczyta ze standardowego wejścia liczbę bierek w worku oraz ich długości,</li>
	<li>obliczy największa˛ liczbę bierek, którą można pozostawić w worku, tak żeby z każdych trzech z nich można było utworzyć trójkąt,</li>
	<li>wypisze wynik na standardowe wyjście.</li>
</ul>

### 입력 

 <p>W pierwszym wierszu zapisano liczbę <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>30</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5 ≤ N ≤ 30\,000$</span></mjx-container>), oznaczającą liczbę bierek w worku. W każdym z następnych <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> wierszy zapisano długość jednej bierki. Długość bierki jest liczbą całkowitą z przedziału <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c5B"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c2E"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2E"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c2E"></mjx-c><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c5D"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">[</mo><mn>1.</mn><mo>.</mo><mn>.500</mn><mo stretchy="false">]</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$[1...500]$</span></mjx-container>.</p>

### 출력 

 <p>W pierwszym wierszu wypisz liczbę bierek, które powinny zostać w worku.</p>

