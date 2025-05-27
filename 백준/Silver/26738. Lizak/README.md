# [Silver I] Lizak - 26738 

[문제 링크](https://www.acmicpc.net/problem/26738) 

### 성능 요약

메모리: 236560 KB, 시간: 392 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵, 두 포인터, 집합과 맵

### 제출 일자

2025년 5월 27일 10:15:12

### 문제 설명

<p>Bajtek udał się do cukierni. Jego uwagę przykuł długi lizak składający się z N części równej długości. Każda część lizaka ma pewien określony smak.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/1b227eaf-4f88-4478-9221-73af9a89711c/-/preview/" style="width: 379px; height: 26px;"></p>

<p>Bajtek chciałby wybrać pewien spójny fragment tego lizaka. Aby to zrobić, może on odłamać pewną liczbę części (być może zero) z lewej i prawej strony tego lizaka. Poniższy rysunek pokazuje kilka możliwości wybrania fragmentów z lizaka przedstawionego powyżej. Przykładowe fragmenty oznaczone są czarną ramką.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/3df885a2-b2e4-4fe1-80c5-e93f73888a49/-/preview/" style="width: 386px; height: 143px;"></p>

<p>Bajtek uważa fragment lizaka za smaczny, jeżeli zawiera co najmniej trzy części o tym samym smaku. Zwróć uwagę, że Bajtka nie interesuje jaki dokładnie smak będzie występował trzy razy, ani ile będzie różnych smaków w tym fragmencie. Zauważ, że wszystkie fragmenty z rysunku powyżej są smaczne.</p>

<p>Bajtek nie zamierza się przejadać. Chciałby więc wybrać najkrótszy smaczny fragment lizaka, czyli taki fragment który składa się z jak najmniejszej liczby części. Pomóż mu!</p>

<p>Napisz program, który na podstawie opisu lizaka wyznaczy długość jego najkrótszego smacznego fragmentu lub stwierdzi że nie jest możliwe wybranie żadnego smacznego fragmentu.</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba naturalna N (1 ≤ N ≤ 500 000) określająca liczbę części dostępnego lizaka w sklepie. W drugim (ostatnim) wierszu wejścia znajduje się opis części tego lizaka. Lizak ten reprezentowany jest jako ciąg N liczb naturalnych A<sub>i</sub> (1 ≤ A<sub>i</sub> ≤ 10<sup>9</sup>). Są to oznaczenia smaków fragmentów lizaka w kolejności ich występowania w lizaku od lewej do prawej. Różne smaki reprezentowane są różnymi liczbami.</p>

### 출력 

 <p>W pierwszym (jedynym) wierszu wyjścia powinna się znaleźć jedna liczba całkowita – minimalna liczba części, które ma smaczny fragment lizaka zgodnie z warunkami powyżej. Jeśli z lizaka opisanego na wejściu nie można wybrać smacznego fragmentu to zamiast tego należy wypisać tylko jedno słowo <code>NIE</code>.</p>

