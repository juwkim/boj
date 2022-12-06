# [Silver V] Szuflady - 8662 

[문제 링크](https://www.acmicpc.net/problem/8662) 

### 성능 요약

메모리: 145280 KB, 시간: 640 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>Michał ma w sypialni szafkę z <em>n</em> szufladami. Każda z nich jest wysunięta na pewną długość. Chłopiec chciałby mieć bezpośredni dostęp do każdej szuflady, tak aby nie musiał ich wysuwać za każdym razem.</p>

<p>Bezpośredni dostęp do danej szuflady jest wtedy, gdy każda szuflada powyżej niej jest mniej wysunięta. Michał postanowił, że będzie tylko wsuwał szuflady (czyli zmniejszał długość ich wysunięcia). Zastanawia się, ile minimalnie szuflad musi wsunąć, aby mieć bezpośredni dostęp do wszystkich z nich.</p>

<p>Zakładamy, że do szuflady, której wysunięcie jest równe 0, nie ma dostępu, oraz że wysunięcie szuflady musi być zawsze wartością całkowitą.</p>

### 입력 

 <p>Pierwszy wiersz standardowego wejścia zawiera jedną liczbę całkowitą <em>n</em> (1 ≤ <em>n</em> ≤ 10<sup>6</sup>), oznaczającą liczbę szuflad. Kolejny wiersz wejścia zawiera <em>n</em> liczb całkowitych <em>a</em><sub>1</sub>, <em>a</em><sub>2</sub>, ..., <em>a<sub>n</sub></em> (1 ≤ <em>a<sub>i</sub></em> ≤ 10<sup>9</sup>), gdzie <em>a<sub>i</sub></em> oznacza długość wysunięcia <em>i</em>-tej (licząc od góry szafki) szuflady.</p>

### 출력 

 <p>Pierwszy wiersz standardowego wyjścia powinien zawierać jedną liczbę całkowitą, równą minimalnej liczbie szuflad, jakie musi wsunąć Michał, aby był bezpośredni dostęp do wszystkich z nich. Jeśli nie jest to możliwe, wynikiem powinna być liczba -1.</p>

