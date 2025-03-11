# [Silver II] Kurs - 8774 

[문제 링크](https://www.acmicpc.net/problem/8774) 

### 성능 요약

메모리: 260444 KB, 시간: 640 ms

### 분류

자료 구조, 스택

### 제출 일자

2025년 3월 12일 02:32:18

### 문제 설명

<p>Hektor zainteresował się niedawno grą na giełdzie - świat akcji, obligacji, kursów i dywidend jest skomplikowany i pełen liczb, co czyni z niego idealnego kandydata na nowe hobby naszego bohatera.</p>

<p>Hektor dysponuje historią notowań pewnej spółki w postaci listy liczb naturalnych opisujących wartość kursu spółki na kolejnych notowaniach. Dla każdego notowania na liście Hektor chciałby obliczyć, kiedy (licząc od momentu rozważanego notowania) kurs spółki po raz pierwszy przekroczył kurs z tego dnia (tj. formalnie: dla każdej pozycji <strong>x</strong> na liście Hektor chciałby znać najmniejsze <strong>y</strong>, które jest większe od <strong>x</strong> i jednocześnie takie, że kurs na pozycji <strong>y</strong> był większy od kursu na pozycji <strong>x</strong>).</p>

<p>Czy potrafisz przygotować program, który będzie realizował takie obliczenia?</p>

### 입력 

 <p>W pierwszej linii wejścia znajduje się liczba naturalna <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10 ) opisująca liczbę zestawów testowych. Następnie opisywane są kolejne zestawy.</p>

<p>Pierwsza linia opisu zestawu testowego zawiera liczbę naturalną <strong>N</strong> ( 1 <= <strong>N</strong> <= 1000000), oznaczającą długość listy Hektora.</p>

<p>W drugiej linii opisu zestawu znajduje się <strong>N</strong> oddzielonych spacjami liczb naturalnych <strong>k</strong><strong><sub>i</sub></strong> ( 1 <= <strong>k</strong><strong><sub>i</sub> </strong><= 1000000000) oznaczających wysokość kursu spółki na kolejnych notowaniach.</p>

### 출력 

 <p>Dla każdego testu należy w osobnej linii wypisać <strong>N</strong> oddzielonych spacjami liczb całkowitych odpowiadających wpisom na liście Hektora. Dla pozycji, dla których istnieje dalsze notowanie o wyższym kursie, należy wypisać numer pierwszego takiego notowania; przy czym kolejne notowania na liście numerujemy od 0. Dla pozostałych pozycji należy wypisać liczbę -1.</p>

