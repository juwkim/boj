# [Bronze I] KHL - 25146 

[문제 링크](https://www.acmicpc.net/problem/25146) 

### 성능 요약

메모리: 30840 KB, 시간: 84 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 파싱(parsing), 문자열(string)

### 문제 설명

<p>Medveščak je hrvatski profesionalni hokejaški klub iz Zagreba koji trenutačno nastupa u međunarodnoj KHL hokejaškoj ligi. Poznati su pod nadimkom Medvjedi, a navijači ih prate povicima "Zig-zag, Medveš-čak!".</p>

<p>Jedna hokejaška utakmica dijeli se na tri trećine. Pobjednik je onaj tim koji u tri trećine ukupno postigne više golova. Za pobjedu nakon tri trećine dobivaju se tri boda, dok se za poraz ne dobivaju bodovi.</p>

<p>U slučaju neodlučenog rezultata nakon tri trećine, igra se produžetak. Tim koji u produžetku postigne više golova je pobjednik i dobiva dva boda, a poraženi dobiva jedan bod.</p>

<p>Ako je rezultat nakon produžetka i dalje neriješen, pristupa se izvođenju kaznenih udaraca. Tim koji pogodi više kaznenih udaraca, pobjednik je meča i dobiva jedan bod, a poraženi ne dobiva bodove.</p>

<p>Ako znamo da Medveščak naizmjence igra jednu utakmicu kod kuće, a sljedeću u gostima i da je prvu u sezoni odigrao kod kuće, odredi i ispiši koliko je ukupno bodova osvojio nakon N odigranih utakmica.</p>

### 입력 

 <p>U prvom retku nalazi se prirodan broj N (1 ≤ N ≤ 60), broj odigranih utakmica iz teksta zadatka.</p>

<p>U narednih N redaka nalazi se rezultat svake od N odigranih utakmica redom od prve do posljednje u sezoni. Rezultat utakmice zadan je u obliku stringa „D1:G1/D2:G2/D3:G3/Dp:Gp/Dk:Gk“ pri čemu su:</p>

<ul>
	<li>cijeli brojevi D1, G1, D2, G2, D3, G3 (0 ≤ D1, G1, D2, G2, D3, G3 ≤ 99), broj golova domaćina i gosta u prvoj, drugoj i trećoj trećini.</li>
</ul>

<p>Ako bude potrebno bit će zadani i:</p>

<ul>
	<li>cijeli brojevi Dp i Gp (0 ≤ Dp, Gp ≤ 99), broj golova domaćina i gosta u produžetku,</li>
</ul>

<p>a ako bude potrebno bit će zadani i:</p>

<ul>
	<li>cijeli brojevi Dk i Gk (0 ≤ Dk ≠ Gk ≤ 99), broj pogođenih kaznenih udaraca domaćina i gosta.</li>
</ul>

### 출력 

 <p>U jednom retku treba ispisati prirodan broj, traženi broj bodova iz teksta zadatka.</p>

