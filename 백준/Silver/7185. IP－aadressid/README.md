# [Silver III] IP-aadressid - 7185 

[문제 링크](https://www.acmicpc.net/problem/7185) 

### 성능 요약

메모리: 116200 KB, 시간: 900 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 정규 표현식, 문자열

### 제출 일자

2024년 9월 14일 15:51:50

### 문제 설명

<p>Matil on veebileht ning ta tahab täpselt teada, kes tema lehte külastavad. Külastajate jälgimiseks koostas Mati skripti, mis töötab järgmiselt:</p>

<ul>
	<li>kõigi seni nähtud külastajate IP-aadresse hoitakse tekstifailis;</li>
	<li>iga uue päringu (külastaja) saabumisel kontrollitakse programmi <code>grep</code> abil IP-aadressi esinemist tekstifailis (<code>grep</code> <em>uusIP</em> <em>fail</em>);</li>
	<li>kui vastavusi ei leitud, lisatakse uus aadress faili lõppu ja saadetakse Matile teavitus;</li>
	<li>muudel juhtudel ei tehta midagi.</li>
</ul>

<p>IP-aadress on sõne, mis koosneb neljast täisarvust vahemikus <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c2026"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>…</mo><mn>255</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \ldots 255$</span></mjx-container> ning punktidest nende vahel.</p>

<p>Programm <code>grep</code> on levinud töövahend regulaaravaldistega kirjeldatud mustrite otsimiseks teksti\-failidest. Antud juhul kasutab Mati programmi <code>grep</code> valesti, sest:</p>

<ul>
	<li><code>grep</code> otsib alamsõnesid: otsitav muster ei pea algama tingimata rea alguses ega lõppema rea lõpus;</li>
	<li>otsitavat mustrit tõlgendatakse regulaaravaldisena ning seetõttu võib otsitava IP-aadressi punktile vastata tekstifailis suvaline sümbol (kuid mitte vastupidi).</li>
</ul>

<p>On antud kõigi Mati skripti poolt töödeldud IP-aadresside loetelu (töötlemise järjekorras). Tuvastada, millised aadressid jättis Mati skript ekslikult faili lisamata.</p>

### 입력 

 <p>Tekstifaili esimesel real on üks täisarv: IP-aadresside arv <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>  (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 1\,000\,000$</span></mjx-container>). Järgmisel <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> real on igaühel üks IP-aadress. Sisendis võib esineda korduvaid aadresse, erinevate aadresside koguarv üheski testis ei ole suurem kui <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2\,000$</span></mjx-container>.</p>

### 출력 

 <p>Tekstifaili esimesele reale väljastada lisamata jäänud aadresside arv <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D449 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$V$</span></mjx-container> ning järgmisele <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D449 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$V$</span></mjx-container> reale lisamata jäänud aadressid nende esimist korda sisendfailis esinemise järjekorras.</p>

