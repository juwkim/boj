# [Silver V] Brakujące cyfry - 8762 

[문제 링크](https://www.acmicpc.net/problem/8762) 

### 성능 요약

메모리: 115268 KB, 시간: 132 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math), 문자열(string)

### 문제 설명

<p>Hektor i Wiktor są w trakcie opracowywania własnego systemu szyfrującego. Prace nad nim posuwają się jednak dość powoli, jak na razie ustalili jedynie, w jaki sposób szyfrowane będą ciągi cyfr.</p>

<p>Szyfrowany ciąg jest rozbijany na pojedyncze cyfry, które są kodowane osobno. Szyfrogram pojedynczej cyfry <strong>d</strong> składa się z dwóch całkowitych dodatnich liczb<strong> A</strong>, <strong>B</strong>. W dokładnie jednej z tych liczb dokładnie jedna cyfra jest zastąpiona znakiem '<strong>x</strong>'. Liczby <strong>A</strong> i <strong>B</strong> oraz pozycja '<strong>x</strong>' dobrane są w ten sposób, że szyfrowana cyfra <strong>d</strong> jest najmniejszą cyfrą, która wstawiona w miejsce '<strong>x</strong>' sprawia, że <strong>A</strong> dzieli się przez <strong>B</strong>.</p>

<p>Hektor z Wiktorem napisali już program szyfrujący i zwrócili się do Ciebie z prośbą o napisanie programu deszyfrującego.</p>

### 입력 

 <p>W pierwszej linii znajduje się liczba naturalna <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10 ) oznaczająca liczbę zestawów testowych. Następnie opisywane są kolejne zestawy.</p>

<p>W pierwszej linii pojedynczego zestawu testowego znajduje się jedna liczba całkowita <strong>N</strong> ( 1 <= <strong>N</strong> <= 100 ), określająca liczbę cyfr zaszyfrowanego ciągu. Każda z następnych <strong>N</strong> linii zawiera szyfrogram jedej cyfry zakodowanego ciągu, składa się więc z dwóch liczb całkowitych <strong>A</strong> i <strong>B</strong> ( 1 <= <strong>B</strong> <= <strong>A</strong> <= 1000000000 ) oddzielonych pojedynczą spacją. W dokładnie jednej z tych dwóch liczb dokładnie jedna cyfra jest zastąpiona znakiem '<strong>x</strong>'.</p>

<p>Ani <strong>A</strong> ani <strong>B</strong> nie zawierają / nie mogą zawierać zer wiodących - tj. nie zaczynają się od 0.</p>

### 출력 

 <p>Dla każdego zestawu testowego należy w osobnej linii wypisać ciąg cyfr, którego szyfrogram został podany na wejściu. Kolejność wypisywanych odpowiedzi musi odpowiadać kolejności zestawów na wejściu.</p>

