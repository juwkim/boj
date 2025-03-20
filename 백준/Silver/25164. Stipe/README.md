# [Silver II] Stipe - 25164 

[문제 링크](https://www.acmicpc.net/problem/25164) 

### 성능 요약

메모리: 138032 KB, 시간: 404 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 3월 21일 01:43:10

### 문제 설명

<p>U redu za cijepljenje stoji N ljudi. Za svaku osobu u redu znamo koliko je stara. Kada redar Stipe vikne Sljedeći!, istupi osoba koja je prva na redu. Na Stipi je tada ili da je propusti na cijepljenje, ili da joj kaže da dođe drugi put.</p>

<p>Doza cjepiva ima ograničeno, njih K, a Stipe će se pobrinuti da se sve iskoriste. Nakon što je cijepljeno K ljudi, Stipe će objaviti kako cjepiva više nema i ostatak ljudi koji stoji u redu poslati kućama.</p>

<p>Za Stipu bi sve bilo jednostavno, kada ne bi postojala opasnost da portali na kraju dana objave vijest: Cijepili mlađeg, a starijeg ne! Kako do toga ne bi došlo, Stipe će paziti da ne postoji nijedan par osoba (X, Y), tako da je osoba X cijepljena, osoba Y ne, a osoba X mlađa je od osobe Y.</p>

<p>Osim toga, Stipe će paziti i da broj ljudi koje pošalje kući dok cjepiva još ima, tj. prije nego što je zadnja osoba cijepljena, bude minimalan. Koliko će ljudi Stipe poslati kući dok cjepiva još ima?</p>

### 입력 

 <p>U prvom su retku prirodni brojevi N (1 ≤ N ≤ 100 000) i K (1 ≤ K ≤ N).</p>

<p>U sljedećih N redaka su po tri nenegativna cijela broja G (0 ≤ G ≤ 99), M (0 ≤ M ≤ 11) i D (0 ≤ D ≤ 29), starost osoba u redu, redom od prve do posljednje, izražena u godinama, mjesecima i danima.</p>

### 출력 

 <p>U prvi i jedini redak ispiši koliko će ljudi Stipe poslati kući dok cjepiva još ima.</p>

