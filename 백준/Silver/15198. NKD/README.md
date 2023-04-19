# [Silver IV] NKD - 15198 

[문제 링크](https://www.acmicpc.net/problem/15198) 

### 성능 요약

메모리: 113112 KB, 시간: 132 ms

### 분류

구현, 시뮬레이션, 문자열

### 문제 설명

<p>U mnogim računalnim programima pojavljuje se lista nedavno korištenih dokumenata (NKD). Kao što joj ime kaže, lista sadrži nedavno korištene dokumente kako bi korisnik mogao brže doći do njih, izbjegavajući mukotrpno traženje medu dokumentima. Lista je ograničenog kapaciteta — poznat je najveći broj dokumenata koji se mogu u istom trenutku nalaziti u listi.</p>

<p>Svaki put kad korisnik otvori neki dokument (bilo izborom iz NKD liste ili na neki drugi način), tada:</p>

<ol>
	<li>Ako se dokument već nalazi negdje u listi, pomakne se na početak liste.</li>
	<li>U suprotnom, umetne se na početak liste. Ukoliko je prekoračen kapacitet liste, zadnji dokument u listi se izbacuje.</li>
</ol>

<p>Zadan je kapacitet liste (koja je na početku prazna) i niz dokumenata koje korisnik otvara. Odredite sadržaj liste nakon otvaranja svih dokumenata u zadanom redoslijedu.</p>

### 입력 

 <p>U prvom redu ulaza nalazi se prirodni broj k (1 ≤ k ≤ 10) — kapacitet liste. U drugom redu nalazi se prirodni broj n (1 ≤ n ≤ 500) — broj dokumenata koje korisnik otvara. Svaki od sljedećih n redova sadrži ime jednog dokumenta kojeg korisnik otvara. Imena svih dokumenata bit će nizovi od najviše 10 malih slova engleske abecede, bez razmaka. Dokumenti su dani u redoslijedu u kojem ih korisnik otvara.</p>

### 출력 

 <p>Potrebno je ispisati sadržaj NKD liste nakon otvaranja svih dokumenata, svaki dokument u svoj red. Prvi ispisani red odgovara dokumentu na početku NKD liste.</p>

