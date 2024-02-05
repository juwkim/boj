# [Silver III] Kulramen - 21282 

[문제 링크](https://www.acmicpc.net/problem/21282) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

구현, 수학

### 제출 일자

2024년 2월 6일 04:12:00

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/9f712b98-1001-4f96-9d0b-3f3e65512d40/-/preview/" style="width: 387px; height: 100px;"></p>

<p style="text-align: center;">Figur 2. Så här kunde Simons kulram (med <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D445 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mo>=</mo><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$R=4$</span></mjx-container>) se ut innan han började äta upp kulorna. Då var det lätt att översätta ställningen till ett decimaltal.</p>

<p>Lille Simon har fått en kulram i present. Kulramen har <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D445 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$R$</span></mjx-container> rader och i varje rad fanns från början 9 kulor, så att man kunde representera <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D445 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$R$</span></mjx-container>-siffriga decimaltal -- en siffra på varje rad. Om en rad hade <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$X$</span></mjx-container> kulor på vänstra sidan, sedan ett mellanrum och övriga kulor på höger sida representerade raden siffran X.</p>

<p>Tyvärr tyckte Simon att kulorna på ramen såg väldigt smaskiga ut, och åt helt enkelt upp några kulor. Det finns dock minst en kula kvar på varje rad.</p>

<p>Simon lärde sig snabbt att räkna på sin nya kulram. Han representerar talet där alla kulor är på högersidan som talet 0, och adderar sedan 1 precis som han hade gjort på en vanlig kulram, genom att flytta en kula från höger till vänster på den nedersta raden som har någon kula kvar på höger sida (låt oss kalla den <em>flyttningsraden</em>) samt flytta alla kulor på raderna nedanför flyttningsraden till höger sida (om inte flyttningsraden är den nedersta raden). Om 1 adderas när alla kulorna på <em>alla</em> rader redan är på vänster sida (så att det inte finns någon flyttningsrad) blir resultatet 0.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/d0e8f205-3e2c-4bfb-a39a-9fbab5749a08/-/preview/" style="width: 510px; height: 300px;"></p>

<p style="text-align: center;">Figur 3. Några exempel på hur Simon adderar 1 på den kulram som återfinns i de två första exemplen. Dubbelpilen markerar "flyttningsraden" vid de olika additionerna.</p>

<p>Simon håller på att räkna sandkornen i sin sandlåda och skulle behöva hjälp att skriva ett program som, givet ett visst utgångsläge på kulramen, räknar ut hur kulramen ser ut när han <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> gånger har adderat 1.</p>

### 입력 

 <p>På första raden står antalet rader <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D445 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$R$</span></mjx-container>. Därefter följer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D445 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$R$</span></mjx-container> rader med vardera två heltal, antalet kulor till vänster respektive höger på varje rad (uppifrån och ned). Slutligen finns en rad med det positiva heltalet <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>. </p>

### 출력 

 <p>Programmet ska skriva ut <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D445 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$R$</span></mjx-container> rader med två tal på varje rad: antalet kulor till vänster respektive höger på varje rad efter additionerna.</p>

