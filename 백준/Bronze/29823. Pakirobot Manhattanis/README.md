# [Bronze IV] Pakirobot Manhattanis - 29823 

[문제 링크](https://www.acmicpc.net/problem/29823) 

### 성능 요약

메모리: 114436 KB, 시간: 140 ms

### 분류

구현, 수학, 문자열

### 문제 설명

<p>New Yorgis Manhattani linnaosas tegutseb isejuhtiv pakirobot. See robot on üsna suur ja suudab korraga kohale toimetada mitu pakki eri sihtkohtadesse. Pärast kõikide pakkide kohaletoimetamist peab robot minema tagasi lattu, et uued pakid võtta.</p>

<p>Manhattani tänavad moodustavad ruudustiku: kõik tänavad on täpselt põhja-lõuna või ida-lääne suunalised. Lisaks on kõik kõrvutiste paralleelsete tänavate vahekaugused võrdsed.</p>

<p>Nimetame roboti <em>sammuks</em> ühest ristmikust mööda mingit tänavat järgmise ristmikuni liikumist.</p>

<p>Leia, kui mitme sammuga on robotil võimalik tagasi lattu jõuda.</p>

### 입력 

 <p>Sisendi esimesel real on roboti praeguseks tehtud sammude arv <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 1\,000$</span></mjx-container>). Teisel real on <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> tähemärki, mis näitavad seda, mis suunas iga roboti samm oli: <code>N</code> tähendab sammu põhja, <code>E</code> ida, <code>S</code> lõuna ja <code>W</code> lääne suunas.</p>

### 출력 

 <p>Väljundi ainsale reale väljastada minimaalne sammude arv, millega robot lattu tagasi saab.</p>

