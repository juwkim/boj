# [Silver II] EGIPAT - 28389 

[문제 링크](https://www.acmicpc.net/problem/28389) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

깊이 우선 탐색, 그래프 이론, 그래프 탐색, 구현, 시뮬레이션

### 제출 일자

2025년 3월 21일 06:09:16

### 문제 설명

<p>Senzacionalna vijest! U Egiptu je otkrivena nova piramida! Najzanimljiviji dio znanstvenicima su crteži na zidovima piramide. Velik dio unutrašnjih zidova prekriven je nekim čudnim crtežima kocaka i tablica brojeva. Čini se kao da su crteži i tablice nekako povezani, no znanstvenici još nisu sigurni kako. Tako dugo dok oni ne pronađu vezu, najbitniji crtež će biti onaj koji se nalazio u jednom mračnom kutku piramide. Naime, njegova važnost proizlazi iz toga da nam on ukazuje kako su već drevni Egipćani posjedovali robote.</p>

<p>Taj crtež je u obliku tablice znakova i na njemu je prikazano kretanje robota. Pretpostavlja se da je faraon robotu izdavao naredbe u obliku “POMAKNI SE DOLJE/GORE/LIJEVO/DESNO”, a njegovi pomoćnici su crtali gdje se robot kretao.</p>

<p>Znanstvenici bi sada htjeli iz crteža odrediti naredbe koje je izgovarao faraon pa mole tebe da napišeš program za taj problem. Također, oni znaju da robot nikada nije stao na neko polje dvaput.</p>

### 입력 

 <p>U prvom se retku nalaze prirodni brojevi <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> i <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>,</mo><mi>M</mi><mo>≤</mo><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ N, M ≤ 10$</span></mjx-container>), broj redaka i stupaca tablice.</p>

<p>U sljedećih <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> redaka nalazi se po <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> znakova. Jedini znakovi koji će se pojavljivati su ‘P’, ‘.’ i ‘x’. ‘P’ će se pojaviti jednom i označava početnu poziciju robota, ‘.’ označava slobodno polje, dok ‘x’ označava polje na koje je robot nekad stao. Samo jedan ‘x’ će biti susjedan ‘P’ i najviše dva ‘x’ će biti susjedna nekom trećem ‘x’-u. U tablici će se sigurno pojaviti barem jedan ‘x’.</p>

### 출력 

 <p>Za svaki pomak robota, tj. za svaki ‘x’ ispiši u kojem se smjeru (gore/dolje/lijevo/desno) pomaknuo robot. Svaka naredba treba biti ispisana u svom retku.</p>

