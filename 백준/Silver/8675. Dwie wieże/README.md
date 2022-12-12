# [Silver IV] Dwie wieże - 8675 

[문제 링크](https://www.acmicpc.net/problem/8675) 

### 성능 요약

메모리: 271056 KB, 시간: 608 ms

### 분류

누적 합(prefix_sum)

### 문제 설명

<p>Mały Bajtek otrzymał od dziadka zestaw klocków. Każdy klocek ma pewną wysokość. Bajtek stawia klocki na sobie i w ten spobób powstaje wieżyczka. Bajtek wybudował dwie wieżyczki, wykorzystując wszystkie swoje klocki.</p>

<p>Zastanawia się teraz, ile minimalnie klocków musi zdjąć z wieżyczek, aby obie miały równą wysokość. Bajtek może zdejmować klocki tylko z szczytów wieżyczek oraz nie może dokładać nowych klocków. W szczególności, Bajek może zdjąć wszystkie klocki ze wieżyczek - wtedy będą miały wysokości równe 0 i będą równe.</p>

### 입력 

 <p>Pierwszy wiersz wejścia zawiera dwie liczby całkowite <em>n</em>, <em>m</em> (1 ≤ <em>n</em>, <em>m</em> ≤ 10<sup>6</sup>), oznaczające odpowiednio liczbę klocków, z których zbudowana jest pierwsza oraz druga wieżyczka.</p>

<p>Drugi wiersz zawiera <em>n</em> liczb całkowitych <em>a</em><sub>1</sub>, <em>a</em><sub>2</sub>, ..., <em>a<sub>n</sub></em> (1 ≤ <em>a<sub>i</sub></em> ≤ 10<sup>9</sup>), gdzie <em>a<sub>i</sub></em> oznacza wysokość <em>i</em>-tego klocka w pierwszej wieżyczce (<em>a</em><sub>1</sub> to klocek znajdujący się na samym dole, <em>a<sub>n</sub></em> to klocek znajdujący się na wierzchołku pierwszej wieżyczki).</p>

<p>Trzeci wiersz zawiera <em>m</em> liczb całkowitych <em>b</em><sub>1</sub>, <em>b</em><sub>2</sub>, ..., <em>b<sub>m</sub></em> (1 ≤ <em>b<sub>i</sub></em> ≤ 10<sup>9</sup>), gdzie <em>b<sub>i</sub></em> oznacza wysokość <em>i</em>-tego klocka w drugiej wieżyczce.</p>

### 출력 

 <p>Pierwszy i jedyny wiersz wyjścia powinien zawierać jedną liczbę całkowitą, równą minimalnej liczbie klocków, jakie Bajtek powinien zdjąć z wieżyczek, aby były tej samej wysokości.</p>

