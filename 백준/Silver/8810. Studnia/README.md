# [Silver II] Studnia - 8810 

[문제 링크](https://www.acmicpc.net/problem/8810) 

### 성능 요약

메모리: 174928 KB, 시간: 352 ms

### 분류

수학

### 제출 일자

2025년 3월 20일 07:13:46

### 문제 설명

<p>Pan Michał chce wykopać nową studnię. Dysponuje planem terenu swojej działki, na którym przedstawione są dwa zarysy: powierzchni gruntu oraz początku warstwy wodonośnej, które mają kształt linii łamanych. Pan Michał wynajął już specjalne wiertło, które może wiercić jedynie w pionie. Koszty wiercenia są całkiem spore, nic dziwnego więc, że zastanawia się, na jaką głębokość co najmniej musi wykonać odwiert, by dotrzeć z powierzchni do warstwy wodonośnej.</p>

### 입력 

 <p>W pierwszej linii znajduje się jedna liczba naturalna <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 5 ) oznaczająca liczbę zestawów testowych. Następnie opisywane są kolejne zestawy.</p>

<p>W pierwszej linii znajduje się jedna liczba naturalna <strong>n </strong>( 2 <= <strong>n</strong> <= 100 000 ), oznaczająca liczbę punktów łamanej opisującej powierzchnię gruntu na działce pana Michała. W drugim wierszu występuje <strong>n</strong> par liczb naturalnych <strong>x<sub>i</sub></strong>, <strong>y<sub>i</sub></strong> ( 1 <= <strong>x<sub>i</sub></strong>, <strong>y<sub>i</sub></strong> <= 10<sup>9</sup> ), pooddzielanych pojedynczymi odstępami. Dla każdego 1 <= <strong>i </strong>< <strong>n </strong>zachodzi: <strong>x</strong><sub><strong>i</strong> </sub>< <strong>x<sub>i+1</sub></strong>.</p>

<p>W kolejnych dwóch liniach znajduje się analogiczny opis łamanej opisującej początek warstwy wodonośnej pod działką pana Michała. W pierwszej z nich znajduje się liczba naturalna <strong>m </strong>( 2 <= <strong>m </strong><<strong> n+m</strong> <= 100 000 ), oznaczająca liczbę punktów, a w drugiej z linii jest <strong>m</strong> par liczb naturalnych <strong>u<sub>i</sub></strong>, <strong>v<sub>i</sub></strong> ( 1 <= <strong>u<sub>i</sub></strong>, <strong>v<sub>i</sub></strong> <= 10<sup>9</sup> ), pooddzielanych pojedynczymi odstępami. Dla każdego 1 <= <strong>i </strong>< <strong>m </strong>zachodzi: <strong>u</strong><sub><strong>i</strong> </sub>< <strong>u<sub>i+1</sub></strong>.</p>

<p>Warstwa wodonośna znajduje się w całości pod powierzchnią gruntu ( te dwie łamane nie mają punktów wspólnych ). Ponadto zachodzą równości: <strong>x<sub>1</sub></strong> = <strong>u<sub>1</sub></strong> oraz <strong>x<sub>n</sub></strong> = <strong>u<sub>m</sub></strong>.</p>

### 출력 

 <p>Dla każdego zestawu testowego w osobnej linii należy wypisać jedną liczbę rzeczywistą dodatnią - minimalną głębokość dzielącą powierzchnię od warstwy wodonośnej. Wartość tę należy zaokrąglić do dokładnie dwóch miejsc po przecinku.</p>

