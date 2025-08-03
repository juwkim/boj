# [Silver I] Plocka Äpplen - 26886 

[문제 링크](https://www.acmicpc.net/problem/26886) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

브루트포스 알고리즘, 백트래킹

### 제출 일자

2025년 8월 4일 05:05:11

### 문제 설명

<p>IOI 2015 avgörs i Almaty, som ungefär betyder "äpplets fader". Olga bor i Almaty, och har en äppelodling med två rader träd. På varje rad finns det <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> träd. Varje träd har ett visst antal mogna äpplen.</p>

<p>Olga börjar besöka trädet i det sydvästra hörnet (det längst till vänster på den undre raden), och plockar alla dessa äpplen. Sedan går hon till ett av de närmsta träden (i norr, öster, väster eller syd) och plockar dess äpplen.</p>

<p>Din uppgift är att beräkna, givet hur många äpplen som är på de olika träden, hur många äpplen Olga sammanlagt kan plocka om hon totalt hinner plocka äpplena från högst <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container> träd.</p>

### 입력 

 <p>Den första raden innehåller heltalen <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> och <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>, separerade med ett blanksteg.</p>

<p>Nästa rad innehåller <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> heltal - antalet äpplen på träden i den norra raden, listade från trädet längst till väst till det längst till öst.</p>

<p>Den tredje och sista raden innehåller också <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> heltal - antalet äpplen på träden i den södra raden.</p>

### 출력 

 <p>Ditt program ska skriva ut ett heltal - antalet äpplen Olga hinner plocka.</p>

