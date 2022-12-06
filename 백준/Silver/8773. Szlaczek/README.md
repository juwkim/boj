# [Silver IV] Szlaczek - 8773 

[문제 링크](https://www.acmicpc.net/problem/8773) 

### 성능 요약

메모리: 185324 KB, 시간: 588 ms

### 분류

애드 혹(ad_hoc), 수학(math)

### 문제 설명

<p>Młodsza siostra Hektora, Kornelia (którą poznaliśmy w zadaniu <a href="/problem/8841">Zgadywanka</a>) z dystansem podchodzi do zajęć prowadzonych w przedszkolu, do którego uczęszcza. Przykładowo - wychowawcy w przedszkolu oczekują od niej, że będzie ćwiczyć sprawność posługiwania się piórem rysując w specjalnym zeszycie tak zwane "szlaczki" - powtarzające się wzory. Kornelia uważa to zajęcie za mało ambitne, postanowiła więc je urozmaicić, i rysować wymyślone przez siebie "szlaczki rekurencyjne".</p>

<p>Szlaczki Kornelii zamiast z graficznych wzorów, składają się z liczb naturalnych. Kornelia rozpoczyna je od zapisania dowolnego ciągu liczb naturalnych, przykładowo:</p>

<p>1 2 1 1 1</p>

<p>A następnie do woli dopisuje do już zapisanego fragmentu "szlaczka" ten sam fragment od końca (każdorazowo podwajając długość szlaczka). Dla przykładowego szlaczka, w następnym kroku wyglądałby on tak:</p>

<p>1 2 1 1 1 <strong>1 1 1 2 1</strong></p>

<p>Natomiast w kolejnym kroku Kornelia uzyskałaby wzór:</p>

<p>1 2 1 1 1 1 1 1 2 1 <strong>1 2 1 1 1 1 1 1 2 1</strong></p>

<p>Proces konstrukcji szlaczka można kontynuuować bez końca.</p>

<p>Znając ciąg, od którego Kornelia rozpoczęła tworzenie szlaczka, oblicz jaka liczba znajdzie się na zadanej pozycji wzoru.</p>

### 입력 

 <p>W pierwszej linii wejścia znajduje się liczba naturalna <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10 ) opisująca liczbę zestawów testowych. Następnie opisywane są kolejne zestawy.</p>

<p>Pierwsza linia opisu zestawu testowego zawiera parę liczb naturalnych <strong>N</strong> i <strong>M</strong> ( 1 <= <strong>N</strong> <= 1000000, 0 <= <strong>M</strong> <= 1000000000), oznaczających kolejno: długość początkowego ciągu oraz pozycję w wynikowym wzorze.</p>

<p>W drugiej linii opisu zestawu znajduje się <strong>N </strong>oddzielonych spacjami liczb naturalnych <strong>c</strong><strong><sub>i</sub></strong> ( 1 <= <strong>c</strong><strong><sub>i</sub> </strong><=<strong> </strong>1000000) oznaczających kolejne liczby w początkowym ciągu.</p>

### 출력 

 <p>Dla każdego testu należy w osobnej linii wypisać liczbę, która znajdzie się na <strong>M</strong>-tej pozycji szlaczka Kornelii, przy czym pozycje w ciągu numerujemy począwszy od zera.</p>

