# [Silver IV] Meli kalikamaka - 7202 

[문제 링크](https://www.acmicpc.net/problem/7202) 

### 성능 요약

메모리: 108080 KB, 시간: 84 ms

### 분류

문자열

### 제출 일자

2024년 8월 23일 03:42:29

### 문제 설명

<p>Mõnedel Polüneesia saartel räägivad inimesed keelt, millel on järgmised omadused:</p>

<ul>
	<li>Sõnades ei ole kunagi korduvaid ega pikki täis- ega kaashäälikuid.</li>
	<li>Igale kaashäälikule järgneb alati üks täishäälik (‘a’, ‘e’, ‘i’, ‘o’ ja ‘u’ on täishäälikud, kõik ülejäänud kaashäälikud).</li>
	<li>Keeles ei eristata ‘r’- ja ‘l’-häälikuid ega ‘s’- ja ‘k’-häälikuid.</li>
</ul>

<p>Kui polüneeslased tahavad ¨ ule võtta teiste keelte sõnu või väljendeid, muutuvad need sõnad või väljendid saarte elanikele hääldamiseks mugavamaks teatud reeglite järgi. Veidi lihtsustatud versioon nendest reeglitest on järgmine:</p>

<ul>
	<li>Kõik pikad ja ülipikad täis- ja kaashäälikud muutuvad lühikesteks. Näiteks sõna ‘tee’ muutub sõnaks ‘te’, ‘toooo’ muutub ‘to’-ks ja ‘mokka’ muutub ‘moka’-ks.</li>
	<li>Mitmest järjestikusest täishäälikust jääb alles ainult esimene. Näiteks sõna ‘tea’ muutub samuti ‘te’-ks.</li>
	<li>Üksteisele järgnevate kaashäälikute vahele ja sõna lõpus olevate kaashäälikute järele lisatakse täishäälikud. Lihtsuse mõttes ütleme, et alati lisatakse ‘a’. Näiteks ‘ahv’ muutub ‘ahava’-ks ja ‘onn’ muutub ‘ona’-ks.</li>
	<li>Häälik ‘r’ muutub ‘l’-ks ja ‘s’ muutub ‘k’-ks. Näiteks ‘kass’ muutub ‘kaka’-ks ja ‘tervist’ muutub ‘telavikata’-ks.</li>
</ul>

<p>Kirjutada programm, mis “tõlgib” antud teksti ülaltoodud reeglite järgi polüneesia häälduseks.</p>

### 입력 

 <p>Tekstifaili ainsal real on väikestest ladina tähtedest a. . . z ja tühikutest koosnev tekst pikkusega 1 kuni 100 märki. Tekst ei alga ega lõpe tühikutega ning kahe sõna vahel on alati täpselt üks tühik.</p>

### 출력 

 <p>Tekstifaili ainsale reale väljastada sisendis antud teksti polüneesia vaste.</p>

