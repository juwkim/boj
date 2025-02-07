# [Silver II] Wieża 2 - 8736 

[문제 링크](https://www.acmicpc.net/problem/8736) 

### 성능 요약

메모리: 191052 KB, 시간: 292 ms

### 분류

이분 탐색

### 제출 일자

2025년 2월 8일 04:18:07

### 문제 설명

<p>W Bajtocji wybudowano wysoką wieżę. Wejście na wieżę składa się z <em>n</em> schodków, a każdy schodek ma pewną wysokość.</p>

<p>Bajtocką wieżę chce odwiedzić <em>m</em> mieszkańców. Każda z osób posiada pewien wzrost, który pomaga w pokonywaniu kolejnych schodków. Aby mieszkaniec Bajtocji mógł wejść na pewien schodek, to musi być wyższy od wysokości schodka. Jeśli pewien schodek jest nie do przejścia przez mieszkańca, to zatrzymuje się on w danym miejscu na wieży - wyżej nie będzie mógł wejść. Niestety schody na wieżę są bardzo wąskie i jeśli pewna osoba zatrzyma się, to każda kolejna nie będzie mogła już wejść wyżej - będzie musiała zatrzymać się schodek wcześniej.</p>

<p>Znając wysokości kolejnych schodków i wzrost kolejnych osób zwiedzających wieżę, chcielibyśmy wiedzieć, w którym miejscu zatrzyma się każdy mieszkaniec Bajtocji.</p>

### 입력 

 <p>Pierwszy wiersz wejścia zawiera dwie liczby całkowite <em>n</em>, <em>m</em> (1 ≤ <em>n</em>, <em>m</em> ≤ 500 000), oznaczające odpowiednio liczbę schodków prowadzących na wieżę oraz liczbę mieszkańców chcących odwiedzić wieżę. Kolejny wiersz zawiera <em>n</em> liczb całkowitych <em>a</em><sub>1</sub>, <em>a</em><sub>2</sub>, ..., <em>a<sub>n</sub></em> (1 ≤ <em>a<sub>i</sub></em> ≤ 10<sup>9</sup>) , gdzie <em>a<sub>i</sub></em> oznacza wysokość <em>i</em>-tego schodka. Pierwszy schodek znajduje się na samym dole wieży, a każdy kolejny wyżej od poprzednich. Następny wiersz wejścia zawiera <em>m</em> liczb całkowitych <em>b</em><sub>1</sub>, <em>b</em><sub>2</sub>, ..., <em>b<sub>m</sub></em> (1 ≤ <em>b<sub>i</sub></em> ≤ 10<sup>9</sup>), gdzie <em>b<sub>i</sub></em> oznacza wzrost <em>i</em>-tego mieszkańca.</p>

### 출력 

 <p>Pierwszy i jedyny wiersz wyjścia powinien zawierać <em>m</em> liczb całkowitych <em>w</em><sub>1</sub>, <em>w</em><sub>2</sub>, ..., <em>w<sub>m</sub></em>, gdzie <em>w<sub>i</sub></em> oznacza maksymalny numer schodka, na który może wejść <em>i</em>-ty mieszkaniec Bajocji.</p>

