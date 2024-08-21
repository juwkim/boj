# [Silver V] Karikakrad ja armastus - 7204 

[문제 링크](https://www.acmicpc.net/problem/7204) 

### 성능 요약

메모리: 108080 KB, 시간: 88 ms

### 분류

수학

### 제출 일자

2024년 8월 22일 01:22:38

### 문제 설명

<p>M-kohaliseks (M > 1) meeldivusseisundite loeteluks nimetame järgmist järjendit: esikohal on seisund “armastab” ja järgmisel M −1 kohal mingid muud meeldivusseisundid. Tüdruk tuvastab poisi suhtumise endasse talle kingitud karikakra õielehtede äratõmbamisega järgmisel viisil:</p>

<ol>
	<li>Enne esimese õielehe tõmbamist oleme seisundis “armastab”.</li>
	<li>Iga järgmise õielehe tõmbamise järel muutub meeldivuse seisund järgmiseks seisundiks selles loetelus.</li>
	<li>Viimasele seisundile järgmiseks seisundiks loeme seisundit “armastab”.</li>
	<li>Kui õies enam lehti pole, lõpetame töö selle karikakraga ja tagastame tulemusena viimase seisundi.</li>
</ol>

<p>Üks võimalik 3-kohaline jada on “armastab”-“meeldin”-“ükskõikne”. Sel juhul saame näiteks viie õielehe puhul tulemuseks “ükskõikne”, aga seitsme puhul “meeldin”.</p>

<p>On teada, et tüdruk usub poisi armastust vaid siis, kui see kingib talle karikakraid ja kõik need tuvastavad seisundi “armastab”. Poiss soovib tüdrukut oma armastuses veenda. Selleks kingib ta tüdrukule N karikakraõit ja tahab sinna lisada võimalikult pika endadefineeritud meeldivusseisundite loetelu.</p>

<p>Leida suurim antud õite korral võimalik M väärtus, mille korral tüdruk jõuab järeldusele, et poiss teda armastab.</p>

### 입력 

 <p>Tekstifaili esimesel real karikakarde arv N (1 ≤ N ≤ 1000) ja teisel real N üksteisest tühikutega eraldatud õielehtede arvu L<sub>i</sub> (1 ≤ L<sub>i</sub> ≤ 100, i ∈ 1 . . . N).</p>

### 출력 

 <p>Tekstifaili ainsale reale väljastada üks täisarv: suurim võimalik M väärtus.</p>

