# [Silver V] TiM - 25153 

[문제 링크](https://www.acmicpc.net/problem/25153) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

사칙연산(arithmetic), 자료 구조(data_structures), 구현(implementation), 수학(math), 스택(stack), 문자열(string)

### 문제 설명

<p>Til i Maja vježbaju zbrajanje i oduzimanje rješavajući zadatke koje si same zadaju uz pomoć jednog posebnog kalkulatora. Taj kalkulator u jednom pokretanju na svoj ekran može ispisati ili znak „X“ (veliko slovo „X“) ili prirodan broj K između 1 i 9999 ili znak „+“ (plus) ili znak „-“ (minus). Pri tome vrijedi sljedeća pravilnost:</p>

<ul>
	<li>u neparnom pokretanju (prvom, trećem, petom...) kalkulator će na ekran moći ispisati samo ili znak „X“ ili prirodan broj K između 1 i 9999;</li>
	<li>u parnom pokretanju (drugom, četvrtom, šestom...) kalkulator će na ekran moći ispisati samo znak „+“ ili znak „-“.</li>
</ul>

<p>Til i Maja će neparan broj puta N pokrenuti kalkulator, a ispise na ekran u svakom od tih N pokretanja će zapisati na papir jedan iza drugog onim redom kako se pojavljuju. Na taj će način kreirati jedan matematički izraz. Npr., izraz može biti sljedećeg oblika: X+2+3+X+1, 235-1+X+7642. Na žalost, curama se kreirani izraz raspao na znakove koje su onda morale zapisale jedan ispod drugog.</p>

<p>Njih dvije sada zanimaju odgovori na sljedeća tri pitanja:</p>

<ol>
	<li>Koliki je zbroj svih znamenki koje su se pojavile na ekranu kalkulatora u svih N pokretanja?</li>
	<li>Koliki je zbroj svih prirodnih brojeva K koje je kalkulator ispisao na ekran?</li>
	<li>Kojim cijelim brojem treba zamijeniti znak „X“ da bi vrijednost izraza bila jednaka nuli? Rješenje će uvijek postojati i biti jedinstveno.</li>
</ol>

<p>Napiši program koji će na osnovi zadanih podataka ispisati odgovore na postavljena pitanja.</p>

### 입력 

 <p>U prvom retku nalazi se neparan prirodan broj N (3 ≤ N ≤ 99), broj pokretanja kalkulatora.</p>

<p>U drugom retku nalazi se prirodan broj M (3 ≤ M ≤ 250), broj znakova u kreiranom izrazu.</p>

<p>U sljedećih M redaka nalazi se po jedan znak, znakovi iz izraza napisani jedan ispod drugog.</p>

### 출력 

 <p>U prvi redak treba ispisati odgovor na prvo pitanje.</p>

<p>U drugi redak treba ispisati odgovor na drugo pitanje.</p>

<p>U treći redak treba ispisati odgovor na treće pitanje.</p>

