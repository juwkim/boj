# [Silver IV] Megawirus - 8544 

[문제 링크](https://www.acmicpc.net/problem/8544) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

사칙연산, 비트마스킹, 수학

### 제출 일자

2023년 10월 26일 05:45:32

### 문제 설명

<p>Haker Limak napisał megawirusa. Każda z kopii wirusa ma swój numer (pierwsza kopia otrzymała numer 0). Co minutę tworzy się nowe pokolenie wirusów. Z wirusa o numerze <em>i</em> w pokoleniu <em>k</em> powstają wirusy (dzieci) o numerach 2 * <em>i</em> i 2 * <em>i</em> + 1 w pokoleniu <em>k</em> + 1. Nowo powstałe wirusy (2 * <em>i</em>, 2 * <em>i</em> + 1) nazwiemy dziećmi wirusa <em>i</em> z pokolenia <em>k</em>. Wirus <em>v</em>, jego dzieci, dzieci jego dzieci, itd. nazywamy potomkami wirusa <em>v</em>, a <em>v</em> jest nazywany ich przodkiem. Pierwsze pokolenie ma numer 0. Czyli w kolejnych pokoleniach żyją wirusy o następujących numerach:</p>

<ul>
	<li>pokolenie 0: wirus: 0,</li>
	<li>pokolenie 1: wirusy: 0, 1,</li>
	<li>pokolenie 2: wirusy: 0, 1, 2, 3,</li>
	<li>pokolenie 3: wirusy: 0, 1, 2, 3, 4, 5, 6, 7,</li>
	<li>...</li>
</ul>

<p>Napisz program który:</p>

<ul>
	<li>wczyta numer pokolenia i numery pewnej liczby wirusów z tego pokolenia,</li>
	<li>policzy największy numer pokolenia zawierającego wspólnego przodka wczytanych wirusów,</li>
	<li>wypisze obliczoną wartość.</li>
</ul>

### 입력 

 <p>W pierwszym wierszu podane są dwie liczby całkowite <em>k</em>, <em>n</em> oddzielone spacją. Pierwsza z liczb <em>k</em>, 1 ≤ <em>k</em> ≤ 512, jest numerem pokolenia. Druga z liczb <em>n</em>, 1 ≤ <em>n</em> ≤ 150 jest liczbą wirusów do wczytania. W następnych <em>n</em> wierszach podane są numery wirusów (po jednym w wierszu).</p>

### 출력 

 <p>Program powinien wypisać jedną liczbę będącą największym numerem pokolenia zawierającego wspólnego przodka wszystkich wirusów.</p>

