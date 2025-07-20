# [Bronze III] Dviračių lenktynės - 30077 

[문제 링크](https://www.acmicpc.net/problem/30077) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

수학, 구현, 브루트포스 알고리즘, 사칙연산

### 제출 일자

2025년 7월 21일 03:10:04

### 문제 설명

<p>Bitų karalystėje vyksta dviračių treko lenktynės. Visi dviratininkai startuoja vienu metu ir važiuoja <mjx-container class="MathJax" jax="CHTML" style="font-size: 101.8%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> ratų. Jei kurį lenktynininką ratu aplenkia kitas, aplenktasis toliau varžybų nebetęsia. Jei sportininkas, kirsdamas finišo liniją, aplenkia varžovą ratu, aplenktasis taip pat iškrenta iš varžybų.</p>

<p>Žinodami, per kiek laiko kiekvienas dviratininkas įveikia vieną treko ratą bei kiek ratų trunka lenktynės, raskite, kiek dalyvių nebus aplenkti ratu ir finišuos varžybose.</p>

### 입력 

 <p>Pirmojoje eilutėje pateikti trys natūralieji skaičiai atskirti tarpu:</p>

<ul>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 101.8%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> – lenktynininkų skaičius;</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 101.8%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> – varžybų trukmė ratais;</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 101.8%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$L$</span></mjx-container> – treko rato ilgis metrais.</li>
</ul>

<p>Kitose <mjx-container class="MathJax" jax="CHTML" style="font-size: 101.8%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> eilučių pateikta, per kiek sekundžių (<mjx-container class="MathJax" jax="CHTML" style="font-size: 101.8%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.12em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T_i$</span></mjx-container>) kiekvienas iš sportininkų įveikia vieną treko ratą. <mjx-container class="MathJax" jax="CHTML" style="font-size: 101.8%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.12em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>T</mi><mi>i</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$T_i$</span></mjx-container> - natūralusis.</p>

### 출력 

 <p>Išveskite sportininkų, kurie nebuvo aplenkti ratu ir baigė varžybas, skaičių.</p>

