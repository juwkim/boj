# [Silver V] Napor - 28711 

[문제 링크](https://www.acmicpc.net/problem/28711) 

### 성능 요약

메모리: 110432 KB, 시간: 120 ms

### 분류

문자열

### 제출 일자

2024년 3월 30일 07:50:09

### 문제 설명

<p>Opasni hakeri, poznati pod kodnim imenom <em>Haribo s votkom</em>, pokušavaju pronaći posljednju zastavicu, ali to ne ide onako kako su očekivali...</p>

<p>U njihove ruke dospjelo je <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> linija teksta, naizgled nasumičnih znakova. Ali oni znaju da se u njima kriju brojevi koji su im prijeko potrebni.</p>

<p>Svaka od linija sastoji se isključivo od malih slova engleske abecede i znamenki, a znamenke čine tražene brojeve. Svaki broj iz teksta je jednoznačno određen, omeđen je ili slovima ili krajevima linije. Pritom broj može imati vodeće nule, ali njih je potrebno izostaviti.</p>

<p>Dodatno, jednom kad nađu sve brojeve, hakeri ih trebaju posložiti u <strong>neopadajući</strong> poredak kako bi ih mogli dalje iskoristiti.</p>

<p>Nažalost, ovo je tek djelić posla koji moraju obaviti, no ovo je savršena prilika da vi uskočite i pomognete ovom super timu. Pronađite tražene brojeve i ispišite ih u neopadajućem poretku.</p>

### 입력 

 <p>U prvom retku je prirodan broj <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ n ≤ 100$</span></mjx-container>), broj linija teksta.</p>

<p>Slijedi <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> redaka od koji se svaki sastoji isključivo od malih slova engleske abecede i znamenki, a njegova duljina je najviše <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container>.</p>

### 출력 

 <p>Ispišite nađene brojeve u neopadajućem poretku, svaki u svom retku.</p>

