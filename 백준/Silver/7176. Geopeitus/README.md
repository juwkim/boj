# [Silver II] Geopeitus - 7176 

[문제 링크](https://www.acmicpc.net/problem/7176) 

### 성능 요약

메모리: 113500 KB, 시간: 112 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2025년 3월 24일 08:47:00

### 문제 설명

<p>Geopeituse mängus antakse aarete koordinaadid mõnikord valemina, kus mõned numbrid on asendatud tähtedega, näiteks <code>N58 24.1ab E26 44.3c</code>.</p>

<p>Kirjutada programm, mis väljastab kõik antud valemile ja muutujate võimalikele väärtustele vastavad koordinaadid.</p>

### 입력 

 <p>Tekstifaili esimesel real on valem, mis koosneb laius- ja pikkuskraadi esitusest, mis omakorda koosnevad ilmakaare tähisest (<code>N</code>, <code>S</code>, <code>E</code>, <code>W</code>) ning kraadide, minutite ja minuti murdosa näitudest näites antud vormingus. Valemi pikkus ei ületa 25~märki.</p>

<p>Faili teisel real on muutujate arv <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 3$</span></mjx-container>) ja järgmisel <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> real igaühel ühe muutuja kirjeldus: muutuja nimi, võrdusmärk ja komadega eraldatud loetelu, mille elemendid on kas üksikud väärtused või väärtuste vahemikud. Muutuja nimi on alati üks väike ladina täht. Väärtused ja vahemike otspunktid võivad olla ühe- või kahekohalised arvud. Võib eeldada, et ühegi muutuja kirjeldus ei tekita korduvaid väärtusi.</p>

### 출력 

 <p>Tekstifaili väljastada kõik koordinaadid, mis on võimalik saada muutujate lubatud väärtustega asendamisel. Koordinaadid väljastada igaüks eraldi reale, ridade järjekord failis pole oluline.</p>

