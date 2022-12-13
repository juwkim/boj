# [Silver V] XO - 26361 

[문제 링크](https://www.acmicpc.net/problem/26361) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현(implementation)

### 문제 설명

<p>Zaigrajmo igru Križić-kružić. Za one koji ne znaju što je to, slijedi kratko predstavljanje pravila. Igru igraju dva igrača koji, svaki svojim znakom, popunjavaju tablicu koja u početku ima devet praznih polja podijeljenih u tri reda i tri stupca. Igrač X upisuje slovo „X“ – križić, a igrač O upisuje slovo „O“ – kružić. Počevši od onog koji upisuje križić, igrači naizmjenično odabiru prazna polja i unutar njih upisuju svoj znak. Igra završava pobjedom jednog od njih kada upiše tri svoja znaka uzastopno u nekom retku, stupcu, na glavnoj ili na sporednoj dijagonali. Ako to ne uspije niti jednom igraču, a sva polja su popunjena, igra završava bez pobjednika. Npr, na slici je prikazan slijed od sedam odigranih poteza koji je doveo do pobjede prvog igrača.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/3521d414-0c57-4e45-a0fd-bfafa2763033/-/preview/" style="width: 634px; height: 76px;"></p>

<p>Neka je zadan slijed od N odigranih poteza u jednoj realno odigranoj igri. Napiši program koji će odrediti i ispisati što slijedi nakon N-tog odigranog poteza. Na raspolaganju su nam sljedeće mogućnosti:</p>

<ol>
	<li>mogućnost: Igru nastavlja igrač X postavljanjem svog znaka u prazno polje.</li>
	<li>mogućnost: Igru nastavlja igrač O postavljanjem svog znaka u prazno polje.</li>
	<li>mogućnost: Igra je završila pobjedom igrača X.</li>
	<li>mogućnost: Igra je završila pobjedom igrača O.</li>
	<li>mogućnost: Igra je završila jer više nema praznih polja, a nitko nije pobijedio.</li>
</ol>

### 입력 

 <p>U prvom je retku cijeli broj N (0 ≤ N ≤ 9), broj odigranih poteza.</p>

<p>U sljedećih N redaka je prirodan broj P (1 ≤ P ≤ 9), oznaka polja na koji je igrač na potezu upisao svoj znak. Gornje lijevo polje ima oznaku 1, a dolje desno polje ima oznaku 9. Vidi sliku iz teksta zadatka.</p>

### 출력 

 <p>U jedini redak ispiši prirodan broj između jedan i pet, redni broj mogućnosti iz teksta zadatka.</p>

