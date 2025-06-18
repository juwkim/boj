# [Silver I] ŠIFRAT - 25141 

[문제 링크](https://www.acmicpc.net/problem/25141) 

### 성능 요약

메모리: 111276 KB, 시간: 108 ms

### 분류

백트래킹, 브루트포스 알고리즘, 깊이 우선 탐색, 그래프 이론, 그래프 탐색, 구현, 문자열

### 제출 일자

2025년 6월 19일 04:51:59

### 문제 설명

<p>Ivica proučava <em>kriptografiju</em>, znanost koja se bavi šifriranjem i slanjem poruka u takvom obliku da ih samo onaj kome su namijenjene može pročitati. Pronašao je metodu za šifriranje koja odabranu znamenku Z pretvara u zapis (<em>šifrat</em>) koji se sastoji od K nula i jedinica. Prvo se odabere neki ključ. Ključ je uzlazno sortiran niz od K ne nužno različitih znamenki (npr. ako je K=5 tada su „01248“, „12345“, „00122“ neki od mogućih ključeva).</p>

<p>Ako je znamenku Z moguće izraziti kao zbroj od X znamenki koje se pojavljuju u ključu, tada će na itom mjestu, gledajući s lijeva, u šifratu znamenke Z pisati „1“ ako je na i-tom mjestu u ključu, isto gledajući s lijeva, znamenka koja sudjeluje u zbroju. Inače na tom mjestu u šifratu piše „0“. Ako postoji više mogućih šifrata znamenke Z, tada ih treba sve ispisati. Svaku znamenku iz ključa u zbroju smijete iskoristiti najviše jednom.</p>

<p>Npr. ako je Z=8, K=5, X=2, a odabrani ključ „01236“, tada je traženi šifrat oblika „00101“ jer se 8 može izraziti kao zbroj dvije znamenke iz ključa na samo jedan način (2+6=8, „01236“ → „00101“).</p>

<p>Napiši program koji za zadanu znamenku Z, brojeve K i X te ključ duljine K određuje i ispisuje šifrat (ili šifrate) znamenke Z na opisani način. Zadanu znamenku uvijek će biti moguće šifrirati.</p>

### 입력 

 <p>U prvom retku nalazi se prirodan broj K (1 ≤ K ≤ 20), duljina ključa iz teksta zadatka.</p>

<p>U drugom retku nalazi se niz od K znamenki, ključ iz teksta zadatka.</p>

<p>U trećem retku nalazi se prirodan broj X (1 ≤ X ≤ K) iz teksta zadatka.</p>

<p>U četvrtom retku nalazi se znamenka Z (0 ≤ Z ≤ 9) iz teksta zadatka.</p>

### 출력 

 <p>Traženi šifrat ili šifrati znamenke Z, svaki u svom retku. Redoslijed ispisa nije bitan.</p>

