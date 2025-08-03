# [Silver I] ASK - 8861 

[문제 링크](https://www.acmicpc.net/problem/8861) 

### 성능 요약

메모리: 115216 KB, 시간: 136 ms

### 분류

해 구성하기, 그리디 알고리즘

### 제출 일자

2025년 8월 3일 19:22:21

### 문제 설명

<p>Na zajęciach z Architektury Systemów Komputerowych, Paweł przygotował nowy model pamięci operacyjnej, który wspiera szybkie operacje bitowe wykonywane na całej zawartości pamięci. W modelu Pawła, bity stanowią pojedynczy ciąg zerojedynkowy. Zmiana zawartości pamięci realizowana jest poprzez użycie specjalnej elektrody. Jej działanie polega na wybraniu pojedynczego bitu oraz kierunku działania (lewo lub prawo), a następnie zanegowaniu każdej wartości bitu idąc w odpowiednią stronę, aż do końca lub początku pamięci. Przykładowo, jeżeli zawartość pamięci to 0010, to wybierając drugi bit i prawy kierunek elektroda zmieni ją na 0101 - drugi bit zmieniany jest z 0 na 1, trzeci bit z 1 na zero, czwarty bit z 0 na 1.</p>

<p>Paweł chce przetestować skuteczność swojego rozwiązania. W tym celu potrzebuje programu, który mając jako dane początkową i końcową zawartość pamięci, policzy minimalną liczbę operacji potrzebnych do przekształcenia jednej zawartości pamięci w drugą. Twoim zadaniem jest pomóc Pawłowi i napisać dla niego odpowiedni program.</p>

### 입력 

 <p>W pierwszej linii znajduje się jedna liczba całkowita <strong>n</strong> (1<=<strong>n</strong><=1000000). W drugiej linii znajduje się binarny, <strong>n</strong>-elementowy ciąg - jest to początkowa zawartość pamięci. W trzeciej linii znajduje się binarny, <strong>n</strong>-elementowy ciąg - jest to docelowa zawartość pamięci.</p>

### 출력 

 <p>W pierwszej i jedynej linii Twój program powinien wypisać jedną liczbę - minimalną liczbę operacji potrzebną do zamiany początkowej zawartości pamięci w docelową.</p>

