# [Silver II] Dešifravimas - 30065 

[문제 링크](https://www.acmicpc.net/problem/30065) 

### 성능 요약

메모리: 125580 KB, 시간: 132 ms

### 분류

구현, 문자열

### 제출 일자

2025년 3월 18일 21:43:51

### 문제 설명

<p>Informatikas Bitukas turi smalsių draugų, todėl su užjūrio draugu Brituku susirašinėja šifruodamas savo žinutes. Tam jis naudoja Cezario šifrą, kurį nors ir nėra sunku nulaužti, tačiau smalsiems draugams užšifruotos žinutės atrodo kaip atsitiktinė simbolių seka.</p>

<p>Cezario šifras veikia taip: susirašinėjimo dalyviai apsikeičia raktu <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>K</mi><mo>≤</mo><mn>25</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ K ≤ 25$</span></mjx-container>), tuomet kiekviena raidė yra pakeičiama į jos <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>-tąją kaimynę pagal lotyniškąją abėcėlę. Likę simboliai paliekami tokie patys. Abėcėlė apsisuka: <code>Z</code> pirmoji kaimynė yra <code>A</code>, o <code>z</code> pirmoji kaimynė — <code>a</code>.</p>

<p>Pasižiūrėkime, kaip Bitukas užšifruotų žinutę <code>Kaip_gyveni?</code> su raktu <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi><mo>=</mo><mn>7</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K = 7$</span></mjx-container>:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b661c7c3-58aa-42e0-b60f-1ddc8b38e119/-/preview/" style="width: 523px; height: 292px;"></p>

<p>Norėdamas žinutes šifruoti greičiau, Bitukas sukonstravo Bituko Šifravimo Mašiną (BŠM). Bitukas į BŠM įveda pradinę žinutę, tuomet paleidžia mašiną ir ši pradeda šifruoti žinutę po vieną simbolį nuo pradžios iki galo.</p>

<p>Vieną vakarą Bitukas šifravo labai ilgą laišką Britukui, mat norėjo papasakoti apie savo studijas. Tačiau, BŠM netikėtai užstrigo ir užšifravo tik dalį žinutės. Bitukas nepasimetė: paleido mašiną iš naujo ir šį kartą mašina žinutę užšifravo sėkmingai! Tik neapsižiūrėjęs jis išsiuntė Britukui abi žinutes...</p>

<p>Britukui tą vakarą irgi nesisekė: jis pamiršo abiejų sutartą raktą.</p>

<p>Jūsų užduotis – parašyti programą, kuri perskaičiusi abi Brituko gautas žinutes iššifruotų Bituko siųstą žinutę.</p>

### 입력 

 <p>Pirmoje eilutėje įrašytas vienas sveikasis skaičius — žinutės ilgis <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>.</p>

<p>Antroje eilutėje įrašyta Brituko gauta žinutė, užšifruota su užstringančia mašina. Trečioje eilutėje — žinutė, užšifruota su veikiančia mašina.</p>

<p>Žinutėse tarpo simbolių nebus.</p>

### 출력 

 <p>Išveskite vieną eilutę — iššifruotą Bituko siunčiamą žinutę.</p>

