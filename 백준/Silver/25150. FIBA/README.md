# [Silver III] FIBA - 25150 

[문제 링크](https://www.acmicpc.net/problem/25150) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

정렬

### 제출 일자

2024년 2월 6일 01:52:51

### 문제 설명

<p>U prvom krugu svjetskog prvenstva u košarci nastupa N timova. Oni su označeni brojevima od 1 do N. Igra se po principu „svatko sa svakim“, tj. svaki će tim odigrati po jednu utakmicu sa svakim drugim timom na prvenstvu. Rezultat utakmice zadaje se kao broj koševa tima s manjom oznakom nasuprot broju koševa tima s većom oznakom. Pobjednik utakmice je tim koji je dao više koševa. Za pobjedu tim dobiva dva boda, a za poraz jedan bod. Neriješen ishod meča nije moguć.</p>

<p>U prvom krugu prvenstva sudjeluje i Hrvatska. Ona je označena brojem H. Odredi i ispiši koliko je bodova osvojila Hrvatska u prvom krugu natjecanja.</p>

<p>Pobjednik prvog kruga je tim koji je sakupio najviše bodova u susretima sa svim ostalim timovima. Ako više timova ima isti, najveći broj bodova, tada je pobjednik onaj među njima koji je dao ukupno najviše koševa tijekom prvog kruga. Pobjednika će se uvijek moći odrediti na jedan od ovih dvaju načina. Odredi i ispiši oznaku pobjednika prvog kruga natjecanja.</p>

<p>U drugi krug prvenstva prolazi prvih K timova na ljestvici poretka, tj. prvih K timova s najviše bodova osvojenih u prvom krugu natjecanja. U slučaju da dva ili više timova imaju isti broj osvojenih bodova, tada je tim koji je postigao više koševa bolje plasiran na ljestvici poretka. Izbor prvih K timova uvijek će biti moguć.</p>

<p>Timovi koji su prošli u drugi krug prenose bodove osvojene u prvom krugu, ali samo one bodove koje su osvojili protiv timova koji su također prošli u drugi krug. Odredi i ispiši koliko su ukupno bodova timovi prenijeli u drugi krug natjecanja.</p>

### 입력 

 <p>U prvom retku nalaze se tri prirodna broja N, K i H (3 ≤ K < N ≤ 25, H ≤ N), brojevi iz teksta zadatka.</p>

<p>Rezultate utakmica prvog kruga zadajemo u obliku: prvo zadajemo rezultate utakmica tima s oznakom 1 redom sa svim timovima veće oznake, pa rezultate tima s oznakom 2 sa svim timovima veće oznake i tako sve do tima s oznakom N-1. Preciznije, u svakom retku nalaze se po dva broja K<sub>i</sub> i K<sub>j</sub> (0 ≤ K<sub>i</sub>, K<sub>j</sub> ≤ 100, pri čemu je i=1..N-1, a j=i+1..N).</p>

### 출력 

 <p>U prvi redak ispiši prirodan broj, broj bodova koje je osvojila Hrvatska u prvom krugu.</p>

<p>U drugi redak ispiši prirodan broj, oznaku pobjednika prvog kruga.</p>

<p>U treći redak ispiši ukupan broj bodova koji su timovi prenijeli u drugi krug natjecanja.</p>

