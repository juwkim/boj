# [Silver I] Žetva - 14145 

[문제 링크](https://www.acmicpc.net/problem/14145) 

### 성능 요약

메모리: 111516 KB, 시간: 120 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 플러드 필, 그래프 이론, 그래프 탐색

### 제출 일자

2025년 4월 26일 22:00:44

### 문제 설명

<p>Zoran živi na farmi te ima najveći kombajn u selu. Ove je godine, unatoč problemima s otkupom, Zoran posadio nekoliko polja pšenice. Došlo je vrijeme žetve, a njemu se sad baš i ne da raditi.</p>

<p>Ipak, svaki će dan požnjat jedno polje pšenice i to ono najmanje kvadrature.</p>

<p>Njegovo zemljište možemo predstaviti R×S kvadratnom mrežom. Za svaki kvadrat poznato je da li je Zoran tamo posijao pšenicu ili nije. Za dva kvadrata zemljišta kažemo da su susjedni ako imaju zajedničku stranicu.</p>

<p>Jednim poljem pšenice nazivamo maksimalan skup susjednih kvadrata na kojima je posijana pšenica. U lijevoj tablici prepoznajemo tako četiri polja. U desnoj tablici polja su označena redom kojim će ih Zoran žnjeti.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/14145/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-01-03%20%EC%98%A4%ED%9B%84%203.00.16.png" style="height:90px; width:302px"></p>

<p>Napišite program koji će za svaki kvadrat na kojem je posijana pšenica odrediti na koji će dan Zoran proći svojim kombajnom i požnjeti pšenicu. </p>

### 입력 

 <p>U prvom retku nalaze se prirodni brojevi R i S (1 ≤ R, S ≤ 50), dimenzije Zoranovog zemljišta.</p>

<p>U sljedećih R redaka nalazi se po S znakova '0' ili '1'. Znak '0' predstavlja kvadrat zemljišta na kojem nije posijana pšenica, a znak '1' kvadrat zemljišta na kojem je posijana pšenica.</p>

<p>Broj polja pšenice bit će manji od 10, a nijedna dva polja pšenice neće imati jednaku kvadraturu. </p>

### 출력 

 <p>U R redaka potrebno je ispisati po S znakova. Na kvadratima koji ne sadrže pšenicu mora stajati znak '0', dok na preostalim kvadratima mora stajati redni broj dana kad će taj kvadrat biti požnjen. </p>

