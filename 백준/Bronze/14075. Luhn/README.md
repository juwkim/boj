# [Bronze III] Luhn - 14075 

[문제 링크](https://www.acmicpc.net/problem/14075) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Većina bankovnih kartica ima šesnaesteroznamenkasti broj koji zovemo broj kartice. Međutim, nije bilo koji broj ispravan broj kartice - taj broj mora zadovoljavati Luhnov algoritam. Luhnov algoritam funkcionira na slijedeći način:</p>

<ol>
	<li>Počevši od zadnje znamenke, svaka druga znamenka se udvostruči.</li>
	<li>Ako je rezultat udvostručenja znamenke veći ili jednak 10, dobivenom umnošku se zbroje znamenke da se dobije jednoznamenkasti broj.</li>
	<li>Svi brojevi se zbroje.</li>
	<li>Dobiveni zbroj mora biti dijeljiv s 10.</li>
</ol>

<p>Na primjer, ako je broj kartice 1234567890123452, udvostručenjem svake druge znamenke dobili bismo: </p>

<p><img alt="" src="" style="height:89px; width:613px"></p>

<p>Kada svakom broju većem ili jednakom 10 zbroje znamenke, dobijemo: </p>

<p><img alt="" src="" style="height:88px; width:613px"></p>

<p>Kada se tako dobiveni brojevi zbroje, ukupan rezultat je 60, što je djeljivo s 10 pa je i kartica valjana.</p>

<p>Vaš zadatak je provjeriti je li dana kartica valjana. </p>

### 입력 

 <p>U prvom i jedinom retku ulaznih podataka nalazi se jedan cijeli broj: šenaesteroznamenkasti broj koji označava broj kartice. </p>

### 출력 

 <p>Potrebno je ispisati "DA" ako je dani broj valjani broj kartice, odnosno "NE" ako to nije. </p>

