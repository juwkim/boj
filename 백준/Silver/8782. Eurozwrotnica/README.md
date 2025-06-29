# [Silver I] Eurozwrotnica - 8782 

[문제 링크](https://www.acmicpc.net/problem/8782) 

### 성능 요약

메모리: 313480 KB, 시간: 956 ms

### 분류

자료 구조, 그리디 알고리즘, 구현, 큐, 시뮬레이션

### 제출 일자

2025년 6월 29일 23:36:11

### 문제 설명

<p>Czy pamiętacie pana Pawła, kolejarza z podwrocławskiej miejscowości, który był bohaterem zadania Kolejarz Paweł? W ostatnich miesiącach w jego życiu zawodowym sporo się zmieniło. Ze względu na rozbudowę infrastruktury kolejowej przed Euro 2012, na jego malutkiej stacyjce wybudowano drugi tor!</p>

<p>Po rozbudowie stacja pana Pawła pozostała jednokierunkowa. <a href="http://pl.wikipedia.org/wiki/Sk%C5%82ad_kolejowy">Składy kolejowe</a> nadjeżdżają na stację od zachodu, i wyjeżdzają przeciwną stroną. Do pana Pawła należy podejmowanie decyzji na który tor skierować każdy z nadjeżdzających składów, i kiedy nakazać każdemu ze składów opuszczenie stacji. Na jednym torze może oczekiwać wiele składów, ale muszą opuścić stację w takiej kolejności, w której wjechały na tor (to znaczy, pociągi nie mogą wyprzedzać się na torze).</p>

<p>Taka budowa stacji umożliwia panu Pawłowi wpływanie na kolejność składów wyjeżdżających ze stacji. Przykładowo, jeśli na stację przyjeżdżają kolejno pociągi C, A, B, pan Paweł może skierować pierwszy z pociągów na pierwszy tor, dwa kolejne na drugi, a potem nakazać składom odjeżdżać w kolejności A, B, C.</p>

<p>Jutro na stację ma przyjechać <strong>N</strong> składów ponumerowanych od 1 do <strong>N</strong>. Znając kolejność, w jakiej przyjadą na stację sprawdź, czy da się tak przydzielać tory przyjeżdząjącym pociągom, żeby opuszczały stację w kolejności 1,2,...,<strong>N</strong>.</p>

### 입력 

 <p>W pierwszej linii znajduje się liczba naturalna <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10 ) oznaczająca liczbę zestawów testowych. Następnie opisywane są kolejne zestawy.</p>

<p>W pierwszej linii opisu pojedynczego zestawu testowego znajduje się jedna liczba naturalna <strong>N</strong> (1 <= N  <= 1000000) oznaczająca liczbę pociągów przyjeżdzających na stację. W drugiej linii opisu zestawu znajduje się <strong>N</strong> oddzielonych spacjami różnych liczb <strong>p<sub>i</sub></strong> ( 1 <= <strong>p<sub>i</sub></strong> <= <strong>N</strong> ) oznaczających numery pociągów wymienione w kolejności, w jakiej będą przyjeżdżać na stację.</p>

### 출력 

 <p>Dla każdego zestawu testowego należy w osobnej linii wypisać słowo "TAK", jeśli da się ustawić pociągi w wymaganej kolejności i "NIE" w przeciwnym wypadku.</p>

