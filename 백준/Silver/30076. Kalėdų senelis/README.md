# [Silver III] Kalėdų senelis - 30076 

[문제 링크](https://www.acmicpc.net/problem/30076) 

### 성능 요약

메모리: 109240 KB, 시간: 120 ms

### 분류

그리디 알고리즘, 구현, 시뮬레이션

### 제출 일자

2024년 6월 22일 22:48:46

### 문제 설명

<p>Greitai Kalėdos. Elniai jau pakinkyti ir Kalėdų senelis beveik pasiruošęs traukti į kelionę, tik dovanos dar nesukrautos.</p>

<p>Nors rogėse telpa be galo daug dovanų, bet sunkias roges tempiantis kinkinys greitai pavargsta, todėl dovanų reikia krauti kiek galima mažiau.</p>

<p>Tai žinodami nykštukai Kalėdų senelio mašrute ant namų stogų įrengė dovanų slėptuves.</p>

<p>Kalėdų senelis gali pasikrauti dovanų savo trobelėje (t.y. pradiniame taške), o taip pat bet kurioje slėptuvėje.</p>

<p>Žinodami, kiek vaikų turi aplankyti Kalėdų senelis, patarkite, kiek dovanų jam reikia įkrauti į roges savo trobelėje bei kiekvienoje slėptuvėje, kad jų kiekis rogėse visada būtų kuo mažesnis.</p>

<p>Keliaudamas Kalėdų senelis:</p>

<ul>
	<li>lanko vaikus namų numerių didėjimo tvarka, pradėdamas nuo pirmojo;</li>
	<li>negali apgręžti rogių atgal iki neaplanko visų vaikų;</li>
	<li>jei ant namo stogo yra įrengta slėptuvė, jis pirma joje pasipildo roges dovanų, o tuomet neša dovaną tame name gyvenančiam vaikui.</li>
</ul>

<p>Visi vaikai gyvena skirtinguose namuose ir kiekvienam jų atneš vieną dovaną.</p>

### 입력 

 <p>Pirmojoje eilutėje pateikti du sveikieji skaičiai:</p>

<ul>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> – vaikų skaičius;</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> – dovanų slėptuvių skaičius.</li>
</ul>

<p>Kitose <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> eilučių pateikta po du skaičius:</p>

<ul>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.04em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>K</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K_i$</span></mjx-container> – ant kelinto vaiko namo stogo įrengta slėptuvė. Duomenys pateikti <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.04em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>K</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K_i$</span></mjx-container> didėjimo tvarka;</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44D TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.04em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>Z</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$Z_i$</span></mjx-container> – dovanų skaičius šiame sandėlyje.</li>
</ul>

<p>Pradiniame taške yra Kalėdų senelio trobelė, joje yra be galo daug dovanų.</p>

### 출력 

 <p>Išveskite <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi><mo>+</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M + 1$</span></mjx-container> skaičių skirtingose eilutėse. Pirmojoje eilutėje nurodykite, kiek dovanų reikia įsidėti prieš pradedant kelionę. Kitose <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> eilučių išveskite, kiek dovanų reikia pasikrauti kiekvienoje slėptuvėje (rezultatai pateikiami ta tvarka, kokia slėptuvės pateiktos pradiniuose duomenyse).</p>

