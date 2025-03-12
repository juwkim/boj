# [Silver II] Dalsze kłopoty z ogrodem - 8786 

[문제 링크](https://www.acmicpc.net/problem/8786) 

### 성능 요약

메모리: 324988 KB, 시간: 784 ms

### 분류

그리디 알고리즘, 구현, 시뮬레이션

### 제출 일자

2025년 3월 13일 01:46:35

### 문제 설명

<p>W zadaniu <a href="/problem/8847">Kłopoty z ogrodem</a> (FallSpot 2009) mieliśmy okazję poznać pana Wincentego - właściciela ogrodu i wielkiego antymiłośnika grabienia opadłych liści.</p>

<p>Od czasu ostatnich kłopotów minęło już trochę czasu, zmniejszony (por. oryginalne zadanie) ogród nie wymaga już tyle uwagi jesienią. Niestety, wraz z nadejściem tegorocznej wiosny pojawiły się nowe problemy - w ogrodzie zaczęły plenić się chwasty, doprowadzając pana Wincentego do szaleństwa (świadkowie twierdzą, że widzieli pana Wincentego nucącego słowa <em>Chwasty chwaściki chwaściory chwaścięta - cała to roślinność wiecznie nie przycięta! </em>na melodię jednej z symfonii Beethovena). Pewnego dnia pan Wincenty po długich godzinach spędzonych w warsztacie stanął w ogrodzie z przenośnym miotaczem płomieni w rękach.</p>

<p>Ogród pana Wincentego składa się z <strong>N</strong> pól ponumerowanych od 1 do <strong>N</strong>. W każdym polu znajduje się liczba chwastów wyrażona liczbą całkowitą <strong>c</strong><sub>i</sub>. Jednokrotne użycie miotacza płomieni na polu <strong>i</strong> powoduje zmniejszenie o połowę liczby chwastów w polu <strong>i </strong>oraz w sąsiednich polach <strong>i</strong>-1 oraz <strong>i</strong>+1. </p>

<p>Przez zmniejszenie o połowę rozumiemy dzielenie całkowite przez 2, tj. z 8 chwastów zostają 4, z 5 zostają 2. Jako cel miotacza płomieni można wybrać także nieistniejące pola 0 i <strong>N</strong>+1, wtedy jedyne redukowane pola to - odpowiednio - 1 i <strong>N</strong>.</p>

<p>Oblicz ile minimalnie razy pan Wincenty musi skorzystać z miotacza ognia, aby usunąć wszystkie chwasty.</p>

### 입력 

 <p>W pierwszej linii wejścia znajduje się liczba naturalna <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10 ) opisująca liczbę zestawów testowych. Następnie opisywane są kolejne zestawy.</p>

<p>Pierwsza linia opisu zestawu testowego zawiera jedną liczbę naturalną <strong>N</strong> ( 1 <= <strong>N</strong> <= 1000000) oznaczającą liczbę pól w ogrodzie pana Wincentego. </p>

<p>W drugiej linii opisu zestawu znajduje się N oddzielonych spacjami liczb naturalnych <strong>c<sub>i</sub></strong> oznaczających liczbę chwastów w poszczególnych polach ogrodu ( 0 <= <strong>c<sub>i</sub></strong> <= 1000000 ).</p>

### 출력 

 <p>Dla każdego testu należy w osobnej linii wypisać ile minimalnie razy pan Wincenty będzie musiał użyć miotacza płomieni.</p>

