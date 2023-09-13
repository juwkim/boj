# [Bronze III] Leiutaja number üks - 29918 

[문제 링크](https://www.acmicpc.net/problem/29918) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

구현

### 문제 설명

<p>Leiutajatekülas kuulutati välja suur konkurss! Esileiutaja aunime saab see, kellel on 10 nädala pärast kõige rohkem leiutisi ette näidata.</p>

<p>Kui Adalbert konkursist kuulis, käis ta kohe Oskari, Giovanni, Helmi, Väino ja isegi doktor Ave akende taga luuramas, et teada saada, kui palju neil leiutisi juba varuks on. Lisaks teab ta ka seda, mitu leiutist nädalas igaüks juurde leiutada suudab.</p>

<p>Nüüd on tal aga kahtlus, et tema varudest ja leiutamiskiirusest ei piisa, et tal 10 nädala pärast kõige rohkem leiutisi oleks. Sellepärast tahab ta Susumu kaudu Jaapanist mõned eksootilised vidinad juurde tellida, et neid siis konkursil oma leiutistena esitleda.</p>

<p>Mitu vidinat peab Adalbert juurde tellima, et tal oma leiutistega kokku kõige rohkem asju oleks?</p>

### 입력 

 <p>Tekstifailis on täpselt kuus rida, igaühel kaks tühikuga eraldatud täisarvu. Faili esimesel real on arvud <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.085em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>N</mi><mn>0</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N_0$</span></mjx-container> ja <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.081em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>M</mi><mn>0</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M_0$</span></mjx-container>, mis tähendavad, et Adalberdil on praegu varuks <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.085em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>N</mi><mn>0</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N_0$</span></mjx-container> leiutist ja iga järgmise nädalaga jõuab ta <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.081em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>M</mi><mn>0</mn></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M_0$</span></mjx-container> uut juurde leiutada. Järgmisel viiel real on samad andmed Adalberdi konkurentide kohta. Ükski arv pole väiksem kui 0 ega suurem kui 100.</p>

### 출력 

 <p>Tekstifaili ainsale reale väljastada üks täisarv <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>, mis näitab, mitu Jaapani vidinat peab Adalbert juurde tellima, et konkursipäeval oleks tal kõige rohkem uusi asju ette näidata.</p>

