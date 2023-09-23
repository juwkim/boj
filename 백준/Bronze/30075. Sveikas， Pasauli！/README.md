# [Bronze II] Sveikas, Pasauli! - 30075 

[문제 링크](https://www.acmicpc.net/problem/30075) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현, 파싱, 문자열

### 문제 설명

<p>Paulius sukonstravo mini kompiuterį, prie kurio prijungtas ekranas bus pakabintas gerai matomoje vietoje ir rodys draugų žinutes iš socialinių tinklų.</p>

<p>Dabar vaikinas programuoja išvedimo į ekraną komandą SPAUSDINTI, kuri turi ekrane parodyti pateiktą tekstą ir suprasti vieną specialią instrukciją \n – tęsti iš naujos eilutės.</p>

<p><em>Komandos</em> SPAUSDINTI <em>sintaksė</em>. Komanda pradedama didžiosiomis raidėmis užrašytu raktažodžiu SPAUSDINTI. Po vieno tarpo pateikiamas kabutėmis (") apgaubtas tekstas, kurį reikia išvesti į ekraną. Kabučių išvesti nereikia.</p>

<p>Išvedamame tekste gali būti tokių simbolių:</p>

<ul>
	<li>lotyniškų didžiųjų ir mažųjų raidžių;</li>
	<li>skaičių;</li>
	<li>, ./ <>?; : []{}|()− = _ + @! ∗ %$&#</li>
</ul>

<p>Tarpų išvedamame tekste nebus. Jei tarp kabučių yra naujos eilutės komanda (du iš eilės einantys simboliai \n), šie simboliai nėra išvedami, o suprantami kaip instrukcija tolimesnį tekstą išvesti naujoje eilutėje.</p>

<p>Komanda SPAUSDINTI išveda tekstą į tą pačią eilutę, kur baigė prieš tai vykdyta komanda, ir tik \n instrukcija nurodo, kad reikia tęsti naujoje eilutėje.</p>

<p>Pateikta programa sudaryta tik iš komandų SPAUSDINTI. Parašykite programą, kuri interpretuotų pateiktas komandas ir išvestų jų rezultatą.</p>

### 입력 

 <p>Pirmojoje pradinių duomenų eilutėje nurodytas programą sudarančių komandų SPAUSDINTI skaičius <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>. Kitose <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> eilučių pateiktos komandos po vieną eilutėje. Programa yra sintaksiškai teisinga ir jos eilutės yra neilgesnės nei <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>250</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$250$</span></mjx-container> simbolių.</p>

### 출력 

 <p>Išveskite tekstą, kurį atspausdintų duotoji programa.</p>

