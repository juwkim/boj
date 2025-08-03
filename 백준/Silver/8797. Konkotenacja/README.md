# [Silver I] Konkotenacja - 8797 

[문제 링크](https://www.acmicpc.net/problem/8797) 

### 성능 요약

메모리: 159052 KB, 시간: 364 ms

### 분류

다이나믹 프로그래밍, 문자열

### 제출 일자

2025년 8월 4일 03:22:45

### 문제 설명

<p>Konkotenacją słów <strong>A</strong> i <strong>B</strong> nazwiemy słowo <strong>A</strong>kot<strong>B</strong>. Przykładowo konkotenacją słów "mas" oraz "ka" jest słowo "maskotka". Operację tę można zdefiniować dla całych ciągów słów - konkotenujemy wtedy ze sobą wszystkie słowa zgodnie z kolejnością, z jaką w danym ciągu występują. I tak po skonkotenowaniu ciągu słów ( "aa", "b", "cc", "d" ) otrzymujemy słowo "aakotbkotcckotd".</p>

<p>Ile różnych ciągów złożonych z niepustych słów daje po skonkotenowaniu dane słowo <strong>W</strong>?</p>

### 입력 

 <p>W pierwszej linii znajduje się jedna liczba naturalna <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10 ) oznaczająca liczbę zestawów testowych. W kolejnych liniach opisywane są kolejne zestawy.</p>

<p>Pojedynczy zestaw składa się z jednego niepustego słowa <strong>W</strong> złożonego z małych liter alfabetu angielskiego. Długość słowa <strong>W</strong> nie przekracza 1 000 000.</p>

### 출력 

 <p>Dla każdego słowa podanego na wejściu należy wypisać w osobnej linii jedną nieujemną liczbę całkowitą - resztę z dzielenia liczby różnych ciągów dających po skonkotenowaniu dane słowo przez 1 000 000 007.</p>

