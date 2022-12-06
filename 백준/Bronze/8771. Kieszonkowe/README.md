# [Bronze I] Kieszonkowe - 8771 

[문제 링크](https://www.acmicpc.net/problem/8771) 

### 성능 요약

메모리: 215720 KB, 시간: 272 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Wujek Hektora zaproponował mu niedawno drobne kieszonkowe w związku ze zbliżającymi się wakacjami, przy okazji wystawiając na próbę jego zdolności rachunkowe.</p>

<p>Wujek zapisał na kartce kilka liczb naturalnych i poprosił Hektora o podjęcie decyzji - czy chciałby otrzymać kieszonkowe w wysokości sumy, czy iloczynu zapisanych liczb?</p>

<p>Napisz program, który dla zadanego ciągu liczb naturalnych sprawdzi, jaka decyzja będzie najbardziej opłacalna dla Hektora.</p>

### 입력 

 <p>W pierwszej linii wejścia znajduje się liczba naturalna <strong>Z</strong> ( 1 <= <strong>Z</strong> <= 10 ) opisująca liczbę zestawów testowych. Następnie opisywane są kolejne zestawy.</p>

<p>Pierwsza linia opisu zestawu testowego zawiera liczbę naturalną <strong>N</strong> ( 1 <= <strong>N</strong> <= 1000000 ), oznaczającą ilość liczb zapisanych przez wujka Hektora.</p>

<p>W drugiej linii opisu zestawu znajduje się <strong>N</strong> oddzielonych spacjami liczb naturalnych <strong>k</strong><strong><sub>i</sub></strong> ( 1 <= <strong>k</strong><strong><sub>i</sub> </strong><= 1000) oznaczających kolejne liczby zapisane na kartce.</p>

<p>W przypadku, w którym na kartce znajduje się tylko jedna liczba, należy przyjąć że zarówno suma jak i iloczyn takiego ciągu jest równa jedynej liczbie zapisanej na kartce.</p>

### 출력 

 <p>Dla każdego testu należy w osobnej linii wypisać słowo "SUMA", jeśli suma zapisanych liczb jest większa od ich iloczynu, "ILOCZYN", jeśli iloczyn zapisanych liczb jest większy od sumy i "=" (znak równości) jeżeli suma zapisanych liczb jest równa ich iloczynowi. </p>

