# [Silver IV] Lisp till C - 20863 

[문제 링크](https://www.acmicpc.net/problem/20863) 

### 성능 요약

메모리: 115656 KB, 시간: 124 ms

### 분류

문자열

### 제출 일자

2025년 3월 29일 12:18:06

### 문제 설명

<p>C är ett gammalt programmeringsspråk från 70-talet, som trots dess ålder är väldigt välanvänt. I språket skrivs funktionsanrop till en funktion med namnet <code>namn</code> på formen <code>namn(parameter1, parameter2, ..., parameterN)</code>. En parameter kan antingen vara en variabel (som i vårt fall består av en sekvens av tecken <code>a-z</code>), eller ett funktionsanrop i sig. T.ex. kan ett fullständigt funktionsanrop se ut på följande vis:</p>

<pre>a(b, c(d), e(f, g(h, i, j)))</pre>

<p>Ett funktionsanrop utan parametrar skrivs som <code>funktion()</code>.</p>

<p>Lisp är ett annat programmeringsspråk från 50-talet. I språket skrivs funktionsanrop till en funktion med namnet <code>namn</code> på formen <code>(namn parameter1 parameter2 ... parameter N)</code>. Återigen kan en parameter i sig vara en variabel eller ett funktionsanrop. Funktionsanropet i C som beskrivs ovan kan istället skrivas</p>

<pre>(a b (c d) (e f (g h i j)))</pre>

<p>Ett funktionsanrop utan parametrar skrivs som <code>(funktion)</code>.</p>

<p>Varför denna språkhistoria? Jo, det visar sig att domaren Simon gillar C, men inte Lisp. Domaren Johan, å andra sidan, gillar Lisp, men inte C.</p>

<p>Simon blev därför väldigt sur när Johan programmerade alla sina exempellösningar i Lisp, och vill konvertera Johans program till C. Hjälp Simon med detta, genom att skriva ett program som, givet ett funktionsanrop i Lisp konverterar det till ett funktionsanrop i C.</p>

### 입력 

 <p>Indatan består av en rad med ett korrekt formaterat funktionsanrop i Lisp-format, högst <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100\,000$</span></mjx-container> tecken lång. Alla parametrar kommer att vara separerade med exakt ett blanksteg, och det finns inga extra blanksteg där det inte behövs.</p>

### 출력 

 <p>Skriv ut en enda rad, med funktionsanropet konverterat till C-format. Inkludera ett blanksteg efter varje kommatecken, som i exempelfallen.</p>

