# [Bronze I] Przegrody - 8670 

[문제 링크](https://www.acmicpc.net/problem/8670) 

### 성능 요약

메모리: 149432 KB, 시간: 648 ms

### 분류

애드 혹(ad_hoc), 구현(implementation)

### 문제 설명

<p>Jaś wypisał na kartce wszystkie liczby od 1 do <em>n</em> w pewnej losowej kolejności, tworzącej pewien ciąg. Chciałby teraz wstawić jak najwięcej przegród do tej listy.</p>

<p>Przegrody może wstawiać tylko wtedy, gdy pomiędzy wstawianą przegrodą, ustawioną za <em>k</em>-tym elementem ciągu a początkiem ciągu, występuje każda z liczb od 1 do <em>k</em>. W szczególności ostatnią przegrodę Jaś może zawsze wstawić za <em>n</em>-tym elementem ciągu, bowiem będzie to permutacja liczb od 1 do <em>n</em>.</p>

### 입력 

 <p>Pierwszy wiersz standardowego wejścia zawiera jedną liczbę całkowitą <em>n</em> (1 ≤ <em>n</em> ≤ 10<sup>6</sup>), oznaczającą liczbę elementów w ciągu.</p>

<p>Kolejny wiersz zawiera permutację <em>n</em> liczb całkowitych <em>p</em><sub>1</sub>, <em>p</em><sub>2</sub>, ..., <em>p<sub>n</sub></em> (1 ≤ <em>p<sub>i</sub></em> ≤ <em>n</em>), gdzie <em>p<sub>i</sub></em> oznacza <em>i</em>-tą liczbę w ciągu.</p>

### 출력 

 <p>Pierwszy i jedyny wiersz wyjścia powinien zawierać jedną liczbę całkowitą, równą maksymalnej liczbie przegród, jakie może wstawić Jaś.</p>

