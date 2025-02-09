# [Bronze II] Tågväxeln - 26904 

[문제 링크](https://www.acmicpc.net/problem/26904) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

사칙연산, 구현, 수학, 시뮬레이션

### 제출 일자

2025년 2월 9일 20:40:16

### 문제 설명

<p>Växelholm är en väldigt liten stad som ligger långt ute på landet. Den består faktiskt endast av en enda byggnad - Växelholms tågstation. Staden har också bara en invånare, nämligen tågstationens föreståndare, Lokas. </p>

<p>Lokas jobb går i huvudsak ut på att operera stationens manuella tågväxel, så att de två pendeltågen som passerar genom staden åker åt rätt håll. Tågen går periodiskt med <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> respektive <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> minuters mellanrum, med första avgång <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> och <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> minuter <strong>efter midnatt</strong>. Tågen åker alltså ut från stationen åt samma håll men åker sedan ut på två olika spår, som delas upp av en växel.</p>

<p>Nu har Lokas arbetsgivare JS, Järnvägarnas Stat, bestämt att Lokas ska få lön baserat på hur många gånger han måste ändra växeln på en dag. De undrar nu hur många gånger som Lokas måste ändra på växeln under ett helt dygn (dvs 1440 minuter). Tågen avgår alltså bara under minuterna 00:00 till 23:59. </p>

<p>Lokas ska ändra växeln enligt reglerna:</p>

<ol>
	<li>Om ett tåg ska avgå, och växeln är fel inställd, måste Lokas ändra växeln till rätt spår.</li>
	<li>Om båda tåg ska avgå samma minut, så avgår först det tåg som växeln är inställd för, och sedan ska Lokas ändra växeln till det andra tågets spår.</li>
</ol>

<p>I början är växeln inställd på spåret för det tåg som avgår först. </p>

<p>Skriv ett program som beräknar hur många gånger som Lokas måste ändra växeln under ett helt dygn.</p>

### 입력 

 <p>På första raden står två heltal <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> och <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2260"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>,</mo><mi>m</mi><mo>≤</mo><mn>1399</mn><mo>,</mo><mi>n</mi><mo>≠</mo><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq n, m \leq 1399, n \not= m$</span></mjx-container>), perioderna för tågens avgång angivna i minuter.</p>

### 출력 

 <p>Skriv ut ett heltal, minsta antalet gånger som Lokas måste ändra växeln.</p>

