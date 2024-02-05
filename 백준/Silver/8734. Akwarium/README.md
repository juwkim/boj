# [Silver III] Akwarium - 8734 

[문제 링크](https://www.acmicpc.net/problem/8734) 

### 성능 요약

메모리: 252424 KB, 시간: 1472 ms

### 분류

구현, 시뮬레이션, 정렬

### 제출 일자

2024년 2월 6일 05:46:33

### 문제 설명

<p>Kozik dostał w prezencie na urodziny akwarium z mieczykami. Obserwowanie mieczyków szybko mu się znudziło, ponieważ według Kozika nigdy nie działo się nic nowego. Dlatego też mieczyki szybko sprzedał, a za zarobione pieniądze kupił w promocji pewne afrykańskie ryby.</p>

<p>Afrykańska ryba ma określoną masę i wiek oraz charakteryzuje się tym, że musi codziennie zaspokoić swój głód. Jeśli nie dostanie nic do jedzenia, to pożera inną, mniejszą rybę. Jeśli kilka ryb jest głodnych, to pierwszeństwo ma zawsze ryba o największej masie, która wybiera swoją ofiarę (w przypadku równych mas pierwszeństwo ma ryba starsza). Ofiarą będzie zawsze najmniejsza ryba znajdująca się w akwarium (jeśli kilka ryb ma taką samą masę, ofiarą z nich będzie najmłodsza ryba). Dodatkowo afrykańska ryba zwiększa swoją masę o połowę masy zjedzonej przez nią innej ryby. Jeśli afrykańska ryba nie zaspokoi swojego głodu w ciągu dnia, zdycha. Kilka ryb może mieć równe masy, natomiast wszystkie ryby są innego wieku.</p>

<p>Kozik zastanawia się, czy pewna ryba <em>r</em>, wybrana przez niego, będzie żyła za <em>x</em> dni.</p>

### 입력 

 <p>Pierwszy wiersz standardowego wejścia zawiera jedną liczbę całkowitą <em>n</em> (1 ≤ <em>n</em> ≤ 10<sup>6</sup>), oznaczającą liczbę ryb w akwarium. W <em>n</em> kolejnych wierszach znajdują się po dwie liczby całkowite <em>m<sub>i</sub></em>, <em>w<sub>i</sub></em> (1 ≤ <em>m<sub>i</sub></em>, <em>w<sub>i</sub></em> ≤ 10<sup>9</sup>), oznaczające odpowiednio masę i wiek <em>i</em> - tej ryby. W kolejnym wierszu znajduje się jedna całkowta <em>z</em> (1 ≤ <em>z</em> ≤ 10<sup>6</sup>), ozaczająca liczbę zapytań Kozika. W <em>z</em> następnych wierszach znajdują się po dwie liczby całkowite <em>r<sub>k</sub></em>, <em>x<sub>k</sub></em> (1 ≤ <em>r<sub>k</sub></em> ≤ <em>n</em>, 0 ≤ <em>x<sub>k</sub></em> ≤ 10<sup>9</sup>), oznaczjące pytanie: czy ryba <em>r<sub>k</sub></em> będzie żyła za <em>x<sub>k</sub></em> dni?.</p>

### 출력 

 <p>Dla każdego zapytania słowo TAK, jeśli ryba <em>r<sub>k</sub></em> będzie żyła za <em>x<sub>k</sub></em> dni, w przeciwnym wypadku słowo NIE.</p>

