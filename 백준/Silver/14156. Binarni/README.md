# [Silver I] Binarni - 14156 

[문제 링크](https://www.acmicpc.net/problem/14156) 

### 성능 요약

메모리: 111432 KB, 시간: 132 ms

### 분류

비트마스킹, 해 구성하기

### 제출 일자

2025년 6월 19일 02:45:40

### 문제 설명

<p>Mali Nikola je nepresušnim nizom pitanja upravo natjerao svoju profesoricu matematike u ludilo. Posve iznervirana, ona za kaznu zadaje cijelom razredu sljedeći zadatak:</p>

<p>"Promotrimo sve različite NIZOVE (eto ti sad niza, Nikola!) koji se sastoje od N binarnih znamenki (tih nizova ima 2N ). Nañite permutaciju nizova u kojoj je udaljenost svaka dva uzastopna niza jednaka jedan".</p>

<p>Učiteljica je još napomenula da se udaljenost izmeñu dva binarna niza definira kao broj pozicija na kojima se odgovarajući elementi nizova razlikuju. Na primjer:</p>

<p>Udaljenost( 111, 000 ) = 3                    /nizovi se razlikuju na prvoj, drugoj i trećoj poziciji/<br>
Udaljenost( 111100, 101010 ) = 3        /nizovi se razlikuju na drugoj, četvrtoj i petoj poziciji/<br>
Udaljenost( 110011, 110011 ) = 0</p>

<p>Pomozite Nikoli da pronañe traženu permutaciju. </p>

### 입력 

 <p>U prvom i jedinom retku nalazi se prirodni broj N ≤ 16, duljina binarnih nizova. </p>

### 출력 

 <p>Ispišite traženu permutaciju tako da ispišete 2N različitih binarnih nizova, svaki u svojoj liniji. Svaki niz se mora sastojati od točno N znamenki '0' ili '1'. Udaljenost izmeñu svaka dva susjedna niza mora biti točno jedan.</p>

<p>Možete pretpostaviti da će uvijek postojati barem jedno rješenje.</p>

