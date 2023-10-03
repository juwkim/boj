# [Bronze I] Pabėgimo kambarys - 30063 

[문제 링크](https://www.acmicpc.net/problem/30063) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 문자열

### 문제 설명

<p>Norėdami atšvęsti Lietuvos informatikos olimpiadų trisdešimtmetį, Vertinimo komisijos nariai sugalvojo sau pramogą: pabėgimo kambarį. Pabėgimo kambarys – tai seka užuominų, kurių kiekviena yra pažymėta didžiąja lotyniška raide.</p>

<p>Užuominos yra atskleidžiamos po vieną, nuo pirmos iki paskutinės pateikta tvarka. Komisijos nariai iš kambario ištrūkti gali tuomet, kai iš surinktų užuominų pavyksta sudaryti žodį <code>RAKTAS</code>.</p>

<p>Įsivaizduokime pabėgimo kambarį, kurio užuominų seka yra tokia:</p>

<p style="text-align: center;"><code>RAUDONASNYKSTUKAS</code></p>

<p>Iš šio pabėgimo kambario komisija gali ištrūkti įveikusi <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$13$</span></mjx-container> užuominų:</p>

<p style="text-align: center;"><code><u>RA</u>UDON<u>A</u>SNY<u>KST</u>UKAS</code></p>

<p>Keturios paskutinės užuominos (pažymėtos pilkai) nėra būtinos, nes žodį <code>RAKTAS</code> pavyks sudaryti iš jau surinktų užuominų (raidės pabrauktos).</p>

<p>Parašykite programą, kuri rastų, kiek mažiausiai užuominų reikia atskleisti norint ištrūkti iš pabėgimo kambario.</p>

### 입력 

 <p>Pirmoje eilutėje pateiktas vienintelis skaičius – užuominų kiekis <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>.</p>

<p>Antroje eilutėje pateikta <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> ilgio simbolių eilutė – užuominų seka. Užuominos žymimos didžiosiomis lotyniškomis raidėmis nuo <code>A</code> iki <code>Z</code>. Pašalinių simbolių nebus.</p>

### 출력 

 <p>Išveskite vieną sveikąjį skaičių – mažiausią reikalingų užuominų kiekį.</p>

<p>Pradiniai duomenys bus tokie, kad atsakymas visada egzistuos.</p>

