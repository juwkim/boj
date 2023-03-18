# [Silver IV] Krany - 8673 

[문제 링크](https://www.acmicpc.net/problem/8673) 

### 성능 요약

메모리: 213892 KB, 시간: 388 ms

### 분류

정렬, 누적 합

### 문제 설명

<p>W pewnym zakładzie przemysłowym znajduje się <em>n</em> kranów, z których może lać się woda. Przy każdym kranie znajduje się wskaźnik, oznaczający temperaturę wody, dla danego kranu. Woda leje się z kranu, jeśli ustawiona temperatura wody jest większa od zera. Woda z każdego kranu leje się z równą prędkością i trafia do wspólnego zbiornika.</p>

<p>Znając temperatury przy każdym kranie, chcielibyśmy wiedzieć, ile minimalnie kranów musimy zakręcić, aby temperatura wody w zbiorniku była równa lub większa od wartości <em>w</em>.</p>

<p>Zakładamy, że temperatura w zbiorniku jest średnią temperaturą wszystkich kranów, z których leci woda. Temperatura się nie zmienia na skutek oddziaływania temperatury powietrza.</p>

### 입력 

 <p>Pierwszy wiersz standardowego wejścia zawiera dwie liczby całkowite <em>n</em>, <em>w</em> (1 ≤ i ≤ 10<sup>6</sup>, 1 ≤ <em>w</em> ≤ 100), oznaczające odpowiednio liczbę kranów oraz wartość temperatury, którą chcemy uzyskać. W kolejnym wierszu znajduje się <em>n</em> liczb całkowitych <em>t</em><sub>1</sub>, <em>t</em><sub>2</sub>, ..., <em>t<sub>n</sub></em> (-100 ≤ <em>t<sub>i</sub></em> ≤ 100), gdzie <em>t<sub>i</sub></em> oznacza temperaturę wody, ustawioną dla <em>i</em>-tego kranu.</p>

### 출력 

 <p>W pierwszym i jedynym wierszu wyjścia powinna znajdować się jedna liczba całkowita, równa minimalnej liczbie kranów, jakie powinniśmy zakręcić, aby temperatura w zbiorniku wynosiła co najmniej <em>w</em> stopni lub jedno słowo 'NIE', jeśli nie jest możliwe uzyskanie takiej temperatury.</p>

