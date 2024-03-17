# [Bronze II] Palindroom - 29835 

[문제 링크](https://www.acmicpc.net/problem/29835) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

그리디 알고리즘, 구현, 문자열

### 제출 일자

2024년 3월 18일 03:25:22

### 문제 설명

<p>Kevin sai informaatikaolümpiaadi eelvooru palindroomiülesande eest maksimumpunktid. Seda nähes andis õpetaja talle natuke raskema ülesande, milles uuritakse mitmesuguse pikkusega tekstilisi palindroome.</p>

<p>Sarnaselt arvujada juhtumiga nimetatakse teksti palindroomiks, kui see on sama eest tahapoole ja tagant ettepoole lugedes. Näiteks <code>ABBA</code> on palindroom (sest see on ka tagurpidi lugedes <code>ABBA</code>), aga <code>ABCD</code> ei ole (sest see on tagurpidi lugedes <code>DCBA</code>).</p>

<p>Kirjutada programm, mis leiab vähima võimaliku arvu täheasendustega viisi antud tekst palindroomiks muuta.</p>

### 입력 

 <p>Sisendi esimesel real on täisarv <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>300</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 300$</span></mjx-container>).</p>

<p>Teisel real on <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> suurest ladina tähest (<code>A</code> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2026"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>…</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\ldots$</span></mjx-container> <code>Z</code>) koosnev tekst.</p>

### 출력 

 <p>Väljundi esimesele reale väljastada täisarv <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>, mis näitab, mitu tähte on minimaalselt vaja asendada, et sisendis antud tekstist saaks palindroom.</p>

<p>Teisele reale väljastada saadud palindroom. Kui minimaalse täheasenduste arvuga palindroome on mitu, väljastada neist (ladina tähestiku järgi) tähestikulises järjekorras esimene.</p>

