# [Silver III] Izvanredan Ishod - 33216 

[문제 링크](https://www.acmicpc.net/problem/33216) 

### 성능 요약

메모리: 111420 KB, 시간: 112 ms

### 분류

구현

### 제출 일자

2025년 4월 2일 18:51:06

### 문제 설명

<p>Bliži se drevno (čitaj <em>drveno</em>) programersko natjecanje za djecu i mlade koje organizira nitko drugi doli ACM (<em>Avijatičarski Centar Metković</em>). Na natjecanju će nastupiti čak <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> timova uzrasta do šest godina. Među timovima je i zlatni trojac mladih avijatičara Hrvatske: Paula, Marin i Josip (obrnuto abecedno, svaka sličnost sa stvarnim događajima i osobama nije slučajna). Oblik natjecanja je standardan, dok kapetan posade radi piruete, kopilot čita zadatke na ruskom jeziku i Morseovom abecedom diktira kod programeru koji se nalazi izvan zrakoplova, ali je za njega sigurno pričvršćen ljepljivom vrpcom.</p>

<p>Timovi će na natjecanju ukrstiti koplja (preciznije krila) na <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> različitih zadataka. Timovi su na rang listi poredani silazno po broju riješenih zadataka.</p>

<ul>
	<li>„Čekaj malo! Nisi objasnio ljudima kojim su redom poredani timovi sa istim brojem riješenih zadataka!” – dobacuje Marin kroz prozor svojeg krilatog ljubimca.</li>
	<li>„U pravu si, Marine.” – odgovorih mu.</li>
</ul>

<p>Timovi koji imaju isti broj riješenih zadataka poredani su <strong>uzlazno</strong> po penalty vremenu. <em>Penalty</em> vrijeme za neki tim je suma penalty vremena svih točno riješenih zadataka. Penalty vrijeme točno riješenog zadatka odgovara vremenu zadnjeg poslanog rješenja za taj zadatak kojem se pridodaje <strong><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container> minuta</strong> za svako pogrešno poslano rješenje na tom zadatku. Tim neće slati rješenje za zadatak koji su već točno riješili. Najveći dozvoljen broj poslanih rješenja za isti zadatak je <strong><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$9$</span></mjx-container> po timu</strong>. Ako timovi imaju isti broj riješenih zadataka i isto penalty vrijeme, poredani su po imenima abecedno.</p>

<p>Natjecanje traje <strong>pet</strong> sati. Tijekom prva četiri sata rang lista je vidljiva svim timovima te za svaki tim pokazuje informacije o svakom zadatku (koliko je ukupno slanja bilo, je li riješen i u koje vrijeme je riješen). Tijekom ta četiri sata, poredak na listi se sa svakim slanjem automatski ažurira. Nakon četiri sata, lista se zamrzne, tj. ostane u poretku u kojem je bila. Informacije o točnosti rješenja poslanih tijekom zadnjeg sata svaki tim zna samo za svoja vlastita, ali se za svaki tim i dalje za svaki zadatak na listi ažurira koliko je ukupno rješenja poslano i kada je poslano zadnje.</p>

<p>Natjecanje je završilo, lista će se uskoro odmrznuti, a naš trojac, tj. tim s imenom <code>NijeZivotJedanACM</code> treba vašu pomoć. Zanima ih koja je najniža moguća pozicija na kojoj mogu završiti kada se lista odmrzne. Ali u tih pet sati su se toliko izvrtjeli po modrom nebu da im je već zlo i programčić koji ovo provjerava nisu u stanju napisati sami. Pomozite im!</p>

### 입력 

 <p>U prvom su retku prirodni brojevi <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ N ≤ 1000$</span></mjx-container>) i <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>M</mi><mo>≤</mo><mn>15</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ M ≤ 15$</span></mjx-container>) iz teksta zadatka.</p>

<p>U sljedećih <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> redaka je stanje zamrznute liste na kraju natjecanja. Svaki red započinje imenom tima (riječ sastavljena od malih i velikih slova engleske abecede ne duža od <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container> znakova, imena svih timova bit će različita) koje je razmakom odvojeno od <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> riječi koje su međusobno odvojene razmacima, a nose informacije o rješenjima zadataka za taj tim, redom od prvog do zadnjeg zadatka.</p>

<p>Riječi su za svaki zadatak oblika <code>SX/V</code>, gdje je:</p>

<ul>
	<li><code>S</code> stanje poslanih rješenja za taj zadatak (‘<code>+</code>’ označava da je zadatak točno riješen, ‘<code>-</code>’ označava da nije, a ‘<code>?</code>’ označava da je zadnje rješenje poslano nakon zamrzavanja ljestvice).</li>
	<li><code>X</code> je ukupan broj rješenja koja je taj tim poslao za taj zadatak te se izostavlja ako je jednak nuli.</li>
	<li><code>V</code> je vrijeme u kojem je poslano zadnje rješenje. Vrijeme je u formatu <code>HH:MM:SS</code> (sa vodećim nulama) te je manje od <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container> sati. Cijeli <code>/V</code> dio se u riječi izostavlja ako zadatak nije točno riješen.</li>
</ul>

<p>U posljednjem se retku nalazi odmrznuti redak za naš trojac, tim s imenom <code>NijeZivotJedanACM</code>.</p>

### 출력 

 <p>U prvi i jedini redak ispišite najnižu moguću poziciju na kojoj naš trojac može završiti nakon odmrzavanja liste.</p>

