# [Silver V] Metro - 8761 

[문제 링크](https://www.acmicpc.net/problem/8761) 

### 성능 요약

메모리: 316712 KB, 시간: 600 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation)

### 문제 설명

<p>W malowniczym szwajcarskim mieście Lozanna działa nowoczesne metro. Jednym z przykładów ciekawego rozwiązania inżynieryjnego jest jednotorowa, a jednak dwukierunkowa <a href="http://en.wikipedia.org/wiki/Lausanne_Metro#Line_M1" target="_blank">linia M1</a>. Pociągi poruszają się w obu kierunkach po pojedynczym torze, mijając się na dwuperonowych stacjach, w których tor rozwidla się na krótką chwilę.</p>

<p>W zadaniu rozważamy linię metra podobną do lozańskiego M1. Rozważana linia składa się z <strong>N</strong> stacji połączonych pojedynczym torem: pierwsza stacja połączona jest z drugą, druga z pierwszą i trzecią, trzecia z drugą i czwartą, itd. Zakładamy, że odległości pomiędzy stacjami są równe i przejazd pociągu pomiędzy sąsiednimi stacjami zawsze trwa dokładnie jedną minutę.</p>

<p>Niektóre spośród stacji są dwuperonowe - na takiej stacji mogą bezkolizyjnie spotkać się dwa pociągi jadące w przeciwne strony. Pozostałe stacje są jednoperonowe i ew. spotkanie pociągów na takiej stacji byłoby zdarzeniem wyjątkowo niefortunnym (szczególnie dla maszynistów i pasażerów tych pociągów).</p>

<p>Z dwóch końców linii w przeciwnych kierunkach jednocześnie odjeżdżają dwa pociągi. Twoim zadaniem jest wyznaczenie pociągom dodatkowych postojów (dowolnej długości wyrażonej w całkowitej nieujemnej liczbie minut) na dowolnej liczbie stacji tak, aby ich spotkanie wypadło na stacji dwuperonowej (pociągi mogą jednocześnie z dwóch stron wjechać na taką stację, możliwe jest także, że jeden z pociągów będzie oczekiwał na drugi na takiej stacji).</p>

<p>Jaki jest minimalny czas jazdy pociągów przy którym nie dochodzi do kolizji? Przez minimalny czas jazdy rozumiemy minimalny czas po którym oba pociągi, całe, niezderzone i niewykolejone zakończą jazdę na przeciwległych końcach toru. W przypadku, w którym jeden z pociągów kończy jazdę wcześniej, wynikiem jest czas jazdy drugiego pociągu.</p>

### 입력 

 <p>W pierwszej linii znajduje się liczba naturalna <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10 ) oznaczająca liczbę zestawów testowych. Następnie opisywane są kolejne zestawy.</p>

<p>Opis pojedynczego zestawu testowego składa się z dwóch linii. W pierwszej linii znajduje się pojedyncza dodatnia liczba całkowita <strong>N</strong> oznaczająca liczbę stacji metra na linii (2 <= <strong>N</strong> <= 1000000). W drugiej linii znajduje się <strong>N</strong> dodatnich liczb całkowitych <strong>s<sub>i</sub></strong> oddzielonych pojedynczymi spacjami, które odpowiadają kolejnym stacjom. Każda z nich jest równa 1 lub 2 i oznacza liczbę peronów na <strong>i</strong>-tej stacji metra. Co najmniej jedna stacja będzie miała dwa perony.</p>

### 출력 

 <p>Dla każdego zestawu testowego należy w osobnej linii wypisać minimalny czas bezkolizyjnego przejazdu pociągów. Kolejność wypisywanych odpowiedzi musi odpowiadać kolejności zestawów na wejściu.</p>

