# [Silver III] Oranżada - 26695 

[문제 링크](https://www.acmicpc.net/problem/26695) 

### 성능 요약

메모리: 214876 KB, 시간: 272 ms

### 분류

그리디 알고리즘

### 제출 일자

2024년 5월 2일 22:50:56

### 문제 설명

<p>Bajtabasz lubi siedzieć w domu. W końcu mamy środek pandemii – należy zachowywać dystans społeczny. Podczas wieczorów spędzanych przed komputerem, jego ulubionym zajęciem, zaraz obok grania w Byte Defence 3 i rozwiązywania zadań ze starych edycji Potyczek Algorytmicznych, jest picie oranżady. W piwnicy Bajtabasza znajduje się długa półka, na której ułożonych w rzędzie stoi n butelek oranżady. Każda z butelek jest pewnej marki, które oznaczamy liczbami całkowitymi. Piwnica jest ciasna i ma śliską podłogę, więc nierozważnie byłoby chodzić tam i z powrotem z butelkami w rękach – jeszcze któraś by się rozbiła. Z tego względu jedyne, co Bajtabasz może robić, to zamieniać miejscami dwie sąsiednie butelki. Każda taka zamiana zajmuje mu jedną sekundę. Czas poruszania się wzdłuż półki jest pomijalny.</p>

<p>Na dzisiejszy wieczór Bajtabasz zaprosił Bajtolinę na wspólną degustację oranżady. Żeby uświetnić to wydarzenie chciałby, żeby k skrajnie lewych butelek na półce było różnych marek.</p>

<p>Bajtabasz ma mało czasu – musi jeszcze posprzątać cały swój dom – dlatego chciałby przearanżować oranżadową półkę najszybciej, jak to się tylko da. Pomóż mu w tym zadaniu!</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajdują się dwie liczby całkowite n i k (1 ≤ n ≤ 5·10<sup>5</sup>; 1 ≤ k ≤ n)<sup>∗</sup>, oznaczające odpowiednio liczbę butelek na półce oraz liczbę skrajnie lewych butelek, które muszą być różnych marek, aby uszczęśliwić Bajtabasza.</p>

<p>W drugim wierszu wejścia znajduje się ciąg n liczb całkowitych a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, . . . , a<sub>n</sub>, (1 ≤ a<sub>i</sub> ≤ n), gdzie a<sub>i</sub> oznacza markę i-tej od lewej butelki znajdującej się na półce w piwnicy Bajtabasza.</p>

<hr>
<p><sup>∗</sup>Tak ogromna liczba butelek może zadziwić tylko tych, którzy nie wiedzą, że Bajtabasz w czasach swojej młodości był wielokrotnym mistrzem Bajtocji w piciu oranżady na czas.</p>

### 출력 

 <p>Na wyjściu powinna znaleźć się jedna liczba całkowita, oznaczająca minimalną liczbę sekund, po których pierwsze k butelek będzie parami różne, lub −1, jeśli nie da się doprowadzić do takiej sytuacji.</p>

